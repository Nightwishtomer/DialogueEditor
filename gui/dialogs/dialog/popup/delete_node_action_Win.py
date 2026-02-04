# gui.library.delete_node_action_Win.py

import tkinter as tk
from tkinter import ttk, messagebox
from core.dialog.dialogData import dialogData

class DeleteNodeActionWin():
    def __init__(self, root_self, focused):
        self.root_self = root_self
        self.type = type
        self.category = focused
            
        if focused[0] is None or focused[0] == "None":
            return

        # Показываем окно подтверждения
        


        if focused[0] == "node":
            confirm = messagebox.askyesno(
                "Confirm Node Delete ", 
                f"Are you sure you want to delete:\n{focused[1]}?"
            )
            if confirm:
                # Удаляем из данных
                dialogData.delete_node(focused[1])
        elif focused[0] == "option":
            confirm = messagebox.askyesno(
                "Confirm OptionDelete", 
                f"Are you sure you want to delete:\n{focused[1]} -> {focused[2]}?"
            )
            if confirm:
                # Удаляем из данных
                dialogData.delete_option(focused[1], focused[2])
        elif focused[0] == "action":
            confirm = messagebox.askyesno(
                "Confirm Action Delete", 
                f"Are you sure you want to delete:\n{focused[1]}?"
            )
            if confirm:
                # Удаляем из данных
                dialogData.delete_action(focused[1])


        # Обновляем дерево
        self.root_self.app.dialog_tree.refresh_tree()

        
 
        

     
        
        #if confirm:
        #    # Удаляем из данных
        #    if self.phrase == "None":
        #        PlibData.delete_category(self.category)
        #        #EditNodeWin(self, focused)
        #    else:
        #        PlibData.delete_phrase(self.category, self.phrase)
        #    #EditPhraseWin(self, focused)
        #
        
