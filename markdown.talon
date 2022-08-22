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
