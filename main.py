from Components import error_handler
from Components import gsconfig
from Components import env_loader
from Components import memory_manager

import gsparser
import backup
import abstract_st
import type_checking
import module_compiler
import gsc_compile

def load_enviroments() -> list[dict]:
    main_config = env_loader.loadDotEnv('.env')
    compile_config = env_loader.loadDotEnv('config.env')
    
    return [main_config, compile_config]

def check_compile_requirements(file: str) -> dict:
    config = {}
    
    if file.endswith('.gss') == True:
        config['compile-mode'] = 'Standard'
    elif file.endswith('.gsc') == True:
        config['compile-mode'] = 'QuickCompile'
    elif file.endswith('.gsh') == True:
        config['compile-mode'] = 'LibCompile'
    else:
        error_handler.ThrowInternalCompilerWarning('UndecernableFileType', 'Cannot infer compile mode through file type, assuming standard compile')


def loadGSCRequirements(input: str) -> dict:
    gsc = gsc_compile.decodeGSCFile(input)
    ast = gsc.get_ast
    ct = gsc.get_call_tree
    mem = gsc.get_memory_tree
    
    hm = memory_manager.InitHeapMemory(mem['max-heap'])
    ids = memory_manager.IdentifierStack()
    hm.heap_memory = mem['hm']
    ids.id_stack = mem['ids']
    
    mem = [hm, ids]
    
    return {
        'ast': ast,
        'ct': ct,
        'mem': mem
    }

def dumpGSCRequirements(ast: dict, ct: dict, hm: memory_manager.InitHeapMemory, ids: memory_manager.IdentifierStack, mh: int, output: str) -> None:
    memdict = {'hm': hm.heap_memory, 'ids': ids.id_stack, 'max-heap': mh}
    gsc_compile.encodeGSCFile(ast, ct, memdict, output)