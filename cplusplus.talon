code.language: c
-

namespace stand: "using namespace std;\n"

output: " << "
couch|c out: 'cout'
auto: "auto "
scope|scoping: "::"
adress|reference: " &"
dereference: "*"
pointer: " *"
const|state const: "const "
main function: "int main(int argc, char* argv[])"
stand: "std::"

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
standing: "std::string "

classy <user.text>$: 
    insert('class ')
    user.fire_chicken_insert_with_pascal_case(text)
    insert(' {\n')
    key(down end ; up tab)

const: "const "

stirred <user.word>:
    insert('std::')
    insert(word)

