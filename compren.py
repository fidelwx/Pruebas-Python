lista = [ i for i in range(0,101) if i % 2 ==0 ]
#1- valor a agregar a la lista
#2- un ciclo, for

tupla = tuple( ( i for i in range(0,101) if i % 2 !=0 ) )

diccionario = { indice:valor for indice, valor in enumerate(lista) if indice < 10 }

#print(lista)
#print(tupla)
print(diccionario)