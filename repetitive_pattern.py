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
		best_pattern = ""
		best_coverage = 0
		for i in range(len(text)):
			for j in range(i+1, len(text)):
				sequence = text[i:j]
				coverage = text.count(sequence)
				num_occurrences = 0
				if num_occurrences > 1 and coverage > best_coverage:
					best_pattern = sequence
		return best_pattern