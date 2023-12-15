from talon import Module, actions, settings

module = Module()
editor_name_setting_name = 'fire_thicken_programming_editor_name'
editor_name = 'user.' + editor_name_setting_name
module.setting(
    editor_name_setting_name,
    type = str,
    default = 'code',
    desc = 'The name of the editor to switch to that talon can understand'
)

@module.action_class
class Actions:
    def fire_chicken_programming_switch_to_editor():
        ''''''
        actions.user.switcher_focus(settings.get(editor_name))