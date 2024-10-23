class ResourceManager:
    def __init__(self, init_array: list) -> None:
        self.init = init_array
    
    def allocateResource(self, res: int) -> None:
        self.init.append(res)
    
    @property
    def getNextFreeRes(self) -> int:
        if len(self.init) == 0:
            return 1
        else:
            return max(self.init) + 1


def initGroupManager(levelstr: str) -> ResourceManager:
    init_array = []
    split = levelstr.split(';')
    for object in split:
        object = object.split(',')
        
        index = object.index('57')
        init_array.append(split[index]+1)
    
    return ResourceManager(init_array)

def initCounterManager(levelstr: str) -> ResourceManager:
    init_array = []
    split = levelstr.split(';')
    for object in split:
        object = object.split(',')
        
        index = object.index('39')
        init_array.append(split[index]+1)
    
    return ResourceManager(init_array)