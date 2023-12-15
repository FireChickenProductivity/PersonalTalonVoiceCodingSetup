from .text_containers import *
from talon import Module, actions, settings


class StylizedContainer(TextContainer):
    def __init__(self, start, end, style_setting, invalid_left_boundary = '', invalid_right_boundary = ''):
        super().__init__(start, end, invalid_left_boundary, invalid_right_boundary)
        self.style = settings.get(style_setting)
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

flow_control_parentheses_style_setting_name = 'generic_programming_flow_control_parentheses_style'
flow_control_parentheses_style = 'user.' + flow_control_parentheses_style_setting_name
module.setting(
    flow_control_parentheses_style_setting_name,
    type = str,
    default = 'left',
    desc = 'The spacing style to use for flow control parentheses',
)

comma_separator_style_setting_name = 'generic_programming_comma_separator_style'
comma_separator_style = 'user.' + comma_separator_style_setting_name
module.setting(
    comma_separator_style_setting_name,
    type = str,
    default = 'right',
    desc = 'The spacing style to use for comma separators',
)

semicolon_separator_style_setting_name = 'generic_programming_semicolon_separator_style'
semicolon_separator_style = 'user.' + semicolon_separator_style_setting_name
module.setting(
    semicolon_separator_style_setting_name,
    type = str,
    default = 'right',
    desc = 'The spacing style to use for semicolon separators',
)

colon_separator_style_setting_name = 'generic_programming_colon_separator_style'
colon_separator_style = 'user.' + colon_separator_style_setting_name
module.setting(
    colon_separator_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for colon separators',
)

assignment_style_setting_name = 'generic_programming_assignment_style'
assignment_style = 'user.' + assignment_style_setting_name
module.setting(
    assignment_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assignments',
)

plus_style_setting_name = 'generic_programming_plus_style'
plus_style = 'user.' + plus_style_setting_name
module.setting(
    plus_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for plusses',
)

minus_style_setting_name = 'generic_programming_minus_style'
minus_style = 'user.' + minus_style_setting_name
module.setting(
    minus_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for minusses',
)

times_style_setting_name = 'generic_programming_times_style'
times_style = 'user.' + times_style_setting_name
module.setting(
    times_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for times',
)

divide_style_setting_name = 'generic_programming_divide_style'
divide_style = 'user.' + divide_style_setting_name
module.setting(
    divide_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for divide',
)

mod_style_setting_name = 'generic_programming_mod_style'
mod_style = 'user.' + mod_style_setting_name
module.setting(
    mod_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for mod',
)

less_than_style_setting_name = 'generic_programming_less_than_style'
less_than_style = 'user.' + less_than_style_setting_name
module.setting(
    less_than_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for less than',
)

greater_than_style_setting_name = 'generic_programming_greater_than_style'
greater_than_style = 'user.' + greater_than_style_setting_name
module.setting(
    greater_than_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for greater than',
)

less_than_or_equal_style_setting_name = 'generic_programming_less_than_or_equal_style'
less_than_or_equal_style = 'user.' + less_than_or_equal_style_setting_name
module.setting(
    less_than_or_equal_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for less than or equal',
)

greater_than_or_equal_style_setting_name = 'generic_programming_greater_than_or_equal_style'
greater_than_or_equal_style = 'user.' + greater_than_or_equal_style_setting_name
module.setting(
    greater_than_or_equal_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for greater than or equal',
)

assign_plus_style_setting_name = 'generic_programming_assign_plus_style'
assign_plus_style = 'user.' + assign_plus_style_setting_name
module.setting(
    assign_plus_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign plus',
)

assign_minus_style_setting_name = 'generic_programming_assign_minus_style'
assign_minus_style = 'user.' + assign_minus_style_setting_name
module.setting(
    assign_minus_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign minus',
)

assign_times_style_setting_name = 'generic_programming_assign_times_style'
assign_times_style = 'user.' + assign_times_style_setting_name
module.setting(
    assign_times_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign times',
)

