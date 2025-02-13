from talon import Module, actions
from typing import Any

def is_target_not_single_character(target):
    return target.modifiers is not None or target.mark["symbolColor"] != "default"

module = Module()
@module.action_class
class Actions:
    def fire_chicken_cursorless_bring(target: Any):
        ''''''
        actions.user.cursorless_command("replaceWithTarget", target)
    
    def fire_chicken_cursorless_assign(target: Any):
        ''''''
        actions.user.fire_chicken_cursorless_bring(target)
        actions.user.fire_chicken_code_assignment_operator()
    
    def fire_chicken_cursorless_return(target: Any):
        ''''''
        actions.user.code_state_return()
        actions.user.fire_chicken_cursorless_bring(target)
        actions.user.fire_chicken_insert_statement_ending()
    
    def fire_chicken_cursorless_call(target: Any):
        ''''''
        actions.user.cursorless_command("callAsFunction", target)

    def fire_chicken_cursorless_bring_target_or_type_character(target: Any):
        """"""
        if is_target_not_single_character(target):
            actions.user.fire_chicken_cursorless_bring(target)
        else:
            actions.insert(target.mark["character"])