from talon import actions, Module

from .styles import *

module = Module()
@module.action_class
class Actions:
    def talon_programming_insert_keypress(keys: str):
        '''Inserts the talon command needed to make the keypress'''
        actions.insert('key')
        function_call_parentheses = get_function_call_parentheses()
        function_call_parentheses.insert()
        function_call_parentheses.enter_from_right()
        actions.insert(keys)
