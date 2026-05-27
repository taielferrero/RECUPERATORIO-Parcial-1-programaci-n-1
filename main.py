# punto 1
from pokemone import lista_pokemon
from validaciones import *

# punto 2. opcion 2 del menu:
def obtener_datos()->list:
    '''
    brief: crea y retorna una lista con los nombres de los campos de los pokemon.
    recibe: nada.
    retorna: una lista de strings.
    '''
    campos = [
        "Nombre: ",
        "Tipo: ",
        "Altura: ",
        "Peso: ",
        "Nivel: ",
        "Fuerza de ataque: ",
        "Region: ",
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

# punto 3. opcion 3 del menu:
def agregar_dato(lista: list) -> None:
    
    '''
    brief: pide datos por input al usuario para agregarlos a una lista y esta a su vez a una lista de listas.
    recibe: una lista.
    retorna: nada.
    '''

    nombre = pedir_texto(
        "Ingrese nombre del pokemon: ",
        "ERROR: reingrese nombre del pokemon: "
    )

    tipo = pedir_texto(
        "Ingrese tipo del pokemon: ",
        "ERROR: reingrese tipo del pokemon: "
    )

    altura = pedir_float_positivo(
        "Ingrese altura: ",
        "ERROR: reingrese altura: "
    )

    peso = pedir_float_positivo(
        "Ingrese peso: ",
        "ERROR: reingrese peso: "
    )

    nivel = pedir_entero_rango(
        "Ingrese nivel (1-100): ",
        "ERROR: reingrese nivel (1-100): ",
        1,
        100
    )

    fuerza = pedir_entero_rango(
        "Ingrese fuerza (1-255): ",
        "ERROR: reingrese fuerza (1-255): ",
        1,
        255
    )

    region = pedir_opcion(
        "Ingrese region (johto/kanto/sinnoh/hoenn): ",
        "ERROR: reingrese region (johto/kanto/sinnoh/hoenn): ",
        ["johto", "kanto", "sinnoh", "hoenn"]
    )

    nuevo_dato = [nombre, 
                tipo, 
                altura, 
                peso, 
                nivel, 
                fuerza, 
                region]

    lista.append(nuevo_dato)

    print("\n","Pokemon agregado correctamente:")
    mostrar_datos([nuevo_dato])

# punto 4. opcion 4 del menu:
def eliminar_dato (lista: list) ->None:
    '''
    brief: pide un dato por nombre al usuario para eliminarlo de una lista de listas.
    recibe: dato por un input (nombre de la lista a eliminar).
    retorna: nada.
    '''
    
    nombre = pedir_texto(
        "Ingrese nombre del pokemon: ",
        "ERROR: reingrese nombre del pokemon: "
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
                print("\n","dato eliminado")
                
            else:
                print("\n","dato no eliminado")

            break

    if flag == False:
        print("\n","dato no encontrado")

# punto 5. opcion 5 del menu:
def ordenar_mayor_a_menor(lista:list, indice: int)->None:
    '''
    brief: compara las listas de una lista de listas para ordenarlas de mayor a menor.
    recibe: una lista para comparar.
    retorna: nada.
    '''
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][indice]<lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

# puntos 6, 7 y 8. opciones 6, 7 y 8 del menu:
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

        