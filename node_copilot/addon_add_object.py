# To make this add-on installable, create an extension with it:
# https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html

import bpy
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class
from bpy.types import Operator, Panel


class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.node_generator_button"
    bl_label = "Panel Node Generator"

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add()
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