from talon import actions, Module, Context
from .styles import * 

module = Module()

@module.capture(rule = '(pro|pry|pub)')
def java_programming_access_modifier(m) -> str:
    word = m[0]
    if word == 'pub':
        return 'public '
    elif word == 'pry':
        return 'private '
    elif word == 'pro':
        return 'protected '

@module.capture(rule = '<user.java_programming_access_modifier>|prose|prize|pubs')
def java_programming_function_access_modifier(m) -> str:
    word = m[0]
    if word == 'prose':
        return 'protected static '
    elif word == 'prize':
        return 'private static '
    elif word == 'pubs':
        return 'public static '
    else:
        return m.java_programming_access_modifier


@module.action_class
class Actions:
    def java_programming_build_new():
        '''Given a data type and variable name, produces new assignment'''
        current_line = actions.user.generic_programming_get_comma_separated_line_ignoring_standard_separators()
        if len(current_line) != 2:
            return 
        data_type = current_line[0]
        variable_name = current_line[1]
        actions.insert(f'{data_type} {variable_name}{apply_spacing_setting_to(assignment_style, "=")}'
            f'new {data_type}{get_object_parentheses().get_text()};')
        for iteration in range(2):
            actions.edit.left() 
    
context = Context()
context.matches = r'''
tag: user.java
'''

@context.action_class('user')
class UserActions:
    def fire_chicken_code_self_reference_constructor_arguments():
        '''Java version of the self referencing action'''
        actions.user.generic_programming_self_reference_constructor_arguments(self_reference_argument)


def self_reference_argument(argument):
    actions.user.fire_chicken_programming_self_reference_argument_given_strategy_to_find_its_variable(argument, get_argument_variable, statement_ending = ';')

def get_argument_variable(argument):
    stripped_argument = argument.strip()
    space_separated_argument_parts = actions.user.generic_programming_split_string_ignoring_standard_containers(stripped_argument, ' ')
    print(space_separated_argument_parts)
    #to deal with multiple spaces creating empty splits, return 
    #the first part after the initial part (the datatype) that is not empty
    for i in range(1, len(space_separated_argument_parts)):
        part = space_separated_argument_parts[i]
        if part != '':
            return part
