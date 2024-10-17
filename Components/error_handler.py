from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu('GSErrorHandler')

class GSTraceback:
    def __init__(self, archline: str, linenum: int) -> None:
        self.al = archline
        self.ln = linenum
    
    @property
    def getdata(self) -> dict:
        return {
            'al': self.al,
            'ln': self.ln
        }