code.language: rust
-

^(fun|function) <user.text>$:
	insert("fn ")
	user.fire_chicken_insert_with_snake_case(text)
	insert("(")

print: user.fire_chicken_insert_around_cursor('println!("', '");')

allow <user.text>$:
	insert('let ')
	user.fire_chicken_insert_with_snake_case(text)
	user.fire_chicken_insert_around_cursor(" = ", ";")
changeling <user.text>$:
	insert('let mut ')
	user.fire_chicken_insert_with_snake_case(text)
	user.fire_chicken_insert_around_cursor(" = ", ";")

scope: "::"
stand: "std::"
stew: "String::new()"
strum: user.fire_chicken_insert_around_cursor('String::from(', ')')
pub: "pub "
collect: ".collect()"