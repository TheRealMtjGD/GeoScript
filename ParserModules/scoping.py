gsscope = ''

def retractScope() -> None:
    global gsscope
    
    gsscope = gsscope.split('.')
    del gsscope[-1]
    
    gsscope = '.'.join(gsscope)

def updateScope(scope: str) -> None:
    global gsscope
    
    gsscope = f'{gsscope}.{scope}'