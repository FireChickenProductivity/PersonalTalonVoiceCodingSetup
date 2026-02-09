tag: user.cursorless
code.language: python
-
slot <user.cursorless_target>:
	class_text = user.cursorless_get_text(cursorless_target)
	text_with_slots = user.fire_chicken_python_add_slots(class_text)
	user.cursorless_command("setSelection", cursorless_target)
	user.paste(text_with_slots)

cross <user.cursorless_target>:
	user.fire_chicken_cursorless_bring(cursorless_target)
	insert(":")
	edit.line_start()
	user.fire_chicken_insert_around_cursor("for ", " in ")