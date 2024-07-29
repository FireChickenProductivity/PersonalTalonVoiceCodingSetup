from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_programming_insert_c_insert_structure(name: str):
        ''''''
        actions.insert('struct ')
        actions.user.fire_chicken_insert_with_pascal_case(name)
        actions.user.c_style_programming_start_block()
    
    def fire_chicken_programming_insert_c_constant(name: str):
        ''''''
        actions.insert('#define ')
        actions.user.fire_chicken_insert_with_upper_snake_case(name)
        actions.key('space')