# 54 > 0x009 && foo == "bar" 
from  . import value_parser

__comparitives = [
    '>',
    '<',
    '==',
    '>=',
    '<=',
    '&&',
    '!='
]

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
    
    split_comparitive = comparitive.split('&&')
    
    for i in split_comparitive:
        comp = 'errortype?'
        
        for cmp in __comparitives:
            if cmp in i:
                comp = i.split(cmp)
                comp[0] = value_parser.parseType(comp[0])
                comp[1] = value_parser.parseType(comp[1])
                comp.insert(1, cmp)
        
        parsed_comparitive.append(comp)
    
    return parsed_comparitive