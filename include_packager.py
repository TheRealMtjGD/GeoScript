import os
from copy import deepcopy
from components import error_handler

def __include_local_module(module: str) -> str:
    local_module = f'./gs_modules/{module}'
    
    if os.path.isdir(local_module) == True:
        if os.path.exists(f'{local_module}/@packageinit.gsh') == True:
            local_module = f'{local_module}/@packageinit.gsh'
    
    with open(local_module) as file:
        return file.read()

def __include_inner_module(module: str) -> str:
    local_module = module
    
    if os.path.isdir(local_module) == True:
        if os.path.exists(f'{local_module}/@packageinit.gsh') == True:
            local_module = f'{local_module}/@packageinit.gsh'
    
    with open(local_module) as file:
        return file.read()


def includePackager(file: str) -> None:
    with open(file) as rstream:
        filecomp = rstream.read()
        while '#include ' in filecomp:
            for value, component in enumerate(deepcopy(filecomp).split('\n')):
                archname = component
                if component.startswith('#include ') == True:
                    component = component.removeprefix('#include ')
                    
                    if component.startswith('<') == True:
                        component = component.removeprefix('<')
                        component = component.removesuffix('>')
                        filecomp = filecomp.replace(f'#include <{component}>', __include_local_module(component))
                        
                    elif component.startswith('"') == True:
                        component = component.removeprefix('"')
                        component = component.removesuffix('"')
                        filecomp = filecomp.replace(f'#include "{component}"', __include_inner_module(component))
                    
                    else:
                        error_handler.raise_error('InvalidModuleError', f'Module "{component}" does not exist', error_handler.GSTraceback(value, archname, file))
    
    with open('./temp/packager.gss', 'w') as wstream:
        wstream.write(filecomp)