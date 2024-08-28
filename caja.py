# #sistema mediano para la caja de un banco
usuarios = {}
usuarios = {"nombre":"alfredo", "valor":100.00}
# def depositar():
#     nombre=input("Introduce el nombre de Usuario: ")
#     monto=float(input("Introduce el monto a depositar: "))
#     usuarios[nombre] += monto

# usuarios = []
# cuentas = []

# usuario = {"nombre":"alfredo", "estado": "A"}
# usuarios.append(usuario)
# cuenta = {"nombre":"alfredo", "valor":100.00}
# cuentas.append(cuenta)

def depositar():
    # nombre=input("Introduce el nombre de usuario: ")
    # monto=float(input("Introduce el monto a depositar: "))
    # for cuenta_guardada in cuentas:
    #     if (cuenta_guardada["nombre"] == nombre):
    #         cuenta_guardada["valor"] += monto
    nombre=input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto=float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
    else:
        print(f"Usuario {nombre} no existe")
        
def registrar_usuario():
    global usuarios
    nombre=input("Ingrese el nombre del usuario a registrar: ")
    if nombre in usuarios:
        print(f"El usuario {nombre} ya existe, por favor ingrese otro usuario")
        return
    
    monto=float(input("Ingrese el monto inicial a depositar: "))
    usuarios ={"nombre":nombre, "monto":monto}
    
    print(f"Usuario {nombre} registrado, con {monto}")
    
def retirar():
    
    nombre=input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        retiro=float(input("Introduce el monto a retirar: "))
        usuarios[nombre] -= retiro
    else:
        print(f"Usuario {nombre} no existe")

depositar()
print(usuarios)



