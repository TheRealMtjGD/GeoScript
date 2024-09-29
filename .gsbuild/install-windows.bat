@echo off

set "%INSTALL_PATH%=C:/Users/danre/AppData/Local/Programs/GeoScript"
set "%GD_APPDATA_PATH%=C:/Users/danre/AppData/Local/GeometryDash"
set "%GS_MAIN_PATH%=C:/Program Files/Steam/steamapps/common/Geometry Dash"

mkdir %INSTALL_PATH%
copy . %INSTALL_PATH%

set "%PATH%=%INSTALL_PATH%;%PATH%"

echo "gd_appdata_file=%GD_APPDATA_PATH%\ngd_main_file=%GD_MAIN_PATH%" > .env