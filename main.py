from components import error_handler
from components import gc_managers
from components import memory_allocator
from components import enviroment_loader
import json5
from datetime import datetime
import os
import shutil

import include_packager
import gs_lexer
import gs_parser

import abstract_syntax_tree
import memory_manager
import optimiser

import backend_compiler
import linker
import exit_protocol

import out

WARNING = 'WARNING'
SUBPROCESS = 'SUBPROCESS'
PROCESS = 'PROCESS'
ERROR = 'ERROR'

__DATETIME = datetime.now()

def load_arguments() -> dict:
    with open('cliin.json5') as file:
        return json5.load(file)

def logger(prompt: str, description: str) -> None:
    with open('logs/compile.log', 'a') as file:
        file.write(f'[{__DATETIME.hour}:{__DATETIME.minute}.{__DATETIME.second}] {prompt}: {description}\n')




def frontend_compiler(args: dict) -> dict:
    print('Assesing dependencies')
    logger(PROCESS, 'Assesing dependencies')
        
    working_directory: list = os.path.abspath(args['input']).split('\\')
    working_directory.pop()
    working_directory = '/'.join(working_directory)
        
    include_paths = [f'{working_directory}/gslocals/stdlib', f'{working_directory}/gslocals/libraries', f'{working_directory}/gslocals/modules']
    if not args['extra-include-paths'] == None:
        for path in args['extra-include-paths'].split(';'):
            include_paths.append(path)
            logger(SUBPROCESS, f'Adding extra include path: {path}')
        
    fullincludefile = include_packager.packageDependencies(args['input'], include_paths, working_directory)
        
    print('Tokenising File')
    logger(PROCESS, 'Tokinising (Lexing) geoscript file')
        
    tokens = gs_lexer.GSLexer(args['input'], fullincludefile).lexer_array
        
    print('Starting Abstract Syntax Tree')
    logger(PROCESS, 'Creating Abstract Syntax Tree, Stage 1')
        
    ast_body = gs_parser.GSParser(tokens).abstract_syntax_tree
    return ast_body
        
def middleend(ast: dict, gcmanagers: list[gc_managers.GCManager]) -> dict:
    print('Optimising and Froming AST')
    logger(PROCESS, 'Optimising and Forming AST')
    
    scope_ir_groups = abstract_syntax_tree.allocate_scope_groups(ast, gcmanagers[0])
    logger(SUBPROCESS, 'Allocating Scope Groups')
    #memory_manager.unallocate_unused(memory_allocator.PseudoRAMTable)
    logger(SUBPROCESS, 'Deallocating Unused Memory')
    
    return scope_ir_groups

def backend(ast: dict, scopeir_groups: dict, gcmanagers: list[gc_managers.GCManager]) -> dict:
    print('Building level string')
    levelstring = backend_compiler.CompileAbstractSyntaxTree(ast, scopeir_groups, gcmanagers)
    logger(PROCESS, 'Building level string from AST and IR')
    
    return levelstring



def main() -> None:
    args = load_arguments()
    compileoptions = 'generic-compile'
    
    print(f'Starting Compilation at {args['input']}')
    match args['output-quick-compile']:
        case True:
            if args['input'].endswith('.gsc'):
                print(f'Compiling .gsc: output to gdlvl {args['output']}')
                compileoptions = 'quickcompile-install'
            else:
                print('Quick compile: output .gsc')
                compileoptions = 'quick-compile'
        case False:
            print(f'Generic compile: output to gdlvl {args['output']}')
    print('')
    
    enviroment = enviroment_loader.load_enviroment()
    
    shutil.copyfile(f'{enviroment['gd_appdata_file']}/CCLocalLevels.dat', 'temp/backupfile.dat')
    logger(PROCESS, 'Backing up your savefile')
    
    savefile = linker.importSaveFile(f'{enviroment['gd_appdata_file']}/CCLocalLevels.dat')
    
    gm = gc_managers.initGroupManager(savefile.getLevelData(args['output']))
    cm = gc_managers.initCounterManager(savefile.getLevelData(args['output']))
    
    frontend = frontend_compiler(args)
    middle = middleend(frontend, [gm, cm])
    end = backend(frontend, middle, [gm, cm])
    
    # optimisation 2
    end = f'{savefile.getLevelData(args['output'])}{end}'
    optimised_level_string = optimiser.optimise_level_string(end)
    logger(SUBPROCESS, f'Optimised built level string ( Saved Objects: {optimised_level_string['optimise-int']} )')
    
    # linker
    print('Linking to savefile')
    logger(PROCESS, 'Linking to savefile')
    savefile.setLevelData(args['output'], optimised_level_string['lvlstr'])
    
    logger(SUBPROCESS, 'Exporting savefile')
    linker.exportSaveFile(f'{enviroment['gd_appdata_file']}/CCLocalLevels.dat')
    
    # exit protocol
    print('')
    exit_protocol.exit_from_compiler()
    exit_protocol.clear_logs()
    exit_protocol.clear_temp_directory()
    exit(0)

main()