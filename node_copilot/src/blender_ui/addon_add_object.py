# To make this add-on installable, create an extension with it:
# https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html

import os, sys

import bpy
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class
from bpy.types import Operator, Panel

# add the location of the python files into the system path
dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir)

# First import the script
import node_copilot.material
#import file_generator

# this next part forces a reload in case you edit the source after you first start the blender session
import imp
imp.reload(material)
#imp.reload(file_generator)

from .node_copilot.material import assign_principled_material
#from file_generator import create_and_load_py_file

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.node_generator_button"
    bl_label = "Panel Node Generator"
    
    # The py file which will hold all the generated shader nodes from the llm.
    file_to_create = "generated_node.txt" # File name saved on the Hard drive
    text_block_name = "generated_node.txt" # text block name saved in the Text Editor inside Blender.
    
    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add()
    
        # Example usage: apply a red material to the active object
        plane = bpy.context.active_object
        assign_principled_material(plane, color=(1, 0, 0, 1), name="RedMaterial")
        #create_and_load_py_file(file_to_create, text_block_name, content = "# this is the generated content from SLM")

        return {'FINISHED'}
 

class NodeCoPilotPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Node CoPilot Panel"
    bl_idname = "OBJECT_PT_node_copilot"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Node CoPilot" # addon name on the panel itself.

    def draw(self, context):
        layout = self.layout

        obj = context.object
        
        layout = self.layout
        layout.prop(context.scene, "copilot_text", text="")
        layout.operator(ButtonOperator.bl_idname, text="Generate Nodes", icon='WORLD_DATA')

_classes = [ButtonOperator, NodeCoPilotPanel]

def register():
    # 1. Define a StringProperty with the 'AREA' subtype to create a multi-line text box.
    # This property is registered on the global Blender Scene, so its value persists.
    bpy.types.Scene.copilot_text = bpy.props.StringProperty(
        name="Your Text",
        description="Type Here",
        default=""
    )
    for cls in _classes:
        register_class(cls)

def unregister():
    for cls in _classes:
        unregister_class(cls)


if __name__ == '__main__':
    register()