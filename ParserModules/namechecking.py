__checking = [
    '`',
    '¬',
    '!',
    '"',
    '£',
    '$',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '-',
    '=',
    '_',
    '+',
    '[',
    ']',
    '{',
    '}',
    '@',
    "'",
    ':',
    ';',
    '~',
    '#',
    '<',
    ',',
    '>',
    '.',
    '/',
    '?',
    '\\',
    '|'
]

def checkName(name: str) -> bool:
    for i in __checking:
        if i in name:
            return True
    return False