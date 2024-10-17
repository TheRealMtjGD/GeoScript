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
        print('')


def ThrowWarning(warning: str, description: str, traceback: GSTraceback) -> None:
    handler = GSWarningHandler(warning, description, traceback)
    GSWarningHandlerArray.append(handler)

def ThrowError(error: str, description: str, traceback: GSTraceback) -> None:
    consolemenu.clear_screen()
    
    traceback_data = traceback.getdata
    print('Traceback ( with GSErrorHandler )')
    print(f'  File "{traceback_data['f']}", line {traceback_data['ln']}')
    print(f'    {traceback_data['al']}')
    print(f'{error}: {description}')
    
    exit(1)