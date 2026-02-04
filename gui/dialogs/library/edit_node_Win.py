# gui.library.edit_node_Win.py

import tkinter as tk
from tkinter import ttk, messagebox
from core.library.plibData import PlibData

class EditNodeWin():
    def __init__(self, root_self, focused):
        self.root_self = root_self
        self.old_category = focused[0]
        self.new_category = ""

        self.editor_win = tk.Toplevel()
        self.editor_win.title("Edit Node in Phrases library")
        self.editor_win.geometry("400x350")

        # --- Label ---
        tk.Label(self.editor_win, text="Edit Node:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # --- Container for dynamic widgets ---
        self.frame = tk.Frame(self.editor_win)
        self.frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # --- Entry ---
        self.entry_category = tk.Entry(self.frame, width=50 )
        self.entry_category.insert(0, self.old_category)  # 0 — позиция курсора, т.е. начало  # self.old_header - старое значение
        self.entry_category.pack(fill="x", pady=5)
        
        # --- Buttons ---
        self.button_frame = tk.Frame(self.editor_win)
        self.button_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.cancel_btn = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        self.cancel_btn.pack(side="right", padx=5)
        self.save_btn = tk.Button(self.button_frame, text="Save", command=self.save_and_close)
        self.save_btn.pack(side="right", padx=5)

    
    def save_and_close(self):
        self.new_category = self.entry_category.get().strip()  # возвращает строку
        print("Новое имя:", self.new_category)
        
        if not self.new_category:
            messagebox.showwarning("Warning", "Please enter some text!")
            return
        
        # Сохраняем в PlibData    
        PlibData.edit_category_name(self.old_category, self.new_category) # Edit category name
        self.root_self.app.library_tree.refresh_tree() # Refresh tree

        messagebox.showinfo("Success", "Phrase has been successfully updated!")
        
        self.cancel()

    def cancel(self):
        self.editor_win.destroy()