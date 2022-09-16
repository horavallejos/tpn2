import os
import sys

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
    print( "Pulse cualquier tecla para continuar, por favor." )
    input()
    print("")

############## MODULOS DEL PROGRAMA ################

def verificar(op):
    while op!="0" and op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6" and op!="7" and op!="8":
        op=input( "ingrese un valor entre 1 y 8, o 0 para salir -> ")
    return op


#### CREAMOS LOS ARRAYS ####

# ARRAY UNIDIMENSIONAL PRODUCTOS
productos=[" "]*3
for i in range (3):
    productos[i]=" "

# ARRAY BIDIMENSIONAL CUPOS
cupos=[" "]*8
for fil in range (8):
    cupos[fil]=[" "]*3

# ARRAY BIDIMENSIONAL DATOS
datos=[0]*8
for fil in range (8):
    datos[fil]=[0]*3

# ARRAY BIDIMENSIONAL PATENTES MAY y MEN
pate=[" "]*3
for fil in range (3):
    pate[fil]=[" "]*2

# ARRAY BIDIMENSIONAL PESOS MAY y MEN
peso=[0]*3
for fil in range (3):
    peso[fil]=[0]*4

dat=datos

cup=cupos

pat=pate

pesos=peso

def menu_princ():
    print( "")
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
    print("" )

def menu_01_administraciones():
    print( "")
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
    print("" )

def menu_crud():
    print( "")
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
    print("" )

def crud():
    flag2=True
    while flag2==True:
        limpia_pant()
        menu_crud()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
            
        if opcion == "A" or opcion == "a":
            limpia_pant()
            print( "")
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
            print( "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##             CONSULTA DE PRODUCTO                ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################" )
            pulse_Tecla()

        elif opcion == "M" or opcion == "m":
            limpia_pant()
            print( "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##           MODIFICACION DE PRODUCTO              ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################")
            pulse_Tecla()
            
        elif opcion == "V" or opcion == "v":
            flag2=False

def crud_productos():
    flag=True
    while flag==True:
        limpia_pant()
        menu_crud()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
            
        if opcion == "A" or opcion == "a":
            limpia_pant()
            alta_productos()
            pulse_Tecla()
                  
        elif opcion == "B" or opcion == "b":
            limpia_pant()
            baja_prod()
            pulse_Tecla()

        elif opcion == "C" or opcion == "c":
            limpia_pant()
            mostrar_productos()
            pulse_Tecla()

        elif opcion == "M" or opcion == "m":
            limpia_pant()
            modifica_prod()
            pulse_Tecla()
            
        elif opcion == "V" or opcion == "v":
            flag=False

def alta_productos():
    prod=input("INGRESE UN PRODUCTO :-> ")
    while prod=="" or prod==" " or prod==None or len(prod)>7:
        prod=input("INGRESE UN PRODUCTO :-> ")
    prod=prod.upper()
    i=0
    while i<2 and productos[i]!=" ":
        i+=1
    if productos[i]==" ":
        alta_prod(prod)
    else:
        if i<=2 and productos[i]!=" ":
            print("LISTA DE PRODUCTOS LLENA. BORRE ALGUN PRODUCTO O INTENTE MAÑANA :) ")
    
def alta_prod(prod):
    i=0
    while prod!=productos[i] and i<2:
        i+=1
    if prod!=productos[i]:
        i=0
        while productos[i]!=" ":
            i+=1
        productos[i]=prod
        print(f"El producto {prod} se ha agregado correctamente")
    else:
        print(f"El producto {prod} ya se encuentra registrado")
    
def mostrar_productos():
    if productos[0]==" " and productos[1]==" " and productos[2]==" ":
        print("No hay productos para Mostrar. ")
    else:
        for i in range (3):
            if productos[i]!=" ":
                print(f" {i+1} - {productos[i]} ")

def baja_prod():
    if productos[0]==" " and productos[1]==" " and productos[2]==" ":
        print("No hay productos para borrar. ")
    else:
        mostrar_productos()
        print(" 0 - SALIR SIN BORRAR ")
        print("")
        print("")
        prod=input("Ingrese el número del producto a borrar, o 0 para no borrar nada -> ")
        while prod!="1" and prod!="2" and prod!="3" and prod!="0" or prod=="" or prod==" ":
            mostrar_productos()
            print(" 0 - SALIR SIN BORRAR ")
            print("")
            print("")
            prod=input("Ingrese un valor igual o mayor que 1 y menor o igual que 3. Use 0 para no borrar nada")
        
        if prod!="0":
            i=0
            prod=int(prod)
            # verificacion producto asignado a camion RECIBIDO
            while i<7 and productos[prod-1]!=cupos[i][2]:
                i+=1
            if productos[prod-1]!=cupos[i][2]:
                i=0
                while prod!=i+1:
                    i+=1
                print(f"El producto {productos[i]} fue removido con éxito ")
                productos[i]=" "
            else:
                print(f"El producto {productos[prod-1]} NO puede ser borrado debido a que está asignado a, al menos, un camión RECIBIDO. ")
            
        else:
            print("NO SE HA BORRADO NINGUN PRODUCTO DE LA LISTA")
    
