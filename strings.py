my_string = "Hola Mundo!"
my_string = """Este es un string que\ncontiene saltos de linea"""

course = "Python 3"
name = "Eduardo"

final_message = "Nuevo Curso de " + course + " por " + name#1
final_message = "Nuevo Curso de %s por %s" % (course, name)#2
final_message = "Nuevo Curso de {} por {}".format(course, name)#3

print(my_string)
print(final_message)