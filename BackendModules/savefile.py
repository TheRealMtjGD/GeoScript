from . import decoder
import xmltodict

def getLevelData(name: str) -> str|None:
    with open('Temp/savefile.dat') as file:
        sf = xmltodict.parse(file.read())
    
    for level in sf['plist']['dict']['d'][0]['d']:
        if level['s'][0] == name:
            return decoder.DecryptLvl(level['s'][1])
    
    return None

def setLevelInfomation(name: str, lvlstr: str) -> str|None:
    with open('Temp/savefile.dat') as file:
        savefile = xmltodict.parse(file.read())
    
    for index, level in enumerate(savefile['plist']['dict']['d'][0]['d']):
        if level['s'][0] == name:
            savefile['plist']['dict']['d'][0]['d'][index]['s'][1] = lvlstr
            
    with open('Temp/savefile.dat', 'w') as file:
        xmltodict.unparse(savefile, file)

def decodeSavefile() -> None:
    decoder.DecryptCCLL('Temp/savefile.dat')