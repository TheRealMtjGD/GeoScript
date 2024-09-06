import xmltodict
from . import decoder

def getLevelInfomation(name: str) -> str|None:
    with open('temp/savefile.dat') as file:
        savefile = xmltodict.parse(file.read())
    
    for level in savefile['plist']['dict']['d'][0]['d']:
        if level['s'][0] == name:
            return decoder.DecryptLvl(level[''][1])
    
    return None

def decodeSavefile() -> None:
    decoder.DecryptCCLL('temp/savefile.dat')