from components import error_handler
from components import value_parser
from components import memory_allocator

class GSLexer:
    def remove_whitespace(self, line: str) -> str:
        while line.startswith(' ') == True:
            line = line.removeprefix(' ')
        while line.startswith('\n') == True:
            line = line.removeprefix('\n')
        while line.endswith(' ') == True:
            line = line.removesuffix(' ')
        while line.endswith('\n') == True:
            line = line.removesuffix('\n')
        
        return line
    
    def __subparse_opb(self, operation: str, split: str) -> int:
        return len(operation.split(split, 1))
    
    def parse_operation_block(self, operation_statement: str, traceback: error_handler.GSTraceback) -> list:
        for i in ['==', '<=', '<', '>', '>=', '!=']:
            if not self.__subparse_opb(operation_statement, i) == 1:
                ops =  operation_statement.split(i)
                ops.insert(1, i)
                return ops
        
        error_handler.raise_error('ComparitiveError', 'Set comparitive does not exist', traceback)
    
    def strip_whitespace(self, line: str) -> str:
        nline =  ''.join(line.split(' '))
        return nline
    
    def change_scope(self, scope: str) -> None:
        if scope == '..':
            if '.' in self.scope:
                self.scope = self.scope.split('.')
                del self.scope[-1]
                self.scope = '.'.join(self.scope)
            
            else:
                self.scope = ''
        
        else:
            self.scope = f'{self.scope}.{scope}'
    
    def __init__(self, file: str, string: str) -> None:
        self.lexer_array = []
        self.safemode = False
        self.scope = ''
        
        def main():
            for index, line in enumerate(string.split('\n'), 1):
                line = self.remove_whitespace(line)
                debug = {'linenum': index, 'recov-line': line, 'file': file, 'scope': self.scope, 'traceback': error_handler.GSTraceback(index, line, file)}
                gstraceback = error_handler.GSTraceback(index, line, file)
                
                if self.safemode == True:
                    continue
                
                if line.startswith('//') == True:
                    continue
                elif line == '...':
                    continue
                elif line == '':
                    continue
                
                elif line == '}':
                    self.change_scope('..')
                    continue
                
                if line.startswith('#') == True:
                    self.definitive_statements(line, debug, gstraceback)
                elif line.startswith('@') == True:
                    self.structual_statements(line, debug, gstraceback)
                else:
                    self.ctf_jlp_statements(line, debug, gstraceback)
        
        main()
    
    def definitive_statements(self, line: str, debug: dict, traceback_debug: error_handler.GSTraceback) -> None:
        if line.startswith('#define ') == True:
            line = self.strip_whitespace(line)
            line = line.removeprefix('#define')
            line = line.split(':', 1)
            line[1] = line[1].split('=', 1)
            
            namecheck = value_parser.namespace_checker(line[0])
            if namecheck[0] == False:
                error_handler.raise_error('InvalidNamespace', f'Variable cannot have "{namecheck[1]}" in it', traceback_debug)
            
            self.lexer_array.append(
                {
                    'callback': 'allocate-variable',
                    'namespace': line[0],
                    'type': line[1][0],
                    'value': line[1][1],

                    'debug': debug
                }
            )
            memory_slot = memory_allocator.allocateMemory()
            memory_slot.allocate_value(value_parser.value_parser(line[1][0], line[1][1], traceback_debug), line[1][0], 'var')
            memory_slot.allocate_namespace(line[0])
        
        elif line.startswith('#const ') == True:
            line = self.strip_whitespace(line)
            line = line.removeprefix('#const')
            line = line.split(':', 1)
            line[1] = line[1].split('=', 1)
            
            namecheck = value_parser.namespace_checker(line[0])
            if namecheck[0] == False:
                error_handler.raise_error('InvalidNamespace', f'Constant cannot have "{namecheck[1]}" in it', traceback_debug)
            
            self.lexer_array.append(
                {
                    'callback': 'allocate-constant',
                    'namespace': line[0],
                    'type': line[1][0],
                    'value': line[1][1],

                    'debug': debug
                }
            )
            memory_slot = memory_allocator.allocateMemory()
            memory_slot.allocate_value(value_parser.value_parser(line[1][0], line[1][1], traceback_debug), line[1][0], 'const')
            memory_slot.allocate_namespace(line[0])
        
        elif line.startswith('#indef ') == True:
            line = line.removeprefix('#indef ')
            line = line.split(' ', 1)
            
            namecheck = value_parser.namespace_checker(line[0])
            if namecheck[0] == False:
                error_handler.raise_error('InvalidNamespace', f'Macro cannot have "{namecheck[1]}" in it', traceback_debug)
            
            self.lexer_array.append(
                {
                    'callback': 'allocate-macro',
                    'namespace': line[0],
                    'macro': line[1],

                    'debug': debug
                }
            )
            
            memory_allocator.MacroTable[line[0]] = line[1]
        
        elif line.startswith('#function ') == True:
            line = line.removeprefix('#function ')
            line = self.strip_whitespace(line)
            line = line.split('(')
            line[1] = line[1].removesuffix('){')
            line[1] = line[1].split(',')
            
            namecheck = value_parser.namespace_checker(line[0])
            if namecheck[0] == False:
                error_handler.raise_error('InvalidNamespace', f'Function name cannot have "{namecheck[1]}" in it', traceback_debug)
            
            self.lexer_array.append(
                {
                    'callback': 'allocate-function',
                    'namespace': line[0],
                    'arguments': line[1],
                    'jmp-scope': f'{debug['scope']}.{line[0]}',
                    
                    'debug': debug
                }
            )
            
            self.change_scope(line[0])
            
            for i in line[1]:
                malloc = memory_allocator.allocateMemory()
                malloc.allocate_namespace(i)
        
        else:
            error_handler.raise_error('InvalidDefinitiveStatement', 'Definitive statement does not exist (#define, #const, #indef, #function)', traceback_debug)
    
    def structual_statements(self, line: str, debug: dict, traceback_debug: error_handler.GSTraceback) -> None:
        if line.startswith('@gotospace ') == True:
            line = line.removeprefix('@gotospace ')
            self.change_scope(line)
            
            if value_parser.namespace_checker(line)[0] == False:
                error_handler.raise_error('NamespaceError', f'Classes cannot have the character "{value_parser.namespace_checker(line)[1]}" in there name', traceback_debug)
        
        elif line.startswith('@goto ') == True:
            line = line.removeprefix('@goto ')
            
            self.lexer_array.append(
                {
                    'callback': 'code-jump',
                    'scope': line,
                    
                    'debug': debug
                }
            )
        
        elif line.startswith('@struct ') == True:
            line = line.removeprefix('@struct ')
            line = self.strip_whitespace(line)
            line = line.removesuffix('{')
            
            if value_parser.namespace_checker(line)[0] == False:
                error_handler.raise_error('NamespaceError', f'Classes cannot have the character "{value_parser.namespace_checker(line)[1]}" in there name', traceback_debug)
            
            self.change_scope(line)
        
        elif line.startswith('@class ') == True:
            line = line.removeprefix('@class ')
            line = self.strip_whitespace(line)
            line = line.removesuffix('{')
            line = line.split('(')
            
            if value_parser.namespace_checker(line[0])[0] == False:
                error_handler.raise_error('NamespaceError', f'Classes cannot have the character "{value_parser.namespace_checker(line[0])[1]}" in there name', traceback_debug)
            
            try:
                line[1] = line[1].removesuffix(')')
                inheritance = line[1].split(',')
            except IndexError:
                inheritance = None
            
            self.lexer_array.append(
                {
                    'callback': 'allocate-class',
                    'inherit_classes': inheritance,
                    'name': line,
                    
                    'debug': debug
                }
            )
            
            self.change_scope(line)
        
        elif line.startswith('@spawn_group ') == True:
            line = line.removeprefix('@spawn_group ')
            line = line.split(' ')
            
            self.lexer_array.append(
                {
                    'callback': 'spawn-group',
                    'group': line[0],
                    'delay': line[1],
                    
                    'debug': debug
                }
            )
        
        elif line.startswith('@place_obj ') == True:
            line = line.removeprefix('@place_obj ')
            
            self.lexer_array.append(
                {
                    'callback': 'add-obj',
                    'object': line,
                    
                    'debug': debug
                }
            )
        
        else:
            error_handler.raise_error('InvalidStructualStatement', 'Structual statement does not exist (@goto, @gotospace, @struct, @class)', traceback_debug)
    
    def ctf_jlp_statements(self, line: str, debug: dict, traceback_debug: error_handler.GSTraceback) -> None:
        if line.startswith('if ') == True:
            line = line.removeprefix('if (')
            line = self.strip_whitespace(line)
            if line.endswith('{}') == True:
                return None
            line = line.removesuffix('){')
            
            operation = self.parse_operation_block(line, traceback_debug)
            
            self.lexer_array.append(
                {
                    'callback': 'if-statement',
                    'operation': operation,
                    'jmp-scope': f'{self.scope}.controll-flow-if',
                    
                    'debug': debug
                }
            )
            self.change_scope('..')
            self.change_scope('controll-flow-if')
        
        elif line.startswith('} else if ') == True:
            line = line.removeprefix('} else if (')
            line = self.strip_whitespace(line)
            if line.endswith('{}') == True:
                return None
            line = line.removesuffix('){')
            
            operation = self.parse_operation_block(line, traceback_debug)
            
            self.lexer_array.append(
                {
                    'callback': 'elif-statement',
                    'operation': operation,
                    'jmp-scope': f'{self.scope}.controll-flow-elif',
                    
                    'debug': debug
                }
            )
            self.change_scope('..')
            self.change_scope('controll-flow-elif')
        
        elif line.startswith('} else ') == True:
            line = line.removeprefix('} else {')
            line = self.strip_whitespace(line)
            if line.endswith('}') == True:
                return None
            
            self.lexer_array.append(
                {
                    'callback': 'else-statement',
                    'jmp-scope': f'{self.scope}.controll-flow-else',
                    
                    'debug': debug
                }
            )
            self.change_scope('..')
            self.change_scope('controll-flow-else')
        
        
        elif line.startswith('while ') == True:
            line = line.removeprefix('while (')
            line = self.strip_whitespace(line)
            if line.endswith('{}') == True:
                return None
            line = line.removesuffix('){')
            
            operation = self.parse_operation_block(line, traceback_debug)
            debug['scope'] = f'{debug['scope']}.while-loop'
            
            self.lexer_array.append(
                {
                    'callback': 'while-loop',
                    'operation': operation,
                    'jmp-scope': self.scope,
                    
                    'debug': debug
                }
            )
            self.change_scope('loops-while')
        
        elif line.startswith('for ') == True:
            line = line.removeprefix('for (')
            line = self.strip_whitespace(line)
            
            if line.endswith('{}') == True:
                return None
            
            line = line.removesuffix('){')
            line = line.split(',')
            
            variable = line[0].removesuffix(': intager')
            operation = self.parse_operation_block(line[1], traceback_debug)
            var_operation = line[2].removeprefix(variable)
            
            memory_allocator.allocateMemory().allocate_namespace(variable)
            debug['scope'] = f'{debug['scope']}.for-loop'
            
            self.lexer_array.append(
                {
                    'callback': 'for-loop',
                    'variable': variable,
                    'operation': operation,
                    'var-operation': var_operation,
                    'jmp-scope': self.scope,
                    
                    'debug': debug
                }
            )
            self.change_scope('loops-for')
            
        
        
        elif '=' in line:
            line = self.strip_whitespace(line)
            
            if '+=' in line:
                line = line.split('+=', 1)
                
                self.lexer_array.append(
                    {
                        'callback': 'modify',
                        'target': line[0],
                        'modification': 'add',
                        'amount': line[1],

                        'debug': debug
                    }
                )
            
            elif '-=' in line:
                line = line.split('-=', 1)
                
                self.lexer_array.append(
                    {
                        'callback': 'modify',
                        'target': line[0],
                        'modification': 'sub',
                        'amount': line[1],

                        'debug': debug
                    }
                )
            
            elif '*=' in line:
                line = line.split('*=', 1)
                
                self.lexer_array.append(
                    {
                        'callback': 'modify',
                        'target': line[0],
                        'modification': 'multiply',
                        'amount': line[1],

                        'debug': debug
                    }
                )
            
            elif '/=' in line:
                line = line.split('/=', 1)
                
                self.lexer_array.append(
                    {
                        'callback': 'modify',
                        'target': line[0],
                        'modification': 'divide',
                        'amount': line[1],

                        'debug': debug
                    }
                )
        
        elif line.endswith(')') == True:
            line = self.strip_whitespace(line)
            line = line.split('(')
            line[1] = line[1].removesuffix(')')
            
            if line[1] == '':
                line[1] = None
            else:
                line[1] = line[1].split(',')
            
            self.lexer_array.append(
                {
                    'callback': 'function-call',
                    'function-name': line[0],
                    'arguments': line[1],
                    
                    'debug': debug
                }
            )
        
        else:
            error_handler.raise_error('UndefinedState', 'Line is not recognised as an definitive statement, structual statement, controll flow, loop, function call or modification', traceback_debug)
