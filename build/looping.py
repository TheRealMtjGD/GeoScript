from . import controll_flow
from . import etc
from . import allocation
from . import value_mod

def createWhileLoopStatic(adress: int, value: str, comparitive: str, groups: dict, conf: dict) -> list:
    objs = []
    
    objs.extend(controll_flow.controllFlowStatic(adress, value, comparitive, groups['scope-call'], groups['stop-call-start'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['call-check']}))
    objs.extend(etc.createSequenceTrigger(0.1, [groups['call-check']], True, conf))
    objs.extend(etc.createStopTrigger(groups['stop-call'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['stop-call-start']}))
    
    return objs

def createWhileLoopDynamic(adress1: int, adress2: str, comparitive: str, groups: dict, conf: dict) -> list:
    objs = []
    
    objs.extend(controll_flow.controllFlowDynamic(adress1, adress2, comparitive, groups['scope-call'], groups['stop-call-start'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['call-check']}))
    objs.extend(etc.createSequenceTrigger(0.1, [groups['call-check']], True, conf))
    objs.extend(etc.createStopTrigger(groups['stop-call'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['stop-call-start']}))
    
    return objs

def createForLoopStatic(adress: int, value: str, comparitive: str, operation: str, groups: dict, conf: dict) -> list:
    objs = []
    
    objs.extend(allocation.allocateVariableStatic(adress, 0, conf))
    objs.extend(value_mod.modifyValueStatic(adress, 0, operation, {'x': conf['x'], 'y': conf['y'], 'groups': groups['modid']}))
    objs.extend(controll_flow.controllFlowStatic(adress, value, comparitive, groups['scope-call'], groups['stop-call-start'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['call-check']}))
    objs.extend(etc.createSequenceTrigger(0.1, [groups['call-check']], True, conf))
    objs.extend(etc.createStopTrigger(groups['stop-call'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['stop-call-start']}))
    
    return objs

def createForLoopDynamic(adress1: int, adress2: str, comparitive: str, operation: str, groups: dict, conf: dict) -> list:
    objs = []
    
    objs.extend(allocation.allocateVariableStatic(adress1, 0, conf))
    objs.extend(value_mod.modifyValueStatic(adress1, 0, operation, {'x': conf['x'], 'y': conf['y'], 'groups': groups['modid']}))
    objs.extend(controll_flow.controllFlowDynamic(adress1, adress2, comparitive, groups['scope-call'], groups['stop-call-start'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['call-check']}))
    objs.extend(etc.createSequenceTrigger(0.1, [groups['call-check'], groups['modid']], True, conf))
    objs.extend(etc.createStopTrigger(groups['stop-call'], {'x': conf['x'], 'y': conf['y'], 'groups': groups['stop-call-start']}))
    
    return objs