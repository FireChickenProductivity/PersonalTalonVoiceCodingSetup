app: vscode
code.language: python
-
debug <user.cursorless_target>:
    user.generic_programming_start_new_line_if_current_line_not_empty()
    user.fire_chicken_programming_insert_python_debug_print_statement_from_cursorless_target(cursorless_target)

output <user.cursorless_target>:
    user.cursorless_command("editNewLineAfter", cursorless_target)
    user.fire_chicken_programming_insert_python_debug_print_statement_from_cursorless_target(cursorless_target)

query <user.cursorless_target>:
    insert('[')
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert(']')

slicing <user.cursorless_target>:
    user.generic_programming_start_new_line_if_current_line_not_empty()
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert('[')