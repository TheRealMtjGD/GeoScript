#!/bin/sh

INSTALL_PATH=/usr/bin/geoscript
GD_APPDATA_PATH=/
GD_PROGRAM_PATH=/

mkdir $INSTALL_PATH
cp . $INSTALL_PATH

export PATH="$INSTALL_PATH:$PATH"

echo "gd_appdata_file=$GD_APPDATA_PATH\rgd_main_path=$GD_PROGRAM_PATH" > .env