code.language: python
-
tag(): user.fire_chicken_programming_self_reference_constructor
tag(): user.build_for_loops
tag(): user.fire_chicken_snippets

#activating and deactivating talon python commands
talon python activate: user.talon_programming_activate_python_commands()
talon python deactivate: user.talon_programming_deactivate_python_commands()

op (in|each): ' in '
op not: 'not '
op not in: ' not in '
op length: 'len('

annotate <user.code_type>:
    insert(': ')
    insert(code_type)

[state] else if:
    insert('elif :')
    edit.left()

constructor|construct:
    insert('def __init__(self, ):')
    edit.left()
    repeat(1)

fashion:
    insert('def __init__(self):')
    key(enter)

^var <user.text>$:
    user.generic_programming_start_new_line_if_current_line_not_empty()
    user.fire_chicken_insert_formatted_text(text, 'snake')
    insert(" = ")

aimless:
    insert(' = None\)
    user.generic_programming_start_new_line_if_next_line_empty()
worthless: 
    insert(' = 0')
    user.generic_programming_start_new_line_if_next_line_empty()
listing: 
    insert(' = []')
    user.generic_programming_start_new_line_if_next_line_empty()
mapping: 
    insert(' = {}')
    user.generic_programming_start_new_line_if_next_line_empty()
truly: 
    insert(' = True')
    user.generic_programming_start_new_line_if_next_line_empty()
falsely: 
    insert(' = False')
    user.generic_programming_start_new_line_if_next_line_empty()
language: 
    insert(' = ""')
    user.generic_programming_start_new_line_if_next_line_empty()

increment: ' += 1'

[build] plural: user.fire_chicken_programming_build_for_each_loop_using_plural()

return false: insert('return False')
return true: insert('return True')

device <user.text>:
    insert(' = ')
    user.fire_chicken_auto_generated_command_action_insert_formatted_text(user.text_1, 'capitalized', '')
    insert('()')
    key('left')

technique <user.text>$:
    insert('def :')
    edit.left()
    user.fire_chicken_call_function_inside_with_name_formatted(text, 'snake')
    insert('self, ')

approach <user.text>$:
    insert('def :')
    edit.left()
    user.fire_chicken_call_function_inside_with_name_formatted(text, 'snake')
    insert('self')
    edit.line_end()
    key(enter)

private <user.text>$:
    insert('def :')
    edit.left()
    insert("_")
    user.fire_chicken_call_function_inside_with_name_formatted(text, 'snake')
    insert('self')
    

obtain <user.text>$:
    insert('def :')
    edit.left()
    user.fire_chicken_call_function_inside_with_name_formatted('get ' + text, 'snake')
    insert('self')
    edit.line_end()
    key(enter)
    insert('return self.')
    user.fire_chicken_insert_formatted_text(text, 'snake')

elif:
	key('end')
	key('esc')
	key('enter')
	key('backspace')
	key('e')
	key('l')
	key('i')
	key('f')
	key('space')
	key(':')
	key('left')

unit test template:
    insert('import unittest')
    key(enter)
    insert('class (unittest.TestCase):')
    key(enter:2)
    edit.delete()
    insert("if __name__ == '__main__':")
    key(enter)
    insert('unittest.main()')
    edit.up()
    repeat(2)
    edit.line_start()
    edit.right()
    repeat(5)

import numb plot:
    insert('import numpy as np')
    key(enter)
    insert('import matplotlib.pyplot as plt')
    key(enter)

import numb plot pan:
    insert('import numpy as np')
    key(enter)
    insert('import matplotlib.pyplot as plt')
    key(enter)
    insert('import pandas as pd')
    key(enter)

import pie plot: 
    insert('import matplotlib.pyplot as plt')
    key(enter)

linear algebra|lionel: 'linalg.'
least square: 
    user.fire_chicken_call_function_inside('lstsq')
inverse:
    user.fire_chicken_call_function_inside('inv')

if main:
    insert("if __name__ == '__main__':")
    key(enter)

representation|represent:
    insert('def __repr__(self):')
    key(enter)
    insert('return self.__str__()')
    key(enter)
    key(backspace)
    key(enter)
    insert('def __str__(self):')
    key(enter)

equality:
    insert('def __eq__(self, other) -> bool:')
    key(enter)
 
plot: 'plt.'
numpy|nope: 'np.'

testing <user.text>$:   
    insert('def test_')
    user.fire_chicken_insert_formatted_text(text, 'snake')
    insert('(self):')
testing <user.text> over:   
    insert('def test_')
    user.fire_chicken_insert_formatted_text(text, 'snake')
    insert('(self):') 

classy <user.text>$: 
    user.fire_chicken_programming_define_python_class(text)
classy <user.text> over:
    user.fire_chicken_programming_define_python_class(text)

model <user.text>$:
    user.fire_chicken_programming_define_python_class(text)
    insert('def __init__(self):')
    key(enter)

bobby <user.text>$:
    user.fire_chicken_programming_define_python_class(text)
    insert('def __init__(self, ):')
    edit.left()
    repeat(1)

subclass <user.text>$:
    user.fire_chicken_programming_define_python_subclass(text)
subclass <user.text> over:
    user.fire_chicken_programming_define_python_subclass(text)

path join:
    insert('os.path.join')
    user.fire_chicken_insert_around_cursor('(', ')')

path exists:
    insert('os.path.exists')
    user.fire_chicken_insert_around_cursor('(', ')')

mend:
    insert('()')
    key('left')
    insert('self')
    key('end')
    key(':')
    key('enter')

opening:
    insert('with open')
    insert('() as')
    key('left')
    repeat(3)

range:
    insert('range')
    user.fire_chicken_insert_around_cursor('(', ')')

in range:
    insert(' in ')
    insert('range')
    user.fire_chicken_insert_around_cursor('(', ')')

flask route:
    insert("@app.route('/")

assert match: 'self.assertEqual(expected, actual)'

autoline: user.fire_chicken_programming_auto_line()
autoline off: user.fire_chicken_disable_programming_auto_line()

magic call: user.fire_chicken_programming_insert_magic_method("call")

settings():
    user.fire_chicken_default_method_format = 'snake'
    user.fire_chicken_default_variable_format = 'snake'