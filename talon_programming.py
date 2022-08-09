from talon import actions, Module, Context

from .styles import *

talon_python_programming = Context()

module = Module()
module.tag('fire_chicken_talon_python_programming', desc = 'Activate talon python commands')
@module.action_class
class Actions:
    def talon_programming_insert_keypress(keys: str):
        '''Inserts the talon command needed to make the keypress'''
        actions.insert('key')
        function_call_parentheses = get_function_call_parentheses()
        function_call_parentheses.insert()
        function_call_parentheses.enter_from_right()
        actions.insert(keys)

    def talon_programming_activate_python_commands():
        '''activates talon python commands'''
        talon_python_programming.tags = ['user.fire_chicken_talon_python_programming']
    def talon_programming_deactivate_python_commands():
        '''deactivates talon python commands'''
        talon_python_programming.tags = []
    def talon_python_programming_insert_keypress(keys: str):
        '''Inserts the talon command needed to make the key presses'''
        actions.insert('actions.')
        actions.insert('key')
        function_call_parentheses = get_function_call_parentheses()
        function_call_parentheses.insert()
        function_call_parentheses.enter_from_right()
        actions.insert("''")
        actions.edit.left()
        actions.insert(keys)
