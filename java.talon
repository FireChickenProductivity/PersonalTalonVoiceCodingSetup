tag: user.java
-
tag(): user.c_style_programming
tag(): user.fire_chicken_programming_self_reference_constructor

System: 'System.'
system out: 'System.out.'
system in: 'System.in'

console print line:
    insert('System.out.println();')
    edit.left()
    edit.left()
console print:
    insert('System.out.print();')
    edit.left()
    edit.left()     

state continue: 'continue;'
    

main method: 'public static void main(String[] args)'
build new: user.java_programming_build_new()

<user.java_programming_function_access_modifier>:
    insert(java_programming_function_access_modifier )
<user.java_programming_function_access_modifier> <user.c_style_programming_type>:
    insert(java_programming_function_access_modifier + c_style_programming_type)
    insert(' ')
<user.java_programming_function_access_modifier> <user.c_style_programming_type> <user.prose>$:
    insert(java_programming_function_access_modifier + c_style_programming_type)
    insert(' ')
    user.insert_formatted(prose, 'camel')
<user.java_programming_function_access_modifier> <user.c_style_programming_type> <user.prose> over:
    insert(java_programming_function_access_modifier + c_style_programming_type)
    insert(' ')
    user.insert_formatted(prose, 'camel')

import arraylist: 'import java.util.ArrayList;'
import linked list: 'import java.util.LinkedList;'
import hashmap: 'import java.util.HashMap;'
import map: 'import java.util.Map;' 
import hash set: 'import java.util.HashSet;'
import tree set: 'import java.util.TreeSet;'
import linked hash set: 'import java.util.LinkedHashSet;'
import set: 'import java.util.Set;'

import scanner: 'import java.util.Scanner;'

import (util|utilities|utility): 'import java.util.*;'
import io: 'import java.io.*;'

state var: 'var '
state implements: 'implements '
state extends: 'extends '

op ray: user.generic_programming_insert_empty_declaration_squares()


#Short for declare
Claire {user.code_type} <user.prose>$:
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
    insert(' = ;')
    edit.left()
Claire {user.code_type} <user.prose> over:
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
    insert(' = ;')
    edit.left()

param {user.code_type} <user.prose>$:
    insert(', ')
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
param {user.code_type} <user.prose> over:
    insert(', ')
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
    
    

vary <user.prose>$:
    insert('var ')
    user.insert_formatted(prose, 'camel')
    insert(' = ;')
    edit.left()
vary <user.prose> over:
    insert('var ')
    user.insert_formatted(prose, 'camel')
    insert(' = ;')
    edit.left()

pristine <user.prose>$:
    insert('new ')
    user.insert_formatted(prose, 'hammer')
    insert('()')
    edit.left()
pristine <user.prose> over:
    insert('new ')
    user.insert_formatted(prose, 'hammer')
    insert('()')
    edit.left()
