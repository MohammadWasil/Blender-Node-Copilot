import bpy
import threading
import textwrap
from src.blender_ui.llm_response.polling import check_llm_result
from src.blender_ui.llm_response.worker import worker


class ChatOperator(bpy.types.Operator):
    bl_idname = "object.chat_operator"
    bl_label = "Send Message"
    
    def execute(self, context):
        scene = context.scene
        if scene.chat_input:
            # Append the message to the history with a newline
            #scene.chat_history += f"User: {scene.chat_input}\n"
            new_msg = scene.chat_history.add()
            new_msg.content = scene.chat_input # Take what's in the input field
            new_msg.sender = "USER"
            
            thread = threading.Thread(target=worker, args=(new_msg.content,))
            thread.start()

            # Start polling
            bpy.app.timers.register(lambda: check_llm_result(scene))

            # Clear the input box
            scene.chat_input = ""
            
        return {'FINISHED'}