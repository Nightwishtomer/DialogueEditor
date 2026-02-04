# main.py

import tkinter as tk
from gui.main_window import DialogueEditorApp

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = DialogueEditorApp(root)
    root.deiconify()
    root.mainloop()