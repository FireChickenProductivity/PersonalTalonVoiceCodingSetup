#symbol dictation
rope: '"'
lace: user.fire_chicken_insert_around_cursor('"', '"')
(twin|twine): user.fire_chicken_insert_around_cursor("'", "'")
yarn: '`'
noise: '&'
summing: ' + '
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
moding: ' % '
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
staff: ': '
pole:
	edit.line_end()
	insert(': ')
simmer: '; '
swine: ';'
calming: ' , '
calmer: ', '
implies: ' => ' 
dart: ' -> '
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
taco: user.fire_chicken_insert_around_cursor("{", "}")
#fish was conflicting with fifth, so I am using clown (a type of fish) instead
clown: '<'
fishing|clowning: ' < '
left (fish|clown): ' <'
right (fish|clown): '>'
R (fish|clown): ' > '
diamond: '<>'
shoe: '_'
swirl: "@"

oval: insert('()')
slice:
	insert('[]')
	edit.left()