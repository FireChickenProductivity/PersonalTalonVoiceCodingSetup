from talon import Context, actions

context = Context()
context.matches = r"""
os: mac
"""

@context.action_class('user')
class Actions:
    def fire_chicken_switch_to_last_application():
        """Switch to the last application"""
        actions.key('cmd-tab')