from . import etc

def controllFlowDynamic(adress1: int, adress2: int, comparitive: str, tid: int, fid: int, conf: dict) -> list:
    obj = f'1,3620,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,36,1,80,{adress1},51,{tid},71,{fid},476,1,479,1,483,{adress2},480,3,481,3'
    
    if comparitive == '>':
        obj = obj.__add__('482,1')
    elif comparitive == '>=':
        obj = obj.__add__('482,2')
    elif comparitive == '<':
        obj = obj.__add__('482,3')
    elif comparitive == '<=':
        obj = obj.__add__('482,4')
    elif comparitive == '!=':
        obj = obj.__add__('482,5')
    
    return [obj]

def controllFlowStatic(adress1: int, value: str, comparitive: str, tid: int, fid: int, conf: dict) -> list:
    obj = f'1,3620,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,36,1,80,{adress1},51,{tid},71,{fid},476,1,95,{value},479,1,483,0,480,3,481,3'
    
    if comparitive == '>':
        obj = obj.__add__('482,1')
    elif comparitive == '>=':
        obj = obj.__add__('482,2')
    elif comparitive == '<':
        obj = obj.__add__('482,3')
    elif comparitive == '<=':
        obj = obj.__add__('482,4')
    elif comparitive == '!=':
        obj = obj.__add__('482,5')
    
    return [obj]

def controllFlowCompleteStatic(value1: str, value2: str, comparitive: str, tid: int, fid: int, conf: dict) -> list:
    if comparitive == '==':
        if value1 == value2:
            obj = etc.createSpawnTrigger(tid, conf)
        else:
            obj = etc.createSpawnTrigger(fid, conf)
            
    elif comparitive == '>':
        if int(value1) > int(value2):
            obj = etc.createSpawnTrigger(tid, conf)
        else:
            obj = etc.createSpawnTrigger(fid, conf)
    
    elif comparitive == '>=':
        if int(value1) >= int(value2):
            obj = etc.createSpawnTrigger(tid, conf)
        else:
            obj = etc.createSpawnTrigger(fid, conf)
    
    elif comparitive == '<':
        if int(value1) < int(value2):
            obj = etc.createSpawnTrigger(tid, conf)
        else:
            obj = etc.createSpawnTrigger(fid, conf)
    
    elif comparitive == '<=':
        if int(value1) <= int(value2):
            obj = etc.createSpawnTrigger(tid, conf)
        else:
            obj = etc.createSpawnTrigger(fid, conf)
    
    elif comparitive == '!=':
        if not value1 == value2:
            obj = etc.createSpawnTrigger(tid, conf)
        else:
            obj = etc.createSpawnTrigger(fid, conf)
    
    return obj