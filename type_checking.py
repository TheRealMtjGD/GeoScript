from Components import error_handler
from Components import gsconfig
from Components import memory_manager

def controllFlowTypeChecking(comp1: dict, comp2: dict, traceback: error_handler.GSTraceback) -> None:
    if not comp1['base-class'] == comp2['base-class']:
        if gsconfig.GSCONFIG.TYPE_CHECKING == 'strict':
            error_handler.ThrowError('TypeError', f'Unsupported comparison between {comp1['base-class']} and {comp2['base-class']}', traceback)
        elif gsconfig.GSCONFIG.TYPE_CHECKING == 'moderite':
            error_handler.ThrowWarning('TypeError', f'Unsupported comparison between {comp1['base-class']} and {comp2['base-class']}', traceback)

def mathOperationTypeChecking(math: list, traceback: error_handler.GSTraceback) -> None:
    for statement in math:
        if not statement[0]['base-class'] == statement[2]['base-class']:
            if gsconfig.GSCONFIG.TYPE_CHECKING == 'strict':
                error_handler.ThrowError('TypeError', f'Unsupported math operation between 2 types. {statement[0]['base-class']} and {statement[2]['base-class']}', traceback)
            elif gsconfig.GSCONFIG.TYPE_CHECKING == 'moderite':
                error_handler.ThrowWarning('TypeError', f'Unsupported math operation between 2 types. {statement[0]['base-class']} and {statement[2]['base-class']}', traceback)


def implacePointer(value: dict, idstack: memory_manager.IdentifierStack, traceback: error_handler.GSTraceback) -> dict:
    if value['base-class'] == '???':
        if idstack.id_stack.get(value['value']) == None:
            error_handler.ThrowError('ValueError', 'Value presented has no descernable type', traceback)
        
        else:
            adress = idstack.id_stack.get(value['value'])
            return {
                'adress': adress,
                'format': 'hex16',
                'decimal': int(adress, 16),
                'base-class': 'pointer'
            }