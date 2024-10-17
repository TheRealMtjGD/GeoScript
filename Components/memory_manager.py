class InitHeapMemory:
    def __init__(self, max_heap: int|None=None) -> None:
        if max_heap == None:
            max_heap = 5000
            
        self.hmax = max_heap
        self.heap_memory = []
    
    @property
    def get_pointer(self) -> str:
        return hex(max(self.heap_memory) + 1)
    
    def allocateValue(self, adress: str|None=None) -> int:
        if adress == None:
            adress = self.get_pointer
        if len(self.heap_memory) == self.hmax:
            return 1
        
        self.heap_memory.append(adress)
        return 0
    
    def delValue(self, adress: str) -> int:
        if adress in self.heap_memory:
            self.heap_memory.remove(adress)
            return 0
        
        else:
            return 1

class IdentifierStack:
    def __init__(self) -> None:
        self.id_stack = {}
    
    def allocateIdentifier(self, identifier: str, adress: str) -> None:
        self.id_stack.update({identifier: adress})
    
    def delIdentifier(self, identifier: str) -> None:
        del self.id_stack[identifier]