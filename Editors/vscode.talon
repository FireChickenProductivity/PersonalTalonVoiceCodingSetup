app: Visual Studio Code
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
    sleep(0.5)
    edit.paste()
    edit.save()

running: key(ctrl-f5)

settings():
    user.context_sensitive_dictation = 1
    user.fire_chicken_context_sensitive_dictation_use_basic_action_recorder_for_context = 1
