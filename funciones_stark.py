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
def menuOpciones():    
    print("""
          
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
    9- Salir
    """)
    opcion = input("ingrese una opcion: ")
    return opcion
def mostrarNombres(lista):
    for heroe in lista:
        print(heroe["nombre"])
        print("--------------------")            
def mostrarNomyAlt(lista):
    print("    Nombre               altura  ")
    for heroe in lista:
        print(f"{heroe['nombre']:20s} | {float(heroe['altura'])}")   
def heroeMasAlto(lista):
    
    flag_MasAlto = False
    
    for altura in lista:
        if(flag_MasAlto == False or alturaMayor < float(altura["altura"])):
            flag_MasAlto = True
            alturaMayor = float(altura["altura"])
    print("El heroe mas alto mide")        
    print(alturaMayor)
def heroeMenosAlto(lista):
    flag_MasBajo = False
    
    for altura in lista:
        if(flag_MasBajo == False or alturaMenor > float(altura["altura"])):
            flag_MasBajo = True
            alturaMenor = float(altura["altura"])
    print("El heroe mas bajo mide")    
    print(alturaMenor)   
def promedioHeroes(lista):
    acumulador_altura = 0 
    contador = 0
    
    for altura in lista:
        acumulador_altura += float(altura["altura"]) 
        contador += 1
        
        promedio = acumulador_altura/contador  
            
    print(f"{float(promedio):.2f}")    
def nombreAltoyBajo(lista):
    flag_MasBajo = False 
    flag_MasAlto = False
    
    for altura in lista:
            if(flag_MasAlto == False or alturaMayor < float(altura["altura"])):
                flag_MasAlto = True
                nombreMayor = altura["nombre"]
                alturaMayor = float(altura["altura"])   
        
    for altura in lista:
        if(flag_MasBajo == False or alturaMenor > float(altura["altura"])):
            flag_MasBajo = True
            nombreMenor = altura["nombre"]
            alturaMenor = float(altura["altura"])
        
    print(f"{nombreMayor} es el mas alto con: {alturaMayor} y {nombreMenor} es el mas bajo con: {alturaMenor}")    
def nombrePesyLig(lista):
    flag_MasPesado = False
    flag_MasLigero = False
    
    for heroe in lista:
        if(flag_MasPesado == False or pesoMayor < float(heroe["peso"])):
            flag_MasPesado = True
            nombreMasPesado = heroe["nombre"]
            pesoMayor = float(heroe["peso"]) 
        
    for heroe in lista:
        if(flag_MasLigero == False or pesoMenor > float(heroe["peso"])):
            flag_MasLigero = True
            nombreMasLigero = heroe["nombre"]
            pesoMenor = float(heroe["peso"])
                
    print(f"El heroe mas pesado es {nombreMasPesado} con: {pesoMayor} y El heroe mas ligero es {nombreMasLigero} con: {pesoMenor}")        
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