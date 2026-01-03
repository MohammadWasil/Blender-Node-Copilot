# this script will help us geenrate new python script file, which will hold all
# the generated code.

import bpy

def create_and_load_py_file(file_path : str, text_block_name : str, content : str) -> None:
    """
    Creates an external text file and then loads it as an internal text data block.

    Args:
        file_path (str): The full path for the external file.
        text_block_name (str): The name for the new internal text data block.
    """
    try:
        # Step 1: Create the external file and write content to it.
        with open(file_path, 'w') as file:
            file.write(content)

        # Step 2: Read the content of the external file.
        with open(file_path, 'r') as file:
            content = file.read()

        # Step 3: Create a new internal text data block.n
        text_block = bpy.data.texts.new(name=text_block_name)
        text_block.write(content)

    except IOError as e:
        print(f"An error occurred: {e}")

# Example usage:
# Adjust the path and name as needed. The text_block_name will appear in the dropdown.
# file_to_create = "sample2.txt"
# text_block_name = "My_Sample_File2.txt"
#
# create_and_load_py_file(file_to_create, text_block_name, content="Hello, this file was created and loaded automatically by a Blender script.")