import zlib
import base64
import json5

class GSCOUT:
    def __init__(self, ast: dict, mmap: dict, gcm: dict) -> None:
        self.ast = ast
        self.mmap = mmap
        self.gcm = gcm

def gsc_decompile(infile: str) -> GSCOUT:
    with open(infile, 'rb') as file:
        jsonload = file.read()
        jsonload = zlib.decompress(jsonload, wbits=zlib.MAX_WBITS)
        jsonload = base64.b64decode(jsonload.decode()).decode()
        jsonload = json5.loads(jsonload)
        
        return GSCOUT(jsonload['ast'], jsonload['mmap'], jsonload['gcm'])