#This file contains actions used to interact with the community repository actions
from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_programming_insert_with_history(text: str):
        '''Inserts the text and adds it to the phrase history'''
        actions.insert(text)
        actions.user.add_phrase_to_history(text)
