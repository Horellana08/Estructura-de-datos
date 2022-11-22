from stat import IO_REPARSE_TAG_APPEXECLINK

# Agenda telefonica
agenda = []
ingreso = input("Desesa agregar un contacto: y/n \n")

while ingreso.lower() in "y":
    nombre = input("Ingrese el nombre del contacto:\n")
    numero= input("Ingrese el numero de telefonico del contacto:\n")

    contacto =[nombre, numero]
    agenda.append(contacto)
    ingreso = input("Desea agregar otro contacto: y/n \n")

    print(agenda)