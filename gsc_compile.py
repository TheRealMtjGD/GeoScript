import zlib
import base64
import json

def encodeGSCFile(ast: str, ct: dict, mem: dict, output: str) -> None:
    with open(output, 'wb') as file:
        out = {
            'abstrct-syntax-tree': ast,
            'call-tree': ct,
            'memory-tree': mem
        }
        
        outbytes = json.dumps(out).encode()
        outbytes = zlib.compress(base64.b64encode(outbytes))
        file.write(outbytes)

class decodeGSCFile:
    def __init__(self, input: str) -> None:
        with open(input, 'rb') as file:
            inbytes = base64.b64decode(zlib.decompress(file.read()))
            self.inf = json.loads(inbytes)
    
    @property
    def get_ast(self) -> dict:
        return eval(self.inf['abstract-syntax-tree'])
    
    @property
    def get_call_tree(self) -> dict:
        return self.inf['call-tree']
    
    @property
    def get_memory_tree(self) -> dict:
        return self.inf['memory-tree']