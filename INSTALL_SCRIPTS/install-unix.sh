#!/bin/sh

GSPATH=/usr/bin/geoscript
GD_MAIN_PATH=""
GD_APPDATA_PATH=""


echo "Installing GeoScript"

echo "Copying main compiler"
cp . $GSPATH

echo "Installing STDLIB"
cd $GSPATH
git clone https://github.com/TheRealMtjGD/GSLIB.git

echo "Creating config file"
echo "gd_main_path=$GD_MAIN_PATH\ngd_appdata_path=$GD_APPDATA_PATH" > $GSPATH/.env