class TypeTemplates:
    def __init__(self) -> None:
        ...
    
    def pointer_template(self, adress: str) -> dict:
        return {
            'adress': adress,
            'format': 'hex16',
            'decimal': int(adress, 16),
            'base-class': 'pointer'
        }
    
    def intager_template(self, value: int) -> dict:
        return {
            'value': value,
            'format': 'decimal',
            'hex': hex(value),
            'binary': bin(value).removeprefix('0b'),
            'base-class': 'intager'
        }
    
    def function_template(self, value: str) -> dict:
        value = value.removesuffix(')')
        value = value.split('(', 1)
                
        unparsed_args = value[1].split(',')
        value[1] = [parseType(i) for i in unparsed_args]
        return {
            'base-class': 'function',
            'name': value[0],
            'arguments': value[1]
        }
    
    def string_template(self, value: str) -> dict:
        return {
            'value': value,
            'strlen': len(value),
            'ascii': '\00'.join([ord(str(i)) for i in value]),
            'base-class': 'string'
        }
    
    def float_template(self, value: float) -> dict:
        stringify = str(value).split('.', 1)
        return {
            'value': value,
            'rint': round(value),
            'binary': f'{bin(int(stringify[0])).removeprefix('0b')}{bin(int(stringify[1])).removeprefix('0b')}',
            'base-class': 'float'
        }
    
    def bool_template(self, value: str) -> dict:
        if value == 'true':
            return TypeTemplates().intager_template(1)
        elif value == 'false':
            return TypeTemplates().intager_template(0)
    
    def undefined_template(self, value: str) -> dict:
        return {
            'value': value,
            'base-class': '???'
        }

def parseType(value: str) -> dict:
    gtype = 'undefined'
    
    if value.startswith('"'):
        return TypeTemplates().string_template(value)
    elif value.isdigit():
        return TypeTemplates().intager_template(int(value))
    elif '.' in value:
        return TypeTemplates().float_template(float(value))
    
    elif 'true' == value:
        return TypeTemplates().bool_template(value)
    elif 'false' == value:
        return TypeTemplates().bool_template(value)
    
    try:
        int(value, 16)
        return TypeTemplates().pointer_template(value)
    except ValueError:
        return TypeTemplates().undefined_template(value)