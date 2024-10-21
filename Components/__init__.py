def removeWhitespace(comp: str) -> str:
    comp: list = comp.split(' ')
    for _ in comp:
        try:
            comp.remove('')
        except ValueError:
            ...
    
    return ''.join(comp)