code.language: /[a-z]+/i
-
gifting: 
    edit.line_end()
    insert(' = ')

back {user.snippet}:
    key(end enter backspace)
    user.insert_snippet_by_name_with_stop_at_end(snippet)

start {user.snippet}:
    key(end enter)
    user.insert_snippet_by_name_with_stop_at_end(snippet)