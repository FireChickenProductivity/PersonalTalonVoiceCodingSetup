tag: user.java
-
tag(): user.c_style_programming
tag(): user.fire_chicken_programming_self_reference_constructor
tag(): user.fire_chicken_snippets
tag(): user.fire_chicken_class_command
tag(): user.fire_chicken_programming_math_methods

System: 'System.'
system out: 'System.out.'
system in: 'System.in'
Math: 'Math'

console print line:
    user.java_programming_system_out_method('println')
console print:
    user.java_programming_system_out_method('print')
console print f:
    user.java_programming_system_out_method('printf')

state continue: 'continue;'
    

main method:
    insert('public static void main')
    user.generic_programming_insert_function_call_parentheses()
    user.generic_programming_enter_function_call_parentheses_from_right()
    insert('String')
    user.generic_programming_insert_empty_declaration_squares()
    insert(' args')

build new: user.java_programming_build_new()

<user.java_programming_function_access_modifier>:
    insert(java_programming_function_access_modifier)
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

import <user.fire_chicken_programming_package>: user.fire_chicken_programming_import_package(fire_chicken_programming_package)
from <user.fire_chicken_programming_package> import <user.fire_chicken_programming_class>: 
    user.fire_chicken_programming_from_import(fire_chicken_programming_package, fire_chicken_programming_class)
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
state (implements|imp|imply): ' implements '
state extends: ' extends '

op ray: user.generic_programming_insert_empty_declaration_squares()


#Short for declare
Claire {user.code_type} <user.prose>$:
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
    user.generic_programming_insert_assignment()
    insert(';')
    edit.left()
Claire {user.code_type} <user.prose> over:
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
    user.generic_programming_insert_assignment()
    insert(';')
    edit.left()

param {user.code_type} <user.prose>$:
    user.generic_programming_insert_comma_separator()
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
param {user.code_type} <user.prose> over:
    user.generic_programming_insert_comma_separator()
    insert(user.code_type + ' ')
    user.insert_formatted(prose, 'camel')
    
    

vary <user.prose>$:
    insert('var ')
    user.insert_formatted(prose, 'camel')
    user.generic_programming_insert_assignment()
    insert(';')
    edit.left()
vary <user.prose> over:
    insert('var ')
    user.insert_formatted(prose, 'camel')
    user.generic_programming_insert_assignment()
    insert(';')
    edit.left()

pristine <user.prose>$:
    insert('new ')
    user.insert_formatted(prose, 'hammer')
    user.generic_programming_insert_object_parentheses()
    user.generic_programming_enter_object_parentheses_from_right()
pristine <user.prose> over:
    insert('new ')
    user.insert_formatted(prose, 'hammer')
    user.generic_programming_insert_object_parentheses()
    user.generic_programming_enter_object_parentheses_from_right()

new <user.fire_chicken_programming_class>:
    insert('new ')
    insert(fire_chicken_programming_class)
    user.generic_programming_insert_object_parentheses()
    user.generic_programming_enter_object_parentheses_from_right()

new plain <user.fire_chicken_programming_generic_class>:
    insert('new ')
    insert(fire_chicken_programming_generic_class)
    user.fire_chicken_programming_code_empty_generics_operator()
    user.generic_programming_insert_object_parentheses()
    user.generic_programming_enter_object_parentheses_from_right()

<user.fire_chicken_programming_generic_class> plain <user.fire_chicken_programming_class>+:
    insert(fire_chicken_programming_generic_class)
    user.fire_chicken_programming_code_generic_type_info(fire_chicken_programming_class_list)


(is a|parent) <user.prose>$: user.java_programming_indicate_superclass(prose)
(is a|parent) <user.prose> over: user.java_programming_indicate_superclass(prose)

fulfills <user.prose>$: user.java_programming_indicate_implements(prose)
fulfills <user.prose> over: user.java_programming_indicate_implements(prose)
