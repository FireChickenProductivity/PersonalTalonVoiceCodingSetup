tag: user.talon
-
state user: 'user.'

header (end|ending|finished|finish|done):
    key(enter)
    insert('-')
    key(enter)

(keypress|keystroke) <user.keys>$: user.talon_programming_insert_keypress(keys)
(keypress|keystroke) <user.keys> over: user.talon_programming_insert_keypress(keys)
