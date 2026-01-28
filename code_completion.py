from talon import Module, actions

from contextlib import suppress

mod = Module()

@mod.action_class
class Actions:
	def fire_chicken_get_code_completion_using_file(max_context: int, amount_to_generate: int):
		"""Get code completion using file text"""
		actions.user.ollama_file_rpc_clear_completion_options()
		model = "codegemma:2b-code"
		text_before = actions.user.generic_programming_compute_proceeding_text()[:max_context]
		text_after = actions.user.generic_programming_compute_following_text()[:max_context]
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




