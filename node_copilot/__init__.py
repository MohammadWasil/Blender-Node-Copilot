
"""Module for Node CoPilot Blender UI"""

"Module for Blender UI"

bl_info = {
    "name": "Blender Node CoPilot",
    "author": "Mohammad Wasil Saleem",
    "version": (0, 0, 1),
    "blender": (4, 3, 2),
    "location": "3D View > Sidebar > Node CoPilot",
    "description": "AI assistant for Blender Node Graphs",
    "category": "Node",
}

import sys
import os
import bpy
import importlib

# Remove this when deploying as an addon
# only for developement purposes.
#REPO_PATH = "D:/Blender/Blender Node Copilot/node_copilot"
#if REPO_PATH not in sys.path:
#    sys.path.append(REPO_PATH)

from bpy.utils import register_class, unregister_class

from src.blender_ui.data.properties import ChatMessage, ChatboxData
from src.blender_ui.operators.chat_operator import ChatOperator
from src.blender_ui.operators.clear_chat import ChatClearHistory
from src.blender_ui.operators.node_generator import ButtonOperator
from src.blender_ui.ui.panel import NodeCoPilotPanel

_classes = [
    ChatMessage,
    #ChatboxData,
    ChatOperator,
    ChatClearHistory,
    ButtonOperator,
    NodeCoPilotPanel,
]

def register():

    for cls in _classes:
        register_class(cls)
    # 1. Define a StringProperty with the 'AREA' subtype to create a multi-line text box.
    bpy.types.Scene.my_mesh_placeholder = bpy.props.PointerProperty(
        type=bpy.types.Object,
        name="Mesh Placeholder",
        poll=lambda self, obj: obj.type == 'MESH'
    )
    
    bpy.types.Scene.chat_input = bpy.props.StringProperty(
        name="Chat Input",
        default=""
    )
    
    bpy.types.Scene.chat_history = bpy.props.CollectionProperty(type=ChatMessage)
    
    # Register the PropertyGroup and the PointerProperty to it
    bpy.utils.register_class(ChatboxData)
    bpy.types.Scene.chatbox_data = bpy.props.PointerProperty(type=ChatboxData)
    
def unregister():
    for cls in _classes:
        unregister_class(cls)

if __name__ == '__main__':
    register()