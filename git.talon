mode: command
and not mode: user.exam_mode
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
