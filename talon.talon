tag: user.talon
-
state user: 'user.'

header (end|ending|finished|finish|done):
    key(enter)
    insert('-')
    key(enter)

(keypress|keystroke) <user.keys>$: user.talon_programming_insert_keypress(keys)
(keypress|keystroke) <user.keys> over: user.talon_programming_insert_keypress(keys)

[action|act] <user.talon_programming_standard_actions>:
    insert(talon_programming_standard_actions)
    insert('()')
    edit.left()
insert:
    insert('insert')
    insert('()')
    edit.left()
