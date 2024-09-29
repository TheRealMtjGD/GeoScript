def modifyValueDynamic(adress1: int, adress2: int, operation: str, conf: dict) -> list:
    obj = f'1,3619,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,36,1,80,{adress1},476,1,478,1,51,{adress2},479,1,481,1,482,3'
    
    if operation == '+':
        obj = obj.__add__('480,1')
    elif operation == '-':
        obj = obj.__add__('480,1')
    elif operation == '*':
        obj = obj.__add__('480,1')
    elif operation == '/':
        obj = obj.__add__('480,1')
    
    return [obj]

def modifyValueStatic(adress: int, value: str, operation: str, conf: dict) -> list:
    obj = f'1,1817,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,36,1,80,{adress}'
    
    if operation == '+':
        obj = obj.__add__(f',77,{value}')
    elif operation == '-':
        obj = obj.__add__(f',77,-{value}')
    elif operation == '*':
        obj = obj.__add__(f',88,1,449,{value}')
    elif operation == '/':
        obj = obj.__add__(f',88,2,449,{value}')
    
    return [obj]