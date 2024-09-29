from components import gc_managers
from components import memory_allocator
from components import error_handler
from copy import deepcopy

import zlib


def allocate_scope_groups(abstract_syntax_tree: dict, group_manager: gc_managers.GCManager) -> dict:
    scope_groups = {}
    
    for node in abstract_syntax_tree:
        next_free = group_manager.next_free
        scope_groups[node] = next_free
        group_manager.allocate(next_free)
    
    return scope_groups

def allocate_ir_groups(gsir: list[dict], group_manager: gc_managers.GCManager) -> list:
    gsir_array = []
    
    for _ in gsir:
        next_free = group_manager.next_free
        gsir_array.append(next_free)
        group_manager.allocate(next_free)
    
    return gsir_array



def get_adress_pointer(value: str) -> str:
    return_value = ''
    
    if value.startswith('0x') == True:
        return_value = f'c::{int(value, 16)}'
    
    elif value in memory_allocator.RAMNamespaceTable:
        return_value =  f'c::{int(memory_allocator.RAMNamespaceTable[value], 16)}'
    
    elif value in memory_allocator.MacroTable:
        return_value = memory_allocator.MacroTable[value]
    
    else:
        return_value = value
    
    return return_value

def get_macro_value(value: str) -> str:
    if value in memory_allocator.MacroTable:
        return memory_allocator.MacroTable[value]
    else:
        return value


def inplaceNamespaceVariables(array: list[dict]) -> list[dict]:
    for index, lnode in enumerate(deepcopy(array)):
        match lnode['callback']:
            case 'allocate-variable':
                array[index]['value'] = get_adress_pointer(lnode['value'])
            case 'allocate-constant':
                array[index]['value'] = get_adress_pointer(lnode['value'])
            
            case 'if-statement':
                array[index]['operation'] = [get_adress_pointer(lnode['operation'][0]), lnode['operation'][1], get_adress_pointer(lnode['operation'][2])]
            case 'elif-statement':
                array[index]['operation'] = [get_adress_pointer(lnode['operation'][0]), lnode['operation'][1], get_adress_pointer(lnode['operation'][2])]
            
            case 'while-loop':
                array[index]['operation'] = [get_adress_pointer(lnode['operation'][0]), lnode['operation'][1], get_adress_pointer(lnode['operation'][2])]
            case 'for-loop':
                array[index]['operation'] = [get_adress_pointer(lnode['operation'][0]), lnode['operation'][1], get_adress_pointer(lnode['operation'][2])]
            
            case 'modify':
                array[index]['target'] = get_adress_pointer(lnode['target']).removeprefix('c::')
                array[index]['amount'] = get_adress_pointer(lnode['amount'])
            
            case 'spawn-group':
                array[index]['group'] = get_macro_value(lnode['group'])
                array[index]['delay'] = get_macro_value(lnode['delay'])
                
                if str(array[index]['group']).isdigit() == False:
                    error_handler.raise_error('ValueError', 'Value in spawn object [ group ] can only be "intager"', lnode['debug']['traceback'])
                    
                if str(array[index]['group']).isdigit() == False:
                    if str(array[index]['group']).isdecimal() == False:
                        error_handler.raise_error('ValueError', 'Value in spawn object [ delay ] can only be "intager" or "float"', lnode['debug']['traceback'])
                
            case 'place-obj':
                array[index]['object'] = lnode['object'].split(',')
                for i, ii in enumerate(array[index]['object']):
                    array[index]['object'][i] = get_macro_value(ii)
                    
                    if str(array[index]['object'][ii]).isdigit() == False:
                        if str(array[index]['object'][ii]).isdecimal() == False:
                            try:
                                zlib.decompress(array[index]['object'][ii])
                            except Exception:
                                error_handler.raise_error('ValueError', 'Value in place object can only be "intager", "float" or "gzip compressed string"', lnode['debug']['traceback'])
                    
                array[index]['object'] = ','.join(array[index]['object'])
    
    return array