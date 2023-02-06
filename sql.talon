tag: user.sql
-
create table: 'CREATE TABLE '
varchar: 
    insert(' VARCHAR')
    user.fire_chicken_insert_around_cursor('(', ')')
natural join: ' NATURAL JOIN '
integer: ' INTEGER'
primary key:
    insert('PRIMARY KEY ')
    user.fire_chicken_insert_around_cursor('(', ')')
insert into: 'INSERT INTO '
values:
    insert(' VALUES ')
    user.fire_chicken_insert_around_cursor('(', ')')
delete from: 'DELETE FROM '
