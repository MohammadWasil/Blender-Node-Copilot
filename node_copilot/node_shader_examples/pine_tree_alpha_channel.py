import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: pine_tree_alpha_channel
#--------------------------------------------

mat = bpy.data.materials.new("pine_tree_alpha_channel")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexImage")
node.location = (-440.0, 210.0)
node.label = "BASE COLOR"
node.image = bpy.data.images.get("Image_9.004")

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (10.0, 300.0)
node.inputs["Roughness"].default_value = 0.6000000238418579

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (300.0, 300.0)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Image Texture"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Image Texture"].outputs["Alpha"],
    nodes["Principled BSDF"].inputs["Alpha"]
    )
