GSMacroHandler = {}

class GSMacro:
    def __init__(self, macro_code: str, args: list[str]) -> str:
        self.mc = macro_code,
        self.args = args
    
    def exec_macro(self, arguments: list[str]) -> str:
        macro_code: str = self.mc
        
        for posindex, value, in arguments:
            arg = self.args[posindex]
            
            macro_code = macro_code.replace(arg, value)
        
        return macro_code

def createMacro(identifier: str, args: list[str], code: str) -> None:
    GSMacroHandler[identifier] = GSMacro(code, args)

def execMacro(self, identifier: str, arguments: list[str]) -> str:
    status = GSMacroHandler.get(identifier).exec_macro(arguments)
    
    if status == None:
        return "::GSMACRONOTFOUND::"
    else:
        return status