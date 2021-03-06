"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""




def pregunta_01():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos de la columna #1 del csv
    lista_2 = []  # se almacenan los números que necesitamos
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0])  # ingrese los datos de la columna 1 a lista_1

    for values in lista_1:  # por cada dato en la lista 1
        sub_lista = values.split()[1]  # esta variable almacena el entero que necesitamos
        lista_2.append(int(sub_lista))  # transforma los valores en enteros y los ingresa a la lista

    respuesta = sum(lista_2)

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return respuesta

#print(pregunta_01())


def pregunta_02():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos de la columna #1 del csv
    lista_2 = []  # se almacenan las letras que necesitamos
    diccionario_1={}  #aquí almacenamos las claves y las cantidades
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0])  # ingrese los datos de la columna 1 a lista_1
    for values in lista_1:  # por cada dato en la lista 1
        sub_lista = values.split()[0]  # esta variable almacena la letra que necesitamos
        lista_2.append(sub_lista)  #  los ingresa a la lista
    for letras in lista_2:
        diccionario_1.setdefault(letras, 0)
        diccionario_1[letras] = diccionario_1[letras]+1


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return sorted(diccionario_1.items())
#print(pregunta_02())

def pregunta_03():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos de la columna #1 del csv
    lista_2 = []  # se almacenan los datos 0 y 1
    diccionario_1 = {}  # aquí almacenamos las claves y las cantidades
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0])  # ingrese los datos de la columna 1 a lista_1
    for values in lista_1:  # por cada dato en la lista 1
        sub_lista = values.split()[0:2]  # esta variable almacena los datos que necesitamos
        lista_2.append(sub_lista)  #los ingresa a la lista
    for listas in lista_2: #dentro de la lista 2 hay muchas listas
        if listas[0] not in diccionario_1:
            diccionario_1.setdefault(listas[0],int(listas[1]))
            print(listas)
        else:
            diccionario_1[listas[0]]=diccionario_1[listas[0]]+int(listas[1])
    #print(lista_2)
    #print(diccionario_1)
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return sorted(diccionario_1.items())

#print(pregunta_03())
def pregunta_04():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos de la columna #1 del csv
    lista_2 = []  # se almacenan las fechas que necesitamos
    lista_3= [] #meses
    diccionario_1 = {}  # aquí almacenamos las claves y las cantidades
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0])  # ingrese los datos de la columna 1 a lista_1
    for values in lista_1:  # por cada dato en la lista 1
        sub_lista = values.split()[2]  # esta variable almacena la fecha que necesitamos
        lista_2.append(sub_lista)  # los ingresa a la lista
    for fechas in lista_2:
        sub_lista = fechas.split("-")  #dividimos las fechas con el guion
        lista_3.append(sub_lista) #metemos estas listas en la lista 3
    for listas in lista_3:
        diccionario_1.setdefault(listas[1], 0)
        diccionario_1[listas[1]] = diccionario_1[listas[1]] + 1
    #print(lista_1)
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return sorted(diccionario_1.items())
#print(pregunta_04())

def pregunta_05():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos de la columna #1 del csv
    lista_2=[] #letras
    lista_3=[] #máximo
    lista_4= [] #mínimos
    diccionario_1 = {}  # aquí almacenamos las claves y las cantidades
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0])
    for values in lista_1:  # por cada dato en la lista 1
        if values.split()[0] not in lista_2:
            lista_2.append(values.split()[0])
    for letra in lista_2:
        numeros=[]
        for values in lista_1:
            if letra == values.split()[0]: #si las letras coinciden meter los números en la lista
                numeros.append(int(values.split()[1]))
        lista_3.append(max(numeros))
        lista_4.append(min(numeros))





        
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    # print(lista_4)
    return sorted(zip(lista_2, lista_3, lista_4))

#print(pregunta_05())
def pregunta_06():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos de la columna #1 del csv
    lista_2 = []  # elementos con split
    lista_3 = []  # claves letras
    lista_4 = []  # maximos
    lista_5=[] #minimos
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[2:])
    for values in lista_1:  # por cada dato en la lista 1
        for data in values:
                lista_2.append(data.split("\t"))
    for values in lista_2:
        for data in values:
            if len(data)>1:
                if data[:3] not in lista_3:
                    lista_3.append(data[:3])
    for data in lista_3:
        numeros=[]
        for values in lista_2:
            for datos in values:
                if data in datos:
                    numeros.append(int(datos[4:]))
        lista_4.append(max(numeros))
        lista_5.append(min(numeros))


    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    # print(lista_4)
    # print(lista_5)
    return sorted(zip(lista_3, lista_5, lista_4))

#print(pregunta_06())
def pregunta_07():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan parejas
    lista_2 = []  # claves (números en este caso)
    lista_3 = []  # valores (listas de letras)

    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0][0:3].split("\t"))
    for values in lista_1:  # por cada dato en la lista
        if int(values[1]) not in lista_2:
            lista_2.append(int(values[1]))
    lista_2=sorted(lista_2)
    for values in lista_2:
        letras = []
        for value in lista_1:
            if values == int(value[1]):
                letras.append(value[0])
        lista_3.append(letras)
                

    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    # print(lista_4)
    # print(lista_5)
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return sorted(zip(lista_2, lista_3))

