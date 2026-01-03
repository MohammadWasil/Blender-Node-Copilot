import bpy

def re_render_chat_panel():
    # Refreshes the panel to show the response from LLM.
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()