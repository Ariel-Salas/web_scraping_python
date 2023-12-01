El proyecto contiene 4 clases:

1)Link: Contiene los link de los prodcutos 
2)Main: Contiene el inicio principal del programa
3)Menu: Contiene las opciones a elegir por el ususario
4)Scrapper: Contiene el codigo para realiza rel scraping


PASO 1
Descrompimir la carpeta en la cual se encuentra el proyecto, seleccionar en visual estudio la carpeta.  


PASO 2

Para poder ejecutar el proyecto de scrapping, se deben instalar las siguientes librerias
de python PIP mediante el siguiente comando en simbolo de sistema CMD, estan herramientas 
necesitan tener el python path para ejecutarse. 

pip install requests
pip install beautifulsoup4
pip install numpy
pip install pandas
pip install html5lib
pip install datetime


PASO 3:

Doble click en archivo "main.py" para ejecutar el programa

PASO 4:

Seleccione una de las opciones del menú 1-3 para generar scrapping de 3 tiendas diferentes para un mismo producto:

1- Webscraping de HP omen
2- Webscraping de  Xbox microsoft Series S	
3- Webscraping de  Disco Ssd Kingston Nv2 1000gb Pcie 4.0

PASO 5:

Cuandose se genenere el archivo, la carpeta CSV proyecto tendrá el siguiente formato:

CSV PROYECTO_OPCIONESCOGIDA_FECHAYHORAGENERACIONARCHIVO.csv

Ejemplo: opcion3_precios SSD Kingston NV2 1TB_20221215-213447 (21 Horas,34 minutos,47 segundos)

PASO 6:


Para la correcta visualización del cvs se debe separar por ",". El csv tiene la siguiente información de la comparación
del mismo producto en direrentes paginas, para saber cual es mas conveninete.  

-Nombre de la empresa
-Descripcion del producto
-Precio del prodcuto
-Precio mas bajo del producto /comparacion
-Precio promedio del producto /comparacion
-Precio mas alto del producto /comparacion
-Varianza de los precios del prodcuto escogido
