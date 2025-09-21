"""
This script converts a Blender material or node group into Python code that can recreate it.
It handles node properties, connections, and nested node groups.

Usage:
1. Select an object with a material in Blender.
2. Run this script in Blender's scripting environment.
3. The generated code will be available in a new text block named after the material.
4. Run the generated code to recreate the material or node group for testing purpose.

Source: https://blender.stackexchange.com/questions/214911/whats-the-most-reliable-way-of-converting-a-material-into-reusable-code-blocks
"""

import bpy
from math import isclose
from collections import Counter

LUT = dict()
BLACK = [0.0, 0.0, 0.0, 1.0]
WHITE = [1.0, 1.0, 1.0, 1.0]
ul = f'#{"-" * 44}\n'
buffer = []


def cmp(v1, v2):
    return (
        (len(v1) == len(v2))
        and all(isclose(*v) for v in zip(v1, v2))
    )


def vformat(nums, n, indent=8):
    nums = [f"{d}" for d in nums]
    return f",\n{' ' * indent}".join([", ".join(nums[i: i + n]) for i in range(0, len(nums), n)])


def fes(collection, prop, data, size, indent):
    output(
        f'{" " * indent}{collection}.foreach_set(\n'
        f'       "{prop}", [\n'
        f'        {vformat(data, size, 8 + indent)}\n'
        f'        ])'
    )


def groups_in_tree(node_tree):
    for node in node_tree.nodes:
        if hasattr(node, "node_tree"):
            yield node.node_tree
            yield from groups_in_tree(node.node_tree)


def group_io(n):
    output(f'node = nodes.new("{n.bl_rna.identifier}")')
    output(f'node.name = "{n.name}"')
    sockets = ("inputs", "outputs") if n.type == 'GROUP_INPUT' else ("outputs", "inputs")
    for skt in getattr(n, sockets[1]):
        if skt.type != 'CUSTOM' and skt.name:
            output(
                f"skt = group.{sockets[0]}.new('{skt.__class__.__name__}', "
                f'"{skt.name}", '
                f')'
            )
            output(f'skt.name = "{skt.name}"')
            dv = skt.default_value
            val = dv[:] if hasattr(dv, "foreach_get") else dv
            output(f"skt.default_value = {val}")
    output()


def colorramp(a, b):
    n = len(a.elements)
    output(f'ramp = node.color_ramp')
    compare(a, b, fstring="ramp.{k} = {va}")
    locs, deflocs = [0.0] * n, [0.0, 1.0]
    cols, defcols = [0.0] * (n << 2), BLACK + WHITE
    a.elements.foreach_get("position", locs), a.elements.foreach_get("color", cols)
    n = n - 2
    if n:
        output(
            f"for i in range({n}):\n"
            f"    ramp.elements.new(0.0)"
        )

    if not cmp(locs, deflocs):
        fes("ramp.elements", "position", locs, 1, 0)

    if not cmp(cols, defcols):
        fes(f'ramp.elements', "color", cols, 4, 0)


def mapping(a, b):
    output(f'map = node.mapping')
    compare(a, b, fstring="map.{k} = {va}")

    for i, c in enumerate(a.curves):
        n = len(c.points)
        pts, default = [0, 0] * n, [-1.0, -1.0, 1.0, 1.0]
        n -= 2
        if n:
            output(
                f'for i in range({n}):\n'
                f'    map.curves[{i}].points.new(0.0, 1.0)\n'
            )

        c.points.foreach_get("location", pts)
        if not cmp(pts, default):
            fes(f"map.curves[{i}].points", "location", pts, 2, 0)


def output(*args):
    s = " ".join(args) if args else ""
    buffer.append(s)


