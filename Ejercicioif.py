nombre = ""
edad = 0
nacionalidad = ""

nombre= input("Ingresa tu nombre: ")
edad= int(input("Ingresa tu edad: "))
nacionalidad= input("Ingresa tu nacionalidad: ")

if edad >= 18:
    print("Eres mayor de edad") 
else:
    print("No eres mayor de edad")

if nacionalidad == "N":
    print("Eres de nacionalidad mexicana")
else:
    print("No eres de nacionalidad mexicana")