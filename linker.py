import shutil
from components import decoder
from components import savefile_module

class SaveFileIO:
    def __init__(self) -> None:
        ...
    
    # returns none if level does not exist
    def getLevelData(self, name: str) -> str|None:
        return savefile_module.getLevelInfomation(name)
    
    def setLevelData(self, name: str, string: str) -> None:
        savefile_module.setLevelInfomation(name, string)

def importSaveFile(sfpath: str) -> SaveFileIO:
    shutil.copyfile(sfpath, 'temp/locallevels.dat')
    decoder.DecryptCCLL('temp/locallevels.dat')
    return SaveFileIO()

def exportSaveFile(origin_path: str) -> None:
    shutil.copyfile('temp/savefile.dat', origin_path)