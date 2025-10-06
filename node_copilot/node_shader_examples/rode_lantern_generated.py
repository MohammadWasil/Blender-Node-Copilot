import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: rode_lantern_generated
#--------------------------------------------

mat = bpy.data.materials.new("rode_lantern_generated")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (10.0, 300.0)
node.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Roughness"].default_value = 0.0
node.inputs["Alpha"].default_value = 0.43096232414245605

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (300.0, 300.0)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )
