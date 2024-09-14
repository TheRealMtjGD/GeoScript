import xmltodict
from . import decoder

def getLevelInfomation(name: str) -> str|None:
    with open('temp/savefile.dat') as file:
        savefile = xmltodict.parse(file.read())
    
    for level in savefile['plist']['dict']['d'][0]['d']:
        if level['s'][0] == name:
            return decoder.DecryptLvl(level['s'][1])
    
    return None

def setLevelInfomation(name: str, lvlstr: str) -> str|None:
    with open('temp/savefile.dat') as file:
        savefile = xmltodict.parse(file.read())
    
    for index, level in enumerate(savefile['plist']['dict']['d'][0]['d']):
        if level['s'][0] == name:
            savefile['plist']['dict']['d'][0]['d'][index]['s'][1] = lvlstr
            
    with open('temp/savefile.dat') as file:
        xmltodict.unparse(savefile, file)

def decodeSavefile() -> None:
    decoder.DecryptCCLL('temp/savefile.dat')