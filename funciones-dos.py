def suma (valor_uno, valor_dos, valor_tres):
    return valor_uno + valor_dos + valor_tres

def division (valor_uno, valor_dos):
    return valor_uno / valor_dos

def multiplicar (valor_uno, valor_dos = 6):#si y solo si no se envia un valors
    return valor_uno * valor_dos

def multiples_valores ():
    return 'String', 1, True, 25.6

#resultado = multiplicar(6, 10)
#print(resultado)

def mostrar_resultado( funcion ):
    print ( funcion(6,8) )

mi_variable = multiplicar
mostrar_resultado(mi_variable)

string, entero, bouleano, flotante = multiples_valores()

print(string)
print(entero)
print(bouleano)
print(flotante)