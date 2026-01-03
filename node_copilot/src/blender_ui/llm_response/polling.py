from src.blender_ui.data import state
from src.blender_ui.utils.rerender import re_render_chat_panel

def check_llm_result(scene):
    if state.llm_result is not None:
        # Safe: updating Blender or UI
        # Add LLM Response
        llm_msg = scene.chat_history.add()
        llm_msg.content = state.llm_result #"""Hello! 😊 
                            #How can I help you today?""" # replce with LLm invoke function here.
        llm_msg.sender = "LLM"
        
        # Reset the variable
        state.llm_result = None

        re_render_chat_panel()
        
        return None  # Stop the timer
    return 0.2  # Check again in 0.2 seconds