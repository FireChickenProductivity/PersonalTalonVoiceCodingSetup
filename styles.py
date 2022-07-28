from .text_containers import *
from talon import Module, actions


class StylizedContainer(TextContainer):
    def __init__(self, start, end, style_setting, invalid_left_boundary = '', invalid_right_boundary = ''):
        super().__init__(start, end, invalid_left_boundary, invalid_right_boundary)
        self.style = style_setting.get()
    def get_text(self):
        text = apply_spacing_style_to_container(self.style, self)
        return text
    def enter_from_right(self):
        enter_stylized_container_from_right(self.get_text())
    def insert(self):
        text = self.get_text()
        actions.insert(text)
    def get_empty_text(self):
        empty_container_text = apply_spacing_style_to_empty_container(self.style, self)
        return empty_container_text
    def insert_empty(self):
        empty_container_text = self.get_empty_text()
        actions.insert(empty_container_text)


module = Module()

flow_control_parentheses_style = module.setting(
    'generic_programming_flow_control_parentheses_style',
    type = str,
    default = 'left',
    desc = 'The spacing style to use for flow control parentheses',
)

comma_separator_style = module.setting(
    'generic_programming_comma_separator_style',
    type = str,
    default = 'right',
    desc = 'The spacing style to use for comma separators',
)

semicolon_separator_style = module.setting(
    'generic_programming_semicolon_separator_style',
    type = str,
    default = 'right',
    desc = 'The spacing style to use for semicolon separators',
)

assignment_style = module.setting(
    'generic_programming_assignment_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assignments',
)

plus_style = module.setting(
    'generic_programming_plus_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for plusses',
)

minus_style = module.setting(
    'generic_programming_minus_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for minusses',
)

times_style = module.setting(
    'generic_programming_times_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for times',
)

divide_style = module.setting(
    'generic_programming_divide_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for divide',
)

mod_style = module.setting(
    'generic_programming_mod_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for mod',
)

less_than_style = module.setting(
    'generic_programming_less_than_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for less than',
)

greater_than_style = module.setting(
    'generic_programming_greater_than_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for greater than',
)

less_than_or_equal_style = module.setting(
    'generic_programming_less_than_or_equal_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for less than or equal',
)

greater_than_or_equal_style = module.setting(
    'generic_programming_greater_than_or_equal_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for greater than or equal',
)

assign_plus_style = module.setting(
    'generic_programming_assign_plus_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign plus',
)

assign_minus_style = module.setting(
    'generic_programming_assign_minus_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign minus',
)

assign_times_style = module.setting(
    'generic_programming_assign_times_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign times',
)

assign_divide_style = module.setting(
    'generic_programming_assign_divide_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign divide',
)

assign_mod_style = module.setting(
    'generic_programming_assign_mod_style',
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign mod',
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

declaration_squares_style = module.setting(
    'generic_programming_declaration_squares_style',
    type = str,
    default = '',
    desc = 'The spacing style for declaration square brackets'
)
def get_declaration_squares():
    return StylizedContainer('[', ']', declaration_squares_style)

index_squares_style = module.setting(
    'generic_programming_index_squares_style',
    type = str,
    default = '',
    desc = 'The spacing style for index square brackets'
)
def get_index_squares():
    return StylizedContainer('[', ']', index_squares_style)


declaration_braces_style = module.setting(
    'generic_programming_declaration_braces_style',
    type = str,
    default = '',
    desc = 'The spacing style for declaration square brackets'
)
def get_declaration_braces():
    return StylizedContainer('{', '}', declaration_braces_style)

declaration_angles_style = module.setting(
    'generic_programming_declaration_angles_style',
    type = str,
    default = '',
    desc = 'The spacing style for declaration square brackets'
)
def get_declaration_angles():
    return StylizedContainer('<', '>', declaration_angles_style)

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
    def generic_programming_insert_comma_separator():
        '''Inserts a comma separator with the appropriate style'''
        text = apply_spacing_style_to(comma_separator_style.get(), ',')
        actions.insert(text)
    def generic_programming_insert_semicolon_separator():
        '''Inserts a semicolon separator with the appropriate style'''
        text = apply_spacing_style_to(semicolon_separator_style.get(), ';')
        actions.insert(text)
    def generic_programming_insert_assignment():
        '''Inserts an assignment with the appropriate style'''
        text = apply_spacing_style_to(assignment_style.get(), '=')
        actions.insert(text)
    def generic_programming_insert_plus():
        '''Inserts a plus with the appropriate style'''
        text = apply_spacing_style_to(plus_style.get(), '+')
        actions.insert(text)
    def generic_programming_insert_minus():
        '''Inserts a minus with the appropriate style'''
        text = apply_spacing_style_to(minus_style.get(), '-')
        actions.insert(text)
    def generic_programming_insert_times():
        '''Inserts a times with the appropriate style'''
        text = apply_spacing_style_to(times_style.get(), '*')
        actions.insert(text)
    def generic_programming_insert_divide():
        '''Inserts a divide with the appropriate style'''
        text = apply_spacing_style_to(divide_style.get(), '/')
        actions.insert(text)
    def generic_programming_insert_mod():
        '''Inserts a mod with the appropriate style'''
        text = apply_spacing_style_to(mod_style.get(), '%')
        actions.insert(text)
    def generic_programming_insert_less_than():
        '''Inserts a less than with the appropriate style'''
        text = apply_spacing_style_to(less_than_style.get(), '<')
        actions.insert(text)
    def generic_programming_insert_greater_than():
        '''Inserts a greater than with the appropriate style'''
        text = apply_spacing_style_to(greater_than_style.get(), '>')
        actions.insert(text)
    def generic_programming_insert_less_than_or_equal():
        '''Inserts a less than or equal with the appropriate style'''
        text = apply_spacing_style_to(less_than_or_equal_style.get(), '<=')
        actions.insert(text)
    def generic_programming_insert_greater_than_or_equal():
        '''Inserts a greater than or equal with the appropriate style'''
        text = apply_spacing_style_to(greater_than_or_equal_style.get(), '>=')
        actions.insert(text)
    def generic_programming_insert_assign_plus():
        '''Inserts an assign plus with the appropriate style'''
        text = apply_spacing_style_to(assign_plus_style.get(), '+=')
        actions.insert(text)
    def generic_programming_insert_assign_minus():
        '''Inserts an assign minus with the appropriate style'''
        text = apply_spacing_style_to(assign_minus_style.get(), '-=')
        actions.insert(text)
    def generic_programming_insert_assign_times():
        '''Inserts an assign times with the appropriate style'''
        text = apply_spacing_style_to(assign_times_style.get(), '*=')
        actions.insert(text)
    def generic_programming_insert_assign_divide():
        '''Inserts an assign divide with the appropriate style'''
        text = apply_spacing_style_to(assign_divide_style.get(), '/=')
        actions.insert(text)
    def generic_programming_insert_assign_mod():
        '''Inserts an assign mod with the appropriate style'''
        text = apply_spacing_style_to(assign_mod_style.get(), '%=')
        actions.insert(text)

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
    def generic_programming_insert_empty_declaration_squares():
        '''inserts empty declaration squares'''
        get_declaration_squares().insert_empty()
       
def get_parentheses_container():
    return TextContainer('(', ')')
