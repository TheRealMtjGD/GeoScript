class GCManager:
    def __init__(self, group_array: list) -> None:
        self.garray = group_array
        self.garray.sort()
    
    @property
    def next_free(self) -> int:
        return max(self.garray) + 1
    
    def allocate(self, group: int) -> None:
        self.garray.append(group)
    
    def deallocate(self, group: int) -> None:
        del self.garray[group]

def initGroupManager(level_string: str) -> GCManager:
    array = []
    
    for i in level_string.split(';'):
        i = i.split('59,', 1)
        i[1] = i[1].split(',', 1)[0]
        i = i[1]
        
        array.append(int(i))
    
    return GCManager(array)

def initCounterManager(level_string: str) -> GCManager:
    array = []
    
    for i in level_string.split(';'):
        i = i.split('37,', 1)
        i[1] = i[1].split(',', 1)[0]
        i = i[1]
        
        array.append(int(i))
    
    return GCManager(array)
