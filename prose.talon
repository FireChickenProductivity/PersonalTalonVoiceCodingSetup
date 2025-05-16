symbol {user.symbol_key}: 
    insert(symbol_key)

quest <user.prose>: 
    user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")
    insert("? ")
    
shout <user.prose>: 
    user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")
    insert("! ")
