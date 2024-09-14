from copy import deepcopy

def optimise_level_string(lvlstr: str) -> dict:
    lvlsplit = lvlstr.split(';')
    
    optimise_array = []
    optimise_int = 0
    
    for lobject in lvlsplit:
        if not lobject in optimise_array:
            optimise_array.append(lobject)
        else:
            optimise_int += 1
    
    return {
        'lvlstr': ';'.join(optimise_array),
        'optimise-int': optimise_int
    }

def dead_code_remover(abstract_syntax_tree: dict, call_tree: list) -> dict:
    copy_abstract_syntax_tree = deepcopy(abstract_syntax_tree)
    for node in copy_abstract_syntax_tree:
        if node in call_tree:
            del copy_abstract_syntax_tree[node]
    
    return copy_abstract_syntax_tree