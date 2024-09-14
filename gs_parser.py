class GSParser:
    def __init__(self, gslexer: list[dict[str]]) -> None:
        self.gslexer = gslexer
        self.abstract_syntax_tree = {
            'main': []
        }
        
        for lnode in gslexer:
            scope = lnode['debug']['scope']
            if scope == '':
                scope = 'main'
            
            if self.check_tree_node(scope) == True:
                self.abstract_syntax_tree[scope].append(lnode)
            else:
                self.abstract_syntax_tree[scope] = []
    
    
    def check_tree_node(self, node: str) -> bool:
        if self.abstract_syntax_tree.get(node) == None:
            return False
        else:
            return True