# gui.library.delete_node_phrase_Win.py

import tkinter as tk
from tkinter import ttk, messagebox
from core.library.plibData import PlibData

class DeleteNodePhraseWin():
    def __init__(self, root_self, focused):
        self.root_self = root_self
        self.category = focused[0]
        self.phrase = focused[1]


        
 
        

        # Показываем окно подтверждения
        confirm = messagebox.askyesno(
            "Confirm Delete", 
            f"Are you sure you want to delete:\n{self.phrase}?"
        )
        
        if confirm:
            # Удаляем из данных
            if self.phrase == "None":
                PlibData.delete_category(self.category)
                #EditNodeWin(self, focused)
            else:
                PlibData.delete_phrase(self.category, self.phrase)
            #EditPhraseWin(self, focused)

            # Обновляем дерево
            self.root_self.app.library_tree.refresh_tree()
