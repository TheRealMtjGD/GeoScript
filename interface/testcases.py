import os
import sys

try:
    if sys.argv[1] == '--verbose':
        verbose = True
    else:
        verbose = False
except IndexError:
    verbose = False

def run_geoscript_test(file: str) -> bool:
    if os.system(f'geoscript -t {file}') == 0:
        return True
    else:
        return False

def gs_test_fail(test: int) -> None:
    print(f'Failed Test {test}')


# main
print('Testing GeoScript 1.0.0 (stable reliese)')
print('=================================================')

if run_geoscript_test(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN/tests/test1.gss') == True:
    print('Test 1 Complete (Sucsessful)')
else:
    gs_test_fail(1)

if run_geoscript_test(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN/tests/test1.gss') == True:
    print('Test 2 Complete (Sucsessful)')
else:
    gs_test_fail(2)

if run_geoscript_test(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN/tests/test1.gss') == True:
    print('Test 3 Complete (Sucsessful)')
else:
    gs_test_fail(3)

if run_geoscript_test(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN/tests/test1.gss') == True:
    print('Test 4 Complete (Sucsessful)')
else:
    gs_test_fail(4)