def menuOpciones01():
    print(
    """
    ♦♦♦ Menu Extendido Stark ♦♦♦
    _________________________________________    
     
    1- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
    género M
    2- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
    género F
    3- Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    4- Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    5- Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    6- Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    7- Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    8- Recorrer la lista y determinar la altura promedio de los superhéroes de
    género F
    9-Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    10-Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    11-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
    no tener, Inicializarlo con No Tiene).
    12-Listar todos los superhéroes agrupados por color de ojos.
    13-Listar todos los superhéroes agrupados por color de pelo.
    14-Listar todos los superhéroes agrupados por tipo de inteligencia
    15-Volver al menu anterior
    """)
    opcion = input("Ingrese una opcion: ")
    return opcion
 
def imprimirMasculino(lista):
    print("    Nombre          |   Genero")
    for hombre in lista:
        if hombre['genero'] == "M":
            print(f"{hombre['nombre']:20s}| {hombre['genero']}")
def imprimirFemenino(lista):
    print("    Nombre          |   Genero")
    for mujer in lista:
        if mujer['genero'] == "F":
            print(f"{mujer['nombre']:20s}| {mujer['genero']}")
def mostrarMasAltoMasculino(lista):
    flag_MasAltoMasculino = False
    
    for hombre in lista:
        if (hombre['genero']) == "M":
            
            if(flag_MasAltoMasculino == False or alturaMayor < float(hombre["altura"])):
                flag_MasAltoMasculino = True
                alturaMayor = float(hombre["altura"])
                nombreMayor = (hombre['nombre'])
       
    print("El heroe Masculino mas alto es: ")        
    print(f"{nombreMayor + ' ' + str(alturaMayor) } ")    
def mostrarMasAltoFemenino(lista):
    flag_MasAltoFemenino = False
    
    for mujer in lista:
        if (mujer['genero']) == "F":
            
            if(flag_MasAltoFemenino == False or alturaMayor < float(mujer["altura"])):
                flag_MasAltoFemenino = True
                alturaMayor = float(mujer["altura"])
                nombreMayor = (mujer['nombre'])
            
    print("El heroe Femenino mas alto es: ")        
    print(f"{nombreMayor + ' ' + str(alturaMayor) } ")   
def mostrarMasBajoMasculino(lista):
    flag_MasBajoMasculino = False
    
    for hombre in lista:
        if (hombre['genero']) == "M":
            
            if(flag_MasBajoMasculino == False or alturaBajo > float(hombre["altura"])):
                flag_MasBajoMasculino = True
                alturaBajo = float(hombre["altura"])
                nombreBajo = (hombre['nombre'])
                   
    print("El heroe Masculino mas Bajo es: ")        
    print(f"{nombreBajo + ' ' + str(alturaBajo) } ")
def mostrarMasBajoFemenino(lista):
    flag_MasBajoFemenino = False
    
    for mujer in lista:
        if (mujer['genero']== "F"):
            
            if(flag_MasBajoFemenino == False or alturaBajo > float(mujer["altura"])):
                flag_MasBajoFemenino = True
                alturaBajo = float(mujer["altura"])
                nombreBajo = (mujer['nombre'])
            
    print("El heroe Femenino mas Bajo es: ")        
    print(f"{nombreBajo + ' ' + str(alturaBajo) } ")
def promedioAlturaMasculino(lista):
    acumulador_altura = 0 
    contador = 0
    
    for persona in lista:
        if persona['genero'] == "M":
            acumulador_altura += float(persona["altura"]) 
            contador += 1
        
    promedio = acumulador_altura/contador  
            
    print(f"{float(promedio):.2f}")  
def promedioAlturaFemenino(lista):
    acumulador_altura = 0 
    contador = 0
    
    for persona in lista:
        if persona['genero'] == "F":
            acumulador_altura += float(persona["altura"]) 
            contador += 1
        
    promedio = acumulador_altura/contador  
            
    print(f"{float(promedio):.2f}") 
