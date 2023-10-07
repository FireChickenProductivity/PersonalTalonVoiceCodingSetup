from talon import Module, actions
from typing import Any
module = Module()
@module.action_class
class Actions:
    def fire_chicken_cursorless_bring(target: Any):
        ''''''
        actions.user.cursorless_command("replaceWithTarget", target)
    
    def fire_chicken_cursorless_assign(target: Any):
        ''''''
        actions.user.fire_chicken_cursorless_bring(target)
        actions.user.code_operator_assignment()
    
    def fire_chicken_cursorless_return(target: Any):
        ''''''
        actions.user.code_state_return()
        actions.user.fire_chicken_cursorless_bring(target)
        actions.user.fire_chicken_insert_statement_ending()
    
    def fire_chicken_cursorless_call(target: Any):
        ''''''
        actions.user.cursorless_command("callAsFunction", target)