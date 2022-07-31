
coalmine: 
	edit.line_end()
	key(:)
	key(enter)
coaler: ': '
coaling: ' : '

simmer: '; '

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
	insert('{')
	key(enter)
leap:
	edit.line_end()
	key(enter)
beep:
	edit.line_end()
	key(enter)
	edit.delete()
reap:
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

#symbol dictation
(some|sum): ' + '
minus: ' - '
times: ' * '
divide: ' / '
adding: ' += '
increase: '+='
subtract: ' -= '
decrease: '-='
product: ' *= '
growing: '*='
quotient: ' /= '
splitting: '/='
assign|receive: ' = '
lesser: ' < '
greater: ' > '
mod: ' % '
remain: ' %= '
surplus: '%='
same: ' == '
equal: '=='
at least: ' >= '
at most: ' <= '
as small: '<='
as large: '>='
banging: ' ! '
landing: ' && '
lowland: '&&'
laurel: '||'
loring: ' || '
piping: ' | '
amping: ' & '
banger: ' != '
loudly: '!='
coaling: ' : '
calming: ' , '
calmer: ', '
implies: ' => ' 
larrow: ' -> '

#grouping symbols
group: '('
grouping: ' ( '
leftgroup: ' ('
rightgroup: ')'
R group: ' ) '
squaring: ' [ '
left square: ' ['
R square: ' ] '
bracing: ' { '
left brace: ' {'
R brace: ' } '
#fish was conflicting with fifth, so I am using clown (a type of fish) instead
clown: '<'
fishing|clowning: ' < '
left (fish|clown): ' <'
right (fish|clown): '>'
R (fish|clown): ' > '
diamond: '<>'

use:
	insert('()')
	edit.left()
using:
	insert('(  )')
	edit.left()
	repeat(1)
useless:
	insert(' ()')
	edit.left()
uses:
	insert(' (  )')
	edit.left()
	repeat(1)


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

method <user.prose>$:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'camel')
method <user.prose> over:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'camel')

perform <user.prose>$:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'snake')

perform <user.prose> over:
	user.generic_programming_call_method_inside_with_name_formatted(prose, 'snake')

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


#searching:
search <user.text>:
	user.simple_action_search_next(text)

chase <user.spelling_out_symbol>+:
	user.simple_action_search_next_multiple(spelling_out_symbol_list)

bound <user.spelling_out_symbol>:
	user.generic_programming_regular_expression_boundary_search_next(spelling_out_symbol)

kind {user.code_type}:
	insert(code_type + ' ')
kinder {user.code_type} <user.prose>$:
	insert(code_type + ' ')
	user.insert_formatted(prose, 'camel')
kinder {user.code_type} <user.prose> over:
	insert(code_type + ' ')
	user.insert_formatted(prose, 'camel')

reason <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'camel')
reason <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'camel')
proclaim <user.prose>$:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'snake')
proclaim <user.prose> over:
	user.generic_programming_insert_comma_separator()
	user.insert_formatted(prose, 'snake')
