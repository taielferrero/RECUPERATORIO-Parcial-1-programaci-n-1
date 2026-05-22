# punto 1
from heroes import lista_heroes
from validaciones import *

# punto 2. opcion 1 del menu:
def obtener_datos()->list:
    '''
    brief: crea y retorna una lista con los nombres de los campos de los heroes.
    recibe: nada.
    retorna: una lista de strings.
    '''
    campos = [
        "Nombre: ",
        "Identidad: ",
        "Empresa: ",
        "Altura: ",
        "Peso: ",
        "Genero: ",
        "Color de ojos: ",
        "Color de pelo: ",
        "Fuerza: ",
        "Inteligencia: ",
        ]
    return campos

def mostrar_datos(lista: list) ->None:
    '''
    brief: recorre una lista de listas y muestra en consola cada dato de cada lista.
    recibe: una lista de listas.
    retorna: nada.
    '''
    datos = obtener_datos()
    for i in range(len(lista)):
        print("---------------------------------")
        for j in range(len(datos)):
            print(f"{datos[j]} {lista[i][j]}")
        print("---------------------------------", "\n")

# punto 3. opcion 2 del menu:
def agregar_dato(lista: list) -> None:
    
    '''
    brief: pide datos por input al usuario para agregarlos a una lista y esta a su vez a una lista de listas.
    recibe: una lista.
    retorna: nada.
    '''

    nombre = pedir_texto(
        "Ingrese nombre del heroe: ",
        "ERROR: reingrese nombre del heroe: "
    )

    identidad = pedir_texto(
        "Ingrese identidad del heroe: ",
        "ERROR: reingrese identidad del heroe: "
    )

    empresa = pedir_opcion(
        "Ingrese empresa (DC Comics o Marvel Comics): ",
        "ERROR: reingrese empresa: ",
        ["dc comics", "marvel comics"]
    )

    altura = pedir_float_positivo(
        "Ingrese altura: ",
        "ERROR: reingrese altura: "
    )

    peso = pedir_float_positivo(
        "Ingrese peso: ",
        "ERROR: reingrese peso: "
    )

    genero = pedir_opcion(
        "Ingrese genero (m/f/nb): ",
        "ERROR: reingrese genero (m/f/nb): ",
        ["m", "f", "nb"]
    )

    color_ojos = pedir_texto(
        "Ingrese color de ojos: ",
        "ERROR: reingrese color de ojos: "
    )

    color_pelo = pedir_texto(
        "Ingrese color de pelo: ",
        "ERROR: reingrese color de pelo: "
    )

    fuerza = pedir_entero_rango(
        "Ingrese fuerza (1-100): ",
        "ERROR: reingrese fuerza (1-100): ",
        1,
        100
    )

    inteligencia = pedir_opcion(
        "Ingrese inteligencia (low, average, good, high, genius): ",
        "ERROR: reingrese inteligencia (low, average, good, high, genius): ",
        ["low", "average", "good", "high", "genius"]
    )

    nuevo_dato = [nombre, 
                identidad, 
                empresa, 
                altura, 
                peso, 
                genero, 
                color_ojos, 
                color_pelo, 
                fuerza, 
                inteligencia]

    lista.append(nuevo_dato)

# punto 4. opcion 3 del menu:
def eliminar_dato (lista: list) ->None:
    '''
    brief: pide un dato por nombre al usuario para eliminarlo de una lista de listas.
    recibe: dato por un input (nombre de la lista a eliminar).
    retorna: nada.
    '''
    
    nombre = pedir_texto(
        "Ingrese nombre del heroe: ",
        "ERROR: reingrese nombre del heroe: "
    )
    flag = False

    for i in range(len(lista)):
        
        if lista[i][0].lower() == nombre.lower():

            flag = True

            mostrar_datos([lista[i]])

            pregunta = pedir_opcion(
                "Seguro quiere eliminarlo? (si/no): ",
                "ERROR: ingrese si o no: ",
                ["si", "no"]
            )

            if pregunta == "si":
                lista.pop(i)
                print("dato eliminado")
                
            else:
                print("dato no eliminado")

            break

    if flag == False:
        print("dato no encontrado")

# punto 5. opcion 4 del menu:
def ordenar_menor_a_mayor(lista:list, indice: int)->None:
    '''
    brief: compara las listas de una lista de listas para ordenarlas menor a mayor.
    recibe: una lista para comparar.
    retorna: nada.
    '''
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][indice]>lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

# puntos 6, 7 y 8. opciones 5, 6 y 7 del menu:
def buscar_dato (lista:list, indice: int, buscar_maximo: bool)->list:
    '''
    brief: busca un dato maximo o minimo dentro de una lista de listas.
    recibe:
        - una lista de listas
        - un indice para comparar
        - un booleano para decidir si busca maximo o minimo
    retorna: la lista del dato encontrado.
    '''
    
    dato_encontrado = lista[0]
    
    for i in range(1, len(lista)):
        #arranca desde el segundo heroe pq el primero ya esta guardado en dato_encontrado!
        
        if buscar_maximo == True:

            if lista[i][indice] > dato_encontrado[indice]:
                dato_encontrado = lista[i]
        else:
            if lista[i][indice] < dato_encontrado[indice]:
                dato_encontrado = lista[i]

    return dato_encontrado

        