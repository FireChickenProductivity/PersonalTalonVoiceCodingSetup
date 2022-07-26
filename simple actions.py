from talon import Module, actions

mod = Module()

@mod.capture (rule = '<user.letter>|<digits>|<user.symbol_key>|space')
def spelling_out_symbol(symbol: str) -> str:
    '''A symbol letter or digit'''
    if symbol[0] == 'space':
        return ' '
    return str(symbol[0])

@mod.action_class
class Actions:
    def press_keys_repeatedly(key_presses: str, number: str):
        """Repeats the key presses the number of times specified by the string integer number"""
        actions.key(key_presses + ':' + number)
    def press_keys_repeatedly_using_integer_argumet (key_presses: str, number: int):
        '''Repeats the key presses the number of times specified'''
        actions.key(key_presses + ':' + str(number))
    def simple_action_search_next(target: str):
        '''Searches for the desired text and goes to the left of it'''
        actions.key('right')
        actions.edit.find(target)
        actions.key('escape')
        actions.key('left')
    def simple_action_search_next_multiple(target: list):
        '''Searches for the desired text given in list format and goes to the left of it'''
        actual_text_to_search_for = ''
        for element in target:
            actual_text_to_search_for += element

        actions.user.simple_action_search_next(actual_text_to_search_for)

        

