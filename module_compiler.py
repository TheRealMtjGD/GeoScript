from Components import gsconfig
from Components import error_handler
import os

def __mdc(mod: str, traceback: error_handler.GSTraceback) -> str:
    if os.path.isfile(mod) == True:
        with open(mod) as file:
            return file.read()
    
    else:
        if os.path.exists(mod) == True:
            with open(f'{mod}/@gsinit.gsh') as file:
                return file.read()
        
        else:
            error_handler.ThrowError('ModuleNotFoundError', f'Module "{mod}" does not exist', traceback)

def getModuleContents(module: str, global_search: bool, traceback: error_handler.GSTraceback) -> str:
    if global_search == False:
        return __mdc(module, traceback)
    
    else:
        for path in gsconfig.GSCONFIG.INCLUDE_PATHS:
            if os.path.exists(f'{path}/{module}') == True:
                return __mdc(f'{path}/{module}', traceback)


def __getModulesList(filestr: str) -> list:
    modules = []