code.language: cpp
code.language: c
app: vscode
-
debug <user.cursorless_target>:
	user.generic_programming_start_new_line_if_current_line_not_empty()
	insert('std::cout << "')
	user.fire_chicken_cursorless_bring(cursorless_target)
	insert('" << ')
	user.fire_chicken_cursorless_bring(cursorless_target)
	insert(" << '\\n';")
