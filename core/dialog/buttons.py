# core.dialog.buttons.py

from gui.dialogs.dialog.popup.delete_node_action_Win import DeleteNodeActionWin

def node_add(self_tree):
    print("node_add")
    pass

def node_edit(self_tree, focused):
    print("node_edit")
    print("focused")
    print(focused)
    pass


def action_add(self_tree):
    print("action_add")
    pass

def action_edit(self_tree, focused):
    print("action_edit")
    print("focused")
    print(focused)
    pass




def delete(self_tree, focused):
    print("node_delete")
    print("focused")
    print(focused)
    DeleteNodeActionWin(self_tree, focused)
    pass
