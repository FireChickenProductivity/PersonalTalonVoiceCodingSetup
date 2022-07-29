from talon import actions, Module, Context

module = Module()
context = Context()
context.matches = r'''
tag: user.fire_chicken_snippets
'''
module.tag('fire_chicken_snippets', desc = 'commands for using language specific code snippets')
module.list('fire_chicken_method_snippets', desc = 'language specific method snippets')



@module.action_class
class Actions:
    def fire_chicken_call_method_snippet(method_name: str):
        '''Inserts the specified method snippet'''
        actions.user.generic_programming_call_method(method_name)
    def fire_chicken_call_method_snippet_inside(method_name: str):
        '''Inserts the specified method snippet and moves inside the arguments'''
        actions.user.generic_programming_call_method_inside(method_name)



