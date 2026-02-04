# gui.widgets.dialog_tree_dialog.py

from tkinter import *
from tkinter import ttk, Menu
from core.dialog.dialogData import dialogData
from core.dialog.buttons import delete

class DialogTree():
    def __init__(self, app, frame):
        self.app = app

        # --- Основной контейнер ---
        self.main_container = Frame(frame)
        self.main_container.pack(fill=BOTH, expand=True)

        # --- Контейнер с деревом и скроллом ---
        self.tree_container = Frame(self.main_container)
        self.tree_container.pack(fill=BOTH, expand=True)

        # --- Treeview ---
        self.dialog_tree = ttk.Treeview(self.tree_container, show="tree")
        self.dialog_tree.grid(row=0, column=0, sticky="nsew")
        self.dialog_tree.column("#0", width=350, stretch=False)



        # --- Контекстное меню ---
        self.contextMenu()


        # Биндим ПКМ
        self.dialog_tree.bind("<Button-3>", self.show_context_menu)

        # --- Scrollbars ---
        vsb = ttk.Scrollbar(self.tree_container, orient="vertical", command=self.dialog_tree.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb = ttk.Scrollbar(self.tree_container, orient="horizontal", command=self.dialog_tree.xview)
        hsb.grid(row=1, column=0, sticky="ew")
        self.dialog_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree_container.grid_rowconfigure(0, weight=1)
        self.tree_container.grid_columnconfigure(0, weight=1)

        # --- Корневой узел ---
        self.dialog_data = dialogData.get()
        self.dialog_id = self.dialog_data.get("dialog_id", "No ID")
        self.root_node = self.dialog_tree.insert("", "end", text=f"Dialog: {self.dialog_id}", open=True)

        # --- Заполнение дерева ---
        self._populate_tree()

        # --- Панель кнопок под деревом ---
        self.buttons_container = Frame(self.main_container)
        self.buttons_container.pack(fill=X, pady=5)

        # --- Node кнопки ---
        self.frame_button_node = ttk.LabelFrame(self.buttons_container, text="Node")
        self.frame_button_node.pack(side="left", padx=10, pady=5, fill="both", expand=True)

        ttk.Button(self.frame_button_node, text="Add", command=lambda: self.node_add()).pack(pady=5, padx=10, fill="x")
        ttk.Button(self.frame_button_node, text="Edit", command=lambda: self.node_edit()).pack(pady=5, padx=10, fill="x")
        ttk.Button(self.frame_button_node, text="Delete", command=lambda: delete(self, self.get_selected_data())).pack(pady=5, padx=10, fill="x")




        # --- Option кнопки ---
        self.frame_button_node = ttk.LabelFrame(self.buttons_container, text="Option")
        self.frame_button_node.pack(side="left", padx=10, pady=5, fill="both", expand=True)

        ttk.Button(self.frame_button_node, text="Add", command=lambda: self.option_add()).pack(pady=5, padx=10, fill="x")
        ttk.Button(self.frame_button_node, text="Edit", command=lambda: self.option_edit()).pack(pady=5, padx=10, fill="x")
        ttk.Button(self.frame_button_node, text="Delete", command=lambda: delete(self, self.get_selected_data())).pack(pady=5, padx=10, fill="x")

        # --- Action кнопки ---
        self.frame_button_action = ttk.LabelFrame(self.buttons_container, text="Actions")
        self.frame_button_action.pack(side="right", padx=10, pady=5, fill="both", expand=True)

        ttk.Button(self.frame_button_action, text="Add", command=lambda: self.action_add()).pack(pady=5, padx=10, fill="x")
        ttk.Button(self.frame_button_action, text="Edit", command=lambda: self.action_edit()).pack(pady=5, padx=10, fill="x")
        ttk.Button(self.frame_button_action, text="Delete", command=lambda: delete(self, self.get_selected_data())).pack(pady=5, padx=10, fill="x")










    def show_context_menu(self, event):
        """Вызывает нужное контекстное меню"""
        item_id = self.dialog_tree.identify_row(event.y)
        if not item_id:
            return

        # Выбираем элемент под курсором
        self.dialog_tree.selection_set(item_id)
        self.dialog_tree.focus(item_id)

        selected = self.get_selected_data()
        if not selected:
            return

        if selected[0] == "node":
            self.menu_node.tk_popup(event.x_root, event.y_root)
        elif selected[0] == "option":
            self.menu_option.tk_popup(event.x_root, event.y_root)
        elif selected[0] == "action":
            self.menu_action.tk_popup(event.x_root, event.y_root)















    def _populate_tree(self):
        """Добавляет узлы 'Nodes' и 'Actions' в дерево"""
        self.dialog_tree.delete(*self.dialog_tree.get_children(self.root_node))
        data = dialogData.get()

        # --- Nodes ---
        self.node_items = {}      # node_id -> item_id
        self.option_items = {}    # (node_id, option_id) -> item_id
        if data.get("nodes"):
            nodes_root = self.dialog_tree.insert(self.root_node, "end", text="Nodes", open=False)
            for node in data.get("nodes", []):
                node_id = node.get("id")
                node_item = self.dialog_tree.insert(nodes_root, "end", text=f"Node: {node_id}", open=False)
                self.node_items[node_id] = node_item

                # text
                if "text" in node:
                    text_item = self.dialog_tree.insert(node_item, "end", text="text", open=False)
                    for lang, txt in node["text"].items():
                        self.dialog_tree.insert(text_item, "end", text=f"{lang}: {txt}")

                # options
                if "options" in node:
                    options_item = self.dialog_tree.insert(node_item, "end", text="options", open=False)
                    for opt in node["options"]:
                        opt_id = opt.get("id")  # теперь используем id из JSON
                        opt_text_en = opt.get("text", {}).get("en", "No text")
                        opt_item = self.dialog_tree.insert(options_item, "end", text=opt_text_en, open=False)
                        self.option_items[(node_id, opt_id)] = opt_item

                        if "text" in opt:
                            opt_text_item = self.dialog_tree.insert(opt_item, "end", text="text", open=False)
                            for lang, txt in opt["text"].items():
                                self.dialog_tree.insert(opt_text_item, "end", text=f"{lang}: {txt}")

                        if "next" in opt:
                            next_item = self.dialog_tree.insert(opt_item, "end", text="next", open=False)
                            if isinstance(opt["next"], list):
                                for n in opt["next"]:
                                    self.dialog_tree.insert(next_item, "end", text=n)
                            else:
                                self.dialog_tree.insert(next_item, "end", text=opt["next"])


                # action
                print(node)
                print(node.get("action"))
                
                if "action" in node and node["action"]:
                #if "action" in node:
                #if node["action"]:
                    self.dialog_tree.insert(node_item, "end", text=f"action: {node['action']}")

        # --- Actions ---
        self.action_items = {}  # action_id -> item_id
        actions = data.get("actions", [])
        if actions:
            actions_root = self.dialog_tree.insert(self.root_node, "end", text="Actions", open=False)
            for action in actions:
                action_id = action.get("id")
                action_item = self.dialog_tree.insert(actions_root, "end", text=action_id, open=False)
                self.action_items[action_id] = action_item
                self.dialog_tree.insert(action_item, "end", text=f"function: {action.get('function')}")
                self.dialog_tree.insert(action_item, "end", text=f"comment: {action.get('comment')}")


    def refresh_tree(self):
        self._populate_tree()


    def get_selected_data(self):
        """Возвращает данные выбранного узла для редактирования/удаления"""
        selection = self.dialog_tree.selection()
        if not selection:
            return None
        item_id = selection[0]   # берём первый выбранный элемент

        # --- Проверяем Nodes ---
        for node_id, nid in self.node_items.items():
            if item_id == nid:
                return ("node", node_id)

        # --- Проверяем Options ---
        for (node_id, opt_id), oid in self.option_items.items():
            if item_id == oid:
                return ("option", node_id, opt_id)

        # --- Проверяем Actions ---
        for action_id, aid in self.action_items.items():
            if item_id == aid:
                return ("action", action_id)

        return None






    # --- Node ---
    def node_add(self):
        """Функция Add для Node"""
        # передаем текст и переменную в редактор
        #self.app.editor_frame.show_text("Hallo", var="my_variable")
        self.app.editor_frame.show_text("add_node", self, focused=self.get_selected_data())
        
    def node_edit(self):
        """Функция Edit для Action"""
        # передаем текст и переменную в редактор
        #self.app.editor_frame.show_text("Hallo", var="my_variable")
        self.app.editor_frame.show_text("edit_node", self,  focused=self.get_selected_data())


    # --- Option ---
    def option_add(self):
        """Функция Add для Option"""
        # передаем текст и переменную в редактор
        #self.app.editor_frame.show_text("Hallo", var="my_variable")
        self.app.editor_frame.show_text("add_option", self, focused=self.get_selected_data())
        
    def option_edit(self):
        """Функция Edit для Option"""
        # передаем текст и переменную в редактор
        #self.app.editor_frame.show_text("Hallo", var="my_variable")
        self.app.editor_frame.show_text("edit_option", self, focused=self.get_selected_data())


    # --- Action ---
    def action_add(self):
        """Функция Add для Action"""
        # передаем текст и переменную в редактор
        #self.app.editor_frame.show_text("Hallo", var="my_variable")
        self.app.editor_frame.show_text("add_action", self, focused=self.get_selected_data())
        #print("self.refresh_tree()")
        
        
    def action_edit(self):
        """Функция Edit для Action"""
        # передаем текст и переменную в редактор
        #self.app.editor_frame.show_text("Hallo", var="my_variable")
        self.app.editor_frame.show_text("edit_action", self, focused=self.get_selected_data())
        


















    # --- ContextMenu ---
    def contextMenu(self):
        self.menu_node = Menu(self.dialog_tree, tearoff=0)
        self.menu_node.add_command(label="Add new", command=self.node_add)
        self.menu_node.add_command(label="Add option", command=self.option_add)
        self.menu_node.add_command(label="Edit", command=self.node_edit)
        self.menu_node.add_command(label="Delete", command=lambda: delete(self, self.get_selected_data()))

        self.menu_option = Menu(self.dialog_tree, tearoff=0)
        self.menu_option.add_command(label="Add new", command=self.option_add)
        self.menu_option.add_command(label="Edit", command=self.option_edit)
        self.menu_option.add_command(label="Delete", command=lambda: delete(self, self.get_selected_data()))

        self.menu_action = Menu(self.dialog_tree, tearoff=0)
        self.menu_action.add_command(label="Add new", command=self.action_add)
        self.menu_action.add_command(label="Edit", command=self.action_edit)
        self.menu_action.add_command(label="Delete", command=lambda: delete(self, self.get_selected_data()))