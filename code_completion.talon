not tag: user.exam_mode
-
complete: user.fire_chicken_get_code_completion_using_file(300, 128)
^pete$: user.fire_chicken_use_code_completion_option(1)
pete <number_small>: user.fire_chicken_use_code_completion_option(number_small)
^pine$: 
	user.fire_chicken_use_code_completion_option_line(1)
	edit.line_insert_down()
sleet:
	edit.line_insert_down()
	user.fire_chicken_get_code_completion_using_file(300, 128)
replete:
	user.code_operator("ASSIGNMENT")
	user.fire_chicken_get_code_completion_using_file(300, 128)