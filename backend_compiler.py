# build components
from build import allocation
from build import controll_flow
from build import etc
from build import looping
from build import value_mod

from components import memory_allocator
from components import gc_managers

import abstract_syntax_tree

def logger(objid: int, objcoords: tuple, purpouse: str, obj: str) -> None:
    write_string = f'Object id: {objid}, coordinates: ({objcoords[0]}, {objcoords[1]}) :: {purpouse} [{obj}]\n'
    with open('logs/object_placement.log') as file:
        file.write(write_string)


def AllocateMemory(namespace: str, conf: dict) -> list:
    allocation_slot = memory_allocator.getMemoryInfo(memory_allocator.RAMNamespaceTable[namespace])
    value = allocation_slot.get_memory_value()
    adress = int(allocation_slot.memory_adress, 16)
    
    if value['value'].startswith('c::') == True:
        return allocation.allocateVariableDynamic(adress, value['value'].removeprefix('c::'), conf)
    else:
        return allocation.allocateVariableStatic(adress, value['value'], conf)

def ControllFlowStatement(value1: str, comp: str, value2: str, ids: tuple, conf: dict) -> list:
    if value1.startswith('c::') == True:
        if value2.startswith('c::') == True:
            return controll_flow.controllFlowDynamic(value1.removeprefix('c::'), value2.removeprefix('c::'), comp, ids[0], ids[1], conf)
        else:
            return controll_flow.controllFlowStatic(value1.removeprefix('c::'), value2, comp, ids[0], ids[1], conf)
    else:
        return controll_flow.controllFlowCompleteStatic(value1, value2, comp, ids[0], ids[1], conf)

def ValueModification(value1: str, value2: str, operation: str, conf: dict) -> list:
    if value2.removeprefix('c::') == True:
        return value_mod.modifyValueDynamic(value1, value2.removeprefix('c::'), operation, conf)
    else:
        return value_mod.modifyValueStatic(value1, value2, operation, conf)

def CreateLoopStatementWhile(value1: str, value2: str, comp: str, groups: dict, conf: dict) -> list:
    if value2.removeprefix('c::') == True:
        return looping.createWhileLoopDynamic(value1, value2.removeprefix('c::'), comp, groups, conf)
    else:
        return looping.createWhileLoopStatic(value1, value2, comp, groups, conf)

def CreateLoopStatemetFor(value1: str, value2: str, comp: str, operation: str, groups: dict, conf: dict) -> list:
    if value2.startswith('c::') == True:
        return looping.createForLoopDynamic(value1, value2.removeprefix('c::'), comp, operation, groups, conf)
    else:
        return looping.createForLoopStatic(value1, value2, comp, operation, groups, conf)

object_location_cache = {
    'x': [30],
    'y': [30]
}
def object_location_manager() -> tuple:
    x = ( len(object_location_cache['x']) + 1 ) * 30
    y = ( len(object_location_cache['y']) + 1 ) * 30
    
    object_location_cache['x'].append(x)
    object_location_cache['y'].append(y)
    
    return (x, y)

def __CompileASTNodes(nodes: list, group_array: list, gcmanagers: list[gc_managers.GCManager], scope_group: int, groups: dict, ast: dict) -> str:
    objects = []
    nodes = abstract_syntax_tree.inplaceNamespaceVariables(nodes)
    
    for pnode in enumerate(nodes):
        node = pnode[1]
        obj = object_location_manager()
        group = group_array[pnode[0]]
        conf = {'x': obj[0], 'y': obj[1], 'groups': group}
        
        match node['callback']:
            case 'allocate-variable':
                objects.extend(AllocateMemory(node['namespace'], conf))
            case 'allocate-constant':
                objects.extend(AllocateMemory(node['namespace'], conf))
            
            case 'code-jump':
                objects.extend(__CompileASTNodes(ast[node['scope']], abstract_syntax_tree.allocate_ir_groups(group_array), gcmanagers, groups[node['scope']], groups, ast))
            
            case 'spawn-group':
                objects.extend(etc.createSpawnTrigger(node['group'], conf))
            case 'add-obj':
                objects.extend(objects['object'])
            
            case 'if-statement':
                objects.extend(ControllFlowStatement(node['operation'][0], node['operation'][1], node['operation'][2], (node['jmp-scope']), conf))
            case 'elif-statement':
                objects.extend(ControllFlowStatement(node['operation'][0], node['operation'][1], node['operation'][2], (node['jmp-scope']), conf))
            case 'else-statement':
                objects.extend(ControllFlowStatement(node['operation'][0], node['operation'][1], node['operation'][2], (node['jmp-scope']), conf))
            
            case 'while-loop':
                objects.extend(CreateLoopStatementWhile(node['operation'][0], node['operation'][2], node['operation'][1], {
                        "scope-call": ast[node['jmp-scope']],
                        "stop-call-start": gcmanagers[0].next_free,
                        "call-check": gcmanagers[0].next_free,
                        "stop-call": gcmanagers[0].next_free
                    }, conf))
            case 'for-loop':
                objects.extend(CreateLoopStatemetFor(node['operation'][0], node['operation'][2], node['operation'][1], node['var-operation'], {
                        "scope-call": ast[node['jmp-scope']],
                        "stop-call-start": gcmanagers[0].next_free,
                        "call-check": gcmanagers[0].next_free,
                        "stop-call": gcmanagers[0].next_free,
                        "modid": gcmanagers[0].next_free
                    }, conf))
            
            case 'modify':
                match node['modification']:
                    case 'add':
                        objects.extend(ValueModification(node['target'], node['amount'], '+', conf))
                    case 'sub':
                        objects.extend(ValueModification(node['target'], node['amount'], '-', conf))
                    case 'mul':
                        objects.extend(ValueModification(node['target'], node['amount'], '*', conf))
                    case 'div':
                        objects.extend(ValueModification(node['target'], node['amount'], '/', conf))
                        
            case 'code-jump':
                for arg in node['arguments']:
                    objects.extend(AllocateMemory(arg.split(':')[0], conf))
                objects.extend(__CompileASTNodes(ast[f'{node['debug']['scope']}.{node['function-name']}'], abstract_syntax_tree.allocate_ir_groups(group_array), gcmanagers, groups[node['scope']], groups, ast))
                
    objects.extend(etc.createSequenceTrigger(0, group_array, False, {'x': 0, 'y': 0, 'groups': scope_group}))
    return etc.compileObjectArray(objects)

def CompileAbstractSyntaxTree(ast: dict, groups: dict, gcmanagers: list[gc_managers.GCManager]) -> str:
    main_function = ast['main']
    group_array = abstract_syntax_tree.allocate_ir_groups(main_function, gcmanagers[0])
    
    gslvlstr = __CompileASTNodes(main_function, group_array, gcmanagers, groups['main'], groups, ast)
    return gslvlstr