app: vscode
-
store <user.cursorless_target>: 
    user.fire_chicken_cursorless_assign(cursorless_target)

house <user.cursorless_target>:
    user.code_operator_assignment()
    user.fire_chicken_cursorless_bring(cursorless_target)

<user.cursorless_target> (store|house) <user.cursorless_target>: 
    user.fire_chicken_cursorless_assign(cursorless_target_1)
    user.fire_chicken_cursorless_bring(cursorless_target_2)

turn <user.cursorless_target>:
    user.fire_chicken_cursorless_return(cursorless_target)

some <user.cursorless_target>:
    user.code_operator_addition()
    user.fire_chicken_cursorless_bring(cursorless_target)

small <user.cursorless_target>:
    user.code_operator_subtraction()
    user.fire_chicken_cursorless_bring(cursorless_target)

piece <user.cursorless_target>:
    insert(', ')
    user.fire_chicken_cursorless_bring(cursorless_target)

<user.cursorless_target> stow <user.prose>$:
    user.fire_chicken_insert_default_formatted_variable(prose)
    user.code_operator_assignment()
    user.fire_chicken_cursorless_bring(cursorless_target)
