from talon import actions, Module, Context

from .styles import *

talon_python_programming = Context()

module = Module()
module.tag('fire_chicken_talon_python_programming', desc = 'Activate talon python commands')
@module.action_class
class Actions:
    def fire_chicken_talent_programming_start_action_file():
        """Inserts an action file template"""
        actions.user.insert_snippet(r"""from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def $1($2):
        $3""")

    def fire_chicken_talon_programming_define_action():
        """Defines an action"""
        # get the text above and below
        prior_text = actions.user.generic_programming_compute_proceeding_text()
        following_text = actions.user.generic_programming_compute_following_text()
        total_text: str = prior_text + following_text
        # if Module has not been imported, import it
            # if missing talon import do that
        if "from talon import" not in total_text:
            actions.edit.file_start()
            import_text = "from talon import Module"
            actions.insert(import_text)
            for _ in range(2):
                actions.edit.line_insert_down()
            prior_text = import_text + prior_text + "\n\n"
            actions.edit.file_start()
            prior_lines = prior_text.split("\n")
            return_cursor_from_above(prior_lines)
        else:
            # otherwise check if Module is imported at any of the imports
            imports = [l for l in total_text.split("\n") if l.startswith("from talon import ")]
            if not any(["Module" in l for l in imports]):
                first_import_index = total_text.find("from talon import ")
                part_before_import = total_text[:first_import_index]
                lines_from_the_top = part_before_import.count("\n")
                actions.edit.file_start()
                for _ in range(lines_from_the_top): actions.edit.down()
                actions.edit.line_end()
                actions.insert(", Module")
                actions.edit.file_start()
                prior_lines = prior_text.split("\n")
                return_cursor_from_above(prior_lines)

        # if a module has not been defined, define one

        # if an action class does not exist, create one
        # if one exists, define the action at the nearest one

    def talon_programming_insert_keypress(keys: str):
        '''Inserts the talon command needed to make the keypress'''
        actions.insert('key')
        function_call_parentheses = get_function_call_parentheses()
        function_call_parentheses.insert()
        function_call_parentheses.enter_from_right()
        actions.insert(keys)

    def talon_programming_activate_python_commands():
        '''activates talon python commands'''
        talon_python_programming.tags = ['user.fire_chicken_talon_python_programming']
    def talon_programming_deactivate_python_commands():
        '''deactivates talon python commands'''
        talon_python_programming.tags = []
    def talon_python_programming_insert_keypress(keys: str):
        '''Inserts the talon command needed to make the key presses'''
        actions.insert('actions.')
        actions.insert('key')
        function_call_parentheses = get_function_call_parentheses()
        function_call_parentheses.insert()
        function_call_parentheses.enter_from_right()
        actions.insert("''")
        actions.edit.left()
        actions.insert(keys)
    def talon_python_programming_define_module(name: str):
        '''Defines a module'''
        actions.insert(name + ' = ' + 'Module()')
    def talon_python_programming_module_capture(module_name: str):
        '''Starts creating module capture'''
        actions.insert(f'@{module_name}.capture(rule = )')
        actions.edit.left()
    def talon_python_programming_define_context(name: str):
        '''Defines a context'''
        actions.insert(name + ' = ' + 'Context()')
    def talon_python_programming_define_module_action_class(module_name: str, classname: str):
        '''Defines a module action class'''
        actions.insert(f'@{module_name}.action_class')
        actions.key('enter')
        actions.insert(f'class {classname}:')
        actions.key('enter')
    def talon_python_programming_start_setting_definition(module_name: str):
        '''Starts setting definition'''
        actions.insert(f'{module_name}.setting()')
        actions.edit.left()
        actions.key('enter')
        actions.insert("'',")
        actions.key('enter')
        actions.insert('type = ')
        actions.key('enter')
        actions.insert('default = ')
        actions.key('enter')
        actions.insert('desc = ')
        for i in range(3):
            actions.edit.up()
        actions.edit.line_end()
        for i in range(2):
            actions.edit.left()
    def talon_python_programming_start_tag_definition(module_name: str):
        '''Starts tag definition'''
        actions.insert(f'{module_name}.tag()')
        actions.edit.left()

@module.capture(rule = 'mod|module')
def talon_programming_module_name(m) -> str:
    return str(m[0])

@module.capture(rule = 'standard|stand')
def talon_programming_standard(m) -> str:
    return str(m[0])

@module.capture(rule = 'context|ctx')
def talon_programming_context_name(m) -> str:
    return str(m[0])

@module.capture(rule = 'insert|key|sleep|repeat|mouse click|mouse scroll|mouse move')
def talon_programming_standard_actions(m) -> str:
    return str('_'.join(m))

@module.capture(rule = 'mouse pos')
def talon_programming_control_function(m) -> str:
    return str('_'.join(m))

def return_cursor_from_above(lines: list[str]):
    """Moves the cursor to the original position from at the top of the lines"""
    for _ in range(len(lines) - 1):
        actions.edit.down()
    actions.edit.line_start()
    for _ in range(len(lines[-1])):
        actions.edit.right()

def return_cursor_from_below(lines: list[str]):
    """Moves the cursor to the original position from at the bottom of the lines"""
    for _ in range(len(lines) - 1):
        actions.edit.up()
    actions.edit.line_end()
    for _ in range(len(lines[-1])):
        actions.edit.left()