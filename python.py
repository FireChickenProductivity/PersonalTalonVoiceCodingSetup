from talon import Module, actions, Context

module = Module()
context = Context()
context.matches = r'''
tag: user.python
'''

@context.action_class('user')
class UserActions:
    def fire_chicken_code_self_reference_constructor_arguments():
        '''Python version of the self referencing action'''
        actions.user.generic_programming_self_reference_constructor_arguments(self_reference_argument, '(self,')
    def fire_chicken_programming_build_count_loop():
        '''Python version of building counting loops'''
        variable, start, ending, step = actions.user.generic_programming_get_counting_for_loop_components_from_the_current_line()
        if variable is None:
            return 
        actions.insert(f'for {variable} in range')
        actions.user.generic_programming_insert_function_call_parentheses()
        actions.user.generic_programming_enter_function_call_parentheses_from_right()
        if start != '0':
            actions.insert(start)
            actions.user.generic_programming_insert_comma_separator()
        actions.insert(ending)
        if step != '':
            actions.user.generic_programming_insert_comma_separator()
            actions.insert(step)
        start_code_block()


def self_reference_argument(argument):
    actions.user.fire_chicken_programming_self_reference_argument_given_strategy_to_find_its_variable(argument, get_argument_variable)

def get_argument_variable(argument):
    stripped_argument = argument.strip()
    space_separated_argument_parts = stripped_argument.split(' ')
    first_part = space_separated_argument_parts[0]
    if ':' in first_part:
        variable_ending_index = first_part.find(':')
        return first_part[ : variable_ending_index]
    else:
        return first_part

def start_code_block():
    actions.edit.line_end()
    actions.key(':')
    actions.key('enter')
