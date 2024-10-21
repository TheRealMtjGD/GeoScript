import ParserModules
from ParserModules import comparitive_parser as cp
from ParserModules import math_parser as mp
from ParserModules import value_parser as vp
from ParserModules import scoping
from ParserModules import namechecking as nc

from Components import error_handler
from Components import gsconfig
from Components import logging
from Components import macro_handler
from Components import memory_manager
import Components

class GSParser:
    def __init__(self, input_str: str, file: str) -> None:
        self.file = file
        self.parser_list = []
        self.linenum = 1
        
        self.memory_manager = memory_manager.InitHeapMemory()
        self.identifier_stack = memory_manager.IdentifierStack()
        
        debug_backlog = ParserModules.DebugParserBacklog()
        
        for line in input_str.splitlines():
            archline = line
            self.linenum += 1
            line = Components.removeWhitespace(line)
            
            traceback = error_handler.GSTraceback(archline, self.linenum, file)
            debug_backlog.add_to_backlog(traceback, debug_backlog.backlog_template(archline, self.linenum))
            
            if line.startswith('#') == True:
                self.definitive_statements(line, (traceback, debug_backlog.backlog_template(archline, self.linenum)))
            
            elif line.startswith('@') == True:
                self.structule_statements(line, (traceback, debug_backlog.backlog_template(archline, self.linenum)))
            
            elif line.startswith('$') == True:
                self.placement_statements(line, (traceback, debug_backlog.backlog_template(archline, self.linenum)))
            
            else:
                self.ctrlf_and_looping_statements(line, (traceback, debug_backlog.backlog_template(archline, self.linenum)))
    
    
    def definitive_statements(self, line: str, traceback: tuple) -> None:
        if line.startswith('#define') == True:
            line = line.removeprefix('#define')
            line = line.split(':', 1)
            line[1] = line[1].split('=', 1)
            
            pointer = self.memory_manager.get_pointer
            
            if nc.checkName(line[1][1]) == True:
                error_handler.ThrowError('NameError', 'Invalid character in variable name', traceback[0])
            
            self.memory_manager.allocateValue(pointer)
            self.identifier_stack.allocateIdentifier(line[0], pointer)
            
            self.parser_list.append(
                {
                    'operation': 'define',
                    'identifier': line[0],
                    'type': line[1][0],
                    'value': vp.parseType(line[1][1])
                }
            )
        
        elif line.startswith('#const') == True:
            line = line.removeprefix('#const')
            line = line.split(':', 1)
            line[1] = line[1].split('=', 1)
            
            pointer = self.memory_manager.get_pointer
            
            if nc.checkName(line[1][1]) == True:
                error_handler.ThrowError('NameError', 'Invalid character in constant name', traceback[0])
            
            self.memory_manager.allocateValue(pointer)
            self.identifier_stack.allocateIdentifier(line[0], pointer)
            
            self.parser_list.append(
                {
                    'operation': 'define',
                    'identifier': line[0],
                    'type': line[1][0],
                    'value': vp.parseType(line[1][1])
                }
            )
        
        elif line.startswith('#ptralloc') == True:
            line = line.removeprefix('#ptralloc')
            line = line.split(':', 1)
            line[1] = line[1].split('=', 1)
            
            self.memory_manager.allocateValue(line[0])
            
            self.parser_list.append(
                {
                    'operation': 'define',
                    'adress': line[0],
                    'type': line[1][0],
                    'value': vp.parseType(line[1][1])
                }
            )
        
        elif line.startswith('#indef') == True:
            line = line.removeprefix('#indef')
            line = line.split('(', 1)
            line[1] = line[1].split('):', 1)
            
            macro_handler.createMacro(line[0], line[1][0].split(','), line[1][1])
            
        elif line.startswith('#function') == True:
            line = line.removeprefix('#function')
            line = line.split('(', 1)
            
            if line[1].endswith('){}') == True:
                ...
            else:
                line[1] = line[1].removesuffix('){')
                
                if nc.checkName(line[0]) == True:
                    error_handler.ThrowError('NameError', 'Character is not allowed in function name', traceback[0])
                
                line[1] = line[1].split(',')
                for i in enumerate(line[1]):
                    line[1][i[0]] = line[1][i[0]].split(':', 1)
                    
                scoping.updateScope(line[0])
                self.parser_list.append(
                    {
                        'operation': 'function',
                        'identifier': line[0],
                        'arguments': line[1],
                        'scope': scoping.gsscope
                    }
                )
        
        elif line.startswith('#include') == True:
            ...
        
        else:
            error_handler.ThrowError('InvalidStatementError', 'Invalid definitive statement', traceback[0])
    
    def structule_statements(self, line: str, traceback: tuple) -> None:
        if line.startswith('@container') == True:
            line = line.removeprefix('@container')
            
            if line.endswith('{}') == True:
                ...
            else:
                line = line.removesuffix('{')
                line = line.split(',', 1)
                
                scoping.updateScope('container')
                self.parser_list.append(
                    {
                        'operation': 'define-container',
                        'x': line[0],
                        'y': line[1],
                        'scope': scoping.gsscope
                    }
                )
        
        elif line.startswith('@struct') == True:
            line = line.removeprefix('@struct')
            
            if line.endswith('{}') == True:
                ...
            else:
                line = line.removesuffix('{')
                
                scoping.updateScope(line)
                self.parser_list.append(
                    {
                        'operation': 'define-struct',
                        'identifier': line,
                        'scope': scoping.gsscope
                    }
                )
        
        elif line.startswith('@class') == True:
            line = line.removeprefix('@class')
            
            if line.endswith('{}') == True:
                ...
            else:
                line = line.removesuffix('{')
                
                if '(' in line:
                    line = line.removesuffix(')')
                    
                    line = line.split('(')
                    line[1] = line[1].split(',')
                    
                    scoping.updateScope(line[0])
                    self.parser_list.append(
                        {
                            'operation': 'define-class',
                            'identifier': line[0],
                            'inheritince': line[1],
                            'scope': scoping.gsscope
                        }
                    )
                
                else:
                    scoping.updateScope(line[0])
                    self.parser_list.append(
                        {
                            'operation': 'define-class',
                            'identifier': line,
                            'inheritince': None,
                            'scope': scoping.gsscope
                        }
                    )
        
        else:
            error_handler.ThrowError('InvalidStatementError', 'Invalid statement error', traceback[0])
    
    def placement_statements(self, line: str, traceback: tuple) -> None:
        if line.startswith('$add') == True:
            line = line.removeprefix('$add')
            
            self.parser_list.append(
                {
                    'operation': 'add',
                    'object-str': line
                }
            )
        
        elif line.startswith('$spawn') == True:
            line = line.removeprefix('$spawn')
            line = line.split(',')
            
            self.parser_list.append(
                {
                    'operation': 'spawn',
                    'group': line[0],
                    'duration': line[1]
                }
            )
        
        else:
            error_handler.ThrowError('InvalidStatementError', 'Invalid placement statement', traceback[0])
    
    
    def ctrlf_and_looping_statements(self, line: str, traceback: tuple) -> None:
        if line.startswith('if') == True:
            line = line.removeprefix('if(')
            
            if line.endswith('){}') == True:
                ...
            else:
                line = line.removesuffix('){')
                parsed_math = cp.parseComparitive(line)
                
                scoping.updateScope('if-statement')
                
                self.parser_list.append(
                    {
                        'operation': 'if-statement',
                        'math': parsed_math,
                        'scope': scoping.gsscope
                    }
                )
        
        elif line.startswith('}elseif') == True:
            line = line.removeprefix('}elseif(')
            
            if line.endswith('){}') == True:
                ...
            else:
                line = line.removesuffix('){')
                parsed_math = cp.parseComparitive(line)
                
                scoping.updateScope('elif-statement')
                
                self.parser_list.append(
                    {
                        'operation': 'if-statement',
                        'math': parsed_math,
                        'scope': scoping.gsscope
                    }
                )
        
        elif line.startswith('}else') == True:
            line = line.removeprefix('}else{')
            
            if line.endswith('}') == True:
                ...
            else:
                scoping.updateScope('else-statement')
                
                self.parser_list.append(
                    {
                        'operation': 'else-statement',
                        'scope': scoping.gsscope
                    }
                )
        
        
        elif line.startswith('while') == True:
            line = line.removeprefix('while(')
            
            if line.endswith('){}') == True:
                ...
            else:
                line = line.removesuffix('){')
                parsed_math = cp.parseComparitive(line)
                
                scoping.updateScope('while-loop')
                self.parser_list.append(
                    {
                        'operation': 'while-loop',
                        'operand': parsed_math,
                        'scope': scoping.gsscope
                    }
                )
        
        elif line.startswith('for') == True:
            line = line.removeprefix('for(')
            
            if line.endswith('){}') == True:
                ...
            else:
                line = line.removesuffix('){')
                line = line.split(';')
                
                scoping.updateScope('for-loop')
                self.parser_list.append(
                    {
                        'operation': 'for-loop',
                        'variable': line[0],
                        'operand': cp.parseComparitive(line[1]),
                        'oper': line[2].removeprefix(line[0]),
                        'scope': scoping.gsscope
                    }
                )
        
        else:
            if '=' in line:
                line = line.split('=', 1)
                
                self.parser_list.append(
                    {
                        'operation': 'var-operation',
                        'variable': line[0],
                        'operation': mp.parseMathOperation(line[1])
                    }
                )
            
            elif line.endswith(')') == True:
                line = line.removesuffix(')')
                line = line.split('(', 1)
                
                unparsed_args = line[1].split(',')
                line[1] = [vp.parseType(i) for i in unparsed_args]
                
                self.parser_list.append(
                    {
                        'operation': 'call-function',
                        'arguments': line[1],
                        'name': line[0]
                    }
                )
        
    
    def return_parser(self) -> list:
        return self.parser_list