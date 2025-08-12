from talon import Module, actions, Context

from typing import TypedDict, Callable, Optional

Operator = str | Callable[[], None]

class Methods(TypedDict, total=False):
	LANGUAGE: str

	LIST_ADD: Operator
	LIST_POP: Operator
	LIST_CHANGE: Operator
	LIST_REMOVE: Operator
	LIST_GET: Operator
	LIST_NEW: Operator

	MAP_ADD: Operator
	MAP_CHANGE: Operator
	MAP_REMOVE: Operator
	MAP_GET: Operator
	MAP_CONTAINS: Operator
	MAP_NEW: Operator

	SET_ADD: Operator
	SET_REMOVE: Operator
	SET_CONTAINS: Operator
	SET_NEW: Operator

methods: Optional[Methods] = None

module = Module()

module.list('fire_chicken_programming_methods', desc='Active language list of programming method names')

@module.action_class
class Actions:
	def fire_chicken_methods_update():
		'''Updates the current methods object based on the active programming language'''
		pass

	def fire_chicken_methods_should_update(language: str):
		'''Checks if the methods object should be updated based on the active programming language'''
		return not methods or methods['LANGUAGE'] != language

	def fire_chicken_methods_get() -> Optional[Methods]:
		'''Returns the current methods object'''
		return methods

	def fire_chicken_methods_insert(name: str):
		'''Inserts a method with the specified name'''
		actions.user.fire_chicken_methods_update()
			
		if methods is None:
			raise ValueError("Methods object is not initialized.")
		if name not in methods:
			raise ValueError(f"Method '{name}' not found in methods object.")
		method = methods[name]
		if callable(method):
			method()
		else:
			actions.user.fire_chicken_code_object_accessor()
			actions.insert(method)
			actions.user.fire_chicken_insert_around_cursor("(", ")")

javascript_context = Context()
javascript_context.matches = r'''
code.language: javascript
code.language: typescript
'''

def code_generic_subscript():
	actions.user.fire_chicken_insert_around_cursor("[", "]")

def code_generic_subscript_update():
	actions.user.insert_snippet("[$1] = $0")
	

@javascript_context.action_class("user")
class JavascriptActions:
	def fire_chicken_methods_update():
		if actions.user.fire_chicken_methods_should_update('javascript'):
			global methods
			methods = Methods(
				LANGUAGE = 'javascript',
				LIST_ADD = 'push',
				LIST_POP = 'pop',
				LIST_CHANGE = code_generic_subscript_update,
				LIST_REMOVE = lambda: actions.user.fire_chicken_insert_around_cursor('.splice(', ', 1)'),
				LIST_GET = code_generic_subscript,
				LIST_NEW = lambda: actions.user.fire_chicken_insert_around_cursor('[', ']'), 

				MAP_ADD = 'set',
				MAP_CHANGE = 'set',
				MAP_REMOVE = 'delete',
				MAP_GET = 'get',
				MAP_CONTAINS = 'has',
				MAP_NEW = lambda: actions.user.fire_chicken_insert_around_cursor('new Map(', ')'),

				SET_ADD = 'add',
				SET_REMOVE = 'delete',
				SET_CONTAINS = 'has',
				SET_NEW = lambda: actions.user.fire_chicken_insert_around_cursor('new Set(', ')'),

			)

python_context = Context()
python_context.matches = r'''
code.language: python
'''

@python_context.action_class("user")
class PythonActions:
	def fire_chicken_methods_update():
		if actions.user.fire_chicken_methods_should_update('python'):
			global methods
			methods = Methods(
				LANGUAGE = 'python',
				LIST_ADD = 'append',
				LIST_POP = 'pop',
				LIST_CHANGE = code_generic_subscript_update,
				LIST_REMOVE = 'pop',
				LIST_GET = code_generic_subscript,
				LIST_NEW = lambda: actions.user.fire_chicken_insert_around_cursor('[', ']'),

				MAP_ADD = code_generic_subscript_update,
				MAP_CHANGE = code_generic_subscript_update,
				MAP_REMOVE = 'pop',
				MAP_GET = code_generic_subscript,
				MAP_NEW = lambda: actions.user.fire_chicken_insert_around_cursor('{', '}'),

				SET_ADD = 'add',
				SET_REMOVE = 'remove',
				SET_NEW = lambda: actions.user.fire_chicken_insert_around_cursor('set(', ')'),
			)

cpp_context = Context()
cpp_context.matches = r'''
code.language: cpp
code.language: c
'''
@cpp_context.action_class("user")
class CppActions:
	def fire_chicken_methods_update():
		language = 'c++'
		if actions.user.fire_chicken_methods_should_update(language):
			global methods
			methods = Methods(
				LANGUAGE = language,
				LIST_ADD = 'emplace_back',
				LIST_POP = 'pop_back',
				LIST_CHANGE = lambda: actions.user.snippet_insert(".at($1) = $0"),
				LIST_REMOVE = 'erase',
				LIST_GET = 'at',

				MAP_ADD = 'emplace',
				MAP_CHANGE = 'emplace',
				MAP_REMOVE = 'erase',
				MAP_GET = 'at',
				MAP_CONTAINS = lambda: actions.user.fire_chicken_insert_around_cursor('.count(', ') != 0'),

				SET_ADD = 'insert',
				SET_REMOVE = 'erase',
				SET_CONTAINS = lambda: actions.user.fire_chicken_insert_around_cursor('.count(', ') != 0'),
			)