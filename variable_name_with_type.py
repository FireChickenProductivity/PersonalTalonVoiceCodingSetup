from talon import Module, actions

module = Module()
@module.action_class
class Actions:
	def fire_chicken_insert_word_in_uppercase_followed_by_in_lowercase(word: str):
		"""e.g. List list"""
		text = word.capitalize() + " " + word.lower()
		actions.insert(text)

		