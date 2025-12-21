from talon import Module, actions, app

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
		if pattern:
			actions.user.insert_snippet(pattern)

	def fire_chicken_programming_get_pattern() -> str:
		"""Gets the specified programming pattern"""
		return pattern

	def fire_chicken_programming_save_from(text: str):
		"""Save the programming pattern in the text"""
		pattern = actions.user.fire_chicken_programming_find_pattern(text)
		app.notify(pattern)
		actions.user.fire_chicken_programming_save_pattern(pattern)

	def fire_chicken_programming_find_pattern(text: str) -> str:
		"""Finds the most prominent pattern in the text"""
		best_pattern = ""
		best_coverage = 0
		for i in range(len(text)):
			for j in range(i+1, len(text)):
				sequence = text[i:j]
				coverage = len(sequence)
				num_occurrences = text.count(sequence)
				if num_occurrences > 1 and coverage > best_coverage:
					best_coverage = coverage
					best_pattern = sequence
		return best_pattern