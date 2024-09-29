import os
import dotenv

def load_enviroment() -> dict:
    dotenv.load_dotenv()
    enviroment: dict = os.environ
    
    for i in enviroment:
        ii: str = enviroment[i]
        
        # inplace
        ii = ii.replace('{{PublicUSR}}', os.getlogin())
        
        enviroment[i] = ii
    
    return enviroment