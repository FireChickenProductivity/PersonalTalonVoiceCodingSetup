app: vscode
tag: user.python
-
debug <user.cursorless_target>:
    insert("print('")
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert("', ")
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert(")")
