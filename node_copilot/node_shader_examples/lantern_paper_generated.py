import bpy
groups = {}  # for node groups

#--------------------------------------------
#  Material: cube_generated
#--------------------------------------------

mat = bpy.data.materials.new("cube_generated")
mat.use_nodes = True
node_tree = mat.node_tree
nodes = node_tree.nodes
nodes.clear()
links = node_tree.links

node = nodes.new("ShaderNodeBsdfPrincipled")
node.location = (-391.88165283203125, 302.8250732421875)
node.inputs["Roughness"].default_value = 0.0
node.inputs["Transmission Weight"].default_value = 1.0

node = nodes.new("ShaderNodeBsdfTranslucent")
node.location = (-102.66951751708984, 148.81661987304688)

node = nodes.new("ShaderNodeMixShader")
node.location = (116.23619079589844, 284.9114074707031)

node = nodes.new("ShaderNodeOutputMaterial")
node.location = (390.24713134765625, 292.9372863769531)

#Links

links.new(
    nodes["Translucent BSDF"].outputs["BSDF"],
    nodes["Mix Shader"].inputs[2]
    )

links.new(
    nodes["Principled BSDF"].outputs["BSDF"],
    nodes["Mix Shader"].inputs[1]
    )

links.new(
    nodes["Mix Shader"].outputs["Shader"],
    nodes["Material Output"].inputs["Surface"]
    )
