from talon import actions, Module, settings
from typing import List

module = Module()
separator_setting_name = 'fire_chicken_separator'
separator = 'user.' + separator_setting_name
module.setting(
    separator_setting_name,
    type = str,
    default = '   !!&   3$%^$   ',
    desc = 'separator used to separate arguments to commands',
)

def separate_current_line() -> List:
    current_line = get_current_line()
    result = separate_line(current_line)
    return result

#I intend to eventually move that action over to this file
def get_current_line():
    return actions.user.generic_programming_get_line()

def separate_line(line: str):
    return line.split(settings.get(separator))

@module.action_class
class Actions:
    def fire_chicken_insert_separator():
        '''Inserts the separator used to separate arguments to commands'''
        actions.insert(settings.get(separator))
    def fire_chicken_separate_current_line() -> List:
        '''Gets the command arguments from the current line'''
        return separate_current_line()