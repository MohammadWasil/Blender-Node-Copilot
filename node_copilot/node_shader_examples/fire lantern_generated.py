import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: cube_generated_fire_lantern
#--------------------------------------------

mat = bpy.data.materials.new("cube_generated_fire_lantern")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeTexCoord")
node.location = (-512.2546997070312, 280.75091552734375)

node = nodes.new("ShaderNodeMapping")
node.location = (-331.59844970703125, 359.22113037109375)
node.inputs["Location"].default_value = (0.19999992847442627, 0.0, 0.0)
node.inputs["Rotation"].default_value = (0.0, 1.5707963705062866, 0.0)
node.inputs["Scale"].default_value = (1.0, 1.0, 1.3000000715255737)

node = nodes.new("ShaderNodeTexGradient")
node.location = (-156.10372924804688, 280.59161376953125)
node.show_texture = True

node = nodes.new("ShaderNodeValToRGB")
node.location = (24.000001907348633, 304.4724426269531)
ramp = node.color_ramp
ramp.elements.foreach_set(
       "position", [
        0.2436363250017166,
        0.770909309387207
        ])
ramp.elements.foreach_set(
       "color", [
        0.962988018989563, 1.0, 0.026000022888183594, 1.0,
        1.0, 0.09580865502357483, 0.1007322371006012, 1.0
        ])

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (303.7956237792969, 343.4322814941406)

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (593.795654296875, 343.4322814941406)

#Links

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Material Output"].inputs["Surface"]
    )

links.new(
    nodes["Mapping"].outputs["Vector"],
    nodes["Gradient Texture"].inputs["Vector"]
    )

links.new(
    nodes["Color Ramp"].outputs["Color"],
    nodes["Principled BSDF"].inputs["Base Color"]
    )

links.new(
    nodes["Gradient Texture"].outputs["Color"],
    nodes["Color Ramp"].inputs["Fac"]
    )

links.new(
    nodes["Texture Coordinate"].outputs["Normal"],
    nodes["Mapping"].inputs["Vector"]
    )
