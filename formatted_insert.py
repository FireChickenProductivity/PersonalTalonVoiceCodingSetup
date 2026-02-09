from talon import Module, actions, settings

def camel_case_conversion_function(index, word):
    if index == 0:
        return word.lower()
    return word.capitalize()

def lowercase_conversion_function(index, word):
    return word.lower()

def uppercase_conversion_function(index, word):
    return word.upper()

def capitalized_conversion_function(index, word):
    return word.capitalize()

def format_text(text: str, new_separator: str, case_conversion_function):
    words = text.split()
    for index, word in enumerate(words):
        words[index] = case_conversion_function(index, word)
    new_text = new_separator.join(words)
    return new_text

def fire_chicken_format_text_with_came_case(text: str):
    return format_text(text, "", camel_case_conversion_function)

def fire_chicken_format_text_with_pascal_case(text: str):
    return format_text(text, "", capitalized_conversion_function)

def fire_chicken_format_text_with_snake_case(text: str):
    return format_text(text, "_", lowercase_conversion_function)

def fire_chicken_format_text_with_upper_snake_case(text: str):
    return format_text(text, "_", uppercase_conversion_function)

def get_conversion_function(name: str):
    if name == 'camel':
        return camel_case_conversion_function
    elif name == 'pascal':
        return capitalized_conversion_function
    elif name == 'lower':
        return lowercase_conversion_function
    elif name == 'upper':
        return uppercase_conversion_function

class Formatter:
    def __init__(self, case_conversion_function, separator = ""):
        self.case_conversion_function = case_conversion_function
        self.separator = separator

formatters = {
    'camel': Formatter(camel_case_conversion_function),
    'pascal': Formatter(capitalized_conversion_function),
    'lower': Formatter(lowercase_conversion_function),
    'upper': Formatter(uppercase_conversion_function),
    'snake': Formatter(lowercase_conversion_function, "_"),
    'upper snake': Formatter(uppercase_conversion_function, "_"),
}
aliases = {
    'hammer': 'pascal',
}

def format_text_using_formatter(text: str, formatter: Formatter):
    return format_text(text, formatter.separator, formatter.case_conversion_function)

module = Module()
@module.action_class
class Actions:
    def fire_chicken_insert_after(text: str):
        '''Insert text after the cursor'''
        actions.insert(text)
        move_left_for_each_character(text)
    def fire_chicken_insert_around_cursor(text_before_cursor: str, text_after_cursor: str):
        '''Inserts the first argument before the cursor and the second argument after'''
        actions.insert(text_before_cursor)
        actions.user.fire_chicken_insert_after(text_after_cursor)
    def fire_chicken_format_text(text: str, name: str):
        '''Format text with the given formatter'''
        name = aliases.get(name, name)
        formatter = formatters[name]
        new_text = format_text_using_formatter(text, formatter)
        return new_text
    def fire_chicken_insert_formatted_text(text: str, name: str):
        '''Insert the specified text with the specified formatter'''
        new_text = actions.user.fire_chicken_format_text(text, name)
        actions.insert(new_text)
    def fire_chicken_insert_with_snake_case(text: str):
        '''Insert the specified text with snake case'''
        actions.user.fire_chicken_insert_formatted_text(text, 'snake')
    def fire_chicken_insert_with_upper_snake_case(text: str):
        '''Insert the specified text with upper snake case'''
        actions.user.fire_chicken_insert_formatted_text(text, 'upper snake')
    def fire_chicken_insert_with_pascal_case(text: str):
        '''Insert the specified text with pascal case'''
        actions.user.fire_chicken_insert_formatted_text(text, 'pascal')
    def fire_chicken_insert_with_camel_case(text: str):
        '''Insert the specified text with camel case'''
        actions.user.fire_chicken_insert_formatted_text(text, 'camel')
    def fire_chicken_get_default_formatter() -> str:
        '''Returns the default formatter'''
        if formatter := settings.get("user.fire_chicken_default_variable_format"):
            return formatter
        return "camel"

def move_left_for_each_character(text: str):
    for i in range(len(text)):
        actions.edit.left()