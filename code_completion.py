from talon import Module, actions, ui

from contextlib import suppress

mod = Module()

@mod.action_class
class Actions:
	def fire_chicken_get_code_completion_using_file(max_context: int, amount_to_generate: int):
		"""Get code completion using file text"""
		actions.user.ollama_file_rpc_clear_completion_options()
		model = "codegemma:2b-code"
		text_obtained_through_accessibility = get_file_text_through_accessibility()
		if text_obtained_through_accessibility is not None:
			text_before, text_after = text_obtained_through_accessibility
		else:
			text_before = actions.user.generic_programming_compute_proceeding_text()
			text_after = actions.user.generic_programming_compute_following_text()
		if len(text_before) > max_context:
			text_before = text_before[len(text_before) - max_context:]
		text_after = text_after[:max_context]
		actions.user.ollama_file_rpc_prompt_for_code_completion_with_model(
			model,
			text_before,
			text_after,
			amount_to_generate
		)

	def fire_chicken_use_code_completion_option(option: int):
		"""Paste the specified code completion option"""
		with suppress(Exception):
			text = actions.user.ollama_file_rpc_get_completion_options()[option-1]
			actions.user.paste(text.strip())
			actions.user.ollama_file_rpc_clear_completion_options()

	def fire_chicken_use_code_completion_option_line(option: int):
		"""Accept the current line completion"""
		with suppress(Exception):
			text = actions.user.ollama_file_rpc_get_completion_options()[option-1].strip()
			line = text.split("\n")[0]
			actions.user.paste(line.strip())
			actions.user.ollama_file_rpc_clear_completion_options()
			actions.user.fire_chicken_get_code_completion_using_file(300, 128)

def get_file_text_through_accessibility() -> tuple[str, str] | None:
	try:
		win = ui.active_window()
	except Exception as ex:
		return None
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
	return None

