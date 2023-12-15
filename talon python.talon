tag: user.python
and tag: user.fire_chicken_talon_python_programming
-
(keypress|keystroke) <user.keys>$: user.talon_python_programming_insert_keypress(keys)
(keypress|keystroke) <user.keys> over: user.talon_python_programming_insert_keypress(keys)

talon import: 'from talon import '

state user: 'user.'

<user.talon_programming_module_name> <user.talon_programming_standard>: 
    user.talon_python_programming_define_module(talon_programming_module_name)
<user.talon_programming_context_name> <user.talon_programming_standard>:
    user.talon_python_programming_define_context(talon_programming_context_name)
<user.talon_programming_module_name> capture: 
    user.talon_python_programming_module_capture(talon_programming_module_name)
<user.talon_programming_module_name> <user.talon_programming_standard> action class:
    user.talon_python_programming_define_module_action_class(talon_programming_module_name, 'Actions')
<user.talon_programming_module_name> <user.talon_programming_standard> and class:
    user.talon_python_programming_define_module(talon_programming_module_name)
    key(enter)
    user.talon_python_programming_define_module_action_class(talon_programming_module_name, 'Actions')
<user.talon_programming_module_name> setting:
    user.talon_python_programming_start_setting_definition(talon_programming_module_name)
<user.talon_programming_module_name> tag:
    user.talon_python_programming_start_tag_definition(talon_programming_module_name)

settings get: 
    user.fire_chicken_call_function_inside_with_name_formatted('settings.get', 'snake')

action <user.talon_programming_standard_actions>:
    insert('actions.')
    insert(talon_programming_standard_actions)
    insert('()')
    edit.left()
action user: insert('actions.user.')

action edit: insert('actions.edit.')
control <user.talon_programming_control_function>:
    insert('ctrl.')
    insert(talon_programming_control_function)
    insert('()')
    edit.left()