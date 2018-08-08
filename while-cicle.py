contador = 0
bandera = True

while bandera:
    print(contador)
    contador +=1

    if contador == 5:
        continue #permite ejecutar el codigo aunque falten las instrucciones anidadas
    if contador == 6:
        #break #finaliza la ejecución del ciclo
        bandera = False
else:
    print('el while a terminado')