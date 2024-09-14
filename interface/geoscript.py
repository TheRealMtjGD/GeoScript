import os
import documentation
import sys
import json5

def parse_arguments(argv: list[str]) -> dict:
    parse_args = {
        'argv': [],
        'arg_options': {},
        'flags': {}
    }
    
    parse_args['argv'] = argv
    
    for index, value in enumerate(argv):
        if value.startswith('--') == True:
            parse_args['flags'][value.removeprefix('--')] = True
            continue
        
        if value.startswith('-') == True:
            parse_args['arg_options'][value.removeprefix('-')] = argv[index+1]
            continue
    
    return parse_args

parsed_argv = parse_arguments(sys.argv)

if len(parsed_argv['argv']) == 1:
    documentation.gsusage()
    exit(0)
elif parsed_argv['argv'][1] == '--help':
    documentation.gshelp()
    exit(0)
elif parsed_argv['argv'][1] == '--version':
    documentation.gsversion()
    exit(0)
elif parsed_argv['argv'][1] == '--usage':
    documentation.gsusage()
    exit(0)

else:
    geoscript_arguments = {
        'input': parsed_argv['argv'][1],
        'output': parsed_argv['argv'][2],
        'output-quick-compile': parsed_argv['arg_options'].get('gso', False),
        'extra-include-paths': parsed_argv['arg_options'].get('i'),
        'verbose-output': parsed_argv['flags'].get('verbose', False)
    }

    with open('./GeoScriptMAIN/cliin.json5', 'w') as file:
        json5.dump(geoscript_arguments, file)
    
    os.system('cd GeoScriptMAIN')
    os.system('python main.py')
    
    exit(0)