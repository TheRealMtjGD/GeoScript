def allocateVariableStatic(adress: int, value: str, conf: dict) -> list:
    return [f'1,1817,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,36,1,80,{adress},77,{value},139,1,449,1']

def allocateVariableDynamic(adress: int, valueadress: int, conf: dict) -> list:
    return [f'1,3619,2,{conf['x']},3,{conf['y']},57,{conf['groups']},155,1,36,1,80,{adress},476,1,478,1,51,{valueadress},479,1,481,1,482,3']