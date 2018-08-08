fruta = 'manzana'

if fruta == 'kiwis':# < > <= >= != ==
    print('el valor es kiwi')
elif fruta == 'manzana':
    print('es una manzana')
elif fruta == 'pera':
    pass #permite ejecutar el codigo aunque falten las instrucciones anidadas
else:
    print('no son iguales')

valor = None
valor_dos = 21

if valor and valor_dos>20:
    print('es verdad')
else:
    print('es falso')