tag: user.cursorless
-

#^<user.cursorless_target>$:
    #user.fire_chicken_cursorless_bring(cursorless_target)

store <user.cursorless_target>: 
    user.generic_programming_start_new_line_if_current_line_not_empty()
    user.fire_chicken_cursorless_assign(cursorless_target)
    user.fire_chicken_insert_statement_ending_after_cursor()

house <user.cursorless_target>:
    user.fire_chicken_code_assignment_operator()
    user.fire_chicken_cursorless_bring(cursorless_target)

turn <user.cursorless_target>:
    user.fire_chicken_cursorless_return(cursorless_target)

plop <user.cursorless_target>:
    user.generic_programming_create_line_below()
    user.fire_chicken_cursorless_return(cursorless_target)

some <user.cursorless_target>:
    user.fire_chicken_code_addition_operator()
    user.fire_chicken_cursorless_bring(cursorless_target)

small <user.cursorless_target>:
    user.fire_chicken_code_subtraction_operator()
    user.fire_chicken_cursorless_bring(cursorless_target)

lou <user.cursorless_target>:
    user.generic_programming_start_new_line_if_current_line_not_empty()
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

burst <user.cursorless_target>:
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert('.')