
coalmine|heel: 
	edit.line_end()
	key(:)
	key(enter)


embrace:
	edit.line_end()
	insert(" {")
	key(enter)
bracer:
	edit.line_end()
	key("{")
	key(enter)
bracelet:
	edit.line_end()
	key(enter)
	user.fire_chicken_insert_around_cursor('{', '}')
	key(enter)
clasp:
	key('space')
	key('{')
leap|leal:
	edit.line_end()
	key(enter)
beep|feel:
	user.generic_programming_create_line_below()
	edit.delete()
pound:
	user.generic_programming_create_line_below()
	edit.delete()
	key(enter)
reap|real:
	edit.line_end()
	key(enter)
	key(tab)
(release|sheep):
	edit.line_end()
	key(;)
	key(enter)
keep:
	edit.line_end()
	key(,)
	key(enter)


#generic building
build calls <number_small> [args|arg|argue|argues|argument|arguments]:
	user.fire_chicken_build_calls(number_small)

#formatting:
phrasing|sing <user.text>$: insert(' ' + text)
phrasing|sing <user.text> over: insert(' ' + text)
sore <user.prose>$: user.fire_chicken_insert_with_snake_case(prose)
sore <user.prose> over: user.fire_chicken_insert_with_snake_case(prose)
soaring <user.prose>$: user.fire_chicken_insert_with_snake_case('_' + prose)
soaring <user.prose> over: user.fire_chicken_insert_with_snake_case('_' + prose)
flow [case] <user.prose>$: user.fire_chicken_insert_with_upper_snake_case(prose)
flow [case] <user.prose> over: user.fire_chicken_insert_with_upper_snake_case(prose)
flowing <user.prose>$: user.fire_chicken_insert_with_upper_snake_case('_' + prose)
flowing <user.prose> over: user.fire_chicken_insert_with_upper_snake_case('_' + prose)
pascal <user.prose>$: user.fire_chicken_insert_with_pascal_case(prose)
pascal <user.prose> over: user.fire_chicken_insert_with_pascal_case(prose)
object <user.text>$: 
	user.fire_chicken_auto_generated_command_action_insert_formatted_text(user.text_1, 'capitalized', '')
	insert('()')
	key('left')

member <user.prose>$: user.fire_chicken_insert_with_camel_case('.' + prose)
member <user.prose> over: user.fire_chicken_insert_with_camel_case('.' + prose)
fellow <user.prose>$: user.fire_chicken_insert_with_snake_case('.' + prose)
fellow <user.prose> over: user.fire_chicken_insert_with_snake_case('.' + prose)
sword <user.word>:
	insert('.')
	user.fire_chicken_programming_insert_with_history(word)

march <user.word>: insert(word + ' ')
push <user.word>: insert(' ' + word)
shove <user.word>:
	insert(' ' + word)
	insert(' ')

tooth: edit.paste()
fang:
	edit.paste()
	user.fire_chicken_insert_around_cursor('(', ')')

method <user.prose>$:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'camel')
method <user.prose> over:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'camel')

perform <user.prose>$:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'snake')

perform <user.prose> over:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'snake')

routine <user.prose>$:
	user.fire_chicken_call_function_inside_with_name_formatted(prose, 'camel')
routine <user.prose> over:
	user.fire_chicken_call_function_inside_with_name_formatted(prose, 'camel')
process <user.prose>$:
	user.fire_chicken_call_function_inside_with_name_formatted(prose, 'snake')
process <user.prose> over:
	user.fire_chicken_call_function_inside_with_name_formatted(prose, 'snake')

selfie <user.prose>$:
	user.generic_programming_self_dot()
	user.fire_chicken_insert_with_snake_case(prose)
selfie <user.prose> over:
	user.generic_programming_self_dot()
	user.fire_chicken_insert_with_snake_case(prose)

selfish <user.prose>$:
	user.generic_programming_self_dot()
	user.fire_chicken_insert_with_camel_case(prose)
selfish <user.prose> over:
	user.generic_programming_self_dot()
	user.fire_chicken_insert_with_camel_case(prose)


swordfish <user.word>:
	user.generic_programming_self_dot()
	user.fire_chicken_programming_insert_with_history(word)



kind {user.code_type}:
	insert(code_type + ' ')
kinder {user.code_type} <user.prose>$:
	insert(code_type + ' ')
	user.fire_chicken_insert_with_camel_case(prose)
kinder {user.code_type} <user.prose> over:
	insert(code_type + ' ')
	user.fire_chicken_insert_with_camel_case(prose)

#comma related commands
spam: user.generic_programming_insert_comma_separator()
beef:
	edit.right()
	user.generic_programming_insert_comma_separator()

#camel
reason <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.fire_chicken_insert_with_camel_case(prose)
reason <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.fire_chicken_insert_with_camel_case(prose)
#snake
proclaim <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.fire_chicken_insert_with_snake_case(prose)
proclaim <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.fire_chicken_insert_with_snake_case(prose)
#PascalCase
surmise <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.fire_chicken_insert_with_pascal_case(prose)
surmise <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.fire_chicken_insert_with_pascal_case(prose)


#searching:
search <user.text>:
	user.simple_action_search_next(text)

chase <user.spelling_out_symbol>+:
	user.simple_action_search_next_multiple(spelling_out_symbol_list)

bound <user.spelling_out_symbol>:
	user.generic_programming_regular_expression_boundary_search_next(spelling_out_symbol)

#navigation
swim: app.tab_next()
dive: app.tab_previous()