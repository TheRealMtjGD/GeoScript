from base64 import b64decode
from zlib import decompress, MAX_WBITS

class Decrypt:
    def Xor(path: str, key: int) -> str:
        with open(path,'rb') as fr:
            data = fr.read()
        res = []
        for i in data: res.append(i^key)
        return bytearray(res).decode()
 
    def Decrypt(data: str) -> bytes:
        return decompress(b64decode(data.replace('-','+').replace('_','/').encode())[10:],-MAX_WBITS)

def DecryptCCLL(filedir: str) -> None:
    res = Decrypt.Xor(filedir, 11)
    fin = Decrypt.Decrypt(res)
    with open('Temp/savefile.dat','wb') as fw:
        fw.write(fin)

def DecryptLvl(lvlstr: str) -> str:
    return decompress(b64decode(lvlstr.replace('-', '+').replace('_', '/').encode())[10:], -MAX_WBITS).decode()