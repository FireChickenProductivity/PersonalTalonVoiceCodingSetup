#symbol dictation
rope: '"'
yarn: '`'
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
staff: ': '
simmer: '; '
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
