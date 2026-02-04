# gui.wigets.toolbar.py


import tkinter as tk
from tkinter import filedialog, messagebox
from core.toolbar import file_menu_new_file, file_menu_load_file, file_menu_save_file, file_menu_save_as_file, file_menu_exit_app, dict_menu_view_dictionary, dict_menu_new_dictionary, dict_menu_load_dictionary, dict_menu_save_dictionary, json_menu_view_dictionary, dict_menu_save_as_dictionary











import os

class MainMenu():
   def __init__(self, app):
      self.app = app
      self.menu_bar = tk.Menu(app.root)

      # --- File Menu ---
      file_menu = tk.Menu(self.menu_bar, tearoff=0)
      file_menu.add_command(label="New Dialog", command=lambda: file_menu_new_file(self))
      file_menu.add_command(label="Load..", command=lambda: file_menu_load_file(self))
      file_menu.add_command(label="Save", command=lambda: file_menu_save_file(self))
      file_menu.add_command(label="Save as", command=lambda: file_menu_save_as_file(self))
      file_menu.add_separator()
      file_menu.add_command(label="Exit", command=lambda: file_menu_exit_app(self))
      self.menu_bar.add_cascade(label="File", menu=file_menu)

      # --- Dictionary Menu ---
      dict_menu = tk.Menu(self.menu_bar, tearoff=0)
      dict_menu.add_command(label="View", command=lambda: dict_menu_view_dictionary())
      dict_menu.add_separator()
      dict_menu.add_command(label="New", command=lambda: dict_menu_new_dictionary(self))
      dict_menu.add_command(label="Load", command=lambda: dict_menu_load_dictionary(self))
      dict_menu.add_command(label="Save", command=lambda: dict_menu_save_dictionary(self))
      dict_menu.add_command(label="Save as", command=lambda: dict_menu_save_as_dictionary(self))
      self.menu_bar.add_cascade(label="Dictionary", menu=dict_menu)

      # --- JSON Editor Menu ---
      dict_menu = tk.Menu(self.menu_bar, tearoff=0)
      dict_menu.add_command(label="Edit", command=json_menu_view_dictionary)
      self.menu_bar.add_cascade(label="JSON", menu=dict_menu)
 
      app.root.config(menu=self.menu_bar)