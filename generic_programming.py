from talon import Module, actions, clip, settings
from typing import Callable, List, Tuple
from .text_containers import TextContainer, split_string_ignoring_containers
from .styles import * 


mod = Module()

mod.tag(
    'build_for_loops',
    desc = 'enables commands for building for loops'
)

mod.tag(
    'fire_chicken_programming_self_reference_constructor',
    desc = 'self referencing the constructor'
)

clipboard_operation_delay_setting_name = 'generic_programming_clipboard_operation_delay'
clipboard_operation_delay = 'user.' + clipboard_operation_delay_setting_name
mod.setting(
    clipboard_operation_delay_setting_name,
    type = int,
    default = 250,
    desc = 'How long in milliseconds commands will pause when using the clipboard to ensure that they do not restore the clipboard too quickly.'
)

word_movement_delay_setting_name = 'generic_programming_word_movement_delay'
word_movement_delay = 'user.' + word_movement_delay_setting_name
mod.setting(
    word_movement_delay_setting_name,
    type = int,
    default = 100,
    desc = 'How long commands should pause after word movement. Needed to get desired behavior in some editors.'
)

suggestion_closing_delay_setting_name = 'generic_programming_suggestion_closing_delay'
suggestion_closing_delay = 'user.' + suggestion_closing_delay_setting_name
mod.setting(
    suggestion_closing_delay_setting_name,
    type = int,
    default = 100,
    desc = 'How long commands should pause when closing code suggestions in milliseconds',
)
def wait_suggestion_closing_delay():
    actions.sleep(f'{settings.get(suggestion_closing_delay)}ms')

default_method_format_setting_name = 'fire_chicken_default_method_format'
default_method_format = 'user.' + default_method_format_setting_name
mod.setting(
    default_method_format_setting_name,
    type = str,
    default = 'camel',
    desc = 'The default way to format method names',
)

default_variable_format_setting_name = 'fire_chicken_default_variable_format'
default_variable_format = 'user.' + default_variable_format_setting_name
mod.setting(
    default_variable_format_setting_name,
    type = str,
    default = 'camel',
    desc = 'The default way to format variable names'
)

def copy_selection_text(selection_function):
    with clip.revert():
        selection_function()
        actions.edit.copy()
        actions.sleep(f'{settings.get(clipboard_operation_delay)}ms')
        result = clip.text()
        return result