def buscandor_tipo(lista:list, key:str, repe:bool = False):
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.append(heroe[key])
        
    if(not repe):
        lista_aux = []
        for item in lista_filtrada:
            if (not esta_en_lista(lista_aux, item)):
                lista_aux.append(item)
            
            lista_filtrada = lista_aux
            
    return lista_filtrada    
def heroeColorOjo(lista):
    lista_ojo = []
    colores = []

    for heroe in lista:
        lista_ojo.append(heroe.copy())

    for heroe in lista_ojo:
        if not esta_en_lista(colores, heroe['color_ojos']):
            colores.append(heroe['color_ojos'])

    for color in colores:
        print("Color De ojos: " + color)
        for heroe in lista:
            if(heroe['color_ojos'] == color):
                print(heroe['nombre'], heroe['color_ojos'])
                
        print("----------------------------------")
def esta_en_lista(lista:list, item:str)-> bool:
    esta = False
    for elemento in lista:
        if elemento == item:
            esta = True
            break
        
    return esta        
def heroeColorPelo(lista:list): 
    lista_pelo = []
    colores = []

    for heroe in lista:
        lista_pelo.append(heroe.copy())

    for heroe in lista_pelo:
        if not esta_en_lista(colores, heroe['color_pelo']):
            colores.append(heroe['color_pelo'])

    for color in colores:
        print("Color De Pelo: " + color)
        for heroe in lista:
            if(heroe['color_pelo'] == color):
                print(heroe['nombre'], heroe['color_pelo'])
                
        print("----------------------------------")
def heroetipoInteligencia(lista):
    lista_inteligencia = []
    inteligencia = []

    for heroe in lista:
        lista_inteligencia.append(heroe.copy())

    for heroe in lista_inteligencia:
        if not esta_en_lista(inteligencia, heroe['inteligencia']):
            inteligencia.append(heroe['inteligencia'])

    for tipo in inteligencia:
        print("Inteligencia: " + tipo)
        for heroe in lista:
            if(heroe['inteligencia'] == tipo):
                print(heroe['nombre'], heroe['inteligencia'])
                
        print("----------------------------------")
        
def menu_stark01():
    import os
    from data_stark import lista_personajes
    while True:
        os.system("cls")
        
        match(menuOpciones01()):
            case "1":
                imprimirMasculino(lista_personajes)
            
            case "2":
                imprimirFemenino(lista_personajes)
                
            case "3":
                mostrarMasAltoMasculino(lista_personajes)
                
            case "4":
                mostrarMasAltoFemenino(lista_personajes)

            case "5":
                mostrarMasBajoMasculino(lista_personajes)
                
            case "6":
                mostrarMasBajoFemenino(lista_personajes)
            
            case "7":
                promedioAlturaMasculino(lista_personajes)
                
            case "8":
                promedioAlturaFemenino(lista_personajes)
            
            case "9":
                print(buscandor_tipo(lista_personajes,'color_ojos'))
            
            case "10":
                print(buscandor_tipo(lista_personajes,'color_pelo'))
                
            case "11":
                print(buscandor_tipo(lista_personajes,'inteligencia'))
            
            case "12":
                heroeColorOjo(lista_personajes)
            
            case "13":
                heroeColorPelo(lista_personajes)

            case "14": 
                heroetipoInteligencia(lista_personajes)
                
            case"15":
                volver = input("Seguro que desea volver al menu anterior ? s/n: ")
                if volver == "s":
                    break
                
        os.system("pause")  
        

def stark_normalizar_datos(lista:list)->list:
# 0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
# de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
# las keys que representan datos numéricos)
# ● Validar primero que el tipo de dato no sea del tipo al cual será
# casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
# verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá imprimir como
# mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
# caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
  
    lista_normalizada = []
    
    if bool(lista) == False: 
        print("Error, la lista esta vacia")
    else:    
        
        for heroe in lista: 
            lista_normalizada.append(heroe.copy())
        
        for personaje in lista_normalizada:
            
            if type(personaje['altura'] != float):
                personaje['altura'] = float(personaje['altura'])
                
            
            if(type(personaje['peso'] != float)):
                personaje['peso'] = float(personaje['peso'])
                
                
            if(type(personaje['fuerza'] != int)):
                personaje['fuerza'] = int(personaje['fuerza'])
                
                
        
        print("Datos normalizados")
        return lista_normalizada

