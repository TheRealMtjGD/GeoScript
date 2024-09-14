def namespace_checker(name: str) -> list[bool]|list[bool, str]:
    if ' ' in name:
        return [False, ' ']
    elif '@' in name:
        return [False, '@']
    elif "'" in name:
        return [False, "'"]
    elif '#' in name:
        return [False, '#']
    elif ':' in name:
        return [False, ':']
    elif ';' in name:
        return [False, ';']
    elif '.' in name:
        return [False, '.']
    elif ',' in name:
        return [False, ',']
    elif '/' in name:
        return [False, '/']
    elif '\\' in name:
        return [False, '\\']
    elif '?' in name:
        return [False, '?']
    elif '|' in name:
        return [False, '|']
    elif '>' in name:
        return [False, '>']
    elif '<' in name:
        return [False, '<']
    elif ']' in name:
        return [False, ']']
    elif '[' in name:
        return [False, '[']
    elif '-' in name:
        return [False, '-']
    elif '=' in name:
        return [False, '=']
    elif '!' in name:
        return [False, '!']
    elif '"' in name:
        return [False, '"']
    elif '£' in name:
        return [False, '£']
    elif '$' in name:
        return [False, '$']
    elif '%' in name:
        return [False, '%']
    elif '^' in name:
        return [False, '^']
    elif '&' in name:
        return [False, '&']
    elif '*' in name:
        return [False, '*']
    elif '(' in name:
        return [False, '(']
    elif ')' in name:
        return [False, ')']
    elif '{' in name:
        return [False, '{']
    elif '}' in name:
        return [False, '}']
    elif '~' in name:
        return [False, '~']
    elif '`' in name:
        return [False, '`']
    elif '¬' in name:
        return [False, '¬']
    return [True]

class bitclass:
    def __init__(self):
        self.typesys = ''
        self.value = []

class byteint(bitclass):
    def __init__(self, value: list) -> None:
        self.value = value
        self.typesys = 'intager'
class bytefloat(bitclass):
    def __init__(self, value: list) -> None:
        self.value = value
        self.typesys = 'float'
class bytestring(bitclass):
    def __init__(self, value: list) -> None:
        self.value = value
        self.typesys = 'string'
class bytearray(bitclass):
    def __init__(self, value: list) -> None:
        self.value = value
        self.typesys = 'array'
class bytedict(bitclass):
    def __init__(self, value: list) -> None:
        self.value = value
        self.typesys = 'dict'

def value_parser(gtype: str, value: str) -> bitclass:
    return_value = []
    
    if gtype == 'intager':
        return_value = byteint([value])
        
    elif gtype == 'float':
        return_value = bytefloat([value.replace('.', '98789', 1)])
        
    elif gtype == 'string':
        value = value.removeprefix('"')
        value = value.removesuffix('"')
        value = value.removeprefix("'")
        value = value.removesuffix("'")
        
        for i in value:
            return_value.append(str(ord(i)))
        return_value = bytestring(return_value)
    
    elif gtype == 'array':
        value = value.removeprefix('[')
        value = value.removeprefix(']')
        
        for i in value.split(','):
            return_value.append(value_parser(i.split(':', 1)[1], i.split(':', 1)[0]))