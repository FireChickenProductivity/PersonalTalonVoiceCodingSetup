not tag: user.exam_mode
-
complete: user.fire_chicken_get_code_completion_using_file(300, 10)
^pete$: user.fire_chicken_use_code_completion_option(1)
pete <number_small>: user.fire_chicken_use_code_completion_option(number_small)
^pen$: user.fire_chicken_use_code_completion_option_token(1)
^pine$: 
	user.fire_chicken_use_code_completion_option_line(1)
	edit.line_insert_down()
sleet:
	edit.line_insert_down()
	user.fire_chicken_get_code_completion_using_file(300, 10)
replete:
	user.code_operator("ASSIGNMENT")
	user.fire_chicken_get_code_completion_using_file(300, 10)

autocomplete on: user.fire_chicken_set_auto_run_completion(true)
autocomplete off: user.fire_chicken_set_auto_run_completion(false)