import Scraper as sc

       
print("BIENVENIDO AL MEJOR PROGRAMA DE SCRAPING\n")

# Metodo para elegir la opción de scraping
def f_introducir_opcion():
     
     # Validacion de la opción seleccionada
    opcion_correcta=False
    
    numero=0
    # Bucle para validar el menu        
    while(not opcion_correcta):
        try:
            numero = int(input("---- WELCOME -----\n"))
            opcion_correcta=True
        except ValueError:
            print('Error, escoja una opción del menú')
     
    return numero
# Instanciacion el menu
def f_seleccionar_menu():

    #Si es distinta a las opciones dadas, no se iniciará
    salir = False
    
    opcion = 0
    while not  salir:
    
        print("----Escoja una de las siguientes opciones ----- \n")
        print ("1. Webscraping de HP omen \n")
        print ("2. Webscraping de  Xbox microsoft Series S \n")
        print ("3. Webscraping de  Disco Ssd Kingston Nv2 1000gb Pcie 4.0 \n")
        print ("4. Salir del programa\n")
    
        opcion = f_introducir_opcion()
    
        ## Menú de opciones
        if  opcion == 1:
            print ("Opcion 1  - Generando scraping de 3 tiendas\n")
            sc.funcion_menu_opciones(opcion)
            input(" Archivo CVS generado con exito! Presiona cualquier tecla ")
        elif opcion == 2:
            print ("Opcion 2  - Generando scraping de 3 tiendas\n")
            sc.funcion_menu_opciones(opcion)
            input(" Archivo CVS generado con exito! Presiona cualquier tecla ")
        elif opcion == 3:
            print ("Opcion 3  - Generando scraping de 3 tiendas-------- \n")
            sc.funcion_menu_opciones(opcion)
            input(" Archivo CVS generado con exito! Presiona cualquier tecla \n")
        elif opcion == 4:
             salir = True
        else:
            print ("Introduce una opción entre 1-3\n")
    input ("--Saliendo....---\n")

    