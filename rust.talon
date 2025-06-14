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
command line arguments: user.fire_chicken_insert_around_cursor("let ", ": Vec<String> = env::args().collect();")

testy:
	user.fire_chicken_insert_around_cursor("#[test]\nfn ", "()")
newt: user.fire_chicken_insert_around_cursor("::new(", ")")
arc clone: user.fire_chicken_insert_around_cursor("Arc::clone(", ")")
arc mutex: user.fire_chicken_insert_around_cursor("Arc::new(Mutex::new(", "))")