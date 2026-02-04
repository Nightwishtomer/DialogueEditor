# core.library.buttons.py


from gui.dialogs.library.new_node_Win import NewNodeWin
from core.library.plibData import PlibData

from gui.dialogs.library.edit_node_Win import EditNodeWin
from gui.dialogs.library.edit_phrase_Win import EditPhraseWin

from gui.dialogs.library.popup.delete_node_phrase_Win import DeleteNodePhraseWin



# -- Buttons --- main Frame ---
def library_add(self):
    NewNodeWin(self)
    pass


def library_edit(self, focused):
    if focused[1] == "None":
        EditNodeWin(self, focused)
    else:
        EditPhraseWin(self, focused)


def library_delete(self, focused):
    DeleteNodePhraseWin(self, focused)
    #if focused[1] == "None":
    #    EditNodeWin(self, focused)
    #else:
    #    EditPhraseWin(self, focused)
