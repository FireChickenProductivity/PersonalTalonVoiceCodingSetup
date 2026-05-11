code.language: sql
-
create table: 'CREATE TABLE '
snip table:
    user.chicken_notes_display_by_name("sql table creation")
    user.insert_snippet("CREATE TABLE $1 (\n    $0\n)")
snip insert:
    user.insert_snippet("INSERT INTO $1 ($2) VALUES ($0)")
varchar: 
    insert(' VARCHAR')
    user.fire_chicken_insert_around_cursor('(', ')')
natural join: ' NATURAL JOIN '
integer: ' INTEGER'
primary key:
    insert('PRIMARY KEY ')
    user.fire_chicken_insert_around_cursor('(', ')')
foreign key:
    insert('FOREIGN KEY ')
    user.fire_chicken_insert_around_cursor('(', ')')
references:
    insert(' REFERENCES ')
insert into: 'INSERT INTO '
values:
    insert(' VALUES ')
    user.fire_chicken_insert_around_cursor('(', ')')
delete from: 'DELETE FROM '