@echo off

echo "Upgrading pip"
cmd /c python.exe -m pip install --upgrade pip
echo "Installing requirements.txt"
cmd /c pip install -r requirements.txt