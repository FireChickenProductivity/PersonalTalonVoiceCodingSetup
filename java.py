from talon import actions, Module, Context
from .styles import * 

module = Module()

@module.capture(rule = '(pro|pry|pub)')
def java_programming_access_modifier(m) -> str:
    word = m[0]
    if word == 'pub':
        return 'public '
    elif word == 'pry':
        return 'private '
    elif word == 'pro':
        return 'protected '

@module.capture(rule = '<user.java_programming_access_modifier>|prose|prize|pubs')
def java_programming_function_access_modifier(m) -> str:
    word = m[0]
    if word == 'prose':
        return 'protected static '
    elif word == 'prize':
        return 'private static '
    elif word == 'pubs':
        return 'public static '
    else:
        return m.java_programming_access_modifier


@module.action_class
class Actions:
    def java_programming_build_new():
        '''Given a data type and variable name, produces new assignment'''
        current_line = actions.user.generic_programming_get_comma_separated_line_ignoring_standard_separators()
        if len(current_line) != 2:
            return 
        data_type = current_line[0]
        variable_name = current_line[1]
        actions.insert(f'{data_type} {variable_name}{apply_spacing_setting_to(assignment_style, "=")}'
            f'new {data_type}{get_object_parentheses().get_text()};')
        for iteration in range(2):
            actions.edit.left() 
    def java_programming_system_out_method(name: str):
        '''Inserts the specified system out method'''
        container = get_function_call_parentheses()
        actions.insert(f'System.out.{name}{container.get_text()};')
        actions.edit.left()
        container.enter_from_right()
    def java_programming_indicate_superclass(name: str):
        '''Inserts text indicating the superclass'''
        actions.insert('extends ')
        actions.user.insert_formatted(name, 'hammer')

context = Context()
context.matches = r'''
tag: user.java
'''

@context.action_class('user')
class UserActions:
    def fire_chicken_code_self_reference_constructor_arguments():
        '''Java version of the self referencing action'''
        actions.user.generic_programming_self_reference_constructor_arguments(self_reference_argument)


def self_reference_argument(argument):
    actions.user.fire_chicken_programming_self_reference_argument_given_strategy_to_find_its_variable(argument, get_argument_variable, statement_ending = ';')

def get_argument_variable(argument):
    stripped_argument = argument.strip()
    space_separated_argument_parts = actions.user.generic_programming_split_string_ignoring_standard_containers(stripped_argument, ' ')
    print(space_separated_argument_parts)
    #to deal with multiple spaces creating empty splits, return 
    #the first part after the initial part (the datatype) that is not empty
    for i in range(1, len(space_separated_argument_parts)):
        part = space_separated_argument_parts[i]
        if part != '':
            return part

