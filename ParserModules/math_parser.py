from . import value_parser

__operands = [
    '+',
    '-',
    '*',
    '/'
]

def removeWhitespace(comp: str) -> str:
    comp: list = comp.split(' ')
    for _ in comp:
        try:
            comp.remove('')
        except ValueError:
            ...
    
    return ''.join(comp)

def parseMathOperation(operation: str) -> list:
    parsed = []
    
    operation = removeWhitespace(operation)
    
    operation = operation.replace('+', ' + ')
    operation = operation.replace('-', ' - ')
    operation = operation.replace('*', ' * ')
    operation = operation.replace('/', ' / ')
    
    ops = operation.split(' ')
    unsorted_parsed = []
    
    for _ in range(0, len(ops), 4):
        unsorted_parsed.append([ops[0], ops[1], ops[2]])
        
        try:
            unsorted_parsed.append(ops[3])
        except IndexError:
            ...
                
        for _ in range(4):
            try:
                ops.pop(0)
            except IndexError:
                ...
    
    for i in unsorted_parsed:
        try:
            # type checking
            i.append
            
            if i[0].startswith('(') == True:
                i[0] = value_parser.parseType(i[0].removeprefix('('))
                i[2] = value_parser.parseType(i[2].removesuffix(')'))
                
                parsed.insert(0, i)
            
            else:
                i[0] = value_parser.parseType(i[0].removeprefix('('))
                i[2] = value_parser.parseType(i[2].removesuffix(')'))
                
                parsed.append(i)
        
        except AttributeError:
            parsed.insert(0, i)

    return parsed