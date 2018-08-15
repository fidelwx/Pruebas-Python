def crear_funcion(num_uno, num_dos):#funcion closure

    def validacion():
        return num_uno > 0 and num_dos > 0

    return validacion

nueva_funcion = crear_funcion(10, 5)

print(nueva_funcion())