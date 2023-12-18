code.language: talon
-
state user: 'user.'
packed|[act|action] paste:
    insert('user.')
    key(ctrl-v)
    insert('()')
    edit.left()

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
[app] notify:
    insert("app.notify")
    user.fire_chicken_insert_around_cursor('("', '")')

capture:
    user.fire_chicken_insert_around_cursor('<', '>')
    insert('user.')

(number|numb) small: 'number_small'