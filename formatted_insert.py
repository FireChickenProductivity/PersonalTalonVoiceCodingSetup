from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_insert_after(text: str):
        '''Insert text after the cursor'''
        actions.insert(text)
        move_left_for_each_character(text)
    def fire_chicken_insert_around_cursor(text_before_cursor: str, text_after_cursor: str):
        '''Inserts the first argument before the cursor and the second argument after'''
        actions.insert(text_before_cursor)
        actions.user.fire_chicken_insert_after(text_after_cursor)


def move_left_for_each_character(text: str):
    for i in range(len(text)):
        actions.edit.left()