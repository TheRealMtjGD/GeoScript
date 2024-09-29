def spawnTMTrigger(spawn: bool, multi: bool, string: str) -> str:
    obj = string
    
    if spawn == True:
        obj = f'{obj},62,1'
    if multi == True:
        obj = f'{obj},87,1'
    
    return obj

def conf(x: int, y: int, groups: list[int]) -> dict:
    return {
        "x": x,
        "y": y,
        "groups": '.'.join([str(i) for i in groups])
    }

def compileObjectArray(objarray: list) -> str:
    return ';'.join(objarray)


def createSpawnTrigger(group: int, conf: dict) -> list:
    return [f'1,1268,2,{conf['x']},3,{conf['y']},155,1,36,1,51,{group},57,{conf['groups']}']

def createSequenceTrigger(delay: float, call_groups: list[int], loop_mode: bool, conf: dict) -> list:
    groups = []
    
    for index, value in enumerate(call_groups, 1):
        groups.append(f'{value}.{index}')
    
    obj = f'1,3607,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,87,1,36,1,437,{delay},435,{'.'.join(groups)}'
    
    if loop_mode == True:
        obj = f'{obj},436,1'
    
    return [obj]

def createStopTrigger(group: int, conf: dict) -> list:
    ...