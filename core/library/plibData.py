# core.library.plibData.py

import os
from core.library.pLibParser import PLibParser

class PLibData():
    def __init__(self):
        self.__data = {}
        self.__data_text = ""
        self.__file_path = None
        self.__file_name = "new_phrases_library.plib"
        self.__language = "all"


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


    # --- Headers ---
    def get_headers(self):
        return list(self.get().keys()) # headerts of topics


    # --- Category ---
    def get_category(self, category):
        return self.__data[category]
    
    
    def set_category_data(self, category, data):
        self.__data[category] = data


    def add_category(self, category):
        self.__data[category] = []
    


    def edit_category_name(self, old_category, new_category):
        self.add_category(new_category)
        self.set_category_data(new_category, self.__data[old_category])
        self.delete_category(old_category)


    def delete_category(self, category):
        del self.__data[category]


    # --- Data ---
    def add_phrase(self, category, phrase):
        self.__data.setdefault(category, []).append(phrase)


    def edit_phrase(self, category, phrase, new_phrase):
        # search and replace
        for i, phrase_dict in enumerate(self.__data.get(category, [])):
            if phrase_dict.get('en') == phrase:
                self.__data[category][i] = new_phrase
                break  # if there is no more than one such phrase
    
    def delete_phrase(self, category, phrase):
        # search and replace
        for i, phrase_dict in enumerate(self.__data.get(category, [])):
            if phrase_dict.get('en') == phrase:
                del self.__data[category][i]
                break  # if there is no more than one such phrase


    def set_all(self, data):
        # If a string arrived → we try to parse it
        if isinstance(data, str):
            self.__data_text = data
        # If a dict or list arrived → we accept it as is
        elif isinstance(data, (dict, list)):
            self.__data = data
        else:
            raise TypeError("set_all expects str")


    def save(self, filepath):
        # Save PLIB to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.__data_text)


    def load(self, filepath):
        # Load PLIB from file
        with open(filepath, "r", encoding="utf-8") as f:
            self.__data_text = f.read()
            lines = self.__data_text.splitlines() # if needed for line-by-line parsing
            parser = PLibParser(lines, self.__language) # parsing
            self.__data = parser.separation()


    def get(self):
        return dict(self.__data)


    def get_text(self):
        return self.__data_text


    # --- phrase ---
    def get_phrase_by_phrase(self, category, phrase):
        found = None
        for item in self.__data.get(category, []):
            if phrase in item.values():   # check if the string is among the translations
                found = item
                break
        return found
        

    def clear(self):
        self.__data = {}
        self.__data_text = ""


PlibData = PLibData()