#print(pregunta_07())
def pregunta_08():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan parejas
    lista_2 = []  # claves (números en este caso)
    lista_3 = []  # valores (listas de letras)
    lista_4 = []  # valores (listas de letras)
    lista_5 = []  # minimos
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[0][0:3].split("\t"))
    for values in lista_1:  # por cada dato en la lista
        if int(values[1]) not in lista_2:
            lista_2.append(int(values[1]))
    lista_2 = sorted(lista_2)
    for values in lista_2:
        letras = []
        for value in lista_1:
            if values == int(value[1]) and value[0] not in letras:
                letras.append(value[0])
        lista_3.append(sorted(letras))
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    return sorted(zip(lista_2, lista_3))

#print(pregunta_08())
def pregunta_09():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # claves letras
    lista_2 = []  # elementos con split
    lista_3 = []  #valor
    diccionario_1 = {}
    for row in csvreader:  # por cada columna en el documento
        lista_1.append(row[1:])
    for values in lista_1:  # por cada dato en la lista 1
        for data in values:
            lista_2.append(data.split("\t"))
    for values in lista_2:
        for data in values:
            if len(data) > 1:
                    lista_3.append(data[:3])

    for listas in lista_3:
        diccionario_1.setdefault(listas, 0)
        diccionario_1[listas] = diccionario_1[listas] + 1
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return dict(sorted(diccionario_1.items()))
#print(pregunta_09())


def pregunta_10():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # primera letra
    lista_2 = []  # cantidad claves individuales
    lista_3 = []  # cantidad claves triadas

    for row in csvreader:  # por cada columna en el documento
        sublista=[]
        sublista_2=[]
        sublista_3=[]
        lista_1.append(row[0][0])
        sublista.append(row[0][-1])
        for data in row[1:]:
            sublista_2.append(data.split("\t"))
        for data in sublista_2:
            for values in data:
                if len(values)==1:
                    sublista.append(values)
                else:
                    sublista_3.append(values)
        lista_2.append(len(sublista))
        lista_3.append(len(sublista_3))
        # print(sublista, len(sublista))
        # print(sublista_2)
        # print(sublista_3)
        # print(row)



    # for data in lista_3:
    #     numeros = []
    #     for values in lista_2:
    #         for datos in values:
    #             if data in datos:
    #                 numeros.append(int(datos[4:]))
    #     lista_4.append(max(numeros))
    #     lista_5.append(min(numeros))
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return list(zip(lista_1, lista_2, lista_3))
#print(pregunta_10())

def pregunta_11():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos
    lista_2 = []
    lista_3 = []
    lista_4 = []
    diccionario_1 = {}
    for row in csvreader:  # por cada columna en el documento
        sublista = []
        sublista_2 = []
        sublista_3 = []
        sublista.append(row[0][-1])
        sublista_3.append(int(row[0][2]))
        for data in row[1:]:
            sublista_2.append(data.split("\t"))
        for data in sublista_2:
            for values in data:
                if len(values)==1:
                    sublista.append(values)
        print(sublista)
        print(sublista_2)
        print(sublista_3)
        for datos in sublista:
            lista_1.append(datos)
            lista_2.append(sublista_3[0])


    for coord in range(len(lista_1)):
        if lista_1[coord] not in diccionario_1:
            diccionario_1.setdefault(lista_1[coord], lista_2[coord])
        else:
            diccionario_1[lista_1[coord]] = diccionario_1[lista_1[coord]] + lista_2[coord]
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    # print(lista_4)
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return dict(sorted(diccionario_1.items()))
#print(pregunta_11())

def pregunta_12():
    import csv
    datos = open('data.csv')
    csvreader = csv.reader(datos)
    lista_1 = []  # se almacenan los datos
    lista_2 = []
    lista_3 = []
    lista_4 = []
    diccionario_1 = {}
    for row in csvreader:  # por cada columna en el documento
        sublista = []
        sublista_2 = []
        sublista_3 = []
        sublista.append(row[0][0])
        for data in row[1:]:
            sublista_2.append(data.split("\t"))
        for data in sublista_2:
            for values in data:
                if len(values) > 1:
                    sublista_3.append(int(values[4:]))
        # print(sublista)
        # print(sublista_2)
        # print(sublista_3)
        for datos in sublista:
            lista_1.append(datos)
            lista_2.append(sum(sublista_3))

    for coord in range(len(lista_1)):
        if lista_1[coord] not in diccionario_1:
            diccionario_1.setdefault(lista_1[coord], lista_2[coord])
        else:
            diccionario_1[lista_1[coord]] = diccionario_1[lista_1[coord]] + lista_2[coord]
    # print(lista_1)
    # print(lista_2)
    # print(lista_3)
    # print(lista_4)
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return dict(sorted(diccionario_1.items()))
#print(pregunta_12())