def compare(a, b, fstring="{k} = {va}", sockets="", i=0, ignore={'select'}):

    props = (
            (k, v)
        for k, v in a.bl_rna.properties.items()
        if (not v.is_readonly or k in ("mapping", "color_ramp"))
        and k not in ignore
    )

    for k, v in props:
        va = getattr(a, k)
        vb = getattr(b, k, None)

        if v.type in ('FLOAT', 'INT'):
            if v.is_array:
                if not isinstance(va, float):
                    va = va[:]
                if vb and not isinstance(vb, float):
                    vb = vb[:]

        if va != vb:
            if v.type == 'ENUM':
                va = f"'{va}'"
            elif v.type == 'STRING':
                va = f'"{va}"'
            elif v.type == 'POINTER':
                if k == "parent":
                    va = f'nodes.get("{va.name}")'
                elif a.type == 'GROUP':
                    return output(f'node.node_tree = groups.get("{a.node_tree.name}")')
                elif issubclass(v.fixed_type.__class__, bpy.types.ID):
                    va = repr(va).replace(f"['{va.name}']", f'.get("{va.name}")')
                elif k == "mapping":
                    return mapping(va, vb)
                elif k.startswith("color_ramp"):
                    return colorramp(va, vb)
            name = f'"{a.name}"' if hasattr(a, "name") else i
            output(fstring.format(**locals()))


def pnode(n, dummy):
    if n.type in ('GROUP_INPUT', 'GROUP_OUTPUT'):
        return group_io(n)
    nodetype = n.bl_rna.identifier
    default = LUT.setdefault(
        nodetype, dummy.nodes.new(nodetype)
    )

    output(f'node = nodes.new("{nodetype}")')
    compare(n, default, fstring="node.{k} = {va}")
    for sockets in ("inputs", "outputs"):
        for i, (a, b) in enumerate(
                zip(
                    getattr(n, sockets),
                    getattr(default, sockets),
                )
        ):

            compare(a, b, fstring='node.{sockets}[{name}].{k} = {va}', i=i, sockets=sockets)
    output()


def material_to_text(m):
    try:
        dummy = bpy.data.node_groups.get("DUMMY")
        if not dummy:
            output("import bpy")
            dummy = bpy.data.node_groups.new("DUMMY", "ShaderNodeTree")
            output("groups = {}  # for node groups")

        if hasattr(m, "use_nodes"):
            # material
            for gn in set(groups_in_tree(m.node_tree)):
                material_to_text(gn)
            nt = m.node_tree
            output(
                f"\n"
                f"{ul}#  Material: {m.name} \n{ul}\n"
                f'mat = bpy.data.materials.new("{m.name}")\n'
                f"mat.use_nodes = True\n"
                f"node_tree = mat.node_tree\n"
                f"nodes = node_tree.nodes\n"
                f"nodes.clear()\n"
                f"links = node_tree.links\n"
            )

        else:
            # group
            nt = m
            output(
                f"\n"
                f"{ul}#  NodeGroup: {m.name} \n{ul}\n"
                f'group = bpy.data.node_groups.new("{m.name}", "{m.bl_rna.identifier}")\n'
                f'groups["{m.name}"] = group\n'
                f"nodes = group.nodes\n"
                f"links = group.links\n"
            )

        for n in sorted(
            nt.nodes,
            key=lambda n: [n.location.x, n.location.y]
        ):
            pnode(n, dummy)
        if nt.links:
            output("#Links\n")
        for l in nt.links:
            to_node_inputs = l.to_node.inputs
            input_names = [inp.name for inp in to_node_inputs]
            
            # Use Counter to find duplicate names
            name_counts = Counter(input_names)
            
            if name_counts[l.to_socket.name] > 1:
                # If the name is duplicated, find the exact socket's index
                # and use that as the identifier.
                socket_index = list(to_node_inputs).index(l.to_socket)
                to_socket_identifier = f'[{socket_index}]'
            else:
                # Otherwise, use the name as the identifier.
                to_socket_identifier = f'["{l.to_socket.name}"]'
            output(
                f"links.new(\n"
                f'    nodes["{l.from_node.name}"].outputs["{l.from_socket.name}"],\n'
                f'    nodes["{l.to_node.name}"].inputs{to_socket_identifier}\n    )\n'
            )

    except Exception as e:
        print("There has been an ERROR")
        print(e, e.__traceback__.tb_lineno)
        return False  # failure

    if hasattr(m, "use_nodes"):
        bpy.data.node_groups.remove(dummy)
    return True  # success


if __name__ == "__main__":
    m = bpy.context.object.active_material
    material_to_text(m)

    text = bpy.data.texts.new(m.name)
    text.write("\n".join(buffer))