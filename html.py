from talon import Module, actions

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