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