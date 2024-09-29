from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu('GS Error Handler')
warnings = []

class GSTraceback:
    def __init__(self, linenum: int, line: str, file: str):
        self.lindex = linenum
        self.line = line
        self.file = file

class GSCompilerErrorInfo:
    def __init__(self, affile: str, brfile: str):
        self.affile = affile
        self.brfile = brfile

def raise_error(error: str, desc: str, traceback: GSTraceback|None=None) -> None:
    consolemenu.clear_screen()
    
    if not traceback == None:
        print('Traceback most recent calls')
        print(f'  File "{traceback.file}", line {traceback.lindex}')
        print(f'    {traceback.line}')
        
        print('    ', end='')
        for i in traceback.line:
            print('^', end='')
        print('')
        
    print(f'{error}: {desc}')
    exit(1)

def raise_warning(warning: str, desc: str) -> None:
    warnings.append(f'Warning {warning}: {desc}')


def raise_compiler_error(error: str, desc: str, error_info: GSCompilerErrorInfo) -> None:#
    consolemenu.clear_screen()
    print(f'There has been an error compiling: {error}')
    print('==========================================================')
    print(desc)
    print(f'Affected file: {error_info.affile}, Branch of file: {error_info.brfile}')
    print('')
    print('This is a problem with geoscript not your code')
    print('Submit issue at https://github.com/TheRealMtjGD/GeoScript/issues')
    exit(1)