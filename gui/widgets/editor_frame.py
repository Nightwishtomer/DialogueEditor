# gui/widgets/editor_frame.py

from tkinter import *
from tkinter import ttk, messagebox
from core.dialog.dialogData import dialogData

class EditorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Editor")  # The title is embedded in the frame
        self.parent = parent
        self.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # --- scrollable container ---
        self.canvas = Canvas(self, borderwidth=0)
        self.scroll_frame = Frame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.scroll_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)


    def show_widget(self, widget):
        """Clears all current widgets and inserts a new one"""
        self.clear_wiget()
        widget.pack(fill=BOTH, expand=True, padx=5, pady=5)


    def clear_wiget(self):
        for child in self.scroll_frame.winfo_children():
            child.destroy()


    def show_text(self, type, self_dialog_tree, focused=None):
        self.focused = focused
        self.self_dialog_tree = self_dialog_tree

        # we only clean the insides, not the scroll_frame itself
        self.clear_wiget()

        self.var = focused
        #print(f"type={type}, focused={focused}")        

        if type == "add_node":
            self.add_edit_node()
        elif type == "edit_node":
            self.add_edit_node(focused)
        elif type == "add_option":
            self.add_edit_option("add", focused)
        elif type == "edit_option":
            self.add_edit_option("edit", focused)
        elif type == "add_action":
            self.add_edit_action()
        elif type == "edit_action":
            self.add_edit_action(focused)

        lbl = Label(self.scroll_frame, text=type, font=("Arial", 11))
        lbl.pack(anchor="nw", padx=5, pady=5)




    # --- Node ---
    def add_edit_node(self, focused=None):
        self.focused = focused
        # old
        self.old_id,self.old_text_en, self.old_text_de, self.old_text_ru, self.old_action = "", "", "", "", ""
        self.old_options = []

        # new       
        self.new_id, self.new_text_en, self.new_text_de, self.new_text_ru, self.new_action = "", "", "", "", ""
        self.new_options = []

        self.option = {
            "id": 0,
            "text": {
                "en": "",
                "de": "",
                "ru": ""
            },
            "next": ""
        }

        if focused is not None:
            old_data = dialogData.get_node(focused[1])        
            self.old_id = old_data["id"]
            self.old_text_en, self.old_text_de, self.old_text_ru = old_data["text"]["en"], old_data["text"]["de"], old_data["text"]["ru"]
            self.old_options = old_data["options"]
            self.old_action = old_data["action"]

        self.nodes_list = dialogData.get_nodes_list()
        self.actions_list = dialogData.get_actions_list()

        frame = Frame(self.scroll_frame)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # id field
        Label(frame, text="ID:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.id_var = StringVar(value=self.old_id)
        self.entry_id = Entry(frame, textvariable=self.id_var, width=40)
        self.entry_id.grid(row=1, column=0, sticky="ew", padx=5, pady=2)

        # Text (EN) field (multi-line)
        Label(frame, text="Text (EN):", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="nw", padx=5, pady=2)
        self.entry_text_en = Text(frame, width=40, height=3)
        self.entry_text_en.insert("1.0", self.old_text_en)
        self.entry_text_en.grid(row=3, column=0, sticky="ew", padx=5, pady=2)

        # Text (DE) field (multi-line)
        Label(frame, text="Text (DE):", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="nw", padx=5, pady=2)
        self.entry_text_de = Text(frame, width=40, height=3)
        self.entry_text_de.insert("1.0", self.old_text_de)
        self.entry_text_de.grid(row=5, column=0, sticky="ew", padx=5, pady=2)

        # Text (RU) field (multi-line)
        Label(frame, text="Text (RU):", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="nw", padx=5, pady=2)
        self.entry_text_ru = Text(frame, width=40, height=3)
        self.entry_text_ru.insert("1.0", self.old_text_ru)
        self.entry_text_ru.grid(row=7, column=0, sticky="ew", padx=5, pady=2)

        # action field
        Label(frame, text="Action:", font=("Arial", 10, "bold")).grid(
            row=8, column=0, sticky="w", padx=5, pady=2
        )
        # currently selected value
        self.entry_action = StringVar(value=self.old_action or "None")

        # add "None" as the first element
        values = ["None"] + self.actions_list  

        self.combo_action = ttk.Combobox(
            frame,
            textvariable=self.entry_action,
            values=values,              # list ['exit_dialog', 'trade_dialog']
            state="readonly",           # only selection, no manual input
            width=40
        )
        self.combo_action.grid(row=9, column=0, sticky="ew", padx=5, pady=2)

        # frame for buttons (bottom, right)
        btn_frame = Frame(frame)
        btn_frame.grid(row=10, column=0, sticky="e", padx=5, pady=10)

        Button(btn_frame, text="Save", width=10, command=self.save_node).pack(side=RIGHT, padx=5)
        Button(btn_frame, text="Cancel", width=10, command=self.cancel_node).pack(side=RIGHT, padx=5)

        # column stretch
        frame.columnconfigure(0, weight=1)


    def save_node(self):
        self.new_id = self.entry_id.get()
        self.new_text_en = self.entry_text_en.get("1.0", "end-1c")
        self.new_text_de = self.entry_text_de.get("1.0", "end-1c")
        self.new_text_ru = self.entry_text_ru.get("1.0", "end-1c")
        self.new_action = self.entry_action.get()
        if self.new_action == "": self.new_action = None
    
        data = {
            "id": self.new_id,
            "text": {
                "en": self.new_text_en,
                "de": self.new_text_de,
                "ru": self.new_text_ru
            },
            "options": self.new_options,
            "action": self.new_action
        }

        # uniqueness check
        if self.focused is None:
            if self.new_id in self.nodes_list:
                messagebox.showwarning("Ошибка", f"ID '{self.new_id}' уже существует в списке действий!")
                return

        if not self.new_id:
            messagebox.showwarning("Ошибка", "ID не может быть пустым!")
            return

        if self.focused is not None:
            # Edit Action
            dialogData.edit_node(self.old_id, data)
            pass
        else:
            # Add Action
            dialogData.add_node(data)

        self.clear_wiget()
        self.self_dialog_tree.refresh_tree()


    def cancel_node(self):
        self.clear_wiget()
        





    # --- Option ---
    def add_edit_option(self, type="add", focused=None):
        self.focused = focused
        print(f"Type: {type}, focused OPTION: {self.focused}")

        #print(dialogData.get_options_list(self.focused[1]))
        count = dialogData.get_options_count(focused[1])

        self.new_id, self.new_text_en, self.new_text_de, self.new_text_ru, self.new_next = count, "", "", "", ""
        self.old_id, self.old_text_en, self.old_text_de, self.old_text_ru, self.old_next = count, "", "", "", ""
        

        if type == "edit":
            old_data = dialogData.get_option(focused[1], focused[2])          
            self.old_id, self.old_text_en, self.old_text_de, self.old_text_ru, self.old_next = old_data["id"], old_data["text"]["en"], old_data["text"]["de"], old_data["text"]["ru"], old_data["next"] 
            self.new_id = old_data["id"]
        else: 
            
            pass
        print(self.old_id, self.old_text_en, self.old_text_de, self.old_text_ru, self.old_next , count)
        """
        {   
            "id": 0,
            "text": {
                "en" : "Cartridges",
                "de" : "Patronen",
                "ru" : "Патроны"
            },                   
            "next": "ammo"
        }
        """


        frame = Frame(self.scroll_frame)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # id field
        Label(frame, text="ID:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.id_var = StringVar(value=self.old_id)
        self.entry_id = Entry(frame, textvariable=self.id_var, width=40)
        self.entry_id.grid(row=1, column=0, sticky="ew", padx=5, pady=2)

        # Text (EN) field (multi-line)
        Label(frame, text="Text (EN):", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="nw", padx=5, pady=2)
        self.entry_text_en = Text(frame, width=40, height=3)
        self.entry_text_en.insert("1.0", self.old_text_en)
        self.entry_text_en.grid(row=3, column=0, sticky="ew", padx=5, pady=2)

        # Text (DE) field (multi-line)
        Label(frame, text="Text (DE):", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="nw", padx=5, pady=2)
        self.entry_text_de = Text(frame, width=40, height=3)
        self.entry_text_de.insert("1.0", self.old_text_de)
        self.entry_text_de.grid(row=5, column=0, sticky="ew", padx=5, pady=2)

        # Text (RU) field (multi-line)
        Label(frame, text="Text (RU):", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="nw", padx=5, pady=2)
        self.entry_text_ru = Text(frame, width=40, height=3)
        self.entry_text_ru.insert("1.0", self.old_text_ru)
        self.entry_text_ru.grid(row=7, column=0, sticky="ew", padx=5, pady=2)

        # Next field
        Label(frame, text="Next:", font=("Arial", 10, "bold")).grid(row=8, column=0, sticky="nw", padx=5, pady=2)
        self.next_var = StringVar(value=self.old_next)
        self.entry_next = Entry(frame, textvariable=self.next_var, width=40)
        self.entry_next.grid(row=9, column=0, sticky="ew", padx=5, pady=2)

        self.btn_delete = Button(btn_frame, text="< < < Copy", state=DISABLED, command=lambda: self.copy_from_library(self))
        self.btn_delete.pack(side=LEFT, padx=5)


    

        btn_frame = Frame(frame)
        btn_frame.grid(row=10, column=0, sticky="e", padx=5, pady=10)

        Button(btn_frame, text="Save", width=10, command=self.save_node).pack(side=RIGHT, padx=5)
        Button(btn_frame, text="Cancel", width=10, command=self.cancel_node).pack(side=RIGHT, padx=5)

        # column stretch
        frame.columnconfigure(0, weight=1)
        
        pass

















































    def copy_from_library(self):
        pass



    # --- Action --- 
    def add_edit_action(self, focused=None):
        self.focused = focused

        self.new_id, self.new_function, self.new_comment = "", "", ""
        self.old_id, self.old_function, self.old_comment = "", "", ""
        

        if focused is not None:
            old_data = dialogData.get_action(focused[1])          
            self.old_id, self.old_function, self.old_comment = old_data["id"], old_data["function"], old_data["comment"]

        self.actions_list = dialogData.get_actions_list()

        frame = Frame(self.scroll_frame)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # id field
        Label(frame, text="ID:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.id_var = StringVar(value=self.old_id) #text.get("id", "")
        self.entry_id = Entry(frame, textvariable=self.id_var, width=40)
        self.entry_id.grid(row=1, column=0, sticky="ew", padx=5, pady=2)

        # function field
        Label(frame, text="Function:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.func_var = StringVar(value=self.old_function) #text.get("function", "")
        self.entry_function = Entry(frame, textvariable=self.func_var, width=40)
        self.entry_function.grid(row=3, column=0, sticky="ew", padx=5, pady=2)

        # comment field (multi-line)
        Label(frame, text="Comment:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="nw", padx=5, pady=2)
        self.entry_comment = Text(frame, width=40, height=5)
        self.entry_comment.insert("1.0", self.old_comment) #text.get("comment", "")
        self.entry_comment.grid(row=5, column=0, sticky="ew", padx=5, pady=2)

        # frame for buttons (bottom, right)
        btn_frame = Frame(frame)
        btn_frame.grid(row=6, column=0, sticky="e", padx=5, pady=10)

        Button(btn_frame, text="Save", width=10, command=self.save_action).pack(side=RIGHT, padx=5)
        Button(btn_frame, text="Cancel", width=10, command=self.cancel_action).pack(side=RIGHT, padx=5)

        # column stretch
        frame.columnconfigure(0, weight=1)


    def save_action(self):

        self.new_id = self.entry_id.get().strip()
        self.new_function = self.entry_function.get().strip()
        self.new_comment = self.entry_comment.get("1.0", END).strip()
        
        if self.focused is not None:
            # проверка уникальности
            if self.new_id in self.actions_list:
                messagebox.showwarning("Ошибка", f"ID '{self.new_id}' уже существует в списке действий!")
                return

        if not self.new_id:
            messagebox.showwarning("Ошибка", "ID не может быть пустым!")
            return

        if self.focused is not None:
            # Edit Action
            dialogData.edit_action(self.old_id, self.new_id, self.new_function, self.new_comment)
        else:
            # Add Action
            dialogData.add_action(self.new_id, self.new_function, self.new_comment)

        self.clear_wiget()
        self.self_dialog_tree.refresh_tree()
    




    def cancel_action(self):
        self.entry_id.delete(0, END)
        self.entry_function.delete(0, END)
        self.entry_comment.delete(0, END)
        self.clear_wiget()

    def on_frame_configure(self, event):
        """Обновляем scrollregion, когда изменяется размер содержимого"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        """Растягиваем внутренний фрейм под ширину канвы"""
        self.canvas.itemconfig(self.window, width=event.width)