def modifica_prod():
    if productos[0]==" " and productos[1]==" " and productos[2]==" ":
        print("No hay productos para Modificar. ")
    else:
        mostrar_productos()
        print(" 0 - SALIR SIN MODIFICAR ")
        print("")
        print("")
        prod=input("Ingrese el número del producto a Modificar, o 0 para no hacer nada -> ")
        while prod!="1" and prod!="2" and prod!="3" and prod!="0":
            mostrar_productos()
            print(" 0 - SALIR SIN MODIFICAR ")
            print("")
            print("")
        
        if prod!="0":
            i=0
            prod=int(prod)
            while i<7 and productos[prod-1]!=cupos[i][2]:
                i+=1
            if productos[prod-1]==cupos[i][2]:
                print(f"El producto {productos[prod-1]} NO puede ser Modificado debido a que está asignado a, al menos, un camión RECIBIDO. ")
            else:
                i=0
                while prod!=i+1:
                    i+=1
                modif=input(f"Ingrese la modificación que quiera realizar en {productos[i]} -> ")
                modif=modif.upper()
                while modif=="" or modif==" " or modif==None or len(modif)>7:
                    modif=input("INGRESE UN PRODUCTO VALIDO :-> ")
                    modif=modif.upper()
                print(f"El producto {productos[i]} fue modificado por con éxito por {modif} ")
                productos[i]=modif
                mostrar_productos()
        else:
            print("")
            print("NO SE HA MODIFICADO NINGUN PRODUCTO DE LA LISTA")
    
def administraciones():
    flag=True
    while flag==True:
        limpia_pant()
        menu_01_administraciones()
        opcion=input( "\n--> Ingrese de la A a la G según la opción que desea usar, o V para volver al menú anterior: \n--> " )
        if opcion == "A" or opcion == "a":
            crud()
            
        elif opcion == "B" or opcion == "b":
            crud_productos()

        elif opcion == "C" or opcion == "c":
            crud()

        elif opcion == "D" or opcion == "d":
            crud()

        elif opcion == "E" or opcion == "e":
            crud()
        elif opcion == "F" or opcion == "f":
            crud()

        elif opcion == "G" or opcion == "g":
            crud()

        elif opcion == "V" or opcion == "v":
            flag=False

#################### INICIO 2. ENTREGA DE CUPOS ####################

def entrega_cupos():
    cupo=input("INGRESE UNA PATENTE :-> ")
    while len(cupo)<6 or len(cupo)>7:
        cupo=input("INGRESE UNA PATENTE VALIDA :-> ")
    cupo=cupo.upper()
    i=0
    while i<7 and cupos[i][0]!=" ":
        i+=1
    if cupos[i][0]==" ":
        alta_cupo(cupo)
    else:
        if i<=7 and cupos[i][0]!=" ":
            print("LISTA DE CUPOS LLENA. INTENTE MAÑANA :) ")
    
def alta_cupo(cupo):
    i=0
    while cupo!=cupos[i][0] and i<7:
        i+=1
    if cupo!=cupos[i][0]:
        i=0
        while cupos[i][0]!=" ":
            i+=1
        cupos[i][0]=cupo
        cupos[i][1]="P"
        print(f"El Cupo para {cupo} se ha agregado correctamente")
        print(f"Y se ha asignado a {cupo} el estado de P = Pendiente ")
    else:
        print(f"El Cupo para {cupo} ya se encuentra registrado")    


#################### INICIO 3. RECEPCION ####################

