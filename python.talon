tag: user.python
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

state else if:
    insert('elif :')
    edit.left()

constructor|construct:
    insert('def __init__(self, ):')
    edit.left()
    repeat(1)

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
    insert('import matplotlib as plt')
    key(enter)

plot: 'plt.'
numpy: 'np.'

testing <user.prose>$:   
    insert('def test_')
    user.insert_formatted(prose, 'snake')
    insert('(self):')
testing <user.prose> over:   
    insert('def test_')
    user.insert_formatted(prose, 'snake')
    insert('(self):') 

classy <user.prose>$: 
    user.fire_chicken_programming_define_python_class(prose)
classy <user.prose> over:
    user.fire_chicken_programming_define_python_class(prose)

subclass <user.prose>$:
    user.fire_chicken_programming_define_python_subclass(prose)
subclass <user.prose> over:
    user.fire_chicken_programming_define_python_subclass(prose)

settings():
    user.fire_chicken_default_method_format = 'snake'
    user.fire_chicken_default_variable_format = 'snake'
