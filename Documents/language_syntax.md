Definitive statements
==========================
## Include statement:
  #include <[module].gsh> | #include "[module].gsh"

  Imports a module [module] into your script

  __#include <@std/string.gsh>__

## Define statement:
  #define [name]: [type] = [value]

  Creates a mutable value accompanied by an identifier

  __#define test: string = "Hello World"__

## Constant statement:
  #const [name]: [type] = [value]

  Creates an immutable value accompanied by an identifier

  __#const test: intager = 98__

## Pointer Allocate Statement:
  #ptralloc [adress]: [type] = [value]

  Allocates a value to a specific adress

  __#ptralloc 0x007: float = 7.092__

## Macro statement:
  #indef [name] ([arguments]): [code]

  Creates a macro with arguments

  __#indef macro (arg1 arg2): @spawn arg1 arg2__

## Function statement:
  #function [name]([arguments]) {}

  Creates a callable function with arguments

  __#function myFunction(string myarg1, intager arg2) {}__
