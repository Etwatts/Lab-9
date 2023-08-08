""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk

# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False, False)

# Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row= 0, column= 0, columnspan= 2, pady= (20, 10))

frame_info = ttk.LabelFrame(root, text= 'Info')
frame_info.grid(row= 1, column= 0, padx=(10, 20), pady= (20, 10), sticky=N)

frame_stat = ttk.LabelFrame(root, text = 'Stats')
frame_stat.grid(row= 1, column= 1, padx=(10, 20), pady= (10, 20), sticky=N)


# Populate the user input frame with widgets

Label_name = ttk.Label(frame_input, text= "Pokemon Name:")
Label_name.grid(row= 0, column= 0, padx=(10, 5), pady= 10)
name = ttk.Entry(frame_input)
name.insert(0, 'Mewtwo')
name.grid(row= 0, column= 1)

# Define button click event handler function

root.mainloop()