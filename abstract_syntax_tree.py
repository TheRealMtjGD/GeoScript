from components import gc_managers
from components import memory_allocator

def allocate_scope_groups(abstract_syntax_tree: dict, group_manager: gc_managers.GCManager) -> list:
    scope_groups = {}
    
    for node in abstract_syntax_tree:
        next_free = group_manager.next_free
        scope_groups[node] = next_free
        group_manager.allocate(next_free)
    
    return scope_groups

def get_adress_pointer(value: str) -> str:
    return_value = ''
    
    if value.startswith('0x') == True:
        return_value =  int(value, 16)
    
    elif value in memory_allocator.RAMNamespaceTable:
        return_value =  int(memory_allocator.getMemoryInfo(memory_allocator.RAMNamespaceTable[value]).memory_adress, 16)
    
    else:
        return_value = value
    
    return str(return_value)


def inplaceNamespaceVariables(array: list[dict]) -> list[dict]:
    ...