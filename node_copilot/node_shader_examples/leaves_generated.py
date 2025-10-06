import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: leave_generated
#--------------------------------------------

mat = bpy.data.materials.new("leave_generated")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexImage")
node.location = (-640.0, 420.0)
node.image = bpy.data.images.get("Twig_Leaf_Long_Diffuse_C1.png.002")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-617.2301025390625, 142.96298217773438)
node.name = "Image Texture.001"
node.image = bpy.data.images.get("Twig_Leaf_Long_Normal.png.002")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-541.025390625, -169.80352783203125)
node.name = "Image Texture.002"
node.show_texture = True
node.image = bpy.data.images.get("Twig_Leaf_Long_Opacity.png.002")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeNormalMap")
node.location = (-320.0, 120.0)

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (10.0, 300.0)
node.distribution = 'GGX'
node.subsurface_method = 'BURLEY'
node.inputs["IOR"].default_value = 1.4500000476837158
#node.inputs["Subsurface Anisotropy"].enabled = False
node.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Emission Strength"].default_value = 1.0

node = nodes.new("ShaderNodeBsdfTranslucent")
node.location = (84.21241760253906, 456.11737060546875)

node = nodes.new("ShaderNodeBsdfTransparent")
node.location = (440.3087463378906, 128.85995483398438)

node = nodes.new("ShaderNodeMixShader")
node.location = (532.8779907226562, 330.87384033203125)

node = nodes.new("ShaderNodeMixShader")
node.location = (752.8779907226562, 294.0375061035156)
node.name = "Mix Shader.001"

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (986.9733276367188, 249.90260314941406)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Mix Shader"].inputs[1]
    )

links.new(
    nodes["Image Texture"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Image Texture.001"].outputs["Color"],
    nodes["Normal Map"].inputs["Color"]
    )

links.new(
    nodes["Normal Map"].outputs["Normal"],
    nodes["Principled BSDF"].inputs["Normal"]
    )

links.new(
    nodes["Image Texture.002"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Alpha"]
    )

links.new(
    nodes["Translucent BSDF"].outputs["BSDF"],
    nodes["Mix Shader"].inputs[2]
    )

links.new(
    nodes["Image Texture"].outputs["Color"],
    nodes["Translucent BSDF"].inputs["Color"]
    )

links.new(
    nodes["Mix Shader.001"].outputs["Shader"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Transparent BSDF"].outputs["BSDF"],
    nodes["Mix Shader.001"].inputs[1]
    )

links.new(
    nodes["Image Texture.002"].outputs["Color"],
    nodes["Mix Shader.001"].inputs["Fac"]
    )

links.new(
    nodes["Mix Shader"].outputs["Shader"],
    nodes["Mix Shader.001"].inputs[2]
    )
