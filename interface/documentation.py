def gshelp():
    print('GeoScript compiler help')
    print('============================')
    print('')


def gsusage():
    print('geoscript build [SourceFile] [LevelName] : Compiles your source file to a gd level in your save file')
    print('geoscript build [SourceFile] [GQCFile] -bf : Compiles your source file to a .gqc file')
    print('geoscript build [.gqc file] [LevelName] -gso : Compiles a quick compile file')
    print('geoscript build [SourceFile] [LevelName] -i [IncludePaths] : Compiles your source file to a gd level in your save file (with a specified include paths)\n')
    print('geoscript --help : Displays the help menu')
    print('geoscript --version : Displays the version menu')
    print('geoscript --usgae : Displays this menu')
    

def gsversion():
    print('Geoscript 1.0.0 (main, Sep 10 2024) [CPYTHON 3.12.4] on win32')