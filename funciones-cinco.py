mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos
formato = lambda sentencia : '¿{}?'.format(sentencia)
no_valor = lambda : 10
no_retorno = lambda : print('debe ejecutar una acción')

resultado = mi_funcion(10, 20)
print(resultado)

resultado = formato('puedes hacer esto una pregunta')
print(resultado)

resultado = no_valor()
print(resultado)

resultado = no_retorno()