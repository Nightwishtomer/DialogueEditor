# gui.main_window.py

from tkinter import *
from gui.widgets.toolbar import MainMenu
from gui.widgets.dialog_tree import DialogTree
from gui.widgets.library_tree import LibraryTree
from gui.widgets.editor_frame import EditorFrame

class DialogueEditorApp():
    def __init__(self, root):
        
        self.root = root
        self.root.title("Dialogue Editor")
        self.root.geometry("1200x600")

        # --- Menu ---
        self.menu = MainMenu(self)

        # --- Контейнер для главной области ---
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        # --- Левое дерево DialogTree ---
        dialog_frame = Frame(self.main_frame, width=300)
        dialog_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.dialog_tree = DialogTree(self, dialog_frame)

        # --- Центральное окно Editor ---
        self.editor_frame = EditorFrame(self.main_frame)
        self.editor_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        # --- Правое дерево LibraryTree ---
        library_frame = Frame(self.main_frame, width=300)
        library_frame.pack(side=RIGHT, fill=Y, padx=5, pady=5)
        self.library_tree = LibraryTree(self, library_frame)
