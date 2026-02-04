# core.jsonData.py

import json, os

class JsonData():
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
        self.__file_name = os.path.basename(self.__file_path) if self.__file_path else "new_dialog.json"


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



DialogData = JsonData()

