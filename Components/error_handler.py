from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu('GSErrorHandler', items='')

GSWarningHandlerArray = []

class GSTraceback:
    def __init__(self, archline: str, linenum: int, file: str) -> None:
        self.al = archline
        self.ln = linenum
        self.f = file
    
    @property
    def getdata(self) -> dict:
        return {
            'al': self.al,
            'ln': self.ln,
            'f': self.f
        }

class GSWarningHandler:
    def __init__(self, warning: str, desc: str, traceback: GSTraceback) -> None:
        self.handler = {
            'w': warning,
            'd': desc,
            't': traceback
        }
    
    def throw(self) -> None:
        data = self.handler['t'].getdata
        
        print('Warning raised in compiled GSFile')
        print(f'  File "{data['f']}", line {data['ln']}')
        print(f'    {data['al']}')
        print(f'{self.handler['w']}: {self.handler['d']}')
        print('\n')

class InternalWarningHandler:
    def __init_(self, warning: str, description: str) -> None:
        self.w, self.d = warning, description
    
    def throw(self) -> None:
        print('A warning has been raised in the internal compiler')
        print(f'    {self.w}: {self.d}\n')


def ThrowWarning(warning: str, description: str, traceback: GSTraceback) -> None:
    handler = GSWarningHandler(warning, description, traceback)
    GSWarningHandlerArray.append(handler)

def ThrowError(error: str, description: str, traceback: GSTraceback) -> None:
    traceback_data = traceback.getdata
    print('Traceback ( with GSErrorHandler )')
    print(f'  File "{traceback_data['f']}", line {traceback_data['ln']}')
    print(f'    {traceback_data['al']}')
    
    print('    ', end='')
    for _ in traceback_data['al']:
        print('^', end='')
    print('')
    
    print(f'{error}: {description}')
    
    exit(1)

def ThrowInternalCompilerWarning(error: str, description: str) -> None:
    GSWarningHandlerArray.append(InternalWarningHandler(error, description))