def obtener_nombre(diccionario:dict)->str:
# 1.1. Crear la función 'obtener_nombre' la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y devolverá un string el cual
# contenga su nombre formateado de la siguiente manera:
# Nombre: Howard the Duck
    nombre = f"Nombre: {diccionario['nombre']}"
    
    return nombre
    

def imprimir_dato(cadena:str):
# 1.2. Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
# deberá imprimirlo en la consola. La función no tendrá retorno.  
    print(cadena)
  

def stark_imprimir_nombres_heroes(lista:list):
# 1.3. Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por
# parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
# funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía
# para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00

    if not bool(lista):
        return -1 
        
    else:
        for linea in lista: 
            nombre = obtener_nombre(linea)
            imprimir_dato(nombre)
            print("-----------------------------")
            
            
def obtener_nombre_y_dato(diccionario:dict,clave:str)->str:
# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato
# (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
# CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera:
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500
    nombre_y_dato = f"Nombre: {diccionario['nombre']} | {clave}: {diccionario[clave]}"
    
    return nombre_y_dato

def stark_imprimir_nombres_alturas(lista:list):
# 3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
# parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
# alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
# no esté vacía para realizar sus acciones, caso contrario no hará nada y
# retornara -1.
# Con este se resuelve el Ej 2 del desafío #00


    if not bool(lista):
        return -1

    else:
        lista_normalizada = stark_normalizar_datos(lista) 
        for heroe in lista_normalizada:
            
            print(obtener_nombre_y_dato(heroe,'altura'))
            print("-----------------------------------------")
            
            
def calcular_max(lista:list, clave:str):
# 4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más alto.
# Ejemplo de llamada:
# calcular_max(lista, 'edad')
    flag = False
    lista_normalizada = stark_normalizar_datos(lista)
    
    for heroe in lista_normalizada:
        if(not flag or heroe[clave]>heroeMax[clave]):
            heroeMax = heroe
            flag = True
    
    return heroeMax 
        
        
def calcular_min(lista:list, clave:str)->dict:
# 4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más bajo.
# Ejemplo de llamada:
# calcular_min(lista, 'edad')
    flag = False
    lista_normalizada = stark_normalizar_datos(lista)
    
    for heroe in lista_normalizada:
        if(not flag or heroe[clave]<heroeMin[clave]):
            heroeMin = heroe
            flag = True
    
    return heroeMin 

def calcular_max_min_dato(lista:list,metodo:str,clave:str)->dict:    
# 4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar el héroe que cumpla con la condición pedida.
# Reutilizar las funciones hechas en los puntos 4.1 y 4.2
# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

    if(metodo == "maximo"):
        resultado = calcular_max(lista,clave)
    else:
        resultado = calcular_min(lista,clave)
        
    return resultado

def stark_calcular_imprimir_heroe(lista:list,metodo:str,clave:str):   
# 4.4. Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres
# parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir
# su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara -1.
# Ejemplo de llamada:
# stark_calcular_imprimir_heroe (lista, "maximo", "edad")
# Ejemplo de salida:
# Mayor altura: Nombre: Howard the Duck | altura: 79.34
    if not bool(lista):
        return -1
    elif(metodo == "maximo"):
        imprimir_dato(f"Mayor {clave}: {obtener_nombre_y_dato(calcular_max_min_dato(lista,metodo,clave),clave)}")
    else:
        imprimir_dato(f"Menor {clave}: {obtener_nombre_y_dato(calcular_max_min_dato(lista,metodo,clave),clave)}")
        
def sumar_dato_heroe(lista:list,clave:str)-> int:
# 5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
# lista de héroes y un string que representara el dato/key de los héroes que se
# requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un
# diccionario vacío antes de hacer la suma. La función deberá retorna la suma
# de todos los datos según la key pasada por parámetro
    lista_normalizada = stark_normalizar_datos(lista)
    total = 0
    
    for heroe in lista_normalizada:
        if(type(heroe) == dict):
            if not bool(heroe):
                return -1
            else:
               total += heroe[clave]
               
    return total

def dividir(dividendo:int, divisor:int)->int:
# 5.2. Crear la función ‘dividir’ la cual recibirá como parámetro dos números
# (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
# retornar 0, caso contrario realizar la división entre los parámetros y retornar el
# resultado
    if divisor == 0:
        return 0 
    else:
        return dividendo/divisor

def calcular_promedio(lista:list,clave:str)->int:
# 5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
# lista de héroes y un string que representa el dato del héroe que se requiere
# calcular el promedio. La función debe retornar el promedio del dato pasado
# por parámetro
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2       
    contador = len(lista)
    promedio = dividir(sumar_dato_heroe(lista,clave),contador)
        
    return promedio

def stark_calcular_imprimir_promedio_altura(lista:list):
# 5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
# una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
# altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
# acciones, caso contrario no hará nada y retornara -1.
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y
# 5.3
# Con este se resuelve el Ej 5 del desafío #00
    if not bool(lista):
        return -1
    else:
        imprimir_dato(f"{(calcular_promedio(lista,'altura')):2g}") 
        
def imprimir_menu():
# 6.1. Crear la función "imprimir_menu" que imprima el menú de opciones por
# pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se
# deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
    imprimir_dato(
    """    
    ♣♣♣ INDUSTRIAS STARK ♣♣♣
    __________________________________
    
    1- Recorrer la lista imprimiendo el nombre de cada superhéroe
    2- Recorrer la lista imprimiendo nombre de cada superhéroe junto a
    la altura del mismo
    3- Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4- Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5- Recorrer la lista y determinar la altura promedio de los superhéroes
    (PROMEDIO)
    6- Informar cual es el Nombre del superhéroe asociado a cada uno de los
    indicadores anteriores (MÁXIMO, MÍNIMO)
    7- Calcular e informar cual es el superhéroe más y menos pesado.
    8- Ir al siguiente menu
    9- Salir""")
        
def validar_entero(numero:str)->bool:
# 6.2. Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente
# por dígitos. Retornara True en caso de serlo, False caso contrario
    if numero.isdecimal():
        return True
    else:
        return False

def stark_menu_principal()->int:
# 6.3. Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
# menú de opciones y le pedirá al usuario que ingrese el número de una de las
# opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
# lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
# funciones del ejercicio 6.1 y 6.2
    imprimir_menu()
    opcion = input("Ingrese opcion: ")
    
    if validar_entero(opcion):
        return(int(opcion))
    else:
        return -1
            
def stark_marvel_app(lista:list):
# 7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de
# héroes y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con
# python 3.10+). Debe informar por consola en caso de seleccionar una opción
# incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con
# prefijo 'stark_' donde crea correspondiente.  
    import os 
    while True:
        os.system("cls")
    
        match(stark_menu_principal()):
            
            case 1:
                stark_imprimir_nombres_heroes(lista)
                    
            case 2:
                stark_imprimir_nombres_alturas(lista)
                    
            case 3:
                stark_calcular_imprimir_heroe(lista,"maximo",'altura')
            
            case 4:
                stark_calcular_imprimir_heroe(lista,"minimo",'altura')
            
            case 5:
                stark_calcular_imprimir_promedio_altura(lista)
            
            case 6:
                f"{stark_calcular_imprimir_heroe(lista,'maximo','altura')} y {stark_calcular_imprimir_heroe(lista,'minimo','altura')}"
                
            case 7:
                f"{stark_calcular_imprimir_heroe(lista,'maximo','peso')} y {stark_calcular_imprimir_heroe(lista,'minimo','peso')}"
            
            case 8:
                ir = input("seguro que desea ir al siguiente menu ? s/n: ").lower()
                if ir == "s":
                    menu_stark01()        
                        
            case 9:
                salir = input("Seguro que desea salir? s/n: ").lower()
                if salir == "s":
                    break
                                    
            case _default:
                print("Error, esa opcion no esta disponible")
            
        os.system("pause")