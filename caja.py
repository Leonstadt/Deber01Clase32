#sistema mediano para la caja de un banco
usuarios = {}
#usuarios = {"nombre":"alfredo", "valor":100.00}

def registrar_usuario():  
    nombre=input("Ingrese el nombre del usuario a registrar: ")
    if nombre in usuarios:
        print(f"El usuario {nombre} ya existe, por favor ingrese otro usuario")
    else:
        usuarios[nombre]=0
        print(f"Usuario {nombre} registrado")
    
def depositar():
    nombre=input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto=float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
        print(f"deposito de {monto} realizado con exito, nuevo saldo: {usuarios[nombre]}")
    else:
        print(f"Usuario {nombre} no existe")
           
def retirar():   
    nombre=input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        retiro=float(input("Introduce el monto a retirar: "))
        if retiro <= usuarios[nombre]:
            usuarios[nombre] -= retiro
            print(f"Retiro de {retiro} realizado con exito, nuevo saldo {usuarios[nombre]}")
        else:
            print("Saldo insuficiente")
    else:
        print(f"Usuario {nombre} no existe")    

def menu ():
    while True:
        print("Bienvenido al sistema de caja de banco")
        print("1. Registrar Usuario")
        print("2. Deposito")
        print("3. Retiro")
        print("4. Salir")

        opcion=input("Seleccione una opcion: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            depositar()
        elif opcion == '3':
            retirar()
        elif opcion == '4':
            print("Gracias por usar el sistema")
            break    
        else:
            print("Opcion invalida, por favor, intentalo nuevamente")
            
menu()
