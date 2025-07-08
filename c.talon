code.language: c
code.language: cpp
-
tag(): user.c_style_programming

print f: user.fire_chicken_insert_around_cursor('printf(', ');')
print form: user.fire_chicken_insert_around_cursor('printf("', '");')

scan f: user.fire_chicken_insert_around_cursor('scanf(', ');')

include: insert("#include ")

structure <user.prose>$: user.fire_chicken_programming_insert_c_insert_structure(prose)
structure <user.prose> over: user.fire_chicken_programming_insert_c_insert_structure(prose)
constant <user.prose>$: user.fire_chicken_programming_insert_c_constant(prose)
constant <user.prose> over: user.fire_chicken_programming_insert_c_constant(prose)

