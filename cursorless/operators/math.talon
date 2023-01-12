tag: user.code_operators_math
and tag: user.fire_chicken_cursorless
-

# math operators
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (minus | subtract): 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_subtraction()
<user.fire_chicken_cursorless_operator_prefix> (minus | subtract) <user.cursorless_target>: 
    user.code_operator_subtraction()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (minus | subtract) <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_subtraction()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (plus | add): 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_addition()
<user.fire_chicken_cursorless_operator_prefix> (plus | add) <user.cursorless_target>: 
    user.code_operator_addition()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (plus | add) <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_addition()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (times | multiply): 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_multiplication()
<user.fire_chicken_cursorless_operator_prefix> (times | multiply) <user.cursorless_target>: 
    user.code_operator_multiplication()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (times | multiply) <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_multiplication()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> divide: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_division()
<user.fire_chicken_cursorless_operator_prefix> divide <user.cursorless_target>: 
    user.code_operator_division()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> divide <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_division()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> mod: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_modulo()
<user.fire_chicken_cursorless_operator_prefix> mod <user.cursorless_target>: 
    user.code_operator_modulo()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> mod <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_modulo()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (power | exponent): 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_exponent()
<user.fire_chicken_cursorless_operator_prefix> (power | exponent) <user.cursorless_target>: 
    user.code_operator_exponent()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (power | exponent) <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_exponent()
    user.fire_chicken_cursorless_bring(cursorless_target_2)

# comparison operators
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> equal: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_equal()
<user.fire_chicken_cursorless_operator_prefix> equal <user.cursorless_target>: 
    user.code_operator_equal()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> equal <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_equal()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> not equal: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_not_equal()
<user.fire_chicken_cursorless_operator_prefix> not equal <user.cursorless_target>: 
    user.code_operator_not_equal()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> not equal <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_not_equal()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (greater | more): 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_greater_than()
<user.fire_chicken_cursorless_operator_prefix> (greater | more) <user.cursorless_target>: 
    user.code_operator_greater_than()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (greater | more) <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_greater_than()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (less | below) [than]: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_less_than()
<user.fire_chicken_cursorless_operator_prefix> (less | below) [than] <user.cursorless_target>: 
    user.code_operator_less_than()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> (less | below) [than] <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_less_than()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> greater [than] or equal: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_greater_than_or_equal_to()
<user.fire_chicken_cursorless_operator_prefix> greater [than] or equal <user.cursorless_target>: 
    user.code_operator_greater_than_or_equal_to()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> greater [than] or equal <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_greater_than_or_equal_to()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> less [than] or equal: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_less_than_or_equal_to()
<user.fire_chicken_cursorless_operator_prefix> less [than] or equal <user.cursorless_target>: 
    user.code_operator_less_than_or_equal_to()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> less [than] or equal <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_less_than_or_equal_to()
    user.fire_chicken_cursorless_bring(cursorless_target_2)

# logical operators
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> and: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_and()
<user.fire_chicken_cursorless_operator_prefix> and <user.cursorless_target>: 
    user.code_operator_and()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> and <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_and()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> or: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_or()
<user.fire_chicken_cursorless_operator_prefix> or <user.cursorless_target>: 
    user.code_operator_or()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> or <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_or()
    user.fire_chicken_cursorless_bring(cursorless_target_2)

# set operators
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> in: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_in()
<user.fire_chicken_cursorless_operator_prefix> in <user.cursorless_target>: 
    user.code_operator_in()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> in <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_in()
    user.fire_chicken_cursorless_bring(cursorless_target_2)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> not in: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    user.code_operator_not_in()
<user.fire_chicken_cursorless_operator_prefix> not in <user.cursorless_target>: 
    user.code_operator_not_in()
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> not in <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    user.code_operator_not_in()
    user.fire_chicken_cursorless_bring(cursorless_target_2)

# TODO: This operator should either be abstracted into a function or removed.
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> colon: 
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert(" : ")
<user.fire_chicken_cursorless_operator_prefix> colon <user.cursorless_target>: 
    insert(" : ")
    user.fire_chicken_cursorless_bring(cursorless_target)
<user.cursorless_target> <user.fire_chicken_cursorless_operator_prefix> colon <user.cursorless_target>: 
    user.fire_chicken_cursorless_bring(cursorless_target_1)
    insert(" : ")
    user.fire_chicken_cursorless_bring(cursorless_target_2)
