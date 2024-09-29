from . import error_handler

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

def value_parser(gtype: str, value: str, gstraceback: error_handler.GSTraceback) -> str:
    return_value = ''
    
    if gtype == 'intager':
        return value
    if gtype == 'float':
        return value
    
    elif gtype == 'string':
        for i in value:
            return_value = return_value.__add__(str(ord(i)))
        return return_value
    
    elif gtype == 'boolian':
        if value == 'true':
            return 1
        elif value == 'false':
            return 0
        elif value == 'nulltype':
            return 0
        else:
            error_handler.raise_error('TypeError', f'Booian can only have values of "true" and "false" not "{value}"', gstraceback)
    
    else:
        error_handler.raise_error('TypeError', f'Invalid type {gtype}', gstraceback)

def check_type(value: str, gstraceback: error_handler.GSTraceback) -> str:
    if value.startswith('"'):
        return 'string'
    elif value.isdigit():
        return 'intager'
    elif value.isdecimal():
        return 'float'
    elif value in ['true', 'false']:
        return 'boolian'
    elif value == 'null':
        return 'nulltype'
    else:
        error_handler.raise_error('ValueError', 'Value does not have a decernable type', gstraceback)