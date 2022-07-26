from talon import Module, Context, actions

module = Module()
context = Context()
context.matches = r'''
tag: user.javascript
'''

context.lists['user.fire_chicken_fast_functions'] = {
    'prompting' : 'prompt',
    'pieces' : '.forEach',
    'index of' : '.indexOf',
    'last index of' : '.lastIndexOf',
    'unshift' : '.unshift',
    'shifting' : '.shift', 
    'pushing' : '.push',
    'popping' : '.pop',
    'slicing' : '.slice',
    'logging' : 'console.log',
    'warning' : 'console.warn',
    'erring' : 'console.error',
    'object logging' : 'console.dir',
    'mapping' : '.map',
    'filtering' : '.filter',
    'everything' : '.every',
    'summing' : '.some',
    'sub stir' : '.substr',
    'sub string' : '.substring',
    'listening' : '.addEventListener',
    'Jason parse' : 'JSON.parse',
    'Jason string' : 'JSON.stringify',

    'writing' : 'document.writeln',
    'l i d' : 'document.getElementById',
    'l tag' : 'document.getElementByTagName',
    'l class' : 'document.getElementByClassName',
    'query all' : 'document.querySelectorAll',
    'querying' : 'document.querySelector',
    
}

@module.action_class
class Actions:
    def fire_chicken_insert_javascript_property(name: str):
        '''Insert specified JavaScript property declaration start'''
        actions.user.insert_formatted(name, 'camel')
        actions.insert(': ')
