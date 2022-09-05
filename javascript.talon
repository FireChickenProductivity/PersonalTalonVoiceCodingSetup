tag: user.javascript
-
tag(): user.c_style_programming
tag(): user.fire_chicken_fast_functions

dot length: '.length'
dot name: '.name'

state set: 'set '
state get: 'get '
op in: ' in '
op (spread|rest): '...'

strict same: ' === '
strict equal: '==='
strict (bang|banger): ' !== '
strict not: '!=='

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

is (not a number| nan):
    user.fire_chicken_call_function_inside('isNaN')

proper <user.prose>:
    user.fire_chicken_insert_javascript_property(prose)

(proper|prop) method <user.prose>:
    user.fire_chicken_insert_javascript_property(prose)
    user.fire_chicken_call_function_inside('function')

(proper|prop) set <user.prose>:
    insert('set ')
    user.fire_chicken_call_function_inside_with_name_formatted(prose, 'camel')

(proper|prop) get <user.prose>:
    insert('get ')
    user.fire_chicken_call_function_inside_with_name_formatted(prose, 'camel')
