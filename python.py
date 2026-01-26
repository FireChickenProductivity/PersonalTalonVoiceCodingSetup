from talon import Module, actions, Context

import re

module = Module()
context = Context()
context.matches = r'''
code.language: python
'''

module.list("fire_chicken_numpy_functions", desc="Numpy functions")

LINE_STARTING_STATEMENTS = set(['while', 'while :', 'for', 'for ', 'if', 'if :', 'def', 'def :', 'def ', 'return ', 'return', 'else:', 'elif :'])

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

def insert_subtext_if_not_inside_text(subtext, text):
    if subtext not in text:
        actions.insert(subtext)

def compute_lines_from(text):
    text = text.replace("\r", "")
    lines = text.split("\n")
    return lines

def compute_preceding_space(text):
    spaces = ""
    i = 0
    while i < len(text) and text[i].isspace():
        spaces += text[i]
        i += 1
    return spaces

def compute_current_line_from_preceding_text(text: str):
    last_line_start_index = text.rindex('\n')
    if last_line_start_index >= 0:
        return text[last_line_start_index:]
    return text

@module.action_class
class Actions:
    def fire_chicken_programming_copy_initialization():
        """Copies the initialization on the current line and puts the cursor at the start of the line"""
        actions.edit.select_line()
        selected_text: str = actions.edit.selected_text()
        actions.edit.line_insert_down()
        post_variable_index = 0
        while selected_text[post_variable_index].isalnum() or \
            selected_text[post_variable_index] == "_":
            post_variable_index += 1
        initialization = selected_text[post_variable_index:]
        actions.insert(initialization)
        for _ in range(len(initialization)):
            actions.edit.left()

    def fire_chicken_programming_open_python_file(mode: str):
        """Codes the opening of a python file with the specific mode"""
        actions.user.insert_snippet(rf"""with open($1, "{mode}") as f:
    $0""")
    def fire_chicken_programming_read_python_file_lines():
        """Codes reading lines from a file in python"""
        actions.user.insert_snippet(r"""with open($1, "r") as f:
    for line in f.readlines():
        $0""")
    def fire_chicken_programming_define_python_class(classname: str):
        ''''''
        actions.insert('class ')
        actions.user.fire_chicken_insert_formatted_text(classname ,'hammer')
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

    def fire_chicken_programming_build_for_each_loop_using_plural():
        """Builds a python for each loop using a plural target"""
        code = actions.user.fire_chicken_separate_current_line()[0]
        if code.endswith("s"):
            actions.insert(f"for {code[:-1]} in {code}:\n")

    def fire_chicken_programming_auto_line():
        """Activates automatic newline insertion"""
        def on_action(action):
            if action.get_name() == 'insert':
                text = action.get_arguments()[0]
                if text in LINE_STARTING_STATEMENTS:
                    line_before = actions.user.generic_programming_get_line_start()
                    line_before = line_before[:len(line_before) - len(text)]
                    line_after = actions.user.generic_programming_get_line_ending()
                    other_text = line_before + line_after
                    if not other_text.isspace() and len(other_text) > 0:
                        for _ in range(len(text)): actions.edit.delete()
                        actions.edit.line_end()
                        actions.key('enter')
                        actions.edit.line_end()
                        actions.user.paste(text)
        actions.user.basic_action_recorder_register_callback_function_with_name(on_action, 'auto line')

    def fire_chicken_disable_programming_auto_line():
        """Deactivates automatic newline insertion"""
        actions.user.basic_action_recorder_unregister_callback_function_with_name('auto line')

    def fire_chicken_programming_insert_magic_method(name: str, is_no_argument: bool=False):
        """Inserts the specified magic method"""
        actions.insert(f"def __{name}__(self):")
        if is_no_argument:
            actions.edit.line_insert_down()
        else:
            for _ in range(2): actions.edit.left()
            actions.insert(", ")

    def fire_chicken_programming_insert_python_block_starter(name: str):
        """Inserts the specified python block starter"""
        actions.insert(name + " :")
        actions.edit.left()

    def fire_chicken_python_programming_insert_assignment_if_missing():
        """Add assignment operator if missing """
        line_start = actions.user.generic_programming_get_line_start()
        if line_start.isspace():
            actions.insert('return ')
        elif "(" in line_start:
            insert_subtext_if_not_inside_text("=", line_start)
        else:
            insert_subtext_if_not_inside_text(" = ", line_start)
        
    def fire_chicken_python_programming_compute_preceding_class_text():
        """Computes the text before the cursor for the current class assuming one is already inside a class"""
        preceding_text: str = actions.user.generic_programming_compute_proceeding_text()
        class_declaration_index = preceding_text.rindex('\nclass')
        if class_declaration_index >= 0:
            return preceding_text[class_declaration_index:]
        elif preceding_text.startswith('class'):
            return preceding_text
        else:
            return ""
    
    def fire_chicken_python_programming_start_new_method_block():
        """Starts a new block for a method inside the current class"""
        preceding_class_text = actions.user.fire_chicken_python_programming_compute_preceding_class_text()
        if preceding_class_text:
            new_lines_before_last_text = 0
            has_computed_lines_before_last_text = False
            indentation_text = ""
            lines = compute_lines_from(preceding_class_text)
            for i in range(len(lines) - 1, -1, -1):
                line = lines[i]
                if not has_computed_lines_before_last_text:
                    if line.isspace():
                        new_lines_before_last_text += 1
                    else:
                        has_computed_lines_before_last_text = True
                if line.strip().startswith("def "):
                    indentation_text = compute_preceding_space(line)
                    break
            if new_lines_before_last_text < 2:
                for _ in range(2 - new_lines_before_last_text):
                    actions.edit.line_insert_down()
            actions.edit.extend_line_start()
            actions.insert(indentation_text)

    def fire_chicken_python_add_slots(class_text: str) -> str:
        """Adds slots to the specified python class"""
        attribute_assignments = re.findall(r'self.(\w+)\s*=\s*', class_text) + \
            re.findall(r'self.(\w+)\s*:', class_text)
        variable_names = set(attribute_assignments)
        if not variable_names:
            return 
        slot_variables = [f"'{v}'" for v in variable_names]
        if len(slot_variables) > 1:
            slot_text = f"__slots__ = ({', '.join(slot_variables)})"
        else:
            slot_text = slot_text = f"__slots__ = ({slot_variables[0]},)"
        lines = class_text.split("\n")
        indentation_text: str | None = None
        for line in lines:
            if len(line) >= 1 and line[0].isspace():
                leading_spaces = []
                for c in line:
                    if c.isspace():
                        leading_spaces.append(c)
                    else:
                        break
                indentation_text = "".join(leading_spaces)
                break
        if indentation_text is None:
            return 
        first_function_index = -1
        for i, line in enumerate(lines):
            if line.lstrip().startswith("def"):
                first_function_index = i
                break
        if first_function_index < 0:
            return 
        lines.insert(first_function_index, indentation_text + slot_text)
        return "\n".join(lines)
        

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