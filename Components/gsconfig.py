import json5

class GSCONFIG:
    TYPE_CHECKING = 'strict'
    INCLUDE_PATHS = []


def parseGSconfig() -> None:
    with open('./gsconfig.json') as file:
        gsconfig_file = json5.load(file)
    
    GSCONFIG.TYPE_CHECKING = gsconfig_file['compiler-options']['type-checking']
    GSCONFIG.INCLUDE_PATHS = gsconfig_file['compiler-options']['include-paths']

def generateGSconfigTemplates() -> None:
    with open('./gsconfig.json', 'w') as file:
        template = {
            'compiler-options': {
                'type-checking': 'strict',
                
                'include-paths': [
                    './.gslocals/Libraries',
                    './.gslocals/Scripts'
                ]
            }
        }
        
        json5.dump(template, file)