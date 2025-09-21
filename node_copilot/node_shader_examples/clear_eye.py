import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: clear_eye
#--------------------------------------------

mat = bpy.data.materials.new("clear_eye")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (-3.250927686691284, 309.98931884765625)
node.inputs["Roughness"].default_value = 0.0
node.inputs["Transmission Weight"].default_value = 1.0

node = nodes.new("ShaderNodeValue")
node.location = (271.90350341796875, 136.98312377929688)

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (497.79034423828125, 304.2071533203125)
node.inputs["Surface"].show_expanded = True

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Value"].outputs["Value"],
    nodes["Material Output"].inputs["Thickness"]
    )