def recepcion():
    flag=True
    while flag==True:
        limpia_pant()
        print("")
        patente=input("INGRESE LA PATENTE DEL CAMION A RECIBIR :-> ")
        while len(patente)<6 or len(patente)>7:
            patente=input("INGRESE UNA PATENTE VALIDA (minimo 6 caracteres. máximo 7 caracteres. ):-> ")
        patente=patente.upper()
        i=0
        while i<7 and patente!=cupos[i][0]:
            i+=1
        if patente==cupos[i][0]:
            if cupos[i][1]=="P":
                
                ##### CAMBIO EL ESTADO
                cupos[i][1]="E"
                
                ###### agrego carga de productos
                mostrar_productos()
                print("")
                print("")
                prod=input("Ingrese el numero correspondiente al tipo de carga a recibir.")
                while prod!="1" and prod!="2" and prod!="3":
                    mostrar_productos()
                    print("")
                    print("")
                    prod=input("Ingrese el numero correspondiente al tipo de carga a recibir.")
                
                prod=int(prod)
                prod=prod-1
                ## Contador Camiones por Producto ##
                for p in range (3):
                    if prod==p:
                        peso[p][3]+=1
                                
                ## Insertor de producto asociado al camión ##
                cupos[i][2]=productos[prod]
                
                print(f"Se ha Recibido el Camión {patente} y se ha cambiado su estado a 'E: En-Proceso' ")
                print(f"Se ha registrado su carga como {productos[prod]} ")

            elif cupos[i][1]=="E":
                print(f"El Camión {patente} ya se ha Recibido y su estado es EN PROCESO. Proceda a cargar datos.")
            elif cupos[i][1]=="C":
                print(f"El Camión {patente} ya se ha Recibido y su estado es CUMPLIDO.")
        else:
            print(f"El Camión {patente} no se encuentra en la lista de Cupos registrados para el día de hoy. ")
        
        pulse_Tecla()
        limpia_pant()
        print("")

        go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        while go_on!="S" and go_on!="s" and go_on!="N" and go_on!="n":
            go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        if go_on=="N" or go_on=="n":
            flag=False
        else:
            flag=True
    
##############################################################

#################### INICIO 4. REGISTRAR CALIDAD ##################
###################################################################

########### INICIO 5. REGISTRAR PESO BRUTO ########################

def peso_bruto():
    flag=True
    while flag==True:
        limpia_pant()
        print("")
        patente=input("INGRESE LA PATENTE DEL CAMION A REGISTRAR EL PESO BRUTO :-> ")
        while len(patente)<6 or len(patente)>7:
            patente=input("INGRESE UNA PATENTE VALIDA (minimo 6 caracteres. máximo 7 caracteres. ):-> ")
        patente=patente.upper()
        i=0
        while i<7 and patente!=cupos[i][0]:
            i+=1
        if patente==cupos[i][0]:
            if cupos[i][1]=="E":
                if datos[i][0]==0:
                    bruto=int(input("Ingrese las toneladas -sin decimales- |-> "))
                    while bruto<10 and bruto>56:
                        bruto=int(input("Ingrese las toneladas -sin decimales- |-> "))
                    datos[i][0]=bruto
                else:
                    print(f"El camión {patente} ya tiene registrado un peso bruto de {datos[i][0]} ")
            
            elif cupos[i][1]=="P":
                print(f"El camión {patente} todavía no ha pasado por RECEPCION. Vaya a RECEPCION y vuelva a cargar. ")
            
            elif cupos[i][1]=="C":
                print(f"El camión {patente} ya ha COMPLETADO el proceso de cargas. Vaya a REPORTES.")
            
        else:
            print(f"El Camión {patente} no se encuentra en la lista de Cupos registrados para el día de hoy. ")
        
        go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        while go_on!="S" and go_on!="s" and go_on!="N" and go_on!="n":
            go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        if go_on=="N" or go_on=="n":
            flag=False
        else:
            flag=True

###################################################################

################ INICIO 6. REGISTRAR DESCARGA #####################
# #################################################################

################ INICIO 7. REGISTRAR TARA  ########################

def peso_tara():
    flag=True
    while flag==True:
        limpia_pant()
        print("")
        patente=input("INGRESE LA PATENTE DEL CAMION A REGISTRAR LA TARA :-> ")
        while len(patente)<6 or len(patente)>7:
            patente=input("INGRESE UNA PATENTE VALIDA (minimo 6 caracteres. máximo 7 caracteres. ):-> ")
        patente=patente.upper()
        i=0
        while i<7 and patente!=cupos[i][0]:
            i+=1
        if patente==cupos[i][0]:
            if cupos[i][1]=="E":
                if datos[i][0]!=0:
                    if datos[i][1]==0:
                        print(f"el camión {patente} se ha encontrado y su peso bruto es de {datos[i][0]} ")
                        tara=int(input("Ingrese las toneladas | Sin Decimales y Tara < P.Bruto |-> "))
                        while tara<10 or tara>56 or tara>datos[i][0]:
                            tara=int(input("Verifique el dato ingresado. TARA debe ser menor que PESO BRUTO |-> "))
                        datos[i][1]=tara
                        
                        #### PESO NETO #####
                        # al tener la tara y el p.bruto, ya puedo calcular el peso neto
                        datos[i][2]=datos[i][0]-datos[i][1]
                        ###################################
                    else:
                        print(f"El camión {patente} ya tiene registrado una TARA de {datos[i][1]} ")
                else:
                    print(f"El camión {patente} no registra PESO BRUTO. Cargue el P.Bruto y vuelva. Gracias.  ")
                
            elif cupos[i][1]=="P":
                print(f"El camión {patente} todavía no ha pasado por RECEPCION. Vaya a RECEPCION y vuelva a cargar. ")
            
            elif cupos[i][1]=="C":
                print(f"El camión {patente} ya ha COMPLETADO el proceso de cargas. Vaya a REPORTES.")
            
        else:
            print(f"El Camión {patente} no se encuentra en la lista de Cupos registrados para el día de hoy. ")
        
        go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        while go_on!="S" and go_on!="s" and go_on!="N" and go_on!="n":
            go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        if go_on=="N" or go_on=="n":
            flag=False
        else:
            flag=True

