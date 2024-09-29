@echo off

echo "Removing all cache folders"
cd ..

echo "removing ./__pycache__"
rmdir __pycache__

echo "removing ./build/__pycache__"
rmdir build/__pycache__

echo "removing ./components/__pycache"
rmdir components/__pycache

echo "removing ./interface/__pycache__"
rmdir interface/__pycache__

echo "removing ./out/__pycache__"
rmdir out/__pycache__