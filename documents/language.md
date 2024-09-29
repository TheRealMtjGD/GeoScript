General Language Rules
-----------------------
GeoScript it staticly typed and object oriented __( syntax similar to C++ and JavaScript )__


Difinitive statements
-----------------------
### #include
Syntax: #include <module.gsh> | #include "module.gsh"

Imports a module from the stdlib path __./gslocals/stdlib__ or your local modules __./gslocals/libraries__ or just your working directory. Import from stdlib or local modules with <> sorrounding the module __eg. #include <stdlib.gsh>__, import from your working directory with "" sorrounding your modules __eg. #include "module.gsh"__


### #define
Syntax: #define [name]: [type] = [value]

Defines a variable to be used around the script __eg. #define variable: string = "Hello World"__


### #const
Syntax: #const [name]: [type] = [value]

Defines a constant value to be used around the script __eg. #const constant: intager = 9__


### #indef
Syntax: #indef [name] [value]

Creates a namespace and when you reference this namespace it will be swapped with the value at compile time __eg. #indef macro 9.7__


### #function
Syntax: #function [name] ([arguments]) {[code]}

Creates a function to be called throughout a script, arguments can be defined in the [arguments] section and those are like variables you can set throughout the function __#function function(arg: string, arg1: intager) {}__


Structual Statements
-----------------------

### @gotospace
Syntax: @gotospace [namespace] {[code]}

Creates a namespace witch you can call to quickly jump to that block of code __eg. @gotospace namespace { variable += 1 }__


### @goto
Syntax: @goto [namespace]

Calls the goto namespace you provided with the @gotospace statement __eg: @goto namespace__


### @class
Syntax: @class [name] {}

Creates a class witch is like a blueprint for an object, you can put functions inside of this class which you can call by referencing the name of the class then after a "." add the name of the class __eg. @class dog {}__


### @struct
Syntax: @struct [name] {}

Creates an object similar to a class but only variables and constants can be defined in it __eg. @struct animal_config {}__


### @place_obj
Syntax: @place_obj [obj_string]

Places an object in the gd level __eg. @place_obj 1,1,2,64,3,647__


### @spawn_group
Syntax: @spawn_group [group] [delay]

Calls a spawn group __eg. @spawn_group 8 0__