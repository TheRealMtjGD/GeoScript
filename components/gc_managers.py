class GCManager:
    def __init__(self, group_array: list) -> None:
        self.garray = group_array
        self.garray.sort()
    
    @property
    def get_next_free(self) -> int:
        for i in range(1, 10000):
            try:
                if self.garray[i] == i:
                    continue
            except IndexError:
                return i
    
    @property
    def allocate(self, group: int) -> None:
        self.garray.append(group)
        self.garray.sort()
    
    @property
    def deallocate(self, group: int) -> None:
        del self.garray[group]
        self.garray.sort()

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
