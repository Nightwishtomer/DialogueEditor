# core.dialog.dialogData.py

import json, os

class DialogData():
    def __init__(self):
        self.__data = {}
        self.__file_path = None
        self.__file_name = "new_dialog.json"


    # --- File path --
    def set_file_path(self, file_path):
        self.__file_path = file_path

    
    def get_file_path(self):
        return self.__file_path
        

    # --- File name --
    def set_file_name(self):
        self.__file_name = os.path.basename(self.__file_path) if self.__file_path else self.__file_name


    def get_file_name(self):
        return self.__file_name


    # --- Data ---
    def set(self, id, data):
        pass


    def set_all(self, json_data):
        # Если пришла строка → пробуем распарсить
        if isinstance(json_data, str):
            try:
                self.__data = json.loads(json_data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON string: {e}")
        
        # Если пришёл dict или list → принимаем как есть
        elif isinstance(json_data, (dict, list)):
            self.__data = json_data
        
        else:
            raise TypeError("set_all expects str (JSON) or dict/list")


    def save(self, filepath):
        """Save JSON to file"""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.__data, f, indent=2, ensure_ascii=False)


    def load(self, filepath):
        """Load JSON from file"""
        with open(filepath, "r", encoding="utf-8") as f:
            self.__data = json.load(f)


    def get(self):
        """Return all data"""
        return dict(self.__data)
    

    def get_text(self):
        return json.dumps(self.__data, indent=2, ensure_ascii=False)


    def update(self, id, type, data):
        pass


    def get_data(self, id, type):
        pass


    def clear(self):
        self.__data = {}

    


















    # --- Nodes ---
    def get_nodes_list(self):
        result = []
        actions = self.__data.get("nodes", [])
        for i, action in enumerate(actions):
            result.append(action.get("id"))
        return result

    def get_node(self, node_id):
        nodes = self.__data.get("nodes", [])
        for node in nodes:    
            if node.get("id") == node_id:
                return node
    

    def delete_node(self, node_id):
        # Delete the node
        #del self.__data["nodes"][node_id]

        """Удаляет node по его id"""
        nodes = self.__data.get("nodes", [])
        for i, node in enumerate(nodes):
            if node.get("id") == node_id:
                del nodes[i]
                break


    def add_node(self, data):
        if "nodes" not in self.__data or not isinstance(self.__data["nodes"], list):
            self.__data["nodes"] = []
        self.__data["nodes"].append(data)


    def edit_node(self, old_id, data):
        nodes = self.__data.get("nodes", [])
        for i, node in enumerate(nodes):
            if node.get("id") == old_id:
                # Вставляем новые значения прямо в self.__data
                self.__data["nodes"][i] = data
                return




        """
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
        """





















    # --- Options ---

    def get_option(self, node_id, option_id):
        for node in self.__data.get("nodes", []):
            if node.get("id") == node_id:
                options = node.get("options", [])
                for option in options:
                    if option.get("id") == option_id:
                        return option

    def get_options_count(self, node_id):
        for node in self.__data.get("nodes", []):
            if node.get("id") == node_id:
                return len(node.get("options", []))
        return 0  # если узел не найден


    def delete_option(self, node_id: str, option_id: int | str):
        """Удаляет option из узла по его node_id и option_id"""
        for node in self.__data.get("nodes", []):
            if node.get("id") == node_id:
                options = node.get("options", [])
                for i, option in enumerate(options):
                    if option.get("id") == option_id:
                        del options[i]
                        return True
        return False  # если ничего не нашли






















    # --- Actions ---
    def get_actions_list(self):
        #self.__data.get("actions", [])
        result = []
        actions = self.__data.get("actions", [])
        for i, action in enumerate(actions):
            result.append(action.get("id"))
        return result   

    def add_action(self, action_id, function, comment):
        if "actions" not in self.__data or not isinstance(self.__data["actions"], list):
            self.__data["actions"] = []
        self.__data.setdefault("actions", []).append({"id": action_id, "function": function, "comment": comment})       

    def get_action(self, action_id):
        actions = self.__data.get("actions", [])
        for action in actions:    
            if action.get("id") == action_id:
                return action      

    def edit_action(self, action_id, new_id, new_function, new_comment):
        actions = self.__data.get("actions", [])
        for i, action in enumerate(actions):
            if action.get("id") == action_id:
                # Вставляем новые значения прямо в self.__data
                self.__data["actions"][i] = {
                    "id": new_id,
                    "function": new_function,
                    "comment": new_comment
                }
                return
            
    def delete_action(self, action_id):
        """Удаляет action по его id"""
        actions = self.__data.get("actions", [])
        for i, action in enumerate(actions):
            if action.get("id") == action_id:
                del actions[i]
                break












        



