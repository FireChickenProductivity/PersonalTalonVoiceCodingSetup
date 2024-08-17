write <user.prose>: 
    user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")
    insert(". ")

quest <user.prose>: 
    user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")
    insert("? ")
    
shout <user.prose>: 
    user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")
    insert("! ")
