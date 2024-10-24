class DebugParserBacklog:
    def __init__(self) -> None:
        self.backlog = {}
    
    
    def backlog_template(self, archline: str, linenum: int) -> None:
        return {
            'al': archline,
            'ln': linenum
        }
    
    def add_to_backlog(self, gstraceback, backup: dict) -> None:
        backup['tb'] = gstraceback
        self.backlog[backup['ln']] = backup