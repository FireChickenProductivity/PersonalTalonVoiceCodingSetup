from talon import Context, actions

context = Context()
context.matches = r"""
app.name: Visual Studio Code
"""

@context.action_class("code")
class Actions:
    def language():
        file_extension = actions.win.file_ext()
        if file_extension == ".html":
            return "html"
        else:
            return actions.next()