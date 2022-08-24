tag: user.markdown
-
header <number_small>: 
    insert('#')
    repeat(number_small - 1)
    insert(' ')
    #    insert('<h></h>')
#    key(left:1)
#    insert(number_small)
#    key(left:5)
#    insert(number_small)
#    key(right)

empty checkbox: '- [ ] '
full checkbox: '- [x] '

image: 
    insert('![]()')
    edit.left()
    repeat(2)

link:
    insert('[]()')
    edit.left()
    repeat(2)

emoji:
    user.fire_chicken_insert_around_cursor(':', ':')

italics: user.fire_chicken_insert_around_cursor('*', '*')
bold: user.fire_chicken_insert_around_cursor('**', '**')
