#This file contains actions used to interact with the community repository actions
from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_programming_insert_with_history(text: str):
        '''Inserts the text and adds it to the phrase history'''
        actions.insert(text)
        actions.user.add_phrase_to_history(text)

    def fire_chicken_convert_text_to_pascal_case(text: str) -> str:
        '''Converts the text to pascal case'''
        return actions.user.formatted_text(text, "hammer")

