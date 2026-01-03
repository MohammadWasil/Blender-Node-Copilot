import bpy
from src.blender_ui.utils.text_wrap import draw_multiline_text
from src.blender_ui.operators.node_generator import ButtonOperator

class NodeCoPilotPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Node CoPilot Panel"
    bl_idname = "OBJECT_PT_node_copilot"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Node CoPilot" # addon name on the panel itself.

    def draw(self, context):
        obj = context.object
        
        layout = self.layout
        # Draw the new mesh placeholder property
        layout.prop(context.scene, "my_mesh_placeholder", text="Mesh Object")
        
        # Start of Chat Box UI #

        # A horizontal line to separate the sections
        layout.separator()
        layout.label(text="Chat with Blender Node Copilot:")
        
        # Conversation History
        box = layout.box()
        #box.prop(context.scene, "chat_history", text="", emboss=False)
        
        # To make it look like a square, we create a column 
        # inside the box and scale its height.
        col = box.column(align=True)
        
        # Adding a label or empty space keeps the box from collapsing
        col.label(text="")
    
        # Initial greeting message from the LLM
        initial_row = col.row()
        # Create the individual bubble
        initial_box = initial_row.box()
        initial_col = initial_box.column(align=True)
        initial_col.scale_y = 1
        draw_multiline_text(initial_col, "Hello Wasil, how can I help you today!", width=30)
        initial_row.separator()

        # Create a box for eveyr new message
        for msg in context.scene.chat_history:
            # Create a row to align left (LLM) /right (USER)
            row = col.row()
            if msg.sender == "USER":
                row.separator(factor=2)
            
                # Create the individual bubble
                inner_box = row.box()
                inner_col = inner_box.column(align=True)
                inner_col.scale_y = 1
    
                # Draw the text using your function
                draw_multiline_text(inner_col, msg.content, width=30)

            else:
                # Create the individual bubble
                inner_box = row.box()
                inner_col = inner_box.column(align=True)
                inner_col.scale_y = 1
                
                # Draw the text using your function
                draw_multiline_text(inner_col, msg.content, width=30)
                row.separator()
        # END OF THE CHATBOX UI # 

        # Input Field and Send Button
        row = layout.row(align=True)
        row.prop(context.scene, "chat_input", text="")
        row.operator("object.chat_operator", text="", icon='RIGHTARROW')
        
        # End of Chat Box UI
        
        # Add the Chat clear button
        layout.operator("chat.clear_history", text="Clear Chat History", icon='TRASH')
        
        layout.operator(ButtonOperator.bl_idname, text="Generate Nodes (Python Code)", icon='WORLD_DATA')
