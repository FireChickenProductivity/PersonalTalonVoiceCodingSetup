from talon import Module, actions, clip
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

clipboard_operation_delay = mod.setting(
    'generic_programming_clipboard_operation_delay',
    type = int,
    default = 250,
    desc = 'How long in milliseconds commands will pause when using the clipboard to ensure that they do not restore the clipboard too quickly.'
)

word_movement_delay = mod.setting(
    'generic_programming_word_movement_delay',
    type = int,
    default = 100,
    desc = 'How long commands should pause after word movement. Needed to get desired behavior in some editors.'
)

suggestion_closing_delay = mod.setting(
    'generic_programming_suggestion_closing_delay',
    type = int,
    default = 100,
    desc = 'How long commands should pause when closing code suggestions in milliseconds',
)
def wait_suggestion_closing_delay():
    actions.sleep(f'{suggestion_closing_delay.get()}ms')


@mod.action_class
class Actions:
    def generic_programming_get_line() -> str:
        '''Returns the current line'''
        with clip.revert():
            actions.edit.select_line()
            actions.edit.copy()
            actions.sleep(f'{clipboard_operation_delay.get()}ms')
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
        formatted_name = actions.user.formatted_text(name, format)
        actions.user.generic_programming_call_method(formatted_name)
    def generic_programming_call_method_inside_with_name_formatted(name: str, format: str):
        '''Inserts the specified method call and enters the parentheses'''
        formatted_name = actions.user.formatted_text(name, format)
        actions.user.generic_programming_call_method_inside(formatted_name)
    
    

    def generic_programming_build_for(beginning: str, separator_after_initialization: str, separator_after_condition: str, ending: str ):
        '''Builds a for loop using the code written on the current line'''
        current_line = actions.user.generic_programming_get_comma_separated_line()
        initialization = current_line[0]
        condition = current_line[1]
        next_iteration_variable_change = current_line[2]
        result_string = beginning + initialization + separator_after_initialization + condition + separator_after_condition + next_iteration_variable_change + ending
        actions.insert(result_string)
    def generic_programming_wait_word_movement_delay():
        '''Sleeps for the word movement delay amount'''
        actions.sleep(f'{word_movement_delay.get()}ms')
    def generic_programming_self_dot():
        '''Uses the community repository code to create the language version of self dot'''
        actions.user.code_self()
        actions.user.code_operator_object_accessor()
    def fire_chicken_code_self_reference_constructor_arguments():
        '''Generic function that should be overridden for specific programming languages'''
        pass
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
        code = actions.user.generic_programming_get_comma_separated_line_ignoring_standard_separators()
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
        

    def fire_chicken_programming_build_count_loop():
        '''Does nothing intended to be overridden'''
        pass
    def fire_chicken_programming_build_for_loop():
        '''Does nothing intended to be overridden'''
        pass

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
