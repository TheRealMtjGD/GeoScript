@echo off

set "%GSPATH%=C:/Users/Public/AppData/Local/Programs/GeoScript"
set "%GD_MAIN_PATH%=C:/Program Files/Steam/steamapps/common/GeometryDash"
set "%GD_APPDATA_PATH%=C:/Users/Public/AppData/Local/GeometryDash"


echo "Installing GeoScript"

echo "Copying main compiler"
robocopy . %GSPATH%

echo "Installing STDLIB"
cd %GSPATH%
git clone https://github.com/TheRealMtjGD/GSLIB.git

echo "Creating config file"
echo "gd_main_path=%GD_MAIN_PATH%\ngd_appdata_path=%GD_APPDATA_PATH%" > %GSPATH%/.env