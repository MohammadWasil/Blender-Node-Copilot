import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: emission_light
#--------------------------------------------

mat = bpy.data.materials.new("emission_light")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeNormalMap")
node.location = (-300.0, -300.0)
node.label = "Normal/Map"

node = nodes.new("ShaderNodeEmission")
node.location = (10.0, 300.0)
node.inputs["Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Strength"].default_value = 0.0

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (300.0, 300.0)
node.inputs["Surface"].show_expanded = True

#Links

links.new(
    nodes["Emission"].outputs["Emission"],
    nodes["Material Output"].inputs["Surface"]
    )
