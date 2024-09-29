import os
from copy import deepcopy
from components import error_handler

def __getIncludeModule(directory: str, module: str|None) -> str|None:
    dirloads = os.listdir(directory)
    
    if not module == None:
        if module in dirloads:
            with open(f'{dirloads}/{module}') as file:
                return file.read()
        
        else:
            return None
    
    else:
        if os.path.isdir(f'{directory}/{module}'):
            return None
        
        else:
            with open(f'{dirloads}/@init.gsh') as file:
                return file.read()


def packageDependencies(file: str, include_paths: list, working_directory: str) -> str:
    with open(file) as rstream:
        contents = rstream.read()
        index = 1
        
        while '#include ' in contents:
            for line in deepcopy(contents).split('\n'):
                arch = line
                if line.startswith('#include '):
                    line = line.removeprefix('#include ')
                    
                    if line.startswith('<'):
                        line = line.removeprefix('<')
                        line = line.removesuffix('>')
                        
                        for i in include_paths:
                            module = __getIncludeModule(i, line)
                            
                            if module == None:
                                continue
                            else:
                                contents.replace(f'#include <{line}>', module)
                                break
                    
                    elif line.startswith('"'):
                        line = line.removeprefix('"')
                        line = line.removesuffix('"')
                        
                        module = __getIncludeModule(working_directory, line)
                        
                        if module == None:
                            error_handler.raise_error('ImportError', f'Failed to import module {line} from working directory', error_handler.GSTraceback(index, arch, file))
            
        index = 1

    return contents