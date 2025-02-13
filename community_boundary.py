#This file contains actions used to interact with the community repository actions
from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_programming_insert_with_history(text: str):
        '''Inserts the text and adds it to the phrase history'''
        actions.insert(text)
        actions.user.add_phrase_to_history(text)

    def fire_chicken_programming_add_phrase_to_history(text: str):
        """Inserts the text into the phrase history"""
        actions.user.add_phrase_to_history(text)

    def fire_chicken_convert_text_to_pascal_case(text: str) -> str:
        '''Converts the text to pascal case'''
        return actions.user.fire_chicken_format_text(text, "pascal")

    def fire_chicken_convert_text_to_camel_case(text: str) -> str:
        '''Converts the text to camel case'''
        return actions.user.fire_chicken_format_text(text, "camel")

    def fire_chicken_code_assignment_operator():
        """Uses the language specific assignment operator"""
        actions.user.code_operator("ASSIGNMENT")
    
    def fire_chicken_code_addition_operator():
        """Uses the language specific math add operator"""
        actions.user.code_operator("MATH_ADD")

    def fire_chicken_code_subtraction_operator():
        """Uses the language specific math subtract operator"""
        actions.user.code_operator("MATH_SUBTRACT")