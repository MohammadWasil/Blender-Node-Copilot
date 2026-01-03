import bpy

class ChatClearHistory(bpy.types.Operator):
    bl_idname = "chat.clear_history"
    bl_label = "Clear Chat"
    bl_description = "Delete all messages in the chat history"
    
    def execute(self, context):
        # This empties the entire collection at once
        context.scene.chat_history.clear()
        
        # Optional: Reset the input field too
        context.scene.chat_input = ""
        
        return {'FINISHED'}