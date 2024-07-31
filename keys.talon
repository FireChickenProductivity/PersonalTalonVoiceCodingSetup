jump: edit.line_end()
basement: edit.file_end()
attic: edit.file_start()
pup: key(pageup)
pone: key(pagedown)
boing:
	edit.line_end()
	key(space)
punch: '. '
pounce:
	edit.line_end()
	insert('. ')
spear|spare: key(enter)
lance: key(shift-enter)
wash: key(delete)
wash <number_small>:
	key(delete)
	repeat(number_small - 1)
club:
	edit.line_end()
	key(shift-down)
	key(shift-end)
	key(backspace)
stretch:
	edit.line_start()
	key(shift-up)
	key(shift-home)
	key(backspace)
#On windows, clearing presses backspace
sweep: edit.delete()
sweep <number_small>:
	edit.delete()
	repeat(number_small - 1)
clearing: edit.delete_line()
swing: key(tab)
switch: user.fire_chicken_switch_to_last_application()

fail: edit.undo()
fail <number_small>:
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
pass:
	edit.right()
	edit.right()
sue: edit.word_right()

soap:
	edit.extend_word_right()
	user.generic_programming_wait_word_movement_delay()
	edit.delete()
	user.generic_programming_wait_word_movement_delay()

lone: edit.left()
wolf:
	edit.left()
	edit.left()
sly: edit.word_left()
broom|boom|bloom:
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

cushion:
	key(enter:2)
	edit.up()
stomp:
	key(enter)
	edit.up()

slam: key(escape)

mimic: edit.copy()
miming:
	edit.select_all()
	edit.copy()

blade: ' --'
knife: ' -'