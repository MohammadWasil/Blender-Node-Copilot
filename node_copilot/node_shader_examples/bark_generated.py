import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: bark_generated
#--------------------------------------------

mat = bpy.data.materials.new("bark_generated")
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
node.name = "Image Texture.002"
node.label = "Normal"
node.parent = nodes.get("Frame.001")
node.image = bpy.data.images.get("bark_willow_nor_gl_2k.exr.001")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-540.0, 220.0)
node.name = "Image Texture.001"
node.label = "Roughness"
node.parent = nodes.get("Frame.001")
node.image = bpy.data.images.get("bark_willow_rough_2k.exr.001")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-540.0, 500.0)
node.label = "Base Color"
node.parent = nodes.get("Frame.001")
node.image = bpy.data.images.get("bark_willow_diff_2k.jpg.001")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeNormalMap")
node.location = (-240.0, -60.0)

#node = nodes.new("NodeFrame")
#node.width = 400.0
#node.height = 421.20001220703125
#node.label = "Mapping"

#node = nodes.new("NodeFrame")
#node.width = 356.4000244140625
#node.height = 899.5999755859375
#node.name = "Frame.001"
#node.label = "Textures"

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (10.0, 300.0)
node.distribution = 'GGX'
node.subsurface_method = 'BURLEY'
node.inputs["IOR"].default_value = 1.4500000476837158
#node.inputs["Subsurface Anisotropy"].enabled = False
node.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Emission Strength"].default_value = 1.0

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
    nodes["Image Texture.001"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Roughness"]
    )

links.new(
    nodes["Image Texture.002"].outputs["Color"],
    nodes["Normal Map"].inputs["Color"]
    )

links.new(
    nodes["Normal Map"].outputs["Normal"],
    nodes["Principled BSDF"].inputs["Normal"]
    )

links.new(
    nodes["Reroute"].outputs["Output"],
    nodes["Image Texture"].inputs["Vector"]
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
    nodes["Mapping"].outputs["Vector"],
    nodes["Reroute"].inputs["Input"]
    )

links.new(
    nodes["Texture Coordinate"].outputs["UV"],
    nodes["Mapping"].inputs["Vector"]
    )
