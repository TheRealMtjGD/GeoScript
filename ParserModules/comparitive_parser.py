# 54 > 0x009 && foo == "bar"

from . import value_parser

__comparitives = [
    '>',
    '<',
    '==',
    '>=',
    '<=',
    '&&',
    '!='
]

def __comparitive_locator(comp: str):
    return_comp = {
        '>': 0,
        '<': 0,
        '==': 0,
        '>=': 0,
        '<=': 0,
        '!=': 0,
        
        '&&': 0,
    }
    
    for i in __comparitives:
        if i in comp:
            return_comp[i] += 1
    
    return return_comp

def removeWhitespace(comp: str) -> str:
    comp: list = comp.split(' ')
    for _ in comp:
        try:
            comp.remove('')
        except ValueError:
            ...
    
    return ''.join(comp)


def parseComparitive(comparitive: str) -> list:
    parsed_comparitive = []
    comparitive = removeWhitespace(comparitive)
    comp_location = __comparitive_locator(comparitive)
    
    split_comparitive = comparitive.split('&&')
    
    for i in split_comparitive:
        comp = 'errortype?'
        
        for ii in __comparitives:
            if ii in i:
                comp = comp.split(ii)
                comp[0] = value_parser.parseType(comp[0])
                comp[1] = value_parser.parseType(comp[1])
                comp.insert(1, ii)
        
        parsed_comparitive.append(comp)
    
    return parsed_comparitive