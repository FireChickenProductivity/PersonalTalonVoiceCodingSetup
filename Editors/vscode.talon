app: Visual Studio Code
app: Code
-

#Keyboard shortcut for show code actions
code actions: key(ctrl-.)

#Closes the current folder
workspace folder close:
    user.fire_chicken_close_active_vscode_folder()

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

restart <number_small> terminals:
    user.fire_chicken_repeat_stop_terminals(number_small)

code pass:
    edit.select_all()
    edit.copy()
    key(escape)
    user.fire_chicken_switch_to_last_application()
    sleep(0.5)
    edit.paste()
    edit.save()

running: key(ctrl-f5)

sail | next: user.move_cursor_to_next_snippet_stop()
stale {user.snippet}:
    user.move_cursor_to_next_snippet_stop()
    user.insert_snippet_by_name_with_stop_at_end(snippet)
surd <user.word>:
    user.move_cursor_to_next_snippet_stop()
    insert(word)
mast <user.cursorless_target>:
    user.move_cursor_to_next_snippet_stop()
    user.fire_chicken_cursorless_bring(cursorless_target)

settings():
    user.context_sensitive_dictation = 1
    user.fire_chicken_context_sensitive_dictation_use_basic_action_recorder_for_context = 1
    user.fire_chicken_context_sensitive_dictation_select_word_delay = 100
    user.fire_chicken_context_sensitive_dictation_ending_delay = 50