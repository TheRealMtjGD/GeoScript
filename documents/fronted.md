How the frontend compiler works
================================
The frontend of the compiler is the part of the compiler that packages all your dependencies, parses your code and starts to create the abstract syntax tree

### components of the frontend
* packager __( include_packager.py )__
* lexer __( gs_lexer.py )__
* parser __( gs_parser.py )__

Packager
-------------------------------
The packager is a program that takes all the libraries you have imported with __#include__ will all be packaged into one file

