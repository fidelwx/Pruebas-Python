diccionario = { "a":55, 5:'esto es un string', (1,2):False } #claves deben ser inmutables

diccionario['c'] = 'nuevo string' #si la llave no existe, crea nueva clave/valor
diccionario['a'] = True #si la llave existe, actualiza valor

#valor = diccionario['a']
valor = diccionario.get('z', 'la llave no existe')

#del diccionario[5] #del permite eliminar

#print(diccionario)
#print(valor)

llaves = list ( diccionario.keys() ) #objeto iterablen
valores = tuple (diccionario.values())

diccionario_dos = {'z':23, 'w':88}

diccionario.update(diccionario_dos)

#print(llaves)
#print(valores)
print(diccionario)
