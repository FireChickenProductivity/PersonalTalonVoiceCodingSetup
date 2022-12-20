from talon import Module, actions

module = Module()
editor_name = module.setting(
    'fire_thicken_programming_editor_name',
    type = str,
    default = 'code',
    desc = 'The name of the editor to switch to that talon can understand'
)

@module.action_class
class Actions:
    def fire_chicken_programming_switch_to_editor():
        ''''''
        actions.user.switcher_focus(editor_name.get())