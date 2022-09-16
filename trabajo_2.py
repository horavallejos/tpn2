import os

##################### EMBELLECEDORES ####################

#  VARIABLES COLORES
BLUE = '\033[94m'
WHITE = '\033[0m'
RED = '\033[91m'

#  LIMPIAR PANTALLA
def limpia_pant():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#  MUESTRA EL CLASICO MENSAJE DE ESPERA
def pulse_Tecla():
    print("")
    print(RED + "Pulse cualquier tecla para continuar, por favor." + WHITE)
    input()
    print("")

############## MODULOS DEL PROGRAMA ################

def verificar(op):
    while op!="0" and op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6" and op!="7" and op!="8":
        op=input(RED + "ingrese un valor entre 1 y 8, o 0 para salir -> ")
    return op


def menu_princ():
    print(WHITE + "")
    print("                         ##################################")
    print("                         |   MENU PRINCIPAL EL ACOPIO     |")
    print("                         ##################################")
    print("                         # 1 - ADMININISTRACIONES")
    print("                         # 2 - ENTREGA DE CUPOS")
    print("                         # 3 - RECEPCION")
    print("                         # 4 - REGISTRAR CALIDAD")
    print("                         # 5 - REGISTRAR PESO BRUTO")
    print("                         # 6 - REGISTRAR DESCARGA")
    print("                         # 7 - REGISTRAR TARA")
    print("                         # 8 - REPORTES")
    print("                         # 0 - FIN DEL PROGRAMA")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" + WHITE)

def menu_01_administraciones():
    print(BLUE + "")
    print("                         ##################################")
    print("                         |     MENU ADMINISTRACIONES      |")
    print("                         ##################################")
    print("                         # A - TITULARES")
    print("                         # B - PRODUCTOS")
    print("                         # C - RUBROS")
    print("                         # D - RUBROS x PRODUCTO")
    print("                         # E - SILOS")
    print("                         # F - SUCURSALES")
    print("                         # G - PRODUCTO POR TITULAR")
    print("                         # V - Volver al Menu Principal")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" + WHITE)

def menu_crud():
    print(RED + "")
    print("                         ##################################")
    print("                         |   MENU ALTA-BAJA-CONS-MODIF    |")
    print("                         ##################################")
    print("                         # A - ALTA")
    print("                         # B - BAJA")
    print("                         # C - CONSULTA")
    print("                         # M - MODIFICACION")
    print("                         # V - Volver al Menu Anterior")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" + WHITE)

def opciones2():
    flag2=True
    while flag2==True:
        limpia_pant()
        menu_crud()
        opcion=input(RED + "\n--> Ingrese de la A a la D según la opción que desea usar, o V para volver al menú anterior: \n--> " + WHITE)
            
        if opcion == "A" or opcion == "a":
            limpia_pant()
            print(BLUE + "")
            print("                          #####################################################")
            print("                          #####################################################")
            print("                          ##                                                 ##")
            print("                          ##                 ALTA DE PRODUCTO                ##")
            print("                          ##                                                 ##")
            print("                          #####################################################")
            print("                          #####################################################")
            pulse_Tecla()

        elif opcion == "B" or opcion == "b":
            limpia_pant()
            print("                         #####################################################")
            print("                         #####################################################")
            print("                         ##                                                 ##")
            print("                         ##                 BAJA DE PRODUCTO                ##")
            print("                         ##                                                 ##")
            print("                         #####################################################")
            print("                         #####################################################")
            pulse_Tecla()

        elif opcion == "C" or opcion == "c":
            limpia_pant()
            print(BLUE + "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##             CONSULTA DE PRODUCTO                ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################" + WHITE)
            pulse_Tecla()

        elif opcion == "M" or opcion == "m":
            limpia_pant()
            print(BLUE + "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##           MODIFICACION DE PRODUCTO              ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################"+ WHITE)
            pulse_Tecla()
            
        elif opcion == "V" or opcion == "v":
            flag2=False

def opciones1():
    flag1=True
    while flag1==True:
        limpia_pant()
        menu_01_administraciones()
        opcion=input(BLUE + "\n--> Ingrese de la A a la G según la opción que desea usar, o V para volver al menú anterior: \n--> " + WHITE)
        if opcion == "A" or opcion == "a":
            opciones2()
            
        elif opcion == "B" or opcion == "b":
            opciones2()

        elif opcion == "C" or opcion == "c":
            opciones2()

        elif opcion == "D" or opcion == "d":
            opciones2()

        elif opcion == "E" or opcion == "e":
            opciones2()

        elif opcion == "F" or opcion == "f":
            opciones2()

        elif opcion == "G" or opcion == "g":
            opciones2()

        elif opcion == "V" or opcion == "v":
            flag1=False
    

flag=True
while flag==True:
    limpia_pant()    
    menu_princ()
    
    op=input("ingrese un valor entre 1 y 8, o 0 -> ")
    opc=verificar(op)
  
    if opc == "1":
        opciones1()
    elif opc =="2":
        print("estas en la op 2")
    elif opc =="3":
        print("estas en la op 3")
    elif opc =="4":
        print("estas en la op 4")
    elif opc =="5":
        print("estas en la op 5")
    elif opc =="6":
        print("estas en la op 6")
    elif opc =="7":
        print("estas en la op 7")
    elif opc =="8":
        print("estas en la op 8")
    elif opc =="0":
        flag=False

print("see you later, aligator...")