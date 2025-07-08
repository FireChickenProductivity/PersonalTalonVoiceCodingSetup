code.language: c
code.language: cpp
-

namespace stand: "using namespace std;\n"

heading: '#include "'
helmet: user.fire_chicken_insert_around_cursor('#include <', '>')

output: " << "
line put: insert(' << "\\n";')
couch|c out: 'cout'
sofa: 'std::cout << '
auto: "auto "
scope|scoping: "::"
adress|reference: " &"
dereference: "*"
pointer: " *"
const|state const: "const "
main function: "int main(int argc, char* argv[])"
stand: "std::"
typedef: 'typedef '
null pointer: 'nullptr'

^header guard <user.text>$: 
    name = text + ' h'
    insert('#ifndef ')
    user.fire_chicken_insert_with_upper_snake_case(name)
    insert('\n#define ')
    user.fire_chicken_insert_with_upper_snake_case(name)
    insert('\n\n\n\n')
    insert('#endif')
    key(up:2)

private:
    insert('private:\n\t')
public:
    insert('public:\n\t')

(const|constant) (exp|expression): 'constexpr '
bowl: "bool"
bowler: "bool "
strung: "std::string "
size type: "size_t "

classy <user.text>$: 
    insert('class ')
    user.fire_chicken_insert_with_pascal_case(text)
    insert(' {\n')
    key(down end ; up tab)

classing <user.text>$:
    user.fire_chicken_insert_with_pascal_case(text)
    insert(' ')

const: "const "

stirred <user.word>:
    insert('std::')
    insert(word)

stir ref: "const std::string &"

recompile:
    edit.save()
    user.vscode("workbench.action.terminal.focus")
    key(up:2 enter)
    key(up:2 enter)
    user.vscode("workbench.action.focusActiveEditorGroup")

template: 
    insert("template <typename >")
    edit.left()
    
van <user.text>$:
    insert("void ")
    user.fire_chicken_insert_formatted_text(text, 'camel')
    insert("(")

build size type:
    user.c_style_programming_make_count_for_loop_given_datatype("size_t")

build size:
    insert(".size()")
    user.c_style_programming_make_count_for_loop_given_datatype("size_t")

length <user.cursorless_target>:
    user.fire_chicken_cursorless_bring(cursorless_target)
    insert(".size()")

refer: " = &"