from talon import Module, actions, clip

from typing import Callable, List

from .modified_string_split import TextContainer, split_string_ignoring_containers

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


flow_control_parentheses_style = mod.setting(
    'generic_programming_flow_control_parentheses_style',
    type = str,
    default = 'left',
    desc = 'The spacing style to use for flow control parentheses',
)

function_parentheses_style = mod.setting(
    'generic_function_parentheses_style',
    type = str,
    default = '',
    desc = 'The spacing style to use for function parentheses',
)

function_call_parentheses_style = mod.setting(
    'generic_function_call_parentheses_style',
    type = str,
    default = '',
    desc = 'The spacing style to use for function call parentheses',
)


def apply_spacing_style_to(style, target):
    space_before = ''
    space_after = ''
    if 'left' in style:
        space_before = ' '
    if 'right' in style:
        space_after = ' '
    if 'both' in style:
        space_before = ' '
        space_after = ' '
    return f'{space_before}{target}{space_after}'

def apply_spacing_style_to_container(style, container):
    result = apply_spacing_style_to_container_inside(style, container)
    result = apply_spacing_style_to(style, result)
    return result
def apply_spacing_style_to_container_inside(style, container):
    start = container.get_start()
    ending = container.get_end()
    middle = ''
    if 'pad' in style:
        middle = '  '
    return start + middle + ending

def enter_stylized_container_from_right(container: str):
    actions.edit.left()
    #If padding within the container, go left a second time
    if '  ' in container:
        actions.edit.left()
    #If the container are followed by a space, go left again
    if container.endswith(' '):
       actions.edit.left()

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

    def generic_programming_get_flow_control_parentheses() -> str:
        '''returns parentheses with the flow control parentheses style'''
        parentheses_container = get_parentheses_container()
        stylized_parentheses = apply_spacing_style_to_container(flow_control_parentheses_style.get(), parentheses_container)
        return stylized_parentheses
    def generic_programming_insert_flow_control_parentheses():
        '''inserts parentheses with the flow control parentheses style'''
        actions.insert(actions.user.generic_programming_get_flow_control_parentheses())
    def generic_programming_enter_flow_control_parentheses_from_right():
        '''enters the flow control parentheses if called after inserting them'''
        enter_stylized_container_from_right(actions.user.generic_programming_get_flow_control_parentheses())

 
    def generic_programming_get_function_parentheses() -> str:
        '''returns parentheses with the function parentheses style'''
        parentheses_container = get_parentheses_container()
        stylized_parentheses = apply_spacing_style_to_container(function_parentheses_style.get(), parentheses_container)
        return stylized_parentheses
    def generic_programming_insert_function_parentheses():
        '''inserts parentheses with the function parentheses style'''
        actions.insert(actions.user.generic_programming_get_function_parentheses())
    def generic_programming_enter_function_parentheses_from_right():
        '''enters the function parentheses if called after inserting them'''
        enter_stylized_container_from_right(actions.user.generic_programming_get_function_parentheses())

    def generic_programming_get_function_call_parentheses() -> str:
        '''returns parentheses with the function call parentheses style'''
        parentheses_container = get_parentheses_container()
        stylized_parentheses = apply_spacing_style_to_container(function_call_parentheses_style.get(), parentheses_container)
        return stylized_parentheses
    def generic_programming_insert_function_call_parentheses():
        '''inserts parentheses with the function call parentheses style'''
        actions.insert(actions.user.generic_programming_get_function_call_parentheses())
    def generic_programming_enter_function_call_parentheses_from_right():
        '''enters the function call parentheses if called after inserting them'''
        enter_stylized_container_from_right(actions.user.generic_programming_get_function_call_parentheses())
 
 

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
