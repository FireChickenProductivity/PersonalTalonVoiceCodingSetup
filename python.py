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

@module.action_class
class Actions:
    def fire_chicken_programming_define_python_class(classname: str):
        ''''''
        actions.insert('class ')
        actions.user.insert_formatted(classname ,'hammer')
        actions.insert(':')
        actions.user.generic_programming_create_line_below()

    def fire_chicken_programming_define_python_subclass(classname: str):
        ''''''
        actions.user.fire_chicken_programming_define_python_class(classname)
        actions.edit.up()
        actions.edit.line_end()
        actions.edit.left()
        actions.user.fire_chicken_insert_around_cursor('(', ')')
    
    def fire_chicken_programming_insert_python_debug_print_statement_from_cursorless_target(cursorless_target: str):
        ''''''
        actions.insert("print('")
        actions.user.fire_chicken_cursorless_bring(cursorless_target)
        actions.insert("', ")
        actions.user.fire_chicken_cursorless_bring(cursorless_target)
        actions.insert(")")

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

context.lists['user.fire_chicken_method_snippets'] = {
    'as integer ratio' : 'as_integer_ratio',
    'bit count' : 'bit_count',
    'bit length' : 'bit_length',
    'capitalize' : 'capitalize',
    'Case fold' : 'casefold',
    'center' : 'center',
    'clear' : 'clear',
    'copy' : 'copy',
    'count' : 'count',
    'encode' : 'encode',
    'Ends with' : 'endswith',
    'Expand tabs' : 'expandtabs',
    'find' : 'find',
    'format' : 'format',
    'format map' : 'format_map',
    'from bytes' : 'from_bytes',
    'From keys' : 'fromkeys',
    'get' : 'get',
    'hex' : 'hex',
    'index' : 'index',
    'insert' : 'insert',
    'is integer' : 'is_integer',
    'is al num' : 'isalnum',
    'Is alpha' : 'isalpha',
    'Is decimal' : 'isdecimal',
    'Is digit' : 'isdigit',
    'Is identifier' : 'isidentifier',
    'Is lower' : 'islower',
    'Is numeric' : 'isnumeric',
    'Is printable' : 'isprintable',
    'Is space' : 'isspace',
    'Is title' : 'istitle',
    'Is upper' : 'isupper',
    'items' : 'items',
    'join' : 'join',
    'keys' : 'keys',
    'L just' : 'ljust',
    'lower' : 'lower',
    'L strip' : 'lstrip',
    'Make trans' : 'maketrans',
    'partition' : 'partition',
    'pop' : 'pop',
    'Pop item' : 'popitem',
    'remove' : 'remove',
    'replace' : 'replace',
    'reverse' : 'reverse',
    'R find' : 'rfind',
    'R index' : 'rindex',
    'R just' : 'rjust',
    'R partition' : 'rpartition',
    'R split' : 'rsplit',
    'R strip' : 'rstrip',
    'Set default' : 'setdefault',
    'sort' : 'sort',
    'split' : 'split',
    'Split lines' : 'splitlines',
    'Starts with' : 'startswith',
    'strip' : 'strip',
    'Swap case' : 'swapcase',
    'title' : 'title',
    'to bytes' : 'to_bytes',
    'translate' : 'translate',
    'update' : 'update',
    'upper' : 'upper',
    'values' : 'values',
    'Z fill' : 'zfill',
    'to bytes' : 'to_bytes',
    'from bytes' : 'from_bytes',
    'as integer ratio' : 'as_integer_ratio',
    'is integer' : 'is_integer',
    'hex' : 'hex',
}
