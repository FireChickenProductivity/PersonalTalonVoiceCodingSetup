tag: user.c_style_programming
-
tag(): user.build_for_loops

brace style <user.c_style_programming_brace_style>:
    user.c_style_programming_update_brace_style(c_style_programming_brace_style)

form (brace|block): user.c_style_programming_start_block()
more (brace|block): user.c_style_programming_continue_block()
form more <user.c_style_programming_continuation_flow_control_name>: 
    user.c_style_programming_continuation_flow_control(c_style_programming_continuation_flow_control_name)
meal <user.c_style_programming_continuation_flow_control_name>:
    user.c_style_programming_continuation_flow_control_next_line(c_style_programming_continuation_flow_control_name)

op ray: user.generic_programming_insert_empty_declaration_squares()

form else: user.c_style_programming_else()

form do: user.c_style_programming_do()

form <user.c_style_programming_simple_flow_control_name>:
    user.c_style_programming_simple_flow_control(c_style_programming_simple_flow_control_name)

form return:
    insert('return ;')
    edit.left()

type <user.c_style_programming_type>:
    insert(c_style_programming_type)

kind <user.c_style_programming_type>:
    insert(c_style_programming_type + ' ')

stowing:
    insert(" = ;")
    edit.left()

build for each: user.c_style_programming_make_for_each_loop()

#types
desert: 'void '
bushy: 'int '

settings():
    user.fire_chicken_statement_ending = ';'