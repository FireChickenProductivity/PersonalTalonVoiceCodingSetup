from talon import Module, actions, ui, speech_system, cron, Context

from contextlib import suppress

mod = Module()

auto_run_completion: bool = False
old_text_before: str = ""
old_text_after: str = ""

@mod.action_class
class Actions:
	def fire_chicken_get_code_completion_using_file(max_context: int, amount_to_generate: int):
		"""Get code completion using file text"""
		global old_text_after, old_text_before
		actions.user.ollama_file_rpc_clear_completion_options()
		model = "codegemma:2b-code"
		text_before, text_after = actions.user.fire_chicken_get_file_text()
		if old_text_after == text_after and old_text_before == text_before:
			return 
		if len(text_before) > max_context:
			text_before = text_before[len(text_before) - max_context:]
		text_after = text_after[:max_context]
		actions.user.ollama_file_rpc_prompt_for_code_completion_with_model(
			model,
			text_before,
			text_after,
			amount_to_generate
		)
		old_text_after = text_after
		old_text_before = text_before

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

	def fire_chicken_set_auto_run_completion(value: bool):
		""""""
		global auto_run_completion
		auto_run_completion = value

	def fire_chicken_should_run_autocomplete() -> bool:
		""""""
		return False

context_vscode_editor = Context()
context_vscode_editor.matches = r"""
app: vscode
and win.title: /focus:\[Text Editor\]/
"""
@context_vscode_editor.action_class("user")
class VscodeEditorActions:
	def fire_chicken_should_run_autocomplete() -> bool:
		""""""
		return True

request_job = None
def request_completion(args):
	global request_job
	if not auto_run_completion or not actions.user.fire_chicken_should_run_autocomplete():
		return 
	if request_job is not None:
		cron.cancel(request_job)
	request_job = cron.after('2s', lambda: actions.user.fire_chicken_get_code_completion_using_file(300, 10))
	

speech_system.register("post:phrase", request_completion)