@mod.action_class
class Actions:
    def generic_programming_get_line() -> str:
        '''Returns the current line'''
        return copy_selection_text(actions.edit.select_line)
    def generic_programming_get_line_start() -> str:
        """Returns the start of the line"""
        actions.key("space")
        text = copy_selection_text(actions.edit.extend_line_start)[:-1]
        actions.edit.right()
        actions.key('escape')
        actions.edit.delete()
        '''returns a list containing the comma separated stuff on the current line ignoring commas within standard containers'''
        return text
    def generic_programming_get_line_ending() -> str:
        """Returns the ending of the line"""
        actions.key("space")
        actions.edit.left()
        text = copy_selection_text(actions.edit.extend_line_end)[1:]
        actions.edit.left()
        actions.key('escape')
        actions.edit.right()
        actions.edit.delete()
        return text
    def generic_programming_get_selected_text() -> str:
        '''Returns the selected text'''
        with clip.revert():
            actions.edit.copy()
            actions.sleep(f'{settings.get(clipboard_operation_delay)}ms')
            result = clip.text()
        return result
    def generic_programming_get_comma_separated_line():
        '''returns a list containing the comma separated stuff on the current line'''
        current_line = actions.user.generic_programming_get_line()
        return current_line.split(',')
    def generic_programming_get_comma_separated_line_ignoring_standard_separators():
        '''returns a list containing the comma separated stuff on the current line ignoring commas within standard containers'''
        current_line = actions.user.generic_programming_get_line()
        separated_list = split_string_ignoring_containers(current_line, ',', construct_standard_programming_containers())
        return separated_list
    def generic_programming_split_string_ignoring_standard_containers(text: str, separator: str) -> List:
        '''Uses split string ignoring standard containers with standard containers'''
        return split_string_ignoring_containers(text, separator, construct_standard_programming_containers())

    def fire_chicken_call_function(name: str):
        '''Inserts the specified function call'''
        actions.insert(name)
        get_function_call_parentheses().insert_empty()
    def fire_chicken_call_function_inside(name: str):
        '''Inserts the specified function call and enters the parentheses'''
        actions.insert(name)
        get_function_call_parentheses().insert()
        get_function_call_parentheses().enter_from_right()
    def fire_chicken_call_function_with_name_formatted(name: str, format: str):
        '''Calls the function with the name formatted'''
        formatted_name = actions.user.fire_chicken_format_text(name, format)
        actions.user.fire_chicken_call_function(formatted_name)
    def fire_chicken_call_function_inside_with_name_formatted(name: str, format: str):
        '''Calls the function inside with the name formatted'''
        formatted_name = actions.user.fire_chicken_format_text(name, format)
        actions.user.fire_chicken_call_function_inside(formatted_name)
    def generic_programming_call_method(name: str):
        '''Inserts the specified method call'''
        actions.user.code_operator_object_accessor()
        actions.insert(name)
        get_function_call_parentheses().insert_empty()
    def generic_programming_call_method_inside(name: str):
        '''Inserts the specified method call and enters the parentheses'''
        actions.user.code_operator_object_accessor()
        actions.insert(name)
        get_function_call_parentheses().insert()
        get_function_call_parentheses().enter_from_right()
    def generic_programming_call_method_with_name_formatted(name: str, format: str):
        '''Inserts the specified method call'''
        formatted_name = actions.user.fire_chicken_format_text(name, format)
        actions.user.generic_programming_call_method(formatted_name)
    def generic_programming_call_method_inside_with_name_formatted(name: str, format: str):
        '''Inserts the specified method call and enters the parentheses'''
        formatted_name = actions.user.fire_chicken_format_text(name, format)
        actions.user.generic_programming_call_method_inside(formatted_name)
    def fire_chicken_call_default_formatted_method(name: str):
        '''Performs the method call with the given name and the default format'''
        actions.user.generic_programming_call_method_with_name_formatted(name, settings.get(default_method_format))
    def fire_chicken_call_default_formatted_method_inside(name: str):
        '''Performs the method call inside with the given name and the default format'''
        actions.user.generic_programming_call_method_inside_with_name_formatted(name, settings.get(default_method_format))
    def fire_chicken_insert_default_formatted_variable(name: str):
        '''Inserts the variable name with default formatting'''
        formatted_name = actions.user.fire_chicken_format_text(name, settings.get(default_variable_format))
        actions.insert(formatted_name)



        
    def generic_programming_build_for(beginning: str, separator_after_initialization: str, separator_after_condition: str, ending: str ):
        '''Builds a for loop using the code written on the current line'''
        current_line = actions.user.fire_chicken_separate_current_line()
        initialization = current_line[0]
        condition = current_line[1]
        next_iteration_variable_change = current_line[2]
        result_string = beginning + initialization + separator_after_initialization + condition + separator_after_condition + next_iteration_variable_change + ending
        actions.insert(result_string)
    def generic_programming_wait_word_movement_delay():
        '''Sleeps for the word movement delay amount'''
        actions.sleep(f'{settings.get(word_movement_delay)}ms')
    def generic_programming_self_dot():
        '''Uses the community repository code to create the language version of self dot'''
        actions.user.code_self()
        actions.user.code_operator_object_accessor()
    def generic_programming_self_reference_constructor_arguments(handle_argument: Callable[[str], None], start_prefix: str = '(', ending_prefix: str = ')'):
        '''For each constructor argument, does the equivalent of self.argument = argument'''
        current_line = actions.user.generic_programming_get_line()
        if start_prefix not in current_line or ending_prefix not in current_line:
            return
        starting_index = current_line.find(start_prefix) + len(start_prefix)
        ending_index = current_line.rfind(ending_prefix)
        if starting_index >= ending_index:
            return
        constructor_arguments_string = current_line[starting_index : ending_index]
        print(constructor_arguments_string)
        arguments = split_string_ignoring_containers(constructor_arguments_string, ',', construct_standard_programming_containers())
        print(arguments)
        for argument in arguments:
            handle_argument(argument)
    def generic_programming_create_line_below():
        '''Tries to create a line below while exiting out of pop up stuff like code suggestions'''
        actions.edit.line_end()
        wait_suggestion_closing_delay()
        actions.key('esc')
        actions.key('enter')
           
    def fire_chicken_programming_self_reference_argument_given_strategy_to_find_its_variable(argument: str, get_variable: Callable[[str], None], statement_ending: str = ''):          
        '''Self references the argument variable'''
        actions.user.generic_programming_create_line_below()
        variable = get_variable(argument)
        actions.user.fire_chicken_programming_self_reference_variable(variable, statement_ending)

    def fire_chicken_programming_self_reference_variable(variable: str, statement_ending: str = ''):
        '''Tries to do language equivalent of self.variable = variable'''
        actions.user.code_self()
        actions.user.code_operator_object_accessor()
        actions.insert(variable)
        actions.user.code_operator_assignment()
        actions.insert(variable + statement_ending)
    
    def generic_programming_get_counting_for_loop_components_from_the_current_line() -> Tuple:
        '''Builds a simple counting for loop using the current line text'''
        code = actions.user.fire_chicken_separate_current_line()
        variable = 'i'
        start = '0'
        ending = ''
        step = ''

        if len(code) == 0:
            return None, None, None, None
        if len(code) == 1:
            ending = code[0]
        if len(code) > 1:
            variable = code[0]
        if len(code) == 2:
            ending = code[1]
        if len(code) > 2:
            start = code[1]
            ending = code[2]
        if len(code) > 3:
            step = code[3]       

        return variable, start, ending, step
        
    def generic_programming_regular_expression_boundary_search_next(target: str):
        '''Searches for the desired text after a regular expression word boundary and goes to the left of it'''
        actions.edit.right()
        actions.edit.find('')
        actions.user.find_toggle_match_by_regex()
        actions.insert('\\b' + target)
        actions.user.find_toggle_match_by_regex()
        actions.key('escape')
        actions.edit.left()

def construct_standard_programming_containers():
    containers = []
    containers.append(TextContainer('<', '>', invalid_left_boundary = ' ', invalid_right_boundary = ' '))
    containers.append(TextContainer('[', ']'))
    containers.append(TextContainer('(', ')'))
    containers.append(TextContainer('{', '}'))
    containers.append(TextContainer('"', '"'))
    return containers

def get_parentheses_container():
    return TextContainer('(', ')')





@mod.action_class
class Defaults:
    def code_operator_object_accessor():
        '''This default just inserts a dot'''
        actions.insert('.') 
