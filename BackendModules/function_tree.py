functionTree = {}

def defineFunction(name: str, group: int, return_adress: str|None=None) -> None:
    functionTree.update({name: {'group': group, 'adress': return_adress}})

def callFunction(name: str) -> dict|None:
    return functionTree.get(name)