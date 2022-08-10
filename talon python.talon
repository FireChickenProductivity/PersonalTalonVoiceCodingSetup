tag: user.python
and tag: user.fire_chicken_talon_python_programming
-
keypress <user.keys>$: user.talon_python_programming_insert_keypress(keys)
keypress <user.keys> over: user.talon_python_programming_insert_keypress(keys)

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
<user.talon_programming_module_name> setting:
    user.talon_python_programming_start_setting_definition(talon_programming_module_name)

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