###################################################################


############### INICIO 8. REPORTES ################################

def cant_cupos():
    i=0
    while i<=7 and cupos[i][0]!=" ":
        i+=1
    cant_cupos=i
    return cant_cupos

def cam_recib():
    i=0
    while i<=7 and cupos[i][1]!="P" and cupos[i][1]!=" ":
        i+=1
    tot_cam_recibidos=i
    return tot_cam_recibidos

def calculos_productos(peso,pat):
    # inicializo peso menor en 60
    for x in range (3):
        peso[x][2]=60
    
    i=0
    while i<=7 and cupos[i][2]!=" ":
        
        for x in range (3):
            if cupos[i][2]==productos[x]:

                peso[x][0]+=datos[i][2]

                if datos[i][2]>peso[x][1]:
                    peso[x][1]=datos[i][2]
                    pat[x][0]=cupos[i][0]

                if datos[i][2]<peso[x][2]:
                    peso[x][2]=datos[i][2]
                    pat[x][1]=cupos[i][0]


        i+=1
                       
def ordenar(datos,cupos):
    for i in range (cant_cupos()-1):
        for j in range (i+1,cant_cupos()):
            if datos[i][2] <= datos[j][2]:
                for d in range (3):
                    #ordeno array datosos
                    aux=datos[i][d]
                    datos[i][d]=datos[j][d]
                    datos[j][d]=aux
                    #ordeno array cupos
                    aux1=cupos[i][d]
                    cupos[i][d]=cupos[j][d]
                    cupos[j][d]=aux1
                
def reportes():
    
    if cant_cupos()==0:
        print("")
        print("NO SE HAN PROGRAMADO CAMIONES HASTA EL MOMENTO")
    else:
        print(f"Cantidad de Cupos : {cant_cupos()}")
        
        if cam_recib()==0:
            print("")
            print("Todavía NO se han RECIBIDO camiones.")
        else:
            calculos_productos(peso,pat)
            print(f"Camiones Recibidos: {cam_recib()}")

            for m in range (3):
                if productos[m]!=" ":
                    if peso[m][3]==0:
                        print(f"No se han recibido camiones de {productos[m]} ")
                    else:
                        print(f"Cantidad de Camiones de {productos[m]}: {peso[m][3]}")
                        print(f"Peso Neto Total de {productos[m]}: {peso[m][0]} ")
                        print(f"Promedio del Peso Neto de {productos[m]}: {peso[m][0]/peso[m][3]} ")
                        print(f"Patente del Camión de {productos[m]} con MAYOR carga: {pat[m][0]} ")
                        print(f"Patente del Camión de {productos[m]} con MENOR carga: {pat[m][1]} ")
                        print(".......................................................................")
                
            pulse_Tecla()

            print("********************************************")
            print("  PATENTES       PRODUCTO     PESO NETO     ")
            for i in range (8):
                if cupos[i][0]!=" ":
                    print(f"   {cupos[i][0]}         {cupos[i][2]}          {datos[i][2]}       ")
            print("********************************************")

            # ORDENAMOS LA TABLA
            ordenar(datos,cupos)           
            print("********************************************")
            print("    ORDENADO DESCENDENTE POR PESO NETO     *")
            print("********************************************")
            print("  PATENTES       PRODUCTO     PESO NETO     ")
            for i in range (8):
                if cupos[i][0]!=" ":
                    print(f"   {cupos[i][0]}         {cupos[i][2]}          {datos[i][2]}       ")
            print("********************************************")

              
################ PROGRAMA PRINCIPAL #######################

flag=True
while flag==True:
    limpia_pant()    
    menu_princ()
    
    op=input("ingrese un valor entre 1 y 8, o 0 -> ")
    opc=verificar(op)
  
    if opc == "1":
        administraciones()
    elif opc =="2":
        entrega_cupos()
        pulse_Tecla()
    elif opc =="3":
        recepcion()
    elif opc =="4":
        print("FUNCIONALIDAD EN CONSTRUCCION")
    elif opc =="5":
        peso_bruto()
        pulse_Tecla()
    elif opc =="6":
        print("Funcionalidad en CONSTRUCCION")
    elif opc =="7":
        peso_tara()
        pulse_Tecla()
    elif opc =="8":
        reportes()
        pulse_Tecla()

    elif opc =="0":
        flag=False

print("see you later, aligator...")