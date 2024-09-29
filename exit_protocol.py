import os
import webbrowser
from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu('GSExit protocol')

def clear_temp_directory() -> None:
    os.remove('temp/backupfile.dat')
    os.remove('temp/savefile.dat')
    os.remove('temp/locallevels.dat')

def clear_logs() -> None:
    with open('logs/compile.log', 'w') as file:
        file.write('')
    with open('logs/allocator.log', 'w') as file:
        file.write('')
    with open('logs/object_placement.log', 'w') as file:
        file.write('')


def __exit_with_warnings(warnings: list) -> None:
    print(f'Compiled with Warnings: {len(warnings)}')
    print('=======================================================')
    print('1. View Warnings')
    print('2. View Verbose Logs')
    print('3. Get Debug Configurations Log')
    
    endofcompile = int(input('> '))
    
    if endofcompile == 1:
        consolemenu.clear_screen()
        for warning in warnings:
            print(warning)
    
    elif endofcompile == 2:
        consolemenu.clear_screen()
        print('Choose log to view')
        print('=======================================================')
        print('1. General compile log')
        print('2. Allocator log')
        print('3. Object placement')
        
        log = int(input('\n> '))
        
        consolemenu.clear_screen()
        if log == 1:
            with open('logs/compile.log') as file:
                print(file.read())
            with open('logs/allocator.log') as file:
                print(file.read())
            with open('logs/object_placement.log') as file:
                print(file.read())
    
    elif endofcompile == 3:
        ...
    
    else:
        print(f'Invalid option {endofcompile}')

def __exit_sucsessfuly() -> None:
    print(f'Sucsessfuly compiled')
    print('=======================================================')
    print('1. Launch GD')
    print('2. View Verbose Logs')
    print('3. Get Debug Configurations Log')
    
    endofcompile = int(input('\n> '))
    
    if endofcompile == 1:
        consolemenu.clear_screen()
        webbrowser.open('steam://rungameid/322170')
    
    elif endofcompile == 2:
        consolemenu.clear_screen()
        print('Choose log to view')
        print('=======================================================')
        print('1. General compile log')
        print('2. Allocator log')
        print('3. Object placement')
        
        log = int(input('\n> '))
        
        consolemenu.clear_screen()
        if log == 1:
            with open('logs/compile.log') as file:
                print(file.read())
            with open('logs/allocator.log') as file:
                print(file.read())
            with open('logs/object_placement.log') as file:
                print(file.read())
    
    elif endofcompile == 3:
        ...
    
    else:
        print(f'Invalid option {endofcompile}')

def exit_from_compiler(warnings: list|None=None):
    if warnings == None:
        __exit_sucsessfuly()
    else:
        __exit_with_warnings(warnings)
