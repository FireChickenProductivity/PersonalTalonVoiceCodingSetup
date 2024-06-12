from talon import Module, actions
from typing import List

module = Module()

@module.action_class
class Actions:
    def fire_chicken_programming_html_insert_start_template():
        """Inserts a template for the start of an HTML file"""
        actions.insert(r'''<html>
<head>
<title>TITLE</title>
</head>

<body>
    
</body>
</html>''')
        actions.edit.line_start()
        actions.edit.delete()
    
    def fire_chicken_programming_html_insert_version_5_start():
        """Inserts the start of an HTML5 document"""
        actions.insert("<!DOCTYPE html>\n")

    def fire_chicken_programming_html_insert_element(name: str):
        """Inserts the tags for an HTML element"""
        element_text = compute_multiline_element(name)
        actions.insert(element_text)
        actions.edit.line_up()
    
    def fire_chicken_programming_html_insert_single_line_element(name: str):
        """Inserts the tags for a single line HTML element"""
        element_text = compute_single_line_element(name)
        actions.insert(element_text)
        element_ending = compute_element_end(name)
        for character in element_ending:
            actions.edit.left()

    def fire_chicken_programming_html_insert_single_line_element_from_list(characters: List[str]):
        """Inserts the tags for a single line HTML element"""
        name = "".join(characters)
        actions.user.fire_chicken_programming_html_insert_single_line_element(name)
        
    def fire_chicken_programming_html_insert_header(header_number: int):
        """Inserts HTML header tags"""
        name = f"h{header_number}"
        actions.user.fire_chicken_programming_html_insert_single_line_element(name)
    

def compute_element_start(name):
    return f"<{name}>"

def compute_element_end(name):
    return f"</{name}>"

def compute_single_line_element(name):
    return f"<{name}></{name}>"

def compute_multiline_element(name):
    return f"<{name}>\n\n</{name}>"