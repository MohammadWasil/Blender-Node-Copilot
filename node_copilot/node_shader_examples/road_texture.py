import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: road_texture
#--------------------------------------------

mat = bpy.data.materials.new("road_texture")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexCoord")
node.location = (-1240.0, 300.0)
node.parent = nodes.get("Frame")

node = nodes.new("ShaderNodeMapping")
node.location = (-1040.0, 300.0)
node.parent = nodes.get("Frame")

node = nodes.new("NodeReroute")
node.location = (-590.0, 45.0)
node.width = 16.0
node.parent = nodes.get("Frame.001")
node.socket_idname = "NodeSocketVector"
node.inputs["Input"].type = 'VECTOR'
node.inputs["Input"].bl_idname = "NodeSocketVector"
node.inputs["Input"].bl_label = "Vector"
node.inputs["Input"].default_value = (0.0, 0.0, 0.0)
node.outputs["Output"].type = 'VECTOR'
node.outputs["Output"].bl_idname = "NodeSocketVector"
node.outputs["Output"].bl_label = "Vector"
node.outputs["Output"].default_value = (0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-540.0, -60.0)
node.label = "Displacement"
node.parent = nodes.get("Frame.001")
node.image = bpy.data.images.get("Road007_2K-JPG_Displacement.jpg.001")

node = nodes.new("ShaderNodeTexImage")
node.location = (-540.0, 220.0)
node.name = "Image Texture.002"
node.label = "Roughness"
node.parent = nodes.get("Frame.001")
node.image = bpy.data.images.get("Road007_2K-JPG_Roughness.jpg.001")

node = nodes.new("ShaderNodeTexImage")
node.location = (-540.0, 500.0)
node.name = "Image Texture.001"
node.label = "Base Color"
node.parent = nodes.get("Frame.001")
node.image = bpy.data.images.get("Road007_2K-JPG_Color.jpg.001")


node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (10.0, 300.0)

node = nodes.new("ShaderNodeDisplacement")
node.location = (110.0, -400.0)

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (300.0, 300.0)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Image Texture"].outputs["Color"],
    nodes["Displacement"].inputs["Height"]
    )

links.new(
    nodes["Displacement"].outputs["Displacement"],
    nodes["Material Output"].inputs["Displacement"]
    )

links.new(
    nodes["Image Texture.001"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Image Texture.002"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Roughness"]
    )

links.new(
    nodes["Reroute"].outputs["Output"],
    nodes["Image Texture.001"].inputs["Vector"]
    )

links.new(
    nodes["Reroute"].outputs["Output"],
    nodes["Image Texture.002"].inputs["Vector"]
    )

links.new(
    nodes["Reroute"].outputs["Output"],
    nodes["Image Texture"].inputs["Vector"]
    )

links.new(
    nodes["Mapping"].outputs["Vector"],
    nodes["Reroute"].inputs["Input"]
    )

links.new(
    nodes["Texture Coordinate"].outputs["UV"],
    nodes["Mapping"].inputs["Vector"]
    )
