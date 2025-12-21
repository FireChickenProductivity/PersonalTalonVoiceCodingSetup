not tag: user.exam_mode
-

pattern:
	pattern = user.fire_chicken_programming_get_pattern()
	user.fire_chicken_programming_insert_pattern(pattern)

pat <user.cursorless_target>:
	text = user.cursorless_get_text(cursorless_target)
	user.fire_chicken_programming_save_from(text)
