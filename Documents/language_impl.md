GeoScript Language Implimentation
==================================

Memory Management
----------------------------------

### memory management system
HeapMemory:

    the heap memory is the place where all pointers are allocated, the heap is stored in a list / array format
    
    Example:
        HeapMemory = [
            0x001,
            0x002,
            0x004
        ]

IdentifierStack:

    the identifier stack is the place where variable names are stored relitive to there pointers. it is stored in a dictionary / OrderedArray format

    Example:
        IdentifierStack = {
            "test-variable": "0x001"
        }

### allocation syntax
Syntax ( define statement ): #define [name]: [type] = [value]

Syntax ( constant statement ): #const [name]: [type] = [value]

Functionality:
    This will allocate a variable to the Heap Memory.
    Creates a pointer and is saved in the hexadecimal format then allocates it into the HeapMemory, Also creates a identifier (the variable name) and allocates it into the IdentifierStack


Macro Management
--------------------------------

### macro management
