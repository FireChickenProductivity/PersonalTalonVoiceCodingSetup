from talon import Module, actions

module = Module()
@module.action_class
class Actions:
	def fire_chicken_repeat_stop_terminals(number: int):
		""""""
		actions.user.vscode("workbench.action.terminal.focus")
		for i in range(number):
			actions.key('ctrl-c')
			actions.key('up')
			actions.key('enter')
			actions.user.vscode("workbench.action.terminal.focusNext")




		