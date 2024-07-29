code.language: javascript
code.language: html
-
tag(): user.c_style_programming
tag(): user.fire_chicken_fast_functions

dot length: '.length'
dot name: '.name'

state set: 'set '
state get: 'get '
op in: ' in '
op (spread|rest): '...':
dom dot: 'document.'
(win|window) dot: 'window.'

strict same: ' === '
strict equal: '==='
strict (bang|banger): ' !== '
strict not: '!=='

compose <user.text>$:
    user.fire_chicken_insert_react_component(text)
compose <user.text> over:
    user.fire_chicken_insert_react_component(text)

allow <user.prose>$:
    insert('let ')
    user.fire_chicken_insert_formatted_text(prose, 'camel')
allow <user.prose> over:
    insert('let ')
    user.fire_chicken_insert_formatted_text(prose, 'camel')

constant <user.prose>$:
    insert('const ')
    user.fire_chicken_insert_formatted_text(prose, 'camel')
constant <user.prose> over:
    insert('const ')
    user.fire_chicken_insert_formatted_text(prose, 'camel')

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

#The Ren is short for parenthesis
(lamb|lambda) [non] Ren:
    insert('() => {}')
    edit.left()
    key(enter)

(lamb|lambda) non:
    insert(' => {}')
    edit.left()
    key(enter)

inner (html|hit mal):
    insert('.innerHTML = ')

function: 
    insert('function ')

export: 'export '
default: 'default '

importing: 
    insert('import {  ')
    edit.left()
import: 'import '

value: 
    insert('$(')

hooking <user.text>:
    user.fire_chicken_insert_react_hook(text)