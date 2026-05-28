def pedir_texto(mensaje: str, error: str) -> str:
    '''
    brief: valida que se ingrese un dato de tipo string y que el input no quede vacio.
    recibe: un dato de tipo string por input.
    retorna: un string.
    '''

    dato = input(mensaje)

    while dato == "":
        dato = input(error)

    return dato

def es_entero(dato: str) -> bool:

    valido = True

    for i in range(len(dato)):

        if dato[i] < "0" or dato[i] > "9":
            valido = False

    return valido

def pedir_float_positivo(mensaje: str, error: str) -> float:
    '''
    brief: valida que se ingrese un numero flotante mayor a cero.
    recibe: un dato de tipo float por input.
    retorna: un float.
    '''

    dato = input(mensaje)

    while es_entero(dato) == False or float(dato) <= 0:
        dato = input(error)

    return float(dato)



def pedir_entero_rango(
    mensaje: str,
    error: str,
    minimo: int,
    maximo: int
) -> int:
    '''
    brief: valida que se ingrese un numero entero dentro de un rango especificado.
    recibe: un dato de tipo int y dos valores enteros que representan el minimo y maximo permitidos.
    retorna: un entero.
    '''

    dato = input(mensaje)

    while es_entero(dato) == False or int(dato) < minimo or int(dato) > maximo:
        dato = input(error)

    return int(dato)


def pedir_opcion(
    mensaje: str,
    error: str,
    opciones: list
) -> str:
    '''
    brief: valida que el dato ingresado se encuentre dentro de una lista de opciones validas.
    recibe: un dato de tipo string y una lista con las opciones permitidas.
    retorna: un string.
    '''

    dato = input(mensaje).lower()

    flag = False

    while flag == False:

        for i in range(len(opciones)):

            if dato == opciones[i]:
                flag = True

        if flag == False:
            dato = input(error).lower()

    return dato