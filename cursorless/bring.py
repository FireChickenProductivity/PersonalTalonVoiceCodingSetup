from talon import Module, actions
from typing import Any
module = Module()
@module.action_class
class Actions:
    def fire_chicken_cursorless_bring(target: Any):
        ''''''
        actions.user.cursorless_command("callAsFunction", target)
        actions.key('delete')
        actions.key('backspace')
    
    def fire_chicken_cursorless_assign(target: Any):
        ''''''
        actions.user.fire_chicken_cursorless_bring(target)
        actions.user.code_operator_assignment()
