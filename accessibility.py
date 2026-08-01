from talon import Module, actions, ui

from contextlib import suppress

mod = Module()

@mod.action_class
class Actions:
	def fire_chicken_get_file_text_through_accessibility() -> tuple[str, str] | None:
		"""Tries to get the text of the current text area through accessibility. Returns None on no text field or no active window. Throws a RuntimeError in response to internal errors such as accessibility not being implemented on the platform"""
		try:
			win = ui.active_window()
		except Exception as ex:
			return None
		try:
			element = ui.active_app().element
			with suppress(Exception):
				element.AXEnhancedUserInterface = True
			for item in win.children.find():
				if role := getattr(item, "AXRole", None):
					if role == "AXTextArea":
						if getattr(item, "AXFocused"):
							total_text = getattr(item, "AXValue", "")
							selected_range = getattr(item, "AXSelectedTextRange", None)
							if selected_range is None or not total_text:
								return None
							start, end = selected_range.left, selected_range.right
							if start != end:
								return "", ""
							return total_text[:start], total_text[start:]
		except Exception as ex:
			raise RuntimeError("Something went wrong trying to use accessibility!") from ex
		return None
	
	def fire_chicken_get_file_text() -> tuple[str, str] | None:
		"""Get the current file text"""
		try:
			text_obtained_through_accessibility = actions.user.fire_chicken_get_file_text_through_accessibility()
			text_before, text_after = text_obtained_through_accessibility
		except Exception as ex:
			text_before = actions.user.generic_programming_compute_proceeding_text()
			text_after = actions.user.generic_programming_compute_following_text()
		return text_before, text_after