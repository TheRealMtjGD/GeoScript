def createAbstractSyntaxTree(parser: list) -> dict:
    ast = {'main': []}
    
    for block in parser:
        if block['debug']['scope'] == '':
            ast['main'].append(block)
        
        else:
            if ast.get(block['debug']['scope']) == None:
                ast[block['debug']['scope']] = [block]
            else:
                ast[block['debug']['scope']].append(block)
    
    return ast