Visual Studio Code
-

#Keyboard shortcut for show code actions
code actions: key(ctrl-.)

#Closes the current folder
workspace folder close:
    key(alt-f)
    key(f:2)
    key(enter)

#Switch to the terminal
terminal: user.vscode("workbench.action.terminal.focus")

#Switch to the editor
editor: user.vscode("workbench.action.focusActiveEditorGroup")

#Run last terminal command and move back to editor
(terminal|term) (repeat|peat):
    user.vscode("workbench.action.terminal.focus")
    key(up)
    key(enter)
    user.vscode("workbench.action.focusActiveEditorGroup")

(terminal|term) stop (repeat|peat):
    user.vscode("workbench.action.terminal.focus")
    key(ctrl-c)
    key(up)
    key(enter)
    user.vscode("workbench.action.focusActiveEditorGroup")

code pass:
    edit.select_all()
    edit.copy()
    key(escape)
    key(alt-tab)
    edit.paste()
    edit.save()

