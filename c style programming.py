from talon import Module, actions, Context
from .styles import *

module = Module()
context = Context()
context.matches = '''tag: user.c_style_programming'''
context_without_javascript = Context()
context_without_javascript.matches = r'''
tag: user.c_style_programming
and not tag: user.javascript
'''
#Javascript stuff should normally go in the javascript files but not when overriding c style programming stuff
javascript_context = Context()
javascript_context.matches = r'''
tag: user.javascript
'''


module.tag(
    'c_style_programming',
    desc = 'enables commands for c style programming'
)

brace_style = module.setting(
    'c_style_programming_brace_style',
    type = str,
    default = 'same line',
    desc = 'the active brace style',
)

@module.capture(rule = 'if|else if|while|for|catch|try|finally')
def c_style_programming_simple_flow_control_name(flow_control) -> str:
    return str(flow_control[0])

@module.capture(rule = 'same line|next line|same line no space')
def c_style_programming_brace_style(style) -> str:
    return str(' '.join(style))

@module.capture(rule = '<user.code_type> [array|ray]')
def c_style_programming_type(m) -> str:
    result = m.code_type
    if len(m) > 1 and m[1] in ['array', 'ray']:
        result += get_declaration_squares().get_empty_text()
    return result

    

@module.action_class
class Actions:
    def c_style_programming_update_brace_style(new_style: str):
        '''Updates the current brace style'''
        context.settings['user.c_style_programming_brace_style'] = new_style

    def c_style_programming_start_block():
        '''Starts a c style code block'''
        start_block()
    def c_style_programming_return_from_block():
        '''Use after starting a c style code block to return to before it'''
        return_from_block()
    def c_style_programming_move_after_block():
        '''Use after starting a c style code block to move after it'''
        move_after_block()

    def c_style_programming_else():
        '''Makes an else statement'''
        actions.insert(' else')
        start_block()

    def c_style_programming_do():
        '''Makes a do while loop'''
        actions.insert('do')
        start_block()
        move_after_block()
        actions.insert(f' while{actions.user.generic_programming_get_flow_control_parentheses()};')
        actions.user.generic_programming_enter_flow_control_parentheses_from_right()
        actions.edit.left()
        

    def c_style_programming_simple_flow_control(flow_control_text: str):
        '''Makes the specified simple flow control block'''
        flow_control_parentheses = actions.user.generic_programming_get_flow_control_parentheses()
        actions.insert(flow_control_text + flow_control_parentheses)
        start_block()
        return_from_block()
        actions.user.generic_programming_enter_flow_control_parentheses_from_right()
    def c_style_programming_make_count_for_loop_given_datatype(datatype: str = 'int'):
        '''Builds a simple counting for loop using the current line text'''
        code = actions.user.fire_chicken_separate_current_line()
        variable = 'i'
        initial_value = '0'
        target = ''
        adjustment = '++'

        if len(code) == 0:
            return 
        if len(code) == 1:
            target = code[0]
            
        if len(code) > 1:
            variable = code[0]
        if len(code) == 2:
            target = code[1]
        if len(code) > 2:
            initial_value = code[1]
            target = code[2]
        if len(code) > 3:
            adjustment = apply_spacing_style_to(assign_plus_style.get(), '+=') + code[3]

        initialization = datatype + ' ' + variable + apply_spacing_style_to(assignment_style.get(), '=') + initial_value
        condition = variable + apply_spacing_style_to(less_than_style.get(), '<') + target
        adjustment_step = variable + adjustment
        insert_for_loop(initialization, condition, adjustment_step)
        
    def c_style_programming_make_for_each_loop():
        '''Builds a for each loop assuming two separated arguments in the current text'''
        code = actions.user.fire_chicken_separate_current_line()
        if len(code) != 2:
            return 
        variable_declaration = code[0]
        container = code[1]
        actions.insert('for')
        actions.user.generic_programming_insert_flow_control_parentheses()
        actions.user.generic_programming_enter_flow_control_parentheses_from_right()
        actions.insert(variable_declaration)
        actions.user.generic_programming_insert_colon_separator()
        actions.insert(container)
        start_block()

@context.action_class('user')
class UserActions:
    
    def fire_chicken_programming_build_for_loop():
        '''Builds a for loop out of three arguments'''
        code = actions.user.fire_chicken_separate_current_line()
        if len(code) != 3:
            return 
        initialization = code[0]
        condition = code[1]
        adjustment = code[2]
        insert_for_loop(initialization, condition, adjustment)
        
@context_without_javascript.action_class('user')
class UserActionsWithoutJavascript:
      def fire_chicken_programming_build_count_loop():
        '''Builds a cstyle count loop'''
        actions.user.c_style_programming_make_count_for_loop_given_datatype()

@javascript_context.action_class('user')
class JavascriptUserActions:
    def fire_chicken_programming_build_count_loop():
        '''Builds a cstyle count loop'''
        actions.user.c_style_programming_make_count_for_loop_given_datatype('let')

def start_block():
    if brace_style.get() == 'same line':
        start_block_same_line()
    elif brace_style.get() == 'next line':
        start_block_next_line()
    elif brace_style.get() == 'same line no space':
        start_block_same_line_no_space()
def start_block_same_line():
    actions.edit.line_end()
    actions.insert(' {')
    actions.key('enter')
def start_block_next_line():
    actions.edit.line_end()
    actions.key('enter')
    actions.insert('{}')
    actions.edit.left()
    actions.key('enter')
def start_block_same_line_no_space():
    actions.edit.line_end()
    actions.insert('{')
    actions.key('enter')

# use this after starting a block to go before the start of it
def return_from_block():
    if brace_style.get() == 'same line':
        actions.edit.up()
        actions.edit.line_end()
        actions.edit.left()
        actions.edit.left()
    elif brace_style.get() == 'next line':
        actions.edit.up()
        actions.edit.up()
        actions.edit.line_end()
    elif brace_style.get() == 'same line no space':
        actions.edit.up()
        actions.edit.line_end()
        actions.edit.left()


# us this after starting a block to go after it
def move_after_block():
    actions.edit.down()
    actions.edit.line_end()

def insert_for_loop(initialization, condition, adjustment):
    actions.insert('for')
    actions.user.generic_programming_insert_flow_control_parentheses()
    actions.user.generic_programming_enter_flow_control_parentheses_from_right()
    actions.insert(initialization)
    actions.user.generic_programming_insert_semicolon_separator()
    actions.insert(condition)
    actions.user.generic_programming_insert_semicolon_separator()
    actions.insert(adjustment)
    start_block()
