import random

personas = []

def verificar_nif(nif):
    if len(nif) != 12:
        return False
    if not nif[:8].isdigit() or not nif[8] == "-" or not nif[9:].isalpha():
        return False
    return True

def grabar_persona():
    while True:
        nif = input("Ingrese el NIF de la persona (ejemplo: 99999999-RTX): ")
        if verificar_nif(nif):
            break
        print("Error: NIF incorrecto. Por favor, ingrese nuevamente.")

    while True:
        nombre = input("Ingrese el nombre de la persona: ")
        if len(nombre) >= 8:
            break
        print("Error: El nombre debe tener al menos 8 caracteres. Por favor, ingrese nuevamente.")

    while True:
        edad = int(input("Ingrese la edad de la persona: "))
        if edad >= 0:
            break
        print("Error: La edad debe ser mayor o igual a 0. Por favor, ingrese nuevamente.")

    pertenece_union_europea = input("¿La persona pertenece a la Unión Europea? (Sí/No): ")
    estado_conyugal = input("Ingrese el estado conyugal de la persona: ")
    tiene_certificado_nacimiento = input("¿La persona tiene certificado de nacimiento? (Sí/No): ")

    persona = {
        "nif": nif,
        "nombre": nombre,
        "edad": edad,
        "pertenece_union_europea": pertenece_union_europea,
        "estado_conyugal": estado_conyugal,
        "tiene_certificado_nacimiento": tiene_certificado_nacimiento
    }
    personas.append(persona)
    print("Persona registrada exitosamente.")

def buscar_persona():
    nif = input("Ingrese el NIF de la persona que desea buscar: ")
    for persona in personas:
        if persona["nif"] == nif:
            print("Información de la persona:")
            print(f"NIF: {persona['nif']}")
            print(f"Nombre: {persona['nombre']}")
            print(f"Edad: {persona['edad']}")
            print(f"Pertenece a la Unión Europea: {persona['pertenece_union_europea']}")
            print(f"Estado conyugal: {persona['estado_conyugal']}")
            print(f"Tiene certificado de nacimiento: {persona['tiene_certificado_nacimiento']}")
            return
    print("Persona no encontrada.")

def imprimir_certificados():
    for persona in personas:
        print("--------------------------------------")
        print("Certificado de Nacimiento:")
        print("--------------------------------------")
        print(f"Nombre del certificado: Nacimiento")
        print(f"NIF de la persona: {persona['nif']}")
        print(f"Datos de la persona: {persona['nombre']}, {persona['edad']} años")
        print(f"Tiene certificado de nacimiento: {persona['tiene_certificado_nacimiento']}")
        print("--------------------------------------")

        print("Certificado de Estado Conyugal:")
        print("--------------------------------------")
        print(f"Nombre del certificado: Estado Conyugal")
        print(f"NIF de la persona: {persona['nif']}")
        print(f"Datos de la persona: {persona['nombre']}, {persona['edad']} años")
        print(f"Estado conyugal: {persona['estado_conyugal']}")
        print("--------------------------------------")

        print("Certificado de Pertenencia a la Unión Europea:")
        print("--------------------------------------")
        print(f"Nombre del certificado: Pertenencia a la Unión Europea")
        print(f"NIF de la persona: {persona['nif']}")
        print(f"Datos de la persona: {persona['nombre']}, {persona['edad']} años")
        print(f"Pertenece a la Unión Europea: {persona['pertenece_union_europea']}")
        print("--------------------------------------")

def salir_programa(nombre_apellido, version):
    print("--------------------------------------")
    print(f"¡Hasta luego, {nombre_apellido}!")
    print(f"Versión del programa: {version}")
    print("--------------------------------------")

def menu():
    print("==============================================================")
    print("Bienvenido al Registro de Ciudadanos pertenecientes a la Union Europea de la Region Sur de Andalucia")
    print("==============================================================")
    print("Necesitamos primero su Nombre y Apellido (Ingrese por Separado)")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombre_apellido = f"{nombre} {apellido}"
    version = "1.0" 

    while True:
        print("=====MENU=DE=OPCIONES=====")
        print("1. Grabar persona")
        print("2. Buscar persona")
        print("3. Imprimir certificados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            grabar_persona()
        elif opcion == "2":
            buscar_persona()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            salir_programa(nombre_apellido, version)
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
