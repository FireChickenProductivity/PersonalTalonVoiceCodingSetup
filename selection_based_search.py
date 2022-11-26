from talon import actions, Module

module = Module()
@module.action_class
class Actions:
    def fire_chicken_programming_select_next_variable_name_part():
        '''Attempts to select the next part of the variable name'''
        select_next_variable_name_part(is_end_of_variable_name_part)

def select_next_variable_name_part(is_end_of_variable_name_part_function):
    actions.edit.extend_line_end()
    selected_text = actions.user.generic_programming_get_selected_text()
    last_character_index = calculate_next_variable_name_part_index(selected_text, is_end_of_variable_name_part_function)
    actions.edit.left()
    for i in range(last_character_index):
        actions.edit.extend_right()
    

def calculate_next_variable_name_part_index(text, is_end_of_variable_name_part_function):
    last_character_index = 0
    previous_character = ''
    for character in text:
        if is_end_of_variable_name_part_function(character, previous_character):
            return last_character_index
        last_character_index += 1
        previous_character = character
    return last_character_index

def is_end_of_variable_name_part(character: str, previous_character: str):
    return not character.isalnum() or (previous_character.islower() and character.isupper())
