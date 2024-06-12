import os
import time
os.system("cls")
trabajadores=[]
while True:
    try:
        print("Menu")
        print("------------------------")
        print("1) Registrar Trabajador")
        print("2) Lista de todos los trabajadores")
        print("3) Imprimir planilla de sueldos")
        print("4) Salir del Programa")
        opc=int(input("Ingrese opción: "))

        if opc==1:
            os.system("cls")
            print("REGISTRO DE TRABAJADOR")
            nombre=input("Ingrese Nombre:\n")
            apellido=input("Ingrese Apellido:\n")
            cargo=input("Ingrese Cargo:\n")
            sueldo_bruto=int(input("Ingrese Sueldo Bruto:\n"))
            
            trabajadores.append(nombre)
            trabajadores.append(apellido)
            trabajadores.append(cargo)
            trabajadores.append(sueldo_bruto)

            descuentosalud=sueldo_bruto*7/100
            descuentoafp=sueldo_bruto*12/100
            os.system("cls")

        elif opc==2:
            os.system("cls")
            print("LISTA DE TODOS LOS TRABAJADORES")
            for x in range(len(trabajadores)):
             print(f"Trabajadores: {nombre}, Apellidos: {apellido}")
             input("<<Presione tecla para continuar>>")
             os.system("cls")

        elif opc==3:
            os.system("cls")
            print("PLANILLA DE SUELDOS")
            for x in range(len(trabajadores)):
                print(f"Trabajador: {nombre} | Cargo: {cargo} | Sueldo Bruto: {sueldo_bruto}")
                input("<<Presione tecla para continuar>>")
                os.system("cls")
        elif opc==4:
            print("Hasta Luego!")
            break

        else:
            print("Error! Ingrese un numero valido!")
            time.sleep(1)
            os.system("cls")
            continue

    except:
        print("Error! Ingrese un numero valido!")
        time.sleep(1)
        os.system("cls")
        continue