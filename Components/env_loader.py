import os

def loadDotEnv(file: str) -> dict:
    dotenv = {}
    
    with open(file) as rstream:
        for i in rstream.read().splitlines():
            if i.startswith(';'):
                continue
            elif i == '':
                continue
            else:
                lnsplit = i.split('=', 1)
                lnsplit[1] = lnsplit[1].removeprefix('"').removesuffix('"')
                
                if lnsplit[1] == '{{PUBLIC}}':
                    lnsplit[1] = os.getlogin()
                
                dotenv[lnsplit[0]] = lnsplit[1]
    
    return dotenv