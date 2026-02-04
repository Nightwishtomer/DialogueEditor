# gui.library_tree.py

from tkinter import *
from tkinter import ttk
from core.library.plibData import PlibData
from core.library.buttons import *


class LibraryTree():
    def __init__(self, app, frame):
        self.app = app   

        # --- Container for scroll ---
        container = Frame(frame)
        container.pack(fill=BOTH, expand=True)

        # --- Tree ---
        self.tree = ttk.Treeview(container, show="tree", height=20)
        self.tree.grid(row=0, column=0, sticky="nsew")

        # --- scrolls ---
        vsb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb = ttk.Scrollbar(container, orient="horizontal", command=self.tree.xview)
        hsb.grid(row=1, column=0, sticky="ew")

        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # --- Stretching grid ---
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --- Buttons under tree ---
        btn_frame = Frame(frame)
        btn_frame.pack(fill=X, pady=5)
        
        self.btn_delete = Button(btn_frame, text="Delete", state=DISABLED, command=lambda: library_delete(self, self.get_selected_data()))
        self.btn_delete.pack(side=LEFT, padx=5)

        self.btn_edit = Button(btn_frame, text="Edit", state=DISABLED, command=lambda: library_edit(self, self.get_selected_data()))
        self.btn_edit.pack(side=LEFT, padx=5)

        btn_add = Button(btn_frame, text="Add", command=lambda: library_add(self))
        btn_add.pack(side=LEFT, padx=5)     
        
        # --- Data ---
        root_node = self.tree.insert("", "end", text="Library", open=True)  # корневой элемент  
        self.tree.column("#0", width=350, stretch=False)

        self._populate_tree()

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select) 


    def refresh_tree(self):
        self._populate_tree()


    def _populate_tree(self):
        """Заполняет дерево исходя из self.phrases_data"""
        root_node = self.tree.get_children()[0]
        self.tree.delete(*self.tree.get_children(root_node))

        phrases_data = PlibData.get()  # словарь тем -> список фраз

        for topic, phrases in phrases_data.items():
            parent = self.tree.insert(root_node, "end", text=topic, open=False, values=(topic, None))
            for phrase in phrases:
                if isinstance(phrase, dict):
                    en_text = phrase.get("en", "")
                    phrase_node = self.tree.insert(parent, "end", text=en_text, open=False,
                                                   values=(topic, en_text, phrase))  # сохраняем словарь
                    for lang, text in phrase.items():
                        if lang != "en":
                            self.tree.insert(phrase_node, "end", text=f"{lang}: {text}",
                                             values=(topic, en_text, phrase))
                else:
                    self.tree.insert(parent, "end", text=phrase, values=(topic, phrase))


    

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            self.btn_delete.config(state=NORMAL)
            self.btn_edit.config(state=NORMAL)
        else:
            self.btn_delete.config(state=DISABLED)
            self.btn_edit.config(state=DISABLED)

    def get_selected_data(self):
        """Возвращает данные выбранного узла: topic, phrase, словарь (если есть)"""
        item_id = self.tree.focus()
        if not item_id:
            return None
        values = self.tree.item(item_id, "values")
        if not values:
            return None
        # values = (topic, phrase, dict?) 
        return values

    