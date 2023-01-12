from talon import Module

module = Module()
@module.capture(rule = 'ply')
def fire_chicken_cursorless_operator_prefix(m) -> str:
    '''A prefix said before an operator to combine operator and cursorless commands'''
    return m[0]
