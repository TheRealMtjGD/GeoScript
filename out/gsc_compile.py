import base64
import zlib
import json5

class GSCIN:
    def __init__(self, ast: dict, memsnap: dict, group_manager: dict) -> None:
        self.ast = ast
        self.mmap = memsnap
        self.gms = group_manager
        
def compile_gsc(gscin: GSCIN, out: str) -> None:
    form = {
        "ast": gscin.ast,
        "mmap": gscin.mmap,
        "gcm": gscin.gms
    }
    
    with open(out, 'wb') as file:
        jsondump = json5.dumps(form)
        jsondump = base64.b64encode(jsondump.encode())
        jsondump = zlib.compress(jsondump, wbits=zlib.MAX_WBITS)
        
        file.write(jsondump)