#MENÚ:
from main import *
from heroes import lista_heroes
from validaciones import *

opcion = 0

while opcion != 8:
    print("\n","===================","\n",
    "1- Mostrar heroes.","\n",
    "2- Agregar heroe.","\n",
    "3- Eliminar heroe","\n",
    "4- Ordenar heroes alfabeticamente","\n",
    "5- Ver heroe mas alto","\n",
    "6- Ver heroe mas fuerte","\n",
    "7- Ver heroe mas delgado","\n",
    "8- Salir","\n",
    "===================",
    "\n"
    )
    opcion = pedir_entero_rango(
    "Ingrese opcion: ",
    "ERROR: reingrese opcion: ",
    1,
    8
)

    match opcion:

        case 1:
            mostrar_datos(lista_heroes)

        case 2:
            agregar_dato(lista_heroes)

        case 3:
            eliminar_dato(lista_heroes)

        case 4:
            ordenar_menor_a_mayor(lista_heroes, 0)
            mostrar_datos(lista_heroes)

        case 5:
            resultado = buscar_dato(lista_heroes, 3, True)
            mostrar_datos([resultado])
        case 6:
            resultado = buscar_dato(lista_heroes, 8, True)
            mostrar_datos([resultado])

        case 7:
            resultado = buscar_dato(lista_heroes, 4, False)
            mostrar_datos([resultado])

        case 8:
            print("\n")
            print("Adiós.")
            break
        
        case _:
            print("Opcion inválida")