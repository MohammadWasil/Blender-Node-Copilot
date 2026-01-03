import bpy
from bpy.props import StringProperty, CollectionProperty
from bpy.types import PropertyGroup

class ChatMessage(PropertyGroup):
    content: StringProperty(name="Chat", default="")
    sender: StringProperty(name="sender", default="USER") # To track if it's "USER" or "LLM"

class ChatboxData(PropertyGroup):
    chat_history: CollectionProperty(type=ChatMessage)
    chat_input: StringProperty(name="Chat Input", default="")