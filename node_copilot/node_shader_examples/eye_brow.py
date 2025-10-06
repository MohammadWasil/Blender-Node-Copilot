import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: eye_brow
#--------------------------------------------

mat = bpy.data.materials.new("eye_brow")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexImage")
node.location = (-1378.2178955078125, -869.6318359375)
node.name = "Image Texture.001"
node.image = bpy.data.images.get("hair_anisotropy_rotation.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("NodeReroute")
node.location = (-1112.7149658203125, -2049.646728515625)
node.width = 16.0
node.name = "Reroute.008"

node = nodes.new("NodeFrame")
node.location = (-1035.5999755859375, -1123.199951171875)
node.width = 2090.39990234375
node.height = 1296.400146484375
node.label = "Fake Anisotropy"
node.use_custom_color = True
node.color = (0.6000000238418579, 0.6000000238418579, 0.6000000238418579)

node = nodes.new("ShaderNodeTexImage")
node.location = (-357.8899230957031, 467.0393981933594)
node.name = "Image Texture.005"
node.show_texture = True
node.image = bpy.data.images.get("hair_sss_value.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-356.9468994140625, 190.2113800048828)
node.name = "Image Texture.004"
node.image = bpy.data.images.get("hair_sss_color.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-354.29241943359375, -333.7740173339844)
node.image = bpy.data.images.get("hair_anisotropy.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-351.4384765625, 744.4252319335938)
node.name = "Image Texture.002"
node.image = bpy.data.images.get("hair_diffuse.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-350.5947570800781, -70.0701904296875)
node.name = "Image Texture.003"
node.image = bpy.data.images.get("hair_roughness.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTexImage")
node.location = (-344.3995056152344, 1031.590576171875)
node.name = "Image Texture.006"
node.image = bpy.data.images.get("hair_specular.png.012")
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeNewGeometry")
node.location = (29.7685546875, -444.373046875)
node.parent = nodes.get("Frame")
node.outputs["Position"].hide = True
node.outputs["Normal"].hide = True
node.outputs["Tangent"].hide = True
node.outputs["True Normal"].hide = True
node.outputs["Parametric"].hide = True
node.outputs["Backfacing"].hide = True
node.outputs["Pointiness"].hide = True
node.outputs["Random Per Island"].hide = True

node = nodes.new("ShaderNodeVectorTransform")
node.location = (31.545166015625, -524.340087890625)
node.parent = nodes.get("Frame")
node.convert_from = 'CAMERA'
node.convert_to = 'WORLD'
node.inputs["Vector"].default_value = (1.0, 0.0, 0.0)

node = nodes.new("ShaderNodeTangent")
node.location = (200.0020751953125, -619.47705078125)
node.width = 218.75131225585938
node.name = "Tangent.002"
node.parent = nodes.get("Frame")
node.direction_type = 'UV_MAP'
node.uv_map = "UV_Allignment"

node = nodes.new("ShaderNodeVectorRotate")
node.location = (275.8187255859375, -402.266357421875)
node.parent = nodes.get("Frame")
node.inputs["Center"].hide = True
node.inputs["Angle"].default_value = -3.4627325534820557
#node.inputs["Rotation"].hide = True

node = nodes.new("ShaderNodeNewGeometry")
node.location = (277.241455078125, -713.1064453125)
node.name = "Geometry.001"
node.parent = nodes.get("Frame")
node.outputs["Position"].hide = True
node.outputs["Tangent"].hide = True
node.outputs["True Normal"].hide = True
node.outputs["Incoming"].hide = True
node.outputs["Parametric"].hide = True
node.outputs["Backfacing"].hide = True
node.outputs["Pointiness"].hide = True
node.outputs["Random Per Island"].hide = True

node = nodes.new("ShaderNodeValToRGB")
node.location = (379.18927001953125, -693.5789794921875)
node.name = "ColorRamp.001"
ramp = node.color_ramp
ramp.elements.foreach_set(
       "color", [
        0.0, 0.0, 0.0, 1.0,
        0.10796529054641724, 0.10796529054641724, 0.10796529054641724, 1.0
        ])
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeMapRange")
node.location = (380.3316650390625, -792.517578125)
node.name = "Map Range.001"
node.parent = nodes.get("Frame")
node.inputs["To Min"].default_value = 1.7100000381469727
node.inputs["To Max"].default_value = 3.819999933242798

node = nodes.new("ShaderNodeMapRange")
node.location = (384.891845703125, -1027.908935546875)
node.parent = nodes.get("Frame")
node.inputs["To Max"].default_value = 0.3200001120567322

node = nodes.new("ShaderNodeTangent")
node.location = (390.1179504394531, -947.891357421875)
node.width = 218.75131225585938
node.name = "Tangent.003"
node.direction_type = 'UV_MAP'
node.uv_map = "UV_Allignment"

node = nodes.new("ShaderNodeVectorRotate")
node.location = (632.833984375, -580.4912109375)
node.name = "Vector Rotate.001"
node.parent = nodes.get("Frame")
node.inputs["Center"].hide = True
node.inputs["Angle"].default_value = 1.5707963705062866
#node.inputs["Rotation"].hide = True

node = nodes.new("ShaderNodeVectorMath")
node.location = (819.1464233398438, -482.046875)
node.name = "Vector Math.003"
node.parent = nodes.get("Frame")
node.operation = 'DOT_PRODUCT'
#node.outputs["Vector"].enabled = False
#node.outputs["Value"].enabled = True

node = nodes.new("ShaderNodeMix")
node.location = (841.0948486328125, 180.0)
node.data_type = 'RGBA'
node.inputs["Factor"].default_value = 0.0
#node.inputs["A"].enabled = False
#node.inputs["B"].enabled = False
#node.inputs["A"].enabled = True
node.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
#node.inputs["B"].enabled = True
node.inputs["B"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
#node.outputs["Result"].enabled = False
#node.outputs["Result"].enabled = True

node = nodes.new("ShaderNodeMath")
node.location = (986.7313842773438, -478.7080078125)
node.name = "Math.031"
node.parent = nodes.get("Frame")
node.operation = 'ABSOLUTE'
#node.inputs["Value"].enabled = False
node.inputs["Value"].default_value = 0.0

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (1011.0948486328125, 300.0)
node.distribution = 'GGX'
node.subsurface_method = 'BURLEY'
node.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["IOR"].default_value = 1.4500000476837158
node.inputs["Subsurface Weight"].default_value = 1.0
node.inputs["Subsurface Scale"].default_value = 0.0
#node.inputs["Subsurface Anisotropy"].enabled = False
node.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Emission Strength"].default_value = 1.0

node = nodes.new("ShaderNodeMath")
node.location = (1159.69091796875, -473.17138671875)
node.name = "Math.033"
node.parent = nodes.get("Frame")
node.operation = 'POWER'
node.use_clamp = True
node.inputs["Value"].default_value = 0.0

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (1335.27783203125, 301.35162353515625)
node.is_active_output = False
node.target = 'CYCLES'

node = nodes.new("ShaderNodeRGBCurve")
node.location = (1337.0750732421875, -336.35693359375)
node.parent = nodes.get("Frame")
map = node.mapping
map.curves[0].points.foreach_set(
       "location", [
        0.0, 0.0,
        1.0, 1.0
        ])
map.curves[1].points.foreach_set(
       "location", [
        0.0, 0.0,
        1.0, 1.0
        ])
map.curves[2].points.foreach_set(
       "location", [
        0.0, 0.0,
        1.0, 1.0
        ])
for i in range(2):
    map.curves[3].points.new(0.0, 1.0)

map.curves[3].points.foreach_set(
       "location", [
        0.0, 0.37019211053848267,
        0.26471900939941406, 0.36160698533058167,
        0.5998827815055847, 0.17101670801639557,
        1.0, 0.044642865657806396
        ])
node.inputs["Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("NodeReroute")
node.location = (1347.820556640625, 420.1413879394531)
node.width = 16.0
node.name = "Reroute.002"

node = nodes.new("NodeReroute")
node.location = (1347.820556640625, 459.3471374511719)
node.width = 16.0
node.name = "Reroute.001"

node = nodes.new("NodeReroute")
node.location = (1347.820556640625, 703.22509765625)
node.width = 16.0

node = nodes.new("NodeReroute")
node.location = (1349.111083984375, 386.02508544921875)
node.width = 16.0
node.name = "Reroute.003"

node = nodes.new("ShaderNodeAttribute")
node.location = (1400.294677734375, -80.719970703125)
node.parent = nodes.get("Frame")
node.attribute_name = "Col_detail"
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeValToRGB")
node.location = (1624.633544921875, -39.885986328125)
node.name = "ColorRamp.006"
node.parent = nodes.get("Frame")
ramp = node.color_ramp
for i in range(1):
    ramp.elements.new(0.0)
ramp.elements.foreach_set(
       "position", [
        0.10211268067359924,
        0.24647879600524902,
        0.8204221129417419
        ])
ramp.elements.foreach_set(
       "color", [
        1.0, 1.0, 1.0, 1.0,
        0.4999999403953552, 0.4999999403953552, 0.4999999403953552, 1.0,
        0.0, 0.0, 0.0, 1.0
        ])
node.outputs["Color"].default_value = (0.0, 0.0, 0.0, 0.0)

node = nodes.new("ShaderNodeMath")
node.location = (1636.49365234375, -416.8125)
node.name = "Math.032"
node.parent = nodes.get("Frame")
node.operation = 'MULTIPLY'
node.use_clamp = True
node.inputs["Value"].default_value = 0.5199999809265137
node.inputs["Value"].default_value = 0.0

node = nodes.new("ShaderNodeMix")
node.location = (1788.100341796875, 200.36380004882812)
node.name = "Mix.001"
node.data_type = 'RGBA'
node.inputs["Factor"].default_value = 0.0
#node.inputs["A"].enabled = False
#node.inputs["B"].enabled = False
#node.inputs["A"].enabled = True
node.inputs["A"].default_value = (0.0, 0.0, 0.0, 1.0)
#node.inputs["B"].enabled = True
node.inputs["B"].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
#node.outputs["Result"].enabled = False
#node.outputs["Result"].enabled = True

node = nodes.new("ShaderNodeMath")
node.location = (1920.5174560546875, -262.113525390625)
node.name = "Math.034"
node.parent = nodes.get("Frame")
node.operation = 'MULTIPLY'
node.use_clamp = True
node.inputs["Value"].default_value = 0.5199999809265137
node.inputs["Value"].default_value = 0.0

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (1958.100341796875, 320.3638000488281)
node.width = 244.44781494140625
node.name = "Principled BSDF.001"
node.distribution = 'GGX'
node.subsurface_method = 'BURLEY'
node.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Roughness"].default_value = 0.48615920543670654
node.inputs["IOR"].default_value = 1.4500000476837158
node.inputs["Subsurface Weight"].default_value = 1.0
node.inputs["Subsurface Scale"].default_value = 0.0
#node.inputs["Subsurface Anisotropy"].enabled = False
node.inputs["Emission Color"].default_value = (0.0, 0.0, 0.0, 1.0)
node.inputs["Emission Strength"].default_value = 1.0

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (2302.104248046875, 314.8807373046875)
node.name = "Material Output.001"
node.target = 'EEVEE'

#Links

links.new(
    nodes["Image Texture"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Anisotropic"]
    )

links.new(
    nodes["Image Texture.001"].outputs["Color"],
    nodes["ColorRamp.001"].inputs["Fac"]
    )

links.new(
    nodes["Image Texture.003"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Roughness"]
    )

links.new(
    nodes["ColorRamp.001"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Anisotropic Rotation"]
    )

links.new(
    nodes["Tangent.003"].outputs["Tangent"],
    nodes["Principled BSDF"].inputs["Tangent"]
    )

links.new(
    nodes["Tangent.002"].outputs["Tangent"],
    nodes["Vector Rotate.001"].inputs["Vector"]
    )

links.new(
    nodes["Vector Math.003"].outputs["Value"],
    nodes["Math.031"].inputs[0]
    )

links.new(
    nodes["Math.031"].outputs["Value"],
    nodes["Math.033"].inputs[0]
    )

links.new(
    nodes["RGB Curves"].outputs["Color"],
    nodes["Math.032"].inputs[0]
    )

links.new(
    nodes["Vector Rotate"].outputs["Vector"],
    nodes["Vector Math.003"].inputs[0]
    )

links.new(
    nodes["Vector Transform"].outputs["Vector"],
    nodes["Vector Rotate"].inputs["Axis"]
    )

links.new(
    nodes["Geometry"].outputs["Incoming"],
    nodes["Vector Rotate"].inputs["Vector"]
    )

links.new(
    nodes["Geometry.001"].outputs["Normal"],
    nodes["Vector Rotate.001"].inputs["Axis"]
    )

links.new(
    nodes["Vector Rotate.001"].outputs["Vector"],
    nodes["Vector Math.003"].inputs[1]
    )

links.new(
    nodes["Math.033"].outputs["Value"],
    nodes["RGB Curves"].inputs["Color"]
    )

links.new(
    nodes["Math.032"].outputs["Value"],
    nodes["Math.034"].inputs[0]
    )

links.new(
    nodes["Attribute"].outputs["Fac"],
    nodes["ColorRamp.006"].inputs["Fac"]
    )

links.new(
    nodes["ColorRamp.006"].outputs["Color"],
    nodes["Math.034"].inputs[1]
    )

links.new(
    nodes["Reroute.008"].outputs["Output"],
    nodes["Map Range"].inputs["Value"]
    )

links.new(
    nodes["Math.034"].outputs["Value"],
    nodes["Principled BSDF.001"].inputs["Specular IOR Level"]
    )

links.new(
    nodes["Image Texture.001"].outputs["Color"],
    nodes["Reroute.008"].inputs["Input"]
    )

links.new(
    nodes["Reroute.008"].outputs["Output"],
    nodes["Map Range.001"].inputs["Value"]
    )

links.new(
    nodes["Map Range.001"].outputs["Result"],
    nodes["Vector Rotate.001"].inputs["Angle"]
    )

links.new(
    nodes["Image Texture.006"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Specular IOR Level"]
    )

links.new(
    nodes["Reroute.003"].outputs["Output"],
    nodes["Principled BSDF.001"].inputs["Roughness"]
    )

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Principled BSDF.001"].outputs["BSDF"],
    nodes["Material Output.001"].inputs["Surface"]
    )

links.new(
    nodes["Image Texture.002"].outputs["Color"],
    nodes["Reroute"].inputs["Input"]
    )

links.new(
    nodes["Image Texture.005"].outputs["Color"],
    nodes["Reroute.001"].inputs["Input"]
    )

links.new(
    nodes["Image Texture.004"].outputs["Color"],
    nodes["Reroute.002"].inputs["Input"]
    )

links.new(
    nodes["Image Texture.003"].outputs["Color"],
    nodes["Reroute.003"].inputs["Input"]
    )

links.new(
    nodes["Image Texture.002"].outputs["Color"],
    nodes["Mix"].inputs[6]
    )

links.new(
    nodes["Image Texture.004"].outputs["Color"],
    nodes["Mix"].inputs[7]
    )

links.new(
    nodes["Image Texture.005"].outputs["Color"],
    nodes["Mix"].inputs[0]
    )

links.new(
    nodes["Image Texture.005"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Subsurface Scale"]
    )

links.new(
    nodes["Mix"].outputs["Result"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Reroute"].outputs["Output"],
    nodes["Mix.001"].inputs[6]
    )

links.new(
    nodes["Reroute.002"].outputs["Output"],
    nodes["Mix.001"].inputs[7]
    )

links.new(
    nodes["Reroute.001"].outputs["Output"],
    nodes["Mix.001"].inputs[0]
    )

links.new(
    nodes["Reroute.001"].outputs["Output"],
    nodes["Principled BSDF.001"].inputs["Subsurface Scale"]
    )

links.new(
    nodes["Mix.001"].outputs["Result"],
    nodes["Principled BSDF.001"].inputs["Base Color"]
    )
