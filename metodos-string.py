course = "Curso"
my_string = "Codigo Facilito!"

""" Formato """
result = "{b} de {a}".format(b = course, a = my_string)
result = result.lower()#cambia string a minusculas
#result = result.upper()#cambia string a mayusculas
#result = result.title()#combierte string en titulo

""" Busqueda """
pos = result.find("codigo")
count = result.count("c")

""" Sustitución"""
new_string = result.replace("c", "x")

"""Split"""
new_string = result.split(" ")

print(result)
print(pos)
print(count)
print(new_string)