context.lists['user.fire_chicken_method_snippets'] = {
    'absolute' : 'abs',
    'Arc cos' : 'acos',
    'add' : 'add',
    'add All' : 'addAll',
    'arc sine' : 'asin',
    'arc tan' : 'atan',
    'arc tan two' : 'atan2',
    'cube root' : 'cbrt',
    'ceiling' : 'ceil',
    'char At' : 'charAt',
    'chars' : 'chars',
    'clear' : 'clear',
    'clone' : 'clone',
    'close' : 'close',
    'code Point At' : 'codePointAt',
    'code Point Before' : 'codePointBefore',
    'code Point Count' : 'codePointCount',
    'code Points' : 'codePoints',
    'compare To' : 'compareTo',
    'compare To Ignore Case' : 'compareToIgnoreCase',
    'comparing By Key' : 'comparingByKey',
    'comparing By Value' : 'comparingByValue',
    'compute' : 'compute',
    'compute If Absent' : 'computeIfAbsent',
    'compute If Present' : 'computeIfPresent',
    'concat' : 'concat',
    'contains' : 'contains',
    'contains All' : 'containsAll',
    'contains Key' : 'containsKey',
    'contains Value' : 'containsValue',
    'content Equals' : 'contentEquals',
    'copy Of' : 'copyOf',
    'copy Sign' : 'copySign',
    'copy Value Of' : 'copyValueOf',
    'cosine' : 'cos',
    'cosh' : 'cosh',
    'delimiter' : 'delimiter',
    'describe Constable' : 'describeConstable',
    'doubles' : 'doubles',
    'element' : 'element',
    'empty' : 'empty',
    'ends With' : 'endsWith',
    'ensure Capacity' : 'ensureCapacity',
    'entry' : 'entry',
    'entry Set' : 'entrySet',
    'equals' : 'equals',
    'equals Ignore Case' : 'equalsIgnoreCase',
    'exponent' : 'exp',
    'exponent minus ' : 'expm1',
    'filter' : 'filter',
    'finalize' : 'finalize',
    'find All' : 'findAll',
    'find In Line' : 'findInLine',
    'find Within Horizon' : 'findWithinHorizon',
    'flat Map' : 'flatMap',
    'floor' : 'floor',
    'for Each' : 'forEach',
    'for Each Remaining' : 'forEachRemaining',
    'format' : 'format',
    'formatted' : 'formatted',
    'get' : 'get',
    'get Bytes' : 'getBytes',
    'get Chars' : 'getChars',
    'get Class' : 'getClass',
    'get Exponent' : 'getExponent',
    'get Key' : 'getKey',
    'get Or Default' : 'getOrDefault',
    'get Value' : 'getValue',
    'hash Code' : 'hashCode',
    'has Next' : 'hasNext',
    'has Next Big Decimal' : 'hasNextBigDecimal',
    'has Next Big Integer' : 'hasNextBigInteger',
    'has Next Boolean' : 'hasNextBoolean',
    'has Next Byte' : 'hasNextByte',
    'has Next Double' : 'hasNextDouble',
    'has Next Float' : 'hasNextFloat',
    'has Next Int' : 'hasNextInt',
    'has Next Line' : 'hasNextLine',
    'has Next Long' : 'hasNextLong',
    'has Next Short' : 'hasNextShort',
    'hypotenuse' : 'hypot',
    'I triple E remainder' : 'IEEEremainder',
    'if Present' : 'ifPresent',
    'if Present Or Else' : 'ifPresentOrElse',
    'indent' : 'indent',
    'index Of' : 'indexOf',
    'intern' : 'intern',
    'ints' : 'ints',
    'I o Exception' : 'ioException',
    'is Blank' : 'isBlank',
    'is Empty' : 'isEmpty',
    'is Present' : 'isPresent',
    'iterator' : 'iterator',
    'join' : 'join',
    'key Set' : 'keySet',
    'last Index Of' : 'lastIndexOf',
    'length' : 'length',
    'lines' : 'lines',
    'list Iterator' : 'listIterator',
    'locale' : 'locale',
    'log' : 'log',
    'Log ten' : 'log10',
    'Log one p' : 'log1p',
    'longs' : 'longs',
    'map' : 'map',
    'match' : 'match',
    'matches' : 'matches',
    'max' : 'max',
    'merge' : 'merge',
    'min' : 'min',
    'next' : 'next',
    'next After' : 'nextAfter',
    'next Big Decimal' : 'nextBigDecimal',
    'next Big Integer' : 'nextBigInteger',
    'next Boolean' : 'nextBoolean',
    'next Byte' : 'nextByte',
    'next Bytes' : 'nextBytes',
    'next Double' : 'nextDouble',
    'next Float' : 'nextFloat',
    'next Gaussian' : 'nextGaussian',
    'next Int' : 'nextInt',
    'next Line' : 'nextLine',
    'next Long' : 'nextLong',
    'next Short' : 'nextShort',
    'next Up' : 'nextUp',
    'notify' : 'notify',
    'notify All' : 'notifyAll',
    'of' : 'of',
    'of Entries' : 'ofEntries',
    'offer' : 'offer',
    'offset By Code Points' : 'offsetByCodePoints',
    'of Nullable' : 'ofNullable',
    'or' : 'or',
    'or Else' : 'orElse',
    'or Else Get' : 'orElseGet',
    'or Else Throw' : 'orElseThrow',
    'parallel Stream' : 'parallelStream',
    'peek' : 'peek',
    'poll' : 'poll',
    'pow' : 'pow',
    'put' : 'put',
    'put All' : 'putAll',
    'put If Absent' : 'putIfAbsent',
    'radix' : 'radix',
    'random' : 'random',
    'region Matches' : 'regionMatches',
    'remove' : 'remove',
    'remove All' : 'removeAll',
    'remove If' : 'removeIf',
    'remove Range' : 'removeRange',
    'repeat' : 'repeat',
    'replace' : 'replace',
    'replace All' : 'replaceAll',
    'replace First' : 'replaceFirst',
    'reset' : 'reset',
    'resolve Constant Descriptor' : 'resolveConstantDesc',
    'retain All' : 'retainAll',
    'R int' : 'rint',
    'round' : 'round',
    'set' : 'set',
    'set Seed' : 'setSeed',
    'set Value' : 'setValue',
    'signum' : 'signum',
    'sine' : 'sin',
    'Sine h' : 'sinh',
    'size' : 'size',
    'skip' : 'skip',
    'sort' : 'sort',
    'split' : 'split',
    'spliterator' : 'spliterator',
    'square root' : 'sqrt',
    'starts With' : 'startsWith',
    'stream' : 'stream',
    'strip' : 'strip',
    'strip Indent' : 'stripIndent',
    'strip Leading' : 'stripLeading',
    'strip Trailing' : 'stripTrailing',
    'sub List' : 'subList',
    'sub Sequence' : 'subSequence',
    'substring' : 'substring',
    'tan' : 'tan',
    'Tan h' : 'tanh',
    'This object ' : 'This object ',
    'to Array' : 'toArray',
    'to Char Array' : 'toCharArray',
    'to Degrees' : 'toDegrees',
    'tokens' : 'tokens',
    'to Lower Case' : 'toLowerCase',
    'to Radians' : 'toRadians',
    'to String' : 'toString',
    'to Upper Case' : 'toUpperCase',
    'transform' : 'transform',
    'translate Escapes' : 'translateEscapes',
    'trim' : 'trim',
    'trim To Size' : 'trimToSize',
    'u l p' : 'ulp',
    'use Delimiter' : 'useDelimiter',
    'use Locale' : 'useLocale',
    'use Radix' : 'useRadix',
    'value Of' : 'valueOf',
    'values' : 'values',
    'wait' : 'wait',
}
