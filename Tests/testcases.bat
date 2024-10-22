@echo off

set "%gspath%=C:/Users/Public/AppData/Local/Programs/GeoScript"

echo "Testing GeoScript Compiler"

echo "    Testing include modules"
cmd /c %gspath%/Commands/geoscript.exe -gsc %gspath%/Tests/include_tests.gss

echo "    Testing main testcase"
cmd /c %gspath%/Commands/geoscript.exe -gsc %gspath%/Tests/main_testcases.gss