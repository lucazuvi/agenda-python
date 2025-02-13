

def menu():
    print('\n')
    print('-----AGENDA DE CONTACTOS-----\n')
    print('1. Agregar nuevo contacto')
    print('2. Eliminar contacto')
    print('3. Buscar contacto')
    print('4. Lista de contactos')
    print('5. Salir del menu.\n')


def agregarContacto(agenda):
    nombre = input('Nombre completo del nuevo contacto: ')
    telefono = input("Numero del contacto: ")
    email = input("Email del contacto: ")
    agenda[nombre] = {'telefono': telefono, 'email': email}
    print(f'Se agrego con exito el contacto {nombre}.')

def eliminarContacto(agenda):
    nombre = input('Elija el nombre del contacto a eliminar: ')
    if nombre in agenda:
        del agenda[nombre]
        print(f'El contacto {nombre} ha sido eliminado con exito!')
    else:
        print(f'No se ha encontrado el nombre {nombre} en tus contactos.')

def buscarContacto(agenda):
    nombre = input('Ingresa el nombre del contacto que buscas: ')
    if nombre in agenda:
        print(f'Nombre: {nombre}')
        print(f'Telefono: {agenda[nombre]['telefono']}')
        print(f'Email: {agenda[nombre]['email']}')
    else:
        print(f'{nombre} no ha sido encontrado en la agenda.')

def mostrarAgenda(agenda):
    if agenda:
        print('\nLista de contactos: ')
        for nombre, info in agenda.items():
            print(f'Nombre: {nombre}')
            print(f'Telefono: {info['telefono']}')
            print(f'Email: {info['email']}')
            print('-' * 20)
    else:
        print('\nLa agenda esta vacia.')

def agendaContactos():
    agenda = {}

    while True:
        menu()
        opcion = input('Por favor, elija la opcion a realizar: ')

        if opcion == "1":
            agregarContacto(agenda)
        elif opcion == "2":
            eliminarContacto(agenda)
        elif opcion == "3":
            buscarContacto(agenda)
        elif opcion == "4":
            mostrarAgenda(agenda)
        elif opcion == "5":
            print('Saliendo del menu.')
            break
        else:
            print('Elija una opcion disponible del menu (del 1 al 5).')
    
agendaContactos()



