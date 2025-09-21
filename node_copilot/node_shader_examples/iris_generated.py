import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: iris_generated
#--------------------------------------------

mat = bpy.data.materials.new("iris_generated")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexCoord")
node.location = (-1026.843994140625, 282.37127685546875)

node = nodes.new("ShaderNodeTexNoise")
node.location = (-865.1412353515625, 42.90463638305664)

node = nodes.new("ShaderNodeMapping")
node.location = (-856.5115356445312, 334.0043029785156)
node.vector_type = 'NORMAL'
node.inputs["Scale"].default_value = (1.0, 0.0, 1.0)

node = nodes.new("ShaderNodeMix")
node.location = (-639.7274169921875, 250.78775024414062)
node.data_type = 'RGBA'
node.inputs["Factor"].default_value = 0.25

node = nodes.new("ShaderNodeTexVoronoi")
node.location = (-447.0313415527344, 299.72637939453125)
node.show_texture = True
node.inputs["Scale"].default_value = 3.000001907348633

node = nodes.new("ShaderNodeValToRGB")
node.location = (-257.3262023925781, 249.3369903564453)
ramp = node.color_ramp
ramp.elements.foreach_set(
       "position", [
        0.32363635301589966,
        1.0
        ])
ramp.elements.foreach_set(
       "color", [
        0.06480289995670319, 0.030713483691215515, 0.015996305271983147, 1.0,
        0.25818151235580444, 0.11193251609802246, 0.05286070331931114, 1.0
        ])

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (22.2737979888916, 300.0)
node.inputs["Base Color"].default_value = (0.002076924778521061, 0.0, 0.8003553152084351, 1.0)

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (312.2738037109375, 300.0)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Color Ramp"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Texture Coordinate"].outputs["Object"],
    nodes["Mapping"].inputs["Vector"]
    )

links.new(
    nodes["Mapping"].outputs["Vector"],
    nodes["Mix"].inputs[4]
    )

links.new(
    nodes["Noise Texture"].outputs["Fac"],
    nodes["Mix"].inputs[7]
    )

links.new(
    nodes["Mapping"].outputs["Vector"],
    nodes["Mix"].inputs[6]
    )

links.new(
    nodes["Mix"].outputs["Result"],
    nodes["Voronoi Texture"].inputs["Vector"]
    )

links.new(
    nodes["Voronoi Texture"].outputs["Distance"],
    nodes["Color Ramp"].inputs["Fac"]
    )
