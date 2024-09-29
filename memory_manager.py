from copy import deepcopy

class StaticMemoryInfo:
    def __init__(self, ramtable: dict) -> None:
        self.ramtable = ramtable
    
    @property
    def get_ram_consumption(self) -> int:
        'Returns value in bytes'
        return len(self.ramtable)


def unallocate_unused(ramtable: dict) -> dict:
    copy_ramtable = deepcopy(ramtable)
    
    for adress in copy_ramtable:
        bytetable: dict = ramtable[adress]
        
        if bytetable['debug-info']['used'] == False:
            del ramtable[adress]
    
    return copy_ramtable