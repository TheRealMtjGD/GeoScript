from datetime import datetime
dt = datetime.now()

class CompileLog:
    def __init__(self) -> None:
        self.file_path = 'Logs/compile.log'

        self.rstream = open(self.file_path, 'r')
        self.wstream = open(self.file_path, 'w')

class AllocatorLog:
    def __init__(self) -> None:
        self.file_path = 'Logs/allocation_log.log'

        self.rstream = open(self.file_path, 'r')
        self.wstream = open(self.file_path, 'w')

class ObjectLog:
    def __init__(self) -> None:
        self.file_path = 'Logs/object_placement.log'

        self.rstream = open(self.file_path, 'r')
        self.wstream = open(self.file_path, 'w')


W = 'WARNING'
E = 'ERROR'
N = 'NOTE'
P = 'PROCESS'
S = 'SUBPROCESS'

def logToFile(note: str, desc: str, file: CompileLog|AllocatorLog|ObjectLog) -> None:
    logging = f'[{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}]: {note}, {desc}'
    file.wstream.write(logging)

logToFile(W, 'Compiler Stack Overflow Error', CompileLog())