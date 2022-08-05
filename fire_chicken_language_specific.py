from talon import actions, Module
from .styles import * 
from typing import List

module = Module()

@module.action_class
class Actions:
    def fire_chicken_code_self_reference_constructor_arguments():
        '''Generic function that should be overridden for specific programming languages'''
        pass
    def fire_chicken_programming_build_count_loop():
        '''Does nothing intended to be overridden'''
        pass
    def fire_chicken_programming_build_for_loop():
        '''Does nothing intended to be overridden'''
        pass

    def fire_chicken_programming_code_generics_operator():
        '''Uses diamond symbol as default'''
        diamond = get_declaration_angles()
        diamond.insert()
        diamond.enter_from_right()
    def fire_chicken_programming_code_generic_type_start(typename: str):
        '''By default, puts the typename in pascal case and then does the diamond operator'''
        actions.user.insert_formatted(typename, 'hammer')
        actions.user.fire_chicken_programming_code_generics_operator()
    def fire_chicken_programming_code_generic_type_info_start(typename: str):
        '''By default, inserts the diamond operator and puts the argument in it'''
        actions.user.fire_chicken_programming_code_generic_type_info([typename])
    def fire_chicken_programming_code_generic_type_info(typenames: List):
        '''By default, inserts the diamond operator and puts the arguments in it separated by commas'''
        actions.user.fire_chicken_programming_code_generics_operator()
        is_first = True
        for typename in typenames:
            actions.user.insert_formatted(typename, 'hammer')
            if is_first:
                is_first = False
            else:
                actions.user.generic_programming_insert_comma_separator()
