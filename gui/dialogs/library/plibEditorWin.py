# gui/plibEditorWin.py.py

import tkinter as tk
from tkinter import messagebox
from core.library.plibData import PlibData

class PlibEditorWin():
    def __init__(self):
        self.editor_win = tk.Toplevel()
        self.editor_win.title("Phrases library Editor")
        self.editor_win.geometry("1000x600")

        self.editor_win.rowconfigure(0, weight=1)   # строка 0 (текст) растягивается
        self.editor_win.rowconfigure(1, weight=0)   # строка 1 (кнопки) фиксированная
        self.editor_win.columnconfigure(0, weight=1)
    
        # --- TextArea ---
        self.text_area = tk.Text(self.editor_win, wrap="word")
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.text_area.insert(tk.END, PlibData.get_text())
        # --- Buttons Container  ---
        self.button_frame = tk.Frame(self.editor_win)
        self.button_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # --- Buttons ---
        self.cancel_btn = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        self.cancel_btn.pack(side="right", padx=5)

        self.save_btn = tk.Button(self.button_frame, text="Save", command=self.save_and_close)
        self.save_btn.pack(side="right", padx=5)
     

    def save_and_close(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Empty", "Phrases library is empty!")
            return
        
        PlibData.set_all(content)
        messagebox.showinfo("Saved", "Phrases library stored to... nowhere")
        self.editor_win.destroy()


    def cancel(self):
        self.editor_win.destroy()