jump: edit.line_end()
choice: key(enter)
remove: key(delete)
#On windows, clearing presses backspace
clearing: edit.delete()
swing: key(tab)

semi: key(;)
slump:
	edit.line_end()
	key(;)
fly: edit.up()
spring:
	edit.up()
	edit.line_start()

down: edit.down()
dance: 
	edit.down()
	key(tab)

who: edit.right()
sue: edit.word_right()

stew:
	edit.extend_word_right()
	user.generic_programming_wait_word_movement_delay()
	edit.delete()
	user.generic_programming_wait_word_movement_delay()

why: edit.left()
sly: edit.word_left()
sty:
	edit.extend_word_left()
	user.generic_programming_wait_word_movement_delay()
	edit.delete()
	user.generic_programming_wait_word_movement_delay()

choice <number_small>:
	edit.down()
	repeat(number_small - 1)
	key(enter)
choosing <number_small>:
	edit.up()
	repeat(number_small - 1)
	key(enter)

rear <number_small>:
	edit.line_end()
	edit.left()
	repeat(number_small - 1)
stern <number_small>:
	edit.line_end()
	edit.word_left()
	repeat(number_small - 1)
lead <number_small>:
	edit.line_start()
	edit.right()
	repeat(number_small - 1)
steer <number_small>:
	edit.line_start()
	edit.word_right()
	repeat(number_small - 1)