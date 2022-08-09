tag: user.code_functions_common
-
toggle proceed: user.code_toggle_functions()
proceed <user.code_common_function>:
    user.code_insert_function(code_common_function, "")
proceed cell <number>:
    user.code_select_function(number - 1, "")
proceed wrap <user.code_common_function>:
    user.code_insert_function(code_common_function, edit.selected_text())
proceed wrap <number>:
    user.code_select_function(number - 1, edit.selected_text())