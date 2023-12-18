app: vscode
code.language: python
-
debug <user.cursorless_target>:
    user.fire_chicken_programming_insert_python_debug_print_statement_from_cursorless_target(cursorless_target)

output <user.cursorless_target>:
    user.cursorless_command("editNewLineAfter", cursorless_target)
    user.fire_chicken_programming_insert_python_debug_print_statement_from_cursorless_target(cursorless_target)