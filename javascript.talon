tag: user.javascript
-
tag(): user.c_style_programming


logging: insert("console.log(")

dot length: '.length'
dot name: '.name'

state set: 'set '
state get: 'get '
op in: ' in '

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
    user.insert_formatted(prose, 'camel')
constant <user.prose> over:
    insert('const ')
    user.insert_formatted(prose, 'camel')

build for let:
    user.generic_programming_build_for('for (let ', '; ', '; ', ')')

