from . import value_parser

PseudoRAMTable = {}
RAMNamespaceTable = {}
MacroTable = {}

class MemorySlot:
    def __init__(self, adress: str):
        self.memory_adress = adress
    
    def allocate_value(self, value: str, gtype: str, metavalue: str):
        PseudoRAMTable[self.memory_adress] = {
            'type': gtype,
            'value': value,
            'meta-value': metavalue,
            
            'debug-info': {
                'used': False,
                'in-loop': False
            }
        }
    
    def deallocate_memory(self):
        del PseudoRAMTable[self.memory_adress]
    
    def allocate_namespace(self, namespace: str):
        RAMNamespaceTable[namespace] = self.memory_adress
        self.namespace = namespace
    
    def deallocate_namespace(self):
        del RAMNamespaceTable[self.namespace]
    
    def get_memory_value(self) -> dict:
        return PseudoRAMTable.get(self.memory_adress, {'type': None, 'value': 'undefined', 'meta-value': None})

def __next_free_adress() -> str:
    for i in range(1, 10000000):
        if PseudoRAMTable.get(hex(i)) == None:
            return hex(i)


def allocateMemory() -> MemorySlot:
    return MemorySlot(__next_free_adress())

def getMemoryInfo(adress: str) -> MemorySlot:
    return MemorySlot(adress)