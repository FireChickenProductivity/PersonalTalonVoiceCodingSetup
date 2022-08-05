from talon import actions, Module
from .styles import * 
from typing import List

module = Module()

module.tag('fire_chicken_class_command', desc = 'Enables class command')
module.tag('fire_chicken_programming_math_methods', desc = 'Enables math method command')

module.list('fire_chicken_programming_packages', desc = 'Active language list of programming packages')
@module.capture(rule = '{user.fire_chicken_programming_packages}')
def fire_chicken_programming_package(m) -> str:
    return m.fire_chicken_programming_packages

module.list('fire_chicken_programming_classes', desc = 'Active language list of classes')
@module.capture(rule = '{user.fire_chicken_programming_classes}')
def fire_chicken_programming_class(m) -> str:
    return m.fire_chicken_programming_classes

module.list('fire_chicken_programming_generic_classes', desc = 'Active language list of generics')
@module.capture(rule = '{user.fire_chicken_programming_generic_classes}')
def fire_chicken_programming_generic_class(m) -> str:
    return m.fire_chicken_programming_generic_classes

module.list('fire_chicken_math_methods', desc = 'Active language list of math methods')
@module.capture(rule = '{user.fire_chicken_math_methods}')
def fire_chicken_programming_math_method(m) -> str:
    return m.fire_chicken_math_methods


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
    
    def fire_chicken_programming_import_package(name: str):
        '''Does nothing intended to be overridden'''
        pass

    def fire_chicken_programming_import(name: str):
        '''Does nothing intended to be overridden'''
        pass

    def fire_chicken_programming_from_import(package: str, target: str):
        '''Does nothing intended to be overridden'''
        pass

    def fire_chicken_programming_code_generics_operator():
        '''Uses diamond symbol as default'''
        diamond = get_declaration_angles()
        diamond.insert()
        diamond.enter_from_right()
    def fire_chicken_programming_code_empty_generics_operator():
        '''Uses diamond symbol as default'''
        diamond = get_declaration_angles()
        diamond.insert_empty()
    def fire_chicken_programming_code_generic_type_start(typename: str):
        '''By default, puts the typename in pascal case and then does the diamond operator'''
        actions.user.insert_formatted(typename, 'hammer')
        actions.user.fire_chicken_programming_code_generics_operator()
    def fire_chicken_programming_code_generic_type_info_start(typename: str):
        '''By default, inserts the diamond operator and puts the argument in it'''
        pascal_case_text = actions.user.formatted_text(typename, 'hammer')
        actions.user.fire_chicken_programming_code_generic_type_info([pascal_case_text])
    def fire_chicken_programming_code_generic_type_info(typenames: List):
        '''By default, inserts the diamond operator and puts the arguments in it separated by commas'''
        actions.user.fire_chicken_programming_code_generics_operator()
        is_first = True
        for index, typename in enumerate(typenames):
            actions.insert(typename)
            if index + 1 != len(typenames):
                actions.user.generic_programming_insert_comma_separator()
