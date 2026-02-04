# core.toolbar.py


# --- JSON Editor Menu ---
from gui.dialogs.dialog.jsonEditorWin import JsonEditorWin
from gui.dialogs.library.plibEditorWin import PlibEditorWin
from gui.dialogs.library.save_data_to_file import library_save_data_to_file, library_save, library_save_as

from core.dialog.dialogData import dialogData
from core.library.plibData import PlibData
from tkinter import filedialog, messagebox
import json
import os
#dialogData

# --- File Menu ---
def file_menu_new_file(self): 
    dialogData.clear()
    self.app.root.title("Dialogue Editor - New File")


def file_menu_load_file(menu_self):
    file_path = filedialog.askopenfilename(title="Load dialog File", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    print(file_path)
    if file_path:
        dialogData.load(file_path)
        dialogData.set_file_path(file_path) # Set file path
        dialogData.set_file_name() # Set file name
            #data = dialogData.get()
    #print(dialogData.get())
    menu_self.app.dialog_tree.refresh_tree()
       

def file_menu_save_file(menu_self):
    pass

def file_menu_save_as_file(menu_self):
    pass

def file_menu_exit_app(menu_self):
    pass


# --- Dictionary Menu ---
def dict_menu_view_dictionary():
    PlibEditorWin()

def dict_menu_new_dictionary(menu_self):
    PlibData.clear()
    menu_self.app.library_tree.refresh_tree()
    
    pass

def dict_menu_load_dictionary(menu_self):
    file_path = filedialog.askopenfilename(title="Load dictionary File", filetypes=[("Phrases Library files", "*.plib"), ("All files", "*.*")])
    if file_path:
        PlibData.load(file_path)
        PlibData.set_file_path(file_path) # Set file path
        PlibData.set_file_name() # Set file name
        #data = PlibData.get()        
        menu_self.app.library_tree.refresh_tree()


def dict_menu_save_dictionary(menu_self):
    #print(PlibData.get_file_name())
    #print(PlibData.get_file_path())
    #print(PlibData.get())
    
    #library_save(PlibData.get(), PlibData.get_file_path())
    """Save - сохраняем в последний путь, если он есть"""
    last_path = PlibData.get_file_path()
    data = PlibData.get()

    if last_path:
        library_save_data_to_file(data, last_path)
    else:
        dict_menu_save_as_dictionary(menu_self)

    

def dict_menu_save_as_dictionary(menu_self):
    """Save As - выбираем путь через диалог"""
    initial_name = os.path.basename(PlibData.get_file_path()) if PlibData.get_file_path() else "new_dictionary.plib"
    
    filepath = filedialog.asksaveasfilename(
        defaultextension=".plib",
        initialfile=initial_name,
        filetypes=[("Phrases Library files", "*.plib"), ("All files", "*.*")],
        title="Save Dictionary As"
    )
    if not filepath:
        return

    # Сохраняем данные
    library_save_data_to_file(PlibData.get(), filepath)
    
    # Обновляем путь и имя файла
    PlibData.set_file_path(filepath)
    PlibData.set_file_name()




# --- JSON Editor Menu ---
def json_menu_view_dictionary():
    JsonEditorWin()



