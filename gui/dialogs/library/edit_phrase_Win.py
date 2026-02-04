# gui.library.edit_phrase_Win.py

import tkinter as tk
from tkinter import ttk, messagebox
from core.library.plibData import PlibData

class EditPhraseWin():
    def __init__(self, root_self, focused):
        self.root_self = root_self      
        self.category = focused[0]
        self.phrase = focused[1]
        self.old_phrase = PlibData.get_phrase_by_phrase(self.category, self.phrase)

        #print(self.old_phrase)


        #menu_self.app.library_tree.refresh_tree()
        self.editor_win = tk.Toplevel()
        self.editor_win.title("Edit Phrases in Phrases library")
        self.editor_win.geometry("400x350")

        # --- Label ---
        tk.Label(self.editor_win, text="Edit Phrases:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # --- Container for dynamic widgets ---
        self.frame = tk.Frame(self.editor_win)
        self.frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # ---  ----
        tk.Label(self.frame, text="Enter phrases in English:").pack(anchor="w")
        self.text_area_en = tk.Text(self.frame, height=2, width=30)
        self.text_area_en.insert("1.0", self.old_phrase['en'])  # 0 — позиция курсора, т.е. начало  # self.old_header - старое значение
        self.text_area_en.pack(fill="both", pady=5)
        
        tk.Label(self.frame, text="Enter phrases in German:").pack(anchor="w")
        self.text_area_de = tk.Text(self.frame, height=2, width=30)
        self.text_area_de.insert("1.0", self.old_phrase['de'])  # 0 — позиция курсора, т.е. начало  # self.old_header - старое значение
        self.text_area_de.pack(fill="both", pady=5)
        
        tk.Label(self.frame, text="Enter phrases in Russian:").pack(anchor="w")
        self.text_area_ru = tk.Text(self.frame, height=2, width=30)
        self.text_area_ru.insert("1.0", self.old_phrase['ru'])  # 0 — позиция курсора, т.е. начало  # self.old_header - старое значение
        self.text_area_ru.pack(fill="both", pady=5)

        # --- Buttons ---
        self.button_frame = tk.Frame(self.editor_win)
        self.button_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.cancel_btn = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        self.cancel_btn.pack(side="right", padx=5)
        self.save_btn = tk.Button(self.button_frame, text="Save", command=self.save_and_close)
        self.save_btn.pack(side="right", padx=5)


        return
        """
        # --- Main choice ---
        
        self.node_type = tk.StringVar()
        self.type_menu = ttk.Combobox(self.editor_win, textvariable=self.node_type, state="readonly", width=30)
        self.type_menu['values'] = ("Topic", "Phrase")
        self.type_menu.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.type_menu.bind("<<ComboboxSelected>>", self.on_type_selected)

        # --- Container for dynamic widgets ---
        self.dynamic_frame = tk.Frame(self.editor_win)
        self.dynamic_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.dynamic_widgets = {}

        # --- Buttons ---
        self.button_frame = tk.Frame(self.editor_win)
        self.button_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.cancel_btn = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        self.cancel_btn.pack(side="right", padx=5)
        self.save_btn = tk.Button(self.button_frame, text="Save", command=self.save_and_close)
        self.save_btn.pack(side="right", padx=5)
        """
    """
    def on_type_selected(self, event=None):
        # удаляем предыдущие динамические виджеты
        for widgets in self.dynamic_frame.winfo_children():
            widgets.destroy()
        self.dynamic_widgets.clear()

        if self.node_type.get() == "Topic": # 1
            tk.Label(self.dynamic_frame, text="Enter name of topic:").pack(anchor="w")
            entry = tk.Entry(self.dynamic_frame, width=50)
            entry.pack(fill="x", pady=5)
            self.dynamic_widgets['text'] = entry

        elif self.node_type.get() == "Phrase": # 2
           
            #print(PlibData.get())
            headers = PlibData.get_headers() # headerts of topics
            #print(headers)

            tk.Label(self.dynamic_frame, text="Select category:").pack(anchor="w")
            self.category_var = tk.StringVar()
            category_menu = ttk.Combobox(self.dynamic_frame, textvariable=self.category_var, state="readonly", width=30)
            category_menu['values'] = headers
            category_menu.pack(fill="x", pady=5)
            self.dynamic_widgets['category'] = category_menu


            tk.Label(self.dynamic_frame, text="Enter phrases in English:").pack(anchor="w")
            text_area_en = tk.Text(self.dynamic_frame, height=2, width=30)
            text_area_en.pack(fill="both", pady=5)
            self.dynamic_widgets['text_en'] = text_area_en

            tk.Label(self.dynamic_frame, text="Enter phrases in German:").pack(anchor="w")
            text_area_de = tk.Text(self.dynamic_frame, height=2, width=30)
            text_area_de.pack(fill="both", pady=5)
            self.dynamic_widgets['text_de'] = text_area_de

            tk.Label(self.dynamic_frame, text="Enter phrases in Russian:").pack(anchor="w")
            text_area_ru = tk.Text(self.dynamic_frame, height=2, width=30)
            text_area_ru.pack(fill="both", pady=5)
            self.dynamic_widgets['text_ru'] = text_area_ru
    """
    

    def save_and_close(self):
        content_en = self.text_area_en.get("1.0", "end-1c").strip() #("1.0", tk.END)
        content_de = self.text_area_de.get("1.0", "end-1c").strip() #("1.0", tk.END)
        content_ru = self.text_area_ru.get("1.0", "end-1c").strip() #("1.0", tk.END)

        content = {"en" : content_en, "de" : content_de, "ru" : content_ru}

        if not self.category or not self.phrase:
            messagebox.showwarning("Warning", "Please fill text and select category!")
            return
        
        # Сохраняем в PlibData
        PlibData.edit_phrase(self.category, self.phrase, content)
     
        self.root_self.app.library_tree.refresh_tree()

        messagebox.showinfo("Success", "Phrase has been successfully updated!")

        self.cancel()
        

    def cancel(self):
        self.editor_win.destroy()
