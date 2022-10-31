jump: edit.line_end()
spear: key(enter)
remove|clean|wash: key(delete)
(clean|wash) <number_small>:
	key(delete)
	repeat(number_small - 1)
#On windows, clearing presses backspace
clearing|sweep: edit.delete()
sweep <number_small>:
	edit.delete()
	repeat(number_small - 1)
swing: key(tab)
cape: key(escape)

wrong: edit.undo()
wrong <number_small>:
	edit.undo()
	repeat(number_small - 1)

semi: key(;)
slump:
	edit.line_end()
	key(;)
fly: edit.up()
steam:
	edit.up()
	edit.line_start()

rain: edit.down()
snow:
	edit.down()
	edit.line_end()
dance: 
	edit.down()
	key(tab)

who: edit.right()
sue: edit.word_right()

soap:
	edit.extend_word_right()
	user.generic_programming_wait_word_movement_delay()
	edit.delete()
	user.generic_programming_wait_word_movement_delay()

why: edit.left()
sly: edit.word_left()
broom:
	edit.extend_word_left()
	user.generic_programming_wait_word_movement_delay()
	edit.delete()
	user.generic_programming_wait_word_movement_delay()

pick <number_small>:
	edit.down()
	repeat(number_small - 1)
	key(enter)
<number_small> pick:
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