assign_divide_style_setting_name = 'generic_programming_assign_divide_style'
assign_divide_style = 'user.' + assign_divide_style_setting_name
module.setting(
    assign_divide_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign divide',
)

assign_mod_style_setting_name = 'generic_programming_assign_mod_style'
assign_mod_style = 'user.' + assign_mod_style_setting_name
module.setting(
    assign_mod_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for assign mod',
)

binary_logical_operator_style_setting_name = 'generic_programming_binary_logical_operator_style'
binary_logical_operator_style = 'user.' + binary_logical_operator_style_setting_name
module.setting(
    binary_logical_operator_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for binary logical operators',
)

unary_logical_operator_style_setting_name = 'generic_programming_unary_logical_operator_style'
unary_logical_operator_style = 'user.' + unary_logical_operator_style_setting_name
module.setting(
    unary_logical_operator_style_setting_name,
    type = str,
    default = 'both',
    desc = 'The spacing style to use for unary logical operators',
)

function_parentheses_style_setting_name = 'generic_programming_function_parentheses_style'
function_parentheses_style = 'user.' + function_parentheses_style_setting_name
module.setting(
    function_parentheses_style_setting_name,
    type = str,
    default = '',
    desc = 'The spacing style to use for function parentheses',
)

function_call_parentheses_style_setting_name = 'generic_programming_function_call_parentheses_style'
function_call_parentheses_style = 'user.' + function_call_parentheses_style_setting_name
module.setting(
    function_call_parentheses_style_setting_name,
    type = str,
    default = '',
    desc = 'The spacing style to use for function call parentheses',
)
def get_function_call_parentheses():
    return StylizedContainer('(', ')', function_call_parentheses_style)

object_parentheses_style_setting_name = 'generic_programming_object_parentheses_style'
object_parentheses_style = 'user.' + object_parentheses_style_setting_name
module.setting(
    object_parentheses_style_setting_name,
    type = str,
    default = '',
    desc = 'The spacing style used for object constructor call parentheses',
)
def get_object_parentheses():
    return StylizedContainer('(', ')', object_parentheses_style)

declaration_squares_style_setting_name = 'generic_programming_declaration_squares_style'
declaration_squares_style = 'user.' + declaration_squares_style_setting_name
module.setting(
    declaration_squares_style_setting_name,
    type = str,
    default = '',
    desc = 'The spacing style for declaration square brackets'
)
def get_declaration_squares():
    return StylizedContainer('[', ']', declaration_squares_style)

index_squares_style_setting_name = 'generic_programming_index_squares_style'
index_squares_style = 'user.' + index_squares_style_setting_name
module.setting(
    index_squares_style_setting_name,
    type = str,
    default = '',
    desc = 'The spacing style for index square brackets'
)
def get_index_squares():
    return StylizedContainer('[', ']', index_squares_style)


declaration_braces_style_setting_name = 'generic_programming_declaration_braces_style'
declaration_braces_style = 'user.' + declaration_braces_style_setting_name
module.setting(
    declaration_braces_style_setting_name,
    type = str,
    default = '',
    desc = 'The spacing style for declaration square brackets'
)
def get_declaration_braces():
    return StylizedContainer('{', '}', declaration_braces_style)

