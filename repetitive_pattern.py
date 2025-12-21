from talon import Module, actions

mod = Module()

pattern: str = ""

@mod.action_class
class Actions:
	def fire_chicken_programming_save_pattern(new_pattern: str):
		"""Set the current programming pattern"""
		global pattern
		pattern = new_pattern

	def fire_chicken_programming_insert_pattern(pattern: str):
		"""Inserts the specified programming pattern"""
		actions.user.insert_snippet(pattern)

	def fire_chicken_programming_get_pattern() -> str:
		"""Gets the specified programming pattern"""
		return pattern

	def fire_chicken_programming_find_pattern(text: str) -> str:
		"""Finds the most prominent pattern in the text"""
		pass
		