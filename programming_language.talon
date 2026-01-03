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

max equals: user.generic_programming_max_equals()
min equals: user.generic_programming_min_equals()

sibling:
    user.generic_programming_insert_analogous_from_prior_line()