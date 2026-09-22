from paciente import Paciente
Pacientes:list[Paciente]=[]

def leer_numero(mensaje:str)->int:
    while true:
        try:
            numero=int(input(mensaje))
            return numero
            except ValueError:
                print("Error. Debe ingresar un número entero.")

def menu():
    print("="*20)
    print("Menú de Clínica")
    print("="*20)
    print("1.- Agregar Paciente")
    print("2.- Editar Paciente")
    print("3.- Eliminar Paciente")
    print("4.- Mostrar Pacientes")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    op=leer_numero("Ingrese una opción: ")
    print("="*20)
    return op
    
def agregar_paciente()-> None:
    rut=input("Ingrese el Rut del Paciente: ")
    nombre=input("Ingrese nombre del Paciente: ")
    edad=leer_numero("Ingrese edad del Paciente: ")
    print("Seleccione previsión del Paciente: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    op=leer_numero("Seleccione una previsión del paciente: ")
    if op==1:
        prevision="Fonasa"
    elif op==2:
        prevision="Isapre"
    elif op==3:
        prevision="Particular"
    elif op==4:
        prevision="Otro"

    paciente=Paciente(rut,nombre,edad,prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente")
    print(f"Total de Pacientes: (len(pacientes))")

def main():
    while True:
        opción=menu()
        if opcion==1:
            print("Agregar Paciente")
        elif opcion==2:
            print("Editar Paciente")
        elif opcion==3:
            print("Eliminar Paciente")
        elif opcion==4:
            print("Mostrar un Paciente")
        elif opcion==5:
            print("Mostrar todos los Pacientes")
        elif oipcion==0:
            print("Saliendo del Prtograma...")
            break
        else:
            print("Opción Inválida. Intente Nuevamente")


if __name__=="__main__":
    main()