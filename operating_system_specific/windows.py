from talon import Context, actions

context = Context()
context.matches = r"""
os: windows
"""

@context.action_class('user')
class Actions:
    def fire_chicken_switch_to_last_application():
        """Switch to the last application"""
        actions.key('alt-tab')
    def fire_chicken_close_active_vscode_folder():
        """Close the active vscode folder"""
        actions.key('ctrl-k f')