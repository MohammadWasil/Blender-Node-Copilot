import textwrap

def draw_multiline_text(layout, text, width=40):
    # This splits the long string into a list of shorter lines
    lines = textwrap.wrap(text, width=width)
    
    col = layout.column(align=True)
    for line in lines:
        col.label(text=line)