from .text_containers import *
from talon import Module, actions


class StylizedContainer(TextContainer):
    def __init__(self, start, end, style_setting, invalid_left_boundary = '', invalid_right_boundary = ''):
        super().__init__(start, end, invalid_left_boundary, invalid_right_boundary)
        self.style = style_setting.get()
    



module = Module()

flow_control_parentheses_style = module.setting(
    'generic_programming_flow_control_parentheses_style',
    type = str,
    default = 'left',
    desc = 'The spacing style to use for flow control parentheses',
)

function_parentheses_style = module.setting(
    'generic_function_parentheses_style',
    type = str,
    default = '',
    desc = 'The spacing style to use for function parentheses',
)

function_call_parentheses_style = module.setting(
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

def apply_spacing_style_to_empty_container(style, container):
    result = apply_spacing_style_to_container(style, container)
    if 'pad' in style:
        result = get_container_with_padding_reduced_to_single_space(result)
    return result
def get_container_with_padding_reduced_to_single_space(container):
    return container.replace('  ', ' ')

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

@module.action_class
class Actions:
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
 
def get_parentheses_container():
    return TextContainer('(', ')')
