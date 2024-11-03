tag: user.cursorless
-

^<user.cursorless_target>$:
    user.fire_chicken_cursorless_bring(cursorless_target)

store <user.cursorless_target>: 
    user.generic_programming_start_new_line_if_current_line_not_empty()
    user.fire_chicken_cursorless_assign(cursorless_target)

house <user.cursorless_target>:
    user.code_operator_assignment()
    user.fire_chicken_cursorless_bring(cursorless_target)

turn <user.cursorless_target>:
    user.fire_chicken_cursorless_return(cursorless_target)

plop <user.cursorless_target>:
    user.generic_programming_create_line_below()
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

mine <user.cursorless_target>:
    user.generic_programming_self_dot()
    user.fire_chicken_cursorless_bring(cursorless_target)

own <user.cursorless_target>:
    user.generic_programming_self_dot()
    user.fire_chicken_cursorless_call(cursorless_target)

mem <user.cursorless_target>:
    insert('.')
    user.fire_chicken_cursorless_bring(cursorless_target)

mall <user.cursorless_target>:
    insert('.')
    user.fire_chicken_cursorless_call(cursorless_target)
