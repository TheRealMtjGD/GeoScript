from Components import error_handler
from Components import gsconfig
from Components import env_loader
from Components import memory_manager
from Components import logging
from BackendModules import resource_managers
from BackendModules import savefile
import gsparser
import backup
import abstract_st
import module_compiler
import gsc_compile
import shutil

def load_enviroments() -> tuple[dict]:
    main_config = env_loader.loadDotEnv('.env')
    compile_config = env_loader.loadDotEnv('config.env')
    
    return (main_config, compile_config)

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



def main() -> None:
    main_env, config_env = load_enviroments()
    compile_requirements = check_compile_requirements(config_env['file'])
    
    # creating backups
    logging.logToFile(logging.P, 'Creating backups', logging.CompileLog)
    backup.backupSavefile(f'{main_env['gd_appdata_loc']}/CCLocalLevels.dat')
    
    shutil.copyfile(f'{main_env['gd_appdata_loc']}/CCLocalLevels.dat', 'Temp/savefile.dat')
    savefile.decodeSavefile()
    default_level_string = savefile.getLevelData(config_env['level'])
    
    # compile mode
    if config_env['buildmode'] == 'std':
        if compile_requirements['compile-mode'] == 'Standard':
            logging.logToFile(logging.P, 'Starting compilation (mode: standard)', logging.CompileLog)
            
            logging.logToFile(logging.S, 'Creating pointer heap and identifier stack', logging.CompileLog)
            heap_memory = memory_manager.InitHeapMemory(int(main_env['heap_memory_max']))
            identifier_stack = memory_manager.IdentifierStack()
            
            logging.logToFile(logging.S, 'Creating GD Resource managers', logging.CompileLog)
            group_manager = resource_managers.initGroupManager(default_level_string)
            counter_manager = resource_managers.initCounterManager(default_level_string)
            
            # frontend
            logging.logToFile(logging.P, 'Compiling modules into gspackage', logging.CompileLog)
            with open(config_env['file']) as rstream:
                gspackage = module_compiler.compileModules(rstream.read(), ...)
            
            logging.logToFile(logging.P, 'Tokenising files', logging.CompileLog)
            tokenised = gsparser.GSParser(gspackage, config_env['file'], {'hm': heap_memory, 'ids': identifier_stack})
            
            logging.logToFile(logging.P, 'Parsing abstract syntax tree', logging.CompileLog)
            abstract_syntax_tree = abstract_st.createAbstractSyntaxTree(tokenised)
        
        elif compile_requirements['compile-mode'] == 'QuickCompile':
            ...
    
    else:
        logging.logToFile(logging.P, 'Starting compilation (mode: standard)', logging.CompileLog)
            
        logging.logToFile(logging.S, 'Creating pointer heap and identifier stack', logging.CompileLog)
        heap_memory = memory_manager.InitHeapMemory(int(main_env['heap_memory_max']))
        identifier_stack = memory_manager.IdentifierStack()
        
        logging.logToFile(logging.S, 'Creating GD Resource managers', logging.CompileLog)
        group_manager = resource_managers.initGroupManager(default_level_string)
        counter_manager = resource_managers.initCounterManager(default_level_string)
            
        # frontend
        logging.logToFile(logging.P, 'Compiling modules into gspackage', logging.CompileLog)
        with open(config_env['file']) as rstream:
            gspackage = module_compiler.compileModules(rstream.read(), ...)
            
        logging.logToFile(logging.P, 'Tokenising files', logging.CompileLog)
        tokenised = gsparser.GSParser(gspackage, config_env['file'], {'hm': heap_memory, 'ids': identifier_stack})
            
        logging.logToFile(logging.P, 'Parsing abstract syntax tree', logging.CompileLog)
        abstract_syntax_tree = abstract_st.createAbstractSyntaxTree(tokenised)