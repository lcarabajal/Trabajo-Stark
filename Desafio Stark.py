# -----------Desafío #00--------------:

# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener

# -----------Desafío #01------------:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

#Nombre: Lucas Damian
#Apellido: Carabajal Silva
#Legajo: 114419
#DNI: 46583637
#LUCAS CARABAJAL DAMIAN SILVA ©
import os 
from data_stark import lista_personajes
from funciones_stark import *

while True:
    os.system("cls")
   
    match(menuOpciones()):
        
        case "1":
            mostrarNombres(lista_personajes)
                
        case "2":
            mostrarNomyAlt(lista_personajes)
                
        case "3":
            heroeMasAlto(lista_personajes)
        
        case "4":
            heroeMenosAlto(lista_personajes)
        
        case "5":
            promedioHeroes(lista_personajes)
        
        case "6":
            nombreAltoyBajo(lista_personajes)
            
        case "7":
            nombrePesyLig(lista_personajes)
        
        case "8":
            ir = input("seguro que desea ir al siguiente menu ? s/n: ")
            if ir == "s":
                menu_stark01()        
        case "9":
            salir = input("Seguro que desea salir? s/n: ")
            if salir == "s":
                break
           
    os.system("pause")