declaration_angles_style_setting_name = 'generic_programming_declaration_angles_style'
declaration_angles_style = 'user.' + declaration_angles_style_setting_name
module.setting(
    declaration_angles_style_setting_name,
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

def apply_spacing_setting_to(setting, target):
    return apply_spacing_style_to(setting.get(), target)

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
        text = apply_spacing_style_to(settings.get(comma_separator_style), ',')
        actions.insert(text)
    def generic_programming_insert_semicolon_separator():
        '''Inserts a semicolon separator with the appropriate style'''
        text = apply_spacing_style_to(settings.get(semicolon_separator_style), ';')
        actions.insert(text)
    def generic_programming_insert_colon_separator():
        '''Inserts a colon separator with the appropriate style'''
        text = apply_spacing_style_to(settings.get(colon_separator_style), ':')
        actions.insert(text)

    def generic_programming_insert_assignment():
        '''Inserts an assignment with the appropriate style'''
        text = apply_spacing_style_to(settings.get(assignment_style), '=')
        actions.insert(text)
    def generic_programming_insert_plus():
        '''Inserts a plus with the appropriate style'''
        text = apply_spacing_style_to(settings.get(plus_style), '+')
        actions.insert(text)
    def generic_programming_insert_minus():
        '''Inserts a minus with the appropriate style'''
        text = apply_spacing_style_to(settings.get(minus_style), '-')
        actions.insert(text)
    def generic_programming_insert_times():
        '''Inserts a times with the appropriate style'''
        text = apply_spacing_style_to(settings.get(times_style), '*')
        actions.insert(text)
    def generic_programming_insert_divide():
        '''Inserts a divide with the appropriate style'''
        text = apply_spacing_style_to(settings.get(divide_style), '/')
        actions.insert(text)
    def generic_programming_insert_mod():
        '''Inserts a mod with the appropriate style'''
        text = apply_spacing_style_to(settings.get(mod_style), '%')
        actions.insert(text)
    def generic_programming_insert_less_than():
        '''Inserts a less than with the appropriate style'''
        text = apply_spacing_style_to(settings.get(less_than_style), '<')
        actions.insert(text)
    def generic_programming_insert_greater_than():
        '''Inserts a greater than with the appropriate style'''
        text = apply_spacing_style_to(settings.get(greater_than_style), '>')
        actions.insert(text)
    def generic_programming_insert_less_than_or_equal():
        '''Inserts a less than or equal with the appropriate style'''
        text = apply_spacing_style_to(settings.get(less_than_or_equal_style), '<=')
        actions.insert(text)
    def generic_programming_insert_greater_than_or_equal():
        '''Inserts a greater than or equal with the appropriate style'''
        text = apply_spacing_style_to(settings.get(greater_than_or_equal_style), '>=')
        actions.insert(text)
    def generic_programming_insert_assign_plus():
        '''Inserts an assign plus with the appropriate style'''
        text = apply_spacing_style_to(settings.get(assign_plus_style), '+=')
        actions.insert(text)
    def generic_programming_insert_assign_minus():
        '''Inserts an assign minus with the appropriate style'''
        text = apply_spacing_style_to(settings.get(assign_minus_style), '-=')
        actions.insert(text)
    def generic_programming_insert_assign_times():
        '''Inserts an assign times with the appropriate style'''
        text = apply_spacing_style_to(settings.get(assign_times_style), '*=')
        actions.insert(text)
    def generic_programming_insert_assign_divide():
        '''Inserts an assign divide with the appropriate style'''
        text = apply_spacing_style_to(settings.get(assign_divide_style), '/=')
        actions.insert(text)
    def generic_programming_insert_assign_mod():
        '''Inserts an assign mod with the appropriate style'''
        text = apply_spacing_style_to(settings.get(assign_mod_style), '%=')
        actions.insert(text)

    def generic_programming_get_flow_control_parentheses() -> str:
        '''returns parentheses with the flow control parentheses style'''
        parentheses_container = get_parentheses_container()
        stylized_parentheses = apply_spacing_style_to_container(settings.get(flow_control_parentheses_style), parentheses_container)
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
        stylized_parentheses = apply_spacing_style_to_container(settings.get(function_parentheses_style), parentheses_container)
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
        stylized_parentheses = apply_spacing_style_to_container(settings.get(function_call_parentheses_style), parentheses_container)
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
    def generic_programming_insert_object_parentheses():
        '''Inserts object parentheses with the appropriate style'''
        get_object_parentheses().insert()
    def generic_programming_enter_object_parentheses_from_right():
        '''Enters the object parentheses if initially to the right of them'''
        get_object_parentheses().enter_from_right()
       
def get_parentheses_container():
    return TextContainer('(', ')')