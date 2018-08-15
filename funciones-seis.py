def division(num_uno, num_dos):

    def validacion():
        return num_uno > 0 and num_dos > 0

    if validacion():
        return num_uno / num_dos

resultado = division(10,0)
print(resultado)