mode: command
and not tag: user.exam_mode
-
git fetch main:
    insert('git checkout main')
    key(enter)
    insert('git fetch')
    key(enter)
    sleep(3s)
    insert('git status')
    key(enter)
    insert('git pull')
    key(enter)

git fetch remote clipboard:
    insert('git checkout main')
    key(enter)
    insert('git fetch')
    key(enter)
    sleep(3s)
    insert('git fetch origin ')
    edit.paste()
    insert(':')
    edit.paste()
    key(enter)
    sleep(2s)
    insert('git checkout ')
    edit.paste()
    key(enter)

git checkout main:
    insert('git checkout main')
    key(enter)

git checkout: insert('git checkout ')

git checkout clipboard:
    insert('git checkout ')
    edit.paste()
    key(enter)

git (fetching|fetch):
    insert('git fetch')
    key(enter)

git (pulling|pull): insert('git pull')

git obtain changes from main: insert('git pull origin main')

git new branch: insert('git checkout -b ')

git new commit|git commit: 
    insert('git commit -a -m ')
    user.fire_chicken_insert_around_cursor("'", "'")

commit <user.text>$: 
    insert('git commit -a -m \'\'')
    key('left')
    user.fire_chicken_auto_generated_command_action_insert_formatted_text(user.text_1, 'capitalized lower', ' ')

git push changes: 'git push'