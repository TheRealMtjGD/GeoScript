#!/binsh

gspath=/usr/bin/geoscript

echo "Testing GeoScript Compiler"

echo "    Testing include modules"
"$gspath/Commands/geoscript -gsc $gspath/Tests/include_tests.gss"

echo "    Testing main testcase"
"$gspath/Commands/geoscript -gsc $gspath/Tests/main_testcases.gss"