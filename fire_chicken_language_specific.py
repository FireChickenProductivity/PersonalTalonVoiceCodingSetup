from talon import actions, Module, settings
from .styles import * 
from typing import List

module = Module()

module.tag('fire_chicken_class_command', desc = 'Enables class command')
module.tag('fire_chicken_programming_math_methods', desc = 'Enables math method command')
module.tag('fire_chicken_fast_functions', desc = 'Enables fast functions')

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

module.list('fire_chicken_fast_functions', desc = 'Functions that can be dictated by stating a name for them with no prefix')
@module.capture(rule = '{user.fire_chicken_fast_functions}')
def fire_chicken_fast_functions(m) -> str:
    return m.fire_chicken_fast_functions

statement_ending_setting_name = 'fire_chicken_statement_ending'
statement_ending = 'user.' + statement_ending_setting_name
module.setting(
    statement_ending_setting_name,
    type = str,
    default = '',
    desc = 'Language specific statement ending'
)

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
    def fire_chicken_build_calls(arguments_per_call: int):
        '''Converts separated arguments on the current line into function/method calls'''
        def build_call(function_name: str, argument_list: List, ending: str):
            actions.insert(function_name)
            get_function_call_parentheses().insert()
            get_function_call_parentheses().enter_from_right()
            separator = apply_spacing_style_to(comma_separator_style.get(), ',')
            arguments = separator.join(argument_list)
            actions.insert(arguments)
            actions.edit.line_end()
            actions.insert(ending)
            actions.user.generic_programming_create_line_below()
            
            
        line = actions.user.fire_chicken_separate_current_line()
        #If less than two arguments or the number of arguments per call does 
        #not evenly divide the number of function arguments, give up
        if len(line) < 2 or (len(line) - 1) % arguments_per_call != 0:
            return 
        function_name = line[0]
        arguments = line[1 : ]
        argument_lists = get_list_divided_by_continuous_regions_of_length(arguments, arguments_per_call)
        for argument_list in argument_lists:
            build_call(function_name, argument_list, settings.get(statement_ending))
    def fire_chicken_get_statement_ending() -> str:
        ''''''
        return settings.get(statement_ending)
    def fire_chicken_insert_statement_ending():
        ''''''
        actions.insert(actions.user.fire_chicken_get_statement_ending())

def get_list_divided_by_continuous_regions_of_length(list: List, length: int):
    result = [[]]
    current_list_length = 0
    for element in list:
        if current_list_length == length:
            result.append([])
            current_list_length = 0
        result[-1].append(element)
        current_list_length += 1
    return result