dialogData = DialogData()

"""

{
    "dialog_id": "npc_1_intro1111111111",
    "nodes": [
        {
            "id": "start",
            "text": {
                "en" : "Hello, stalker. What are you looking for?",
                "de" : "Hallo, Stalker. Was suchst du?",
                "ru" : "Привет, сталкер. Что ищешь?"
            },
            "options": [
                {   
                    "id": 0,
                    "text": {
                        "en" : "Cartridges",
                        "de" : "Patronen",
                        "ru" : "Патроны"
                    },                   
                    "next": "ammo"
                },
                {
                    "id": 1,
                    "text": {
                        "en" : "Talk",
                        "de" : "Sprechen",
                        "ru" : "Разговор"
                    },
                    "next": [
                        "last_news",
                        "not_local",
                        "why"
                    ]
                },
                {
                    "id": 2,
                    "text": {
                        "en" : "Work",
                        "de" : "Arbeit",
                        "ru" : "Работа"
                    },
                    "next": "quest"
                },
                {
                    "id": 3,
                    "text": {
                        "en" : "Nothing",
                        "de" : "Nichts",
                        "ru" : "Ничего"
                    },
                    "next": "end"
                }
            ],
            "action": null
        },
        {
            "id": "last_news",
            "text": {
                "en" : "Have you heard the latest news?",
                "de" : "Haben Sie die neuesten Nachrichten gehört?",
                "ru" : "Вы слышали последние новости?"
            },
            "options": [
                {
                    "id": 0,
                    "text": {
                        "en" : "No..",
                        "de" : "Nein",
                        "ru" : "Нет"
                    },                   
                    "next": "end"
                }
            ],
            "action": null
        },
        {
            "id": "not_local",
            "text": {
                "en" : "I see you’re not from around here.",
                "de" : "Ich sehe, Sie sind nicht von hier.",
                "ru" : "Я вижу, вы не отсюда."
            },          
            "options": [
                {
                    "id": 0,
                    "text": {
                        "en" : "Yes",
                        "de" : "Ja",
                        "ru" : "Да"
                    },
                    "next": "end"
                }
            ],
            "action": null
        },
        {
            "id": "why",
            "text": {
                "en" : "What brought you here?",
                "de" : "Was hat Sie hierher geführt?",
                "ru" : "Что привело вас сюда?"
            },
            
            
            "options": [
                {
                    "id": 0,
                    "text": {
                        "en" : "Hothing",
                        "de" : "Hothing",
                        "ru" : "Ничего"
                    },
                    "next": "end"
                }
            ],
            "action": null
        },
        {
            "id": "ammo",
            "text": {
                "en" : "I have some ammo. But not for free..",
                "de" : "Ich habe etwas Munition. Aber nicht umsonst..",
                "ru" : "У меня есть кое-какие патроны. Но не даром.."
            },
            "options": [
                {
                    "id": 0,
                    "text": {
                        "en" : "How many?",
                        "de" : "Wie viele?",
                        "ru" : "Сколько?"
                    },
                    "next": "end"
                }
            ],
            "action": null
        },
        {
            "id": "quest",
            "text": {
                "en" : "There is one thing. A mutant has appeared in the catacombs...",
                "de" : "Da ist eine Sache. In den Katakomben ist ein Mutant aufgetaucht ...",
                "ru" : "Есть одно но: в катакомбах появился мутант..."
            },
            "options": [
                {
                    "id": 0,
                    "text": {
                        "en" : "I'm in!",
                        "de" : "Ich bin dabei!",
                        "ru" : "Я в деле!"
                    },
                    "next": "end"
                },
                {
                    "id": 1,
                    "text": {
                        "en" : "Not now",
                        "de" : "Nicht jetzt",
                        "ru" : "Не сейчас"
                    },
                    "next": "end"
                }
            ],
            "action": null
        },
        {
            "id": "end",
            "action": "exit_dialog"
        }
    ],
    "actions": [
        {
            "id": "exit_dialog",
            "function": "exit()",
            "comment": "Exit from this Dialog"
        }
    ]
}
"""