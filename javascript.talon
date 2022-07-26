tag: user.javascript
-
tag(): user.c_style_programming

build coop: user.c_style_programming_make_count_for_loop_given_datatype('let')


logging: insert("console.log(")

dot length: '.length'
dot name: '.name'

state set: 'set '
state get: 'get '
state in: ' in '

strict same: ' === '
strict equal: '==='

allow <user.prose>$:
    insert('let ')
    user.insert_formatted(prose, 'camel')
allow <user.prose> over:
    insert('let ')
    user.insert_formatted(prose, 'camel')

constant <user.prose>$:
    insert('const ')
    user.insert_formatted(prose, 'all cap,snake')
constant <user.prose> over:
    insert('const ')
    user.insert_formatted(prose, 'all cap,snake')

build for:
    user.generic_programming_build_for('for (let ', '; ', '; ', ')')

