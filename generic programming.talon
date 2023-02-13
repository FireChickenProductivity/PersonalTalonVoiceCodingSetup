
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
leap|leal:
	edit.line_end()
	key(enter)
beep|feel:
	user.generic_programming_create_line_below()
	edit.delete()
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
phrasing <user.text>$: user.insert_with_history(' ' + text)
phrasing <user.text> over: user.insert_with_history(' ' + text)
sore <user.prose>$: user.insert_formatted(prose, 'snake')
sore <user.prose> over: user.insert_formatted(prose, 'snake')
soaring <user.prose>$: user.insert_formatted('_' + prose, 'snake')
soaring <user.prose> over: user.insert_formatted('_' + prose, 'snake')
flow [case] <user.prose>$: user.insert_formatted(prose, 'all cap,snake')
flow [case] <user.prose> over: user.insert_formatted(prose, 'all cap,snake')
flowing <user.prose>$: user.insert_formatted('_' + prose, 'all cap,snake')
flowing <user.prose> over: user.insert_formatted('_' + prose, 'all cap,snake')
caps case <user.prose>$: user.insert_formatted(prose ,'hammer')
caps case <user.prose> over: user.insert_formatted(prose ,'hammer')

member <user.prose>$: user.insert_formatted('.' + prose, 'camel')
member <user.prose> over: user.insert_formatted('.' + prose, 'camel')
fellow <user.prose>$: user.insert_formatted('.' + prose, 'snake')
fellow <user.prose> over: user.insert_formatted('.' + prose, 'snake')
sword <user.word>:
	insert('.')
	user.insert_with_history(word)

#Ball is a mix between tall and big. Capitalizes the word
ball <user.word>:
	user.insert_formatted(word, 'hammer')

march <user.word>: insert(word + ' ')
push <user.word>: insert(' ' + word)
shove <user.word>:
	insert(' ' + word)
	insert(' ')

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
	user.insert_formatted(prose, 'snake')
selfie <user.prose> over:
	user.generic_programming_self_dot()
	user.insert_formatted(prose, 'snake')

selfish <user.prose>$:
	user.generic_programming_self_dot()
	user.insert_formatted(prose, 'camel')
selfish <user.prose> over:
	user.generic_programming_self_dot()
	user.insert_formatted(prose, 'camel')


swordfish <user.word>:
	user.generic_programming_self_dot()
	user.insert_with_history(word)



kind {user.code_type}:
	insert(code_type + ' ')
kinder {user.code_type} <user.prose>$:
	insert(code_type + ' ')
	user.insert_formatted(prose, 'camel')
kinder {user.code_type} <user.prose> over:
	insert(code_type + ' ')
	user.insert_formatted(prose, 'camel')

#comma related commands
spam: user.generic_programming_insert_comma_separator()
beef:
	edit.right()
	user.generic_programming_insert_comma_separator()

#camel
reason <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'camel')
reason <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'camel')
#snake
proclaim <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'snake')
proclaim <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'snake')
#PascalCase
surmise <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'hammer')
surmise <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'hammer')


#searching:
search <user.text>:
	user.simple_action_search_next(text)

chase <user.spelling_out_symbol>+:
	user.simple_action_search_next_multiple(spelling_out_symbol_list)

bound <user.spelling_out_symbol>:
	user.generic_programming_regular_expression_boundary_search_next(spelling_out_symbol)
