import requests                       #Libreria la cual permite realizar peticiones http con el fin de realizar web scraping
from bs4 import BeautifulSoup         #Libreria que permite realizar web scraing
import numpy as np                    #Np para calcular la varianza de precios
import pandas as pd                   # Libreria la cuál permite exportar información recopilada a un archivo CSV
import Links
import datetime as dt




def funcion_menu_opciones(opcion):
    
    if opcion == 1:        # Opción 1 Cotizacion HP GAMER OMEN
        

            #Ocupar Requests para obtener los requerimientos pedidos
            pcfatory  = requests.get(Links.pcfatory)
            scglobal = requests.get(Links.scglobal)
            cintegral = requests.get(Links.cintegral)

            #Ocupar BeautifulSoup para obtener los requerimientos pedidos 
            soup_pcfactory = BeautifulSoup(pcfatory.text,'lxml')
            soup_scglobal = BeautifulSoup(scglobal.content,'html.parser')
            soup_cintegral = BeautifulSoup(cintegral.content,'html.parser')


            #Solcitar información de Empresa1
            empresa1= ("Pc factory")
            print(empresa1)
            detalle_producto1=soup_pcfactory.title.text
            print(detalle_producto1)
            precio_Producto1=(soup_pcfactory.find("div",class_="price-xl color-fpago-1").text)


            #Metodo para limpiar el numero y poder manejarlo como entero
            def entero_numbers(numbers):
                numbers = numbers.removeprefix("$")
                numbers = numbers.replace("$","")
                numbers = numbers.removeprefix("]")
                numbers = numbers.replace(".","")
                numbers_final = int(numbers)
                return numbers_final
                
            precio1= entero_numbers(precio_Producto1)
            print(entero_numbers(precio_Producto1))

            #Solcitar información de Empresa2
            empresa2= "scglobal"
            print(empresa2)
            detalle_producto2=soup_scglobal.title.string
            print(detalle_producto2)
            precio_Producto2=(soup_scglobal.find("div",class_="current-price").text)
            #numbers = [d.text for d in precio_Producto]


            precio2= entero_numbers(precio_Producto2)
            print(entero_numbers(precio_Producto2))

            #Solcitar informacion de Empresa3
            empresa3=("Cintegral")
            print(empresa3)
            detalle_producto3=soup_cintegral.title.string
            print(detalle_producto3)
            precio_Producto3=(soup_cintegral.find("div",class_="current-price").text)

            
            precio3= entero_numbers(precio_Producto3)
            print(entero_numbers(precio_Producto3))

            list=[precio1,precio2,precio3]
            precios=list

            print(precios)


            list_nombre=[empresa1,empresa2,empresa3]              
            list_caracteristicas=[detalle_producto1,detalle_producto2,detalle_producto3]
            list_precio=[precio1,precio2,precio3]

            nombre=list_nombre
            caracteristicas=list_caracteristicas
            precios=list_precio

            print(nombre)
            print(caracteristicas)
            print(precios)


            #Encontrar precio mas bajo en la lista
            number_low = [precio1,precio2 , precio3]
            min_value = min(number_low)
            print('El valor mas barato es', min_value)

        
            #Suma de numeros de la lista expresiones regulares
            def suma(*precios):
                    suma_precios = 0
                    for i in precios:
                        suma_precios += i
                    return suma_precios
            
             
        
            # Encontrar la media aritmetica de precios
            def obtener_media(precios):
                
                suma_precios = 0
                for valor in precios:
                    suma_precios += valor
                longitud = len(precios)

                return suma_precios / longitud            

            media_precios=(int(obtener_media(precios)))
            print('El valor promedio es',media_precios)

            #Encontrar precio maximo en la lista
            number_max = [precio1,precio2 , precio3]
            max_value = max(number_low)
            print('El valor mas caro es', max_value)


            #Encontrar la varianza de los precios
            st_var = np.var(precios)
            print('El valor de la varianza de los prodcutos es',st_var)


            #generar csv
            w_fecha_actual = dt.datetime.now()

            # Se genera la fecha del archivo
            w_fecha_generacion = w_fecha_actual.strftime("%Y%m%d-%H%M%S") 

            #Se tomará csv con la info correspondiente separado por coma 
            w_noticia_bt_array = {'Nombre empresa':nombre , 'Caracteristicas producto': caracteristicas, 'Precios':precios, 'Valor mas economico del producto es':min_value, 'El valor promedio del producto es': media_precios, 'El valor mas caro del producto es': max_value,'La varianza de los precios es de':st_var}
            w_data_frame = pd.DataFrame (w_noticia_bt_array)
            w_data_frame.to_csv ('CSV proyecto/precios HP Omen gamer _' + w_fecha_generacion+'.csv', index=False)



    elif opcion == 2:        # Opción 2 Precios Xbox S
            
            pcfactory2  = requests.get(Links.pcfactory2)
            pclinkstore = requests.get(Links.pclinkstore)
            elitecenter = requests.get(Links.elitecenter)


            
            soup_pcfactory2= BeautifulSoup(pcfactory2.text,'html.parser')
            soup_pclinkstore = BeautifulSoup(pclinkstore.content,'html.parser')
            soup_elitecenter = BeautifulSoup(elitecenter.content,'html.parser')


            #Empresa1
            empresa1= ("pcfactory")        
            print(empresa1)
            detalle_producto1= soup_pcfactory2.title.string
            print(detalle_producto1)
            precio_Producto1=(soup_pcfactory2.find("div",class_="price-xl color-fpago-1").text)
            
           
            def entero_numbers(numbers):
                numbers = numbers.removeprefix("\n")
                numbers = numbers.removeprefix("'")
                numbers = numbers.removeprefix("$")
                numbers = numbers.replace("$","")
                numbers = numbers.removeprefix("]")
                numbers = numbers.replace(".","")
                numbers_final = int(numbers)
                return numbers_final
                
            precio1= entero_numbers(precio_Producto1)
            print(precio1)

            #Empresa2
            empresa22= ("Pc linkstore")
            print(empresa22)
            detalle_producto2=soup_pclinkstore.title.string
            print(detalle_producto2)
            precio_Producto2=(soup_pclinkstore.find("div",class_="product-price-normal m-0 p-0").text)

            
            precio2= (entero_numbers(precio_Producto2))
            print(precio2)


            #Empresa3
            empresa3=("elitecenter")
            print(empresa3)
            detalle_producto3=soup_elitecenter.title.string
            print(detalle_producto3)
            precio_Producto3=(soup_elitecenter.find("p",class_="normal p-aj").text)

            
            precio3= entero_numbers(precio_Producto3)
            print(precio3)


            list=[precio1,precio2,precio3]
            precios=list

            print(precios)


            list_nombre=[empresa1,empresa22,empresa3]              
            list_caracteristicas=[detalle_producto1,detalle_producto2,detalle_producto3]
            list_precio=[precio1,precio2,precio3]


            nombre=list_nombre
            caracteristicas=list_caracteristicas
            precios=list_precio

            print(nombre)
            print(caracteristicas)
            print(precios)


            #Encontrar precio mas bajo en la lista
            number_low = [precio1,precio2 , precio3]
            min_value = min(number_low)
            print('El valor mas barato es', min_value)



            #Suma de numeros de la lista expresiones regulares
            def suma(*precios):
                    suma_precios = 0
                    for i in precios:
                        suma_precios += i
                    return suma_precios
            
             
             
            # La media es básicamente el promedio
            def obtener_media(precios):
                
                suma_precios = 0
                for valor in precios:
                    suma_precios += valor
                longitud = len(precios)

                return suma_precios / longitud            

            media_precios=(int(obtener_media(precios)))
            print('El valor promedio es',media_precios)



            #Encontrar precio maximo en la lista
            number_max = [precio1,precio2 , precio3]
            max_value = max(number_max)
            print('El valor mas caro es', max_value)

            #Encontrar la varianza de los precios
            st_var = np.var(precios)
            print('El valor de la varianza de los prodcutos es',st_var)

            #generar csv
            w_fecha_actual = dt.datetime.now()

            # Se genera la fecha del archivo
            w_fecha_generacion = w_fecha_actual.strftime("%Y%m%d-%H%M%S") 

            #Se tomará csv con la info correspondiente separado por coma 
            w_noticia_bt_array = {'Nombre empresa':nombre , 'Caracteristicas producto': caracteristicas, 'Precios':precios, 'Valor mas economico del producto es':min_value, 'El valor promedio del producto es': media_precios, 'El valor mas caro del producto es': max_value,'La varianza de los precios es de':st_var}
            w_data_frame = pd.DataFrame (w_noticia_bt_array)
            w_data_frame.to_csv ('CSV proyecto/Precios Xbox S _' + w_fecha_generacion+'.csv', index=False)
                
        
         
    elif opcion == 3:

            scglobal2 = requests.get(Links.scglobal2)
            cintegral2 = requests.get(Links.cintegral2)
            pclinkstore2 = requests.get(Links.pclinkstore2)


            soup_scglobal2 = BeautifulSoup(scglobal2.text,'html.parser')
            soup_cintegral2 = BeautifulSoup(cintegral2.content,'html.parser')
            soup_pclinkstore2 = BeautifulSoup(pclinkstore2.content,'html.parser')


            #Empresa1
            empresa1= ("Sc global")
            print(empresa1)
            detalle_producto1=soup_scglobal2.title.text
            print(detalle_producto1)
            precio_Producto1=(soup_scglobal2.find("div",class_="current-price").text)


            #Metodo para limpiar el numero y poder manejarlo como entero
            def entero_numbers(numbers):
                numbers = numbers.removeprefix("$")
                numbers = numbers.replace("$","")
                numbers = numbers.removeprefix("]")
                numbers = numbers.replace(".","")
                numbers = numbers.removeprefix("'")
                numbers = numbers.removeprefix(" ")
                numbers_final = int(numbers)
                return numbers_final
                
            precio1= entero_numbers(precio_Producto1)
            print(precio1)

            #Empresa2
            empresa2= "C integral"
            print(empresa2)
            detalle_producto2=soup_cintegral2.title.string
            print(detalle_producto2)
            precio_Producto2=(soup_cintegral2.find("div",class_="current-price").text)

                
            precio2= entero_numbers(precio_Producto2)
            print(precio2)

           
            #Empresa3
            empresa3=("Pc link store")
            print(empresa3)
            detalle_producto3=soup_pclinkstore2.title.string
            print(detalle_producto3)
            precio_Producto3=(soup_pclinkstore2.find("div",class_="product-price-normal m-0 p-0").text)

            
            precio3= entero_numbers(precio_Producto3)
            print(entero_numbers(precio_Producto3))

            list=[precio1,precio2,precio3]
            precios=list

            print(precios)


            list_nombre=[empresa1,empresa2,empresa3]              
            list_caracteristicas=[detalle_producto1,detalle_producto2,detalle_producto3]
            list_precio=[precio1,precio2,precio3]


            nombre=list_nombre
            caracteristicas=list_caracteristicas
            precios=list_precio

            print(nombre)
            print(caracteristicas)
            print(precios)


            #Encontrar precio mas bajo en la lista
            number_low = [precio1,precio2 , precio3]
            min_value = min(number_low)
            print('El valor mas barato es', min_value)


            #Suma de numeros de la lista expresiones regulares
            def suma(*precios):
                    suma_precios = 0
                    for i in precios:
                        suma_precios += i
                    return suma_precios
            
            # La media es básicamente el promedio
            def obtener_media(precios):               
                suma_precios = 0
                for valor in precios:
                    suma_precios += valor
                longitud = len(precios)
                return suma_precios / longitud            

            media_precios=(int(obtener_media(precios)))
            print('El valor promedio es',media_precios)

            #Encontrar precio maximo en la lista
            number_max = [precio1,precio2 , precio3]
            max_value = max(number_low)
            print('El valor mas caro es', max_value)

            #Encontrar la varianza de los precios
            st_var = np.var(precios)
            print('El valor de la varianza de los prodcutos es',st_var)

            #generar csv
            w_fecha_actual = dt.datetime.now()

            # Se genera la fecha del archivo
            w_fecha_generacion = w_fecha_actual.strftime("%Y%m%d-%H%M%S") 

            #Se tomará csv con la info correspondiente separado por coma 
            w_noticia_bt_array = {'Nombre empresa':nombre , 'Caracteristicas producto': caracteristicas, 'Precios':precios, 'Valor mas economico del producto es':min_value, 'El valor promedio del producto es': media_precios, 'El valor mas caro del producto es': max_value,'La varianza de los precios es de':st_var}
            w_data_frame = pd.DataFrame (w_noticia_bt_array)
            w_data_frame.to_csv ('CSV proyecto/precios SSD Kingston NV2 1TB _' + w_fecha_generacion+'.csv', index=False)     
                
    else:
        quit()

    