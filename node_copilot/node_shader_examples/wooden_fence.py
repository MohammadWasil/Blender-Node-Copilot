import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: wooden_fence
#--------------------------------------------

mat = bpy.data.materials.new("wooden_fence")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexImage")
node.location = (-600.0, -900.0)
node.name = "Image Texture.001"
node.image = bpy.data.images.get("Map #1.004")

node = nodes.new("ShaderNodeNormalMap")
node.location = (-300.0, -300.0)
node.label = "Normal/Map"

node = nodes.new("ShaderNodeTexImage")
node.location = (-300.0, 600.0)
node.image = bpy.data.images.get("Map #3.004")

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (10.0, 300.0)
node.inputs["Base Color"].default_value = (0.5882353186607361, 0.5882353186607361, 0.5882353186607361, 1.0)
node.inputs["Metallic"].default_value = 1.0
node.inputs["Roughness"].default_value = 0.858578622341156
node.inputs["Specular IOR Level"].default_value = 0.0
node.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (300.0, 300.0)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Normal Map"].outputs["Normal"],
    nodes["Principled BSDF"].inputs["Normal"]
    )

links.new(
    nodes["Image Texture"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Image Texture.001"].outputs["Color"],
    nodes["Normal Map"].inputs["Color"]
    )
