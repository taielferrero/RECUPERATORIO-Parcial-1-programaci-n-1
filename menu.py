#MENÚ:
from main import *
from validaciones import *
pokemones_cargados = []

opcion = 0

while opcion != 9:
    print("\n","===================","\n",
    "1- Importar lista de pokemones.","\n",
    "2- Mostrar pokemones.","\n",
    "3- Agregar pokemon.","\n",
    "4- Eliminar pokemon","\n",
    "5- Ordenar pokemones alfabeticamente","\n",
    "6- Ver pokemon mas pesado de tipo agua","\n",
    "7- Ver pokemon mas fuerte","\n",
    "8- Ver pokemones por region","\n",
    "9- Salir","\n",
    "===================",
    "\n"
    )
    opcion = pedir_entero_rango(
    "Ingrese opcion: ",
    "ERROR: reingrese opcion: ",
    1,
    9
)

    match opcion:

        case 1:
            from pokemone import lista_pokemon
            pokemones_cargados = lista_pokemon
            print("Lista importada correctamente")

        case 2:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                mostrar_datos(pokemones_cargados)

        case 3:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                agregar_dato(pokemones_cargados)

        case 4:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                eliminar_dato(pokemones_cargados)

        case 5:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                ordenar_mayor_a_menor(pokemones_cargados, 0)
                mostrar_datos(pokemones_cargados)

        case 6:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                lista_agua = []

            for i in range(len(pokemones_cargados)):
                if pokemones_cargados[i][1].lower() == "agua":
                    lista_agua.append(pokemones_cargados[i])

            if lista_agua == []:
                print("No hay pokemones de tipo agua")
            else:
                resultado = buscar_dato(lista_agua, 3, True)
                mostrar_datos([resultado])

        case 7:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                resultado = buscar_dato(pokemones_cargados, 5, True)
                mostrar_datos([resultado])

        case 8:
            if pokemones_cargados == []:
                print("Primero debe importar la lista")
            else:
                region = pedir_opcion(
                    "Ingrese región (johto/kanto/sinnoh/hoenn): ",
                    "ERROR: reingrese región: ",
                    ["johto", "kanto", "sinnoh", "hoenn"]
                )

            lista_region = []

            for i in range(len(pokemones_cargados)):
                if pokemones_cargados[i][6].lower() == region:
                    lista_region.append(pokemones_cargados[i])

            if lista_region == []:
                print("No hay pokemones de esa región")
            else:
                mostrar_datos(lista_region)

        case 9:
            print("\n")
            print("Adiós.")
            break
        
        case _:
            print("Opcion inválida")