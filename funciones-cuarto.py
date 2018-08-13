"""def suma (*args):
    resultado = 0
    for i in args:
        resultado = resultado + i
    return resultado
"""

def suma (**kwargs):
    return(kwargs)


reultado = suma(valor = 'eduardo', x=2, y=9, z=True)
print(reultado)