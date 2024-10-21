from Components import gsconfig
from Components import error_handler
import Components
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


def __getModulesList(filestr: str, traceback: error_handler.GSTraceback) -> list:
    modules = []
    
    if '#include ' in filestr:
        for line in filestr.splitlines():
            line = Components.removeWhitespace(line)
            
            if line.startswith('#include') == True:
                line = line.removeprefix('#include')
                
                if line.startswith('<') == True:
                    line = line.removeprefix('<').removesuffix('>')
                    modules.append((line, True))
                    
                    modulecontents = getModuleContents(line, True, traceback)
                    
                elif line.startswith('"') == True:
                    line = line.removeprefix('"').removesuffix('"')
                    modules.append((line, False))
                
                    modulecontents = getModuleContents(line, False, traceback)
                
                else:
                    error_handler.ThrowError('ImportError', 'Expected "<" or """', traceback)
                
                modules_extend = __getModulesList(modulecontents, traceback)
                modules.extend(modules_extend)
    
    return modules

def compileModules(filestr: str, traceback: error_handler.GSTraceback) -> str:
    compiled = filestr
    
    modules = __getModulesList(filestr, traceback)
    
    for module in modules:
        compiled = f'{getModuleContents(module[0], module[1], traceback)}\n\n{compiled}'
    
    return compiled