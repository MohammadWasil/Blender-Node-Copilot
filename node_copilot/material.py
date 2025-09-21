"""
Example Material utilities for Blender.
"""

import bpy

def assign_principled_material(obj, color=(1, 0, 0, 1), name="NewMaterial"):
    """
    Assigns a Principled BSDF material to the given object.
    
    Parameters:
        obj   -- Blender object (e.g., bpy.context.active_object)
        color -- RGBA tuple (default is red: (1, 0, 0, 1))
        name  -- Name of the new material
    """
    # Create a new material
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    
    # Get Principled BSDF node
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
    
    # Assign to object
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    
    return mat