import random, time
from ui.carga_de_datos import *
from ui.ascii_frame import *
from estructuras.arbol_binario import BST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral, NodoGeneral
from estructuras.heap import Heap
from estructuras.grafos import GrafoLista, cargar_grafo




# CONFIGURACION INICIAL
LOOP = True
ANCHO_RECUADRO = 80
af = AsciiFrame(ANCHO_RECUADRO)

SERIES = cargar_json("datos/dataset_1000.json")["series"]
EDADES = ['TV-Y7', 'TV-14', 'TV-G', 'TV-MA', 'TV-PG']
GENEROS = ['Horror', 'War', 'Comedy', 'Sci-Fi', 'Western', 'Fantasy', 'Game Show', 'Action', 'Thriller', 
           'Reality', 'Crime', 'Drama', 'Talk', 'Animation', 'Mystery', 'Adventure', 'Documentary']


# Crear Arbol Binario De Busqueda
title_bst = BST()

# Crear Arbol AVL 
title_avl = AVL()

# Crear Arbol General - Generos
arbol_general = ArbolGeneral()
arbol_general.insertar_raiz("series")

# Crear Arbol General - Edades
ag = ArbolGeneral()
ag.insertar_raiz("series")

# Carga datos a BST
title_bst.load_str(SERIES, "title")

# Carga datos a AVL
title_avl.load_str(SERIES, "title")

# Carga datos de generos a ArbolGeneral
arbol_generos = arbol_general.cargar_arbol(arbol_general, GENEROS)
arbol_general = arbol_general.cargar_series(arbol_general, arbol_generos, SERIES)

# Carga datos de edades a ArbolGeneral
ag_edades = ag.cargar_arbol(ag, EDADES)
ag = ag.cargar_series(ag, ag_edades, SERIES, category="age_rating")

# Carga datos a Heap
ranking_prioridad = Heap(is_max=True)
ranking_prioridad.load(SERIES)

# Carga de datos al GrafoLista
grafo_lista = GrafoLista(len(SERIES))
cargar_grafo(grafo_lista, SERIES)






# JSON RECORDATORIO
"""
{
"title": "Family Guy",
"genre": "Animation",
"year": 1999,
"popularity_metrics": 79,
"episode_duration_average": 22,
"seasons": 23,
"episodes": 430,
"age_rating": "TV-14",
"is_finished": false
}
"""




##############################################################################################################
# FUNCIONES DE IMPRESION EN PANTALLA
##############################################################################################################

def imprimir_texto_ensanguchado(text, indent="c", separator=" "):
    """ Imprime Texto Dentro De Una Caja ASCII """
    af.print_box("t")
    af.print_text(text, indent, separator)
    af.print_box("b")


def imprimir_pantalla_ensanguchada(lst, indent="l"):
    """ Imprime una lista con "cadena de caracteres" en pantalla
        lst es una lista con cadena de caracteres ["A", "e", "I", "o", "U"]
    """
    af.print_box("t")
    for i, option in enumerate(lst):
        af.print_text(f"[{i+1}]> {option}" , indent)
    af.print_box("b")





##############################################################################################################
# FUNCIONES UTILES PARA EL RESTO DE OPCIONES
##############################################################################################################

def filtrar_por(user_input:str, option:str):
    """ Filtra series por una opcion de manera secuencial:
        title, genre, duration, etc...
    """
    for serie in SERIES:
        if user_input.lower() == serie[option].lower():
            return True
    return False


def seleccionar_por(user_input:str, option:str):
    """" Retorna una lista con los nombres de series que tienen una opcion en comun. """
    lst = []
    for serie in SERIES:
        if user_input.lower() == serie[option].lower():
            lst.append(serie)
    return lst
    
    
def obtener_opcion_aleatoria(option="title"): 
    """ Retorna una opcion aleatoria de a la lista json
        option es la opcion que queremos obtener ("titulo, genero, popularidad")
        "title" por default
    """
    return random.choice(SERIES)[option]
    
    
def salir():
    """ Rompe el while loop para cerrar el programa """
    global LOOP
    LOOP = False


def seleccionar_opcion(user_input:str, method_call_lst:list, callback=None):
    """ Dependiendo de lo que el usuario ingrese va a llamar a la opcion correcta 
        method_call_lst es una lista con funciones(sin parentesis) que seran ejecutadas aqui
        segun corresponda.
    """

    # Solo llama a la funcion si el usuario ingresa un nro mayor que 0 y menor/igual al tamaño de la lista
    if user_input.isdigit() and 0 < int(user_input) <= len(method_call_lst):
        method_call_lst[int(user_input)-1]()
        return True
    else:
        print(MENSAJE_AL_USUARIO_2)
        if callback is not None: callback()
        return False

def get_serie_index(serie_title:str, series:list):
    """ Funcion de ayuda para saber el indice de una serie dentro de la lista de SERIES 
    """
    for i, serie in enumerate(series):
        if serie_title.lower() == serie["title"].lower():
            return series.index(serie)
    return None








##############################################################################################################
# IMPRIMIR FUNCIONALIDAD DE LAS OPCIONES DE LA PANTALLA PRINCIPAL
##############################################################################################################

def buscar_series():
    """ Imprime si la serie ingresada por el usuario esta en la base de datos
        Utiliza el arbol binario para hacer la busqueda
    """
    nombre = input(">>>INGRESE EL NOMBRE DE LA SERIE (en ingles): ")
        
    af.print_space("-")

#    serie = title_bst.search(nombre) # Usando BST
    serie = title_avl.search(nombre) # Usando AVL
    if len(serie) > 0:
        af.print_box("t")
        af.print_text(f'DETALLES DE LA SERIE "{nombre.title()}" ', "c")
        af.print_box("c")
                
        for key, value in SERIES[get_serie_index(serie[0], SERIES)].items():
            af.print_text(f'{key.title().replace("_", " ")}: {value},')
        
        af.print_box("b")
    
    else:
        imprimir_texto_ensanguchado(f'La serie "{nombre.title()}" NO se encuentra disponible.')


    af.print_space("-")

    imprimir_texto_ensanguchado(TITULO_PANTALLA_SECUNDARIA, "c", "-")
    opciones = {
        "Buscar Otra Serie": buscar_series,
        "Volver Al Menu Principal": mostrar_menu_principal,
        "Salir": salir,
    }
    
    imprimir_pantalla_ensanguchada(list(opciones.keys()))
    user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")
    
    while seleccionar_opcion(user, list(opciones.values())) != True:
        imprimir_pantalla_ensanguchada(list(opciones.keys()))
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")




def recomendar_por_tiempo_disponible():
    """Recomienda series en base a su prioridad.
       la prioridad se calcula de la siguiente forma  
       se divide la popularidad de la serie con la duracion_promedio_episodio
       multiplicado por la cantidad_de_episodios.       
       Valora la popularidad sobre la duracion en ciertos casos.
    """
    
    series = ranking_prioridad.top_n(10)
   
    sep = "- -"
    af.print_space("-")
    
    af.print_box("t")
    af.print_text("Ranking de series populares con menos duración por episodio".upper(), "c")
    af.print_box("c")
    af.print_text(" Título - Rango Etario - Popularidad - Menor Duracion Promedio ", "c", "-")
    af.print_space()
    [af.print_text(f"[{i+1}]-{serie["title"]} {sep} {serie["age_rating"]} {sep} {serie["popularity_metrics"]/10}★ {sep} {serie["episode_duration_average"]}min ", "l") for i, serie in enumerate(series)]
    af.print_box("b")


    af.print_space("-")

    imprimir_texto_ensanguchado(TITULO_PANTALLA_SECUNDARIA, "c", "-")
    
    opciones = {
        "Volver Al Menu Principal": mostrar_menu_principal,
        "Salir": salir,
    }
    
    imprimir_pantalla_ensanguchada(list(opciones.keys()))
    user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")
    
    while seleccionar_opcion(user, list(opciones.values())) != True:
        imprimir_pantalla_ensanguchada(list(opciones.keys()))
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")





def recomendar_relacionado():
    """ Recomienda series relacionadas a la serie ingresada por el usuario
        GrafoLista busca y devuelve series relacionadas en genero, edad, 
        que tienen 10min de duracion promedio de episodio de diferencia, 
        con mas o menos 2 temporadas y mas o menos 1 punto de diferencia en popularidad.
    """    
   

    sep = "- -"
    nombre = input(">>>INGRESE EL NOMBRE DE UNA SERIE QUE LE GUSTE (en ingles): ")
    
    # primero reviso que la serie se encuentre en la lista usando el arbol avl
    serie = title_avl.search(nombre)
    serie_index = get_serie_index(nombre, SERIES)
    
    if len(serie) > 0: # Si la serie esta disponible
        # mostrar las series relacionadas
        vecinos = grafo_lista.vecinos(serie_index)
        
        af.print_box("t")
        af.print_text(f'LISTA DE SERIES RELACIONADAS A "{nombre.title()}"', "c")
        af.print_box("c")
        
        if len(vecinos) > 0:
            af.print_text(" Genero - Categoría De Edad - Popularidad - Duracion Promedio - Temporadas ", "c", "-")
            af.print_space()
        
            for i, v in enumerate(vecinos):
                af.print_text(f'[{i+1}]- {SERIES[v]["title"]}: {SERIES[v]["genre"]} {sep} {SERIES[v]["age_rating"]} {sep} {SERIES[v]["popularity_metrics"]/10} {sep} {SERIES[v]["episode_duration_average"]}min {sep} {SERIES[v]["seasons"]}', "l")    
        
        else:    
            af.print_text(f'La serie "{SERIES[serie_index]["title"]}" no tiene series relacionadas.',"c")
        
        af.print_box("b")
    
    else:
        af.print_space("-")
        imprimir_texto_ensanguchado(f'la serie "{nombre}" no se encuentra disponible.', "c")
       
       
    af.print_space("-")

    imprimir_texto_ensanguchado(TITULO_PANTALLA_SECUNDARIA, "c", "-")
    opciones = {
        "Recomendar Otra Serie Relacionada": recomendar_relacionado,
        "Volver Al Menu Principal": mostrar_menu_principal,
        "Salir": salir,
    }
    
    imprimir_pantalla_ensanguchada(list(opciones.keys()))
    user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")
    
    while seleccionar_opcion(user, list(opciones.values())) != True:
        imprimir_pantalla_ensanguchada(list(opciones.keys()))
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")
    




def recomendar_aleatorio():
     # lista de frases para recomendar series
    frases = ["después me lo agradecés.", 
              "está buenísima. Confiá.",
              "te está esperando. No la hagas esperar.",
              "ideal para fingir que descansás mientras hacés maratón.",
              "no te va a decepcionar.",
              "te va a robar la noche. Y vas a dejar que lo haga.",
              'es de esas que dicen "una más" y terminan a las 3 AM.',
              "cancelá todo, después arreglamos.",
              "es plan perfecto para no hacer nada con estilo.",
              "no es una recomendación, es una orden.",
              "viene con riesgo de maratón. Avisado estás.",
              "está muy buena, en serio. Dale una chance.",
              "me tuvo enganchado de principio a fin.",
              "es de esas que se recomiendan solas.",
              "la rompe. Mirala y después me contás.",
              "es una masa.",
              "vale cada minuto.",
              "te va a gustar, apuesto.",
              "hoy es tu mejor plan.",
    ]
    
    nombre = obtener_opcion_aleatoria()
    
    af.print_space("-")
    
    af.print_box("t")
    af.print_text('TE RECOMIENDO QUE MIRES:', "c")
    af.print_text(f'"{nombre.title()}"', "c")
    af.print_text(random.choice(frases).upper(), "c")
    af.print_box("b")
    
    af.print_space("-")
    
    imprimir_texto_ensanguchado(TITULO_PANTALLA_SECUNDARIA, "c", "-")
    opciones = {
        "Recomendar Otra Serie Aleatoria": recomendar_aleatorio,
        "Volver Al Menu Principal": mostrar_menu_principal,
        "Salir": salir,
    }
    
    imprimir_pantalla_ensanguchada(list(opciones.keys()))
    user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")
    
    while seleccionar_opcion(user, list(opciones.values())) != True:
        imprimir_pantalla_ensanguchada(list(opciones.keys()))
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")




def filtrar_por_genero():
    """ Imprime las series del genero ingresado por el usuario """
    print('Lista de generos: ' + ", ".join(GENEROS))
    print()
        
    genero = input(">>>INGRESE EL NOMBRE DEL GENERO: ")

    nodo_genero = arbol_general.buscar(genero) # Retorna el nodo con el genero
    
    af.print_space("-")

    if nodo_genero:
        lst = arbol_general.listar_hijos(nodo_genero) # Retorna una lista con todas las series con ese genero
        imprimir_texto_ensanguchado(f'LAS SIGUIENTES SERIES SON DEL GENERO "{genero.title()}"')
        imprimir_pantalla_ensanguchada(lst)
    else:
        imprimir_texto_ensanguchado(f'NO SE ENCONTRÓ EL GENERO "{genero.title()}"')
    
    
    af.print_space("-")

    imprimir_texto_ensanguchado(TITULO_PANTALLA_SECUNDARIA, "c", "-")
    opciones = {
        "Buscar Otro Genero": filtrar_por_genero,
        "Volver Al Menu Principal": mostrar_menu_principal,
        "Salir": salir,
    }
    
    imprimir_pantalla_ensanguchada(list(opciones.keys()))
    user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")

    while seleccionar_opcion(user, list(opciones.values())) != True:
        imprimir_pantalla_ensanguchada(list(opciones.keys()))
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")





def filtrar_por_temporadas():
    """ Imprime las series que tienen menos o igual cantidad de temporadas
        que la ingresada por el usuario
    """
    print("NO IMPLEMENTADO AUN :(")
    salir()
    
    


def filtrar_por_duracion_episodio():
    """ Imprime las series con menos duracion promedio de episodio
        el usuario debe ingresar la duracion promedio de una lista en pantalla
    """
    print("NO IMPLEMENTADO AUN :(")
    salir()




def filtrar_por_edad():
    """ Imprime las peliculas que son aptas para cierto publico
        el usuario ingresa la opcion de edad de una lista en pantalla
    """
    categoria_etaria = {
        "TV-G":  " Apto Para Todo Público",
        "TV-Y7": "7+",
        "TV-PG": "(8-12+)", # Parent Guidance Suggested
        "TV-14": "14+",
        "TV-MA": "17+",
    }
    
    af.print_space("-")
    
    af.print_box("t")
    af.print_text("SELECCIONE UNA CATEGORÍA DE EDAD:", "c")
    af.print_box("c")
    
    [af.print_text(f'{key}: {value}') for key, value in categoria_etaria.items()]
    
    af.print_box("b")
    
        
    edad = input("INGRESE UNA CATEGORÍA DE EDAD (Ej: TV-PG): ")
    nodo_edad = ag.buscar(edad.lower())
        
    if nodo_edad:
        lst = ag.listar_hijos(nodo_edad)
        imprimir_texto_ensanguchado(f'LAS SIGUIENTES SERIES SON DE LA CATEGORÍA DE EDAD "{edad.upper()}"')
        imprimir_pantalla_ensanguchada(lst)
    
    else:    
        imprimir_texto_ensanguchado(f'NO SE ENCONTRÓ NINGUNA SERIE CON LA CATEGORÍA "{edad.title()}"')


    af.print_space("-")
    
    imprimir_texto_ensanguchado(TITULO_PANTALLA_SECUNDARIA, "c", "-")
    opciones = {
        "Buscar Otra Categoría": filtrar_por_edad,
        "Volver Al Menu Principal": mostrar_menu_principal,
        "Salir": salir,
    }

    imprimir_pantalla_ensanguchada(list(opciones.keys()))
    user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")

    while seleccionar_opcion(user, list(opciones.values())) != True:
        imprimir_pantalla_ensanguchada(list(opciones.keys()))
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(opciones)}): ")
        





##############################################################################################################
# MENUS Y OPCIONES
##############################################################################################################

TITULO_PANTALLA_PRINCIPAL = "🎞 SERIESPLAY+ 🎞"
TITULO_PANTALLA_SECUNDARIA = " MENU DE OPCIONES "

MENSAJE_AL_USUARIO_1 = "SELECCIONE UNA OPCIÓN DEL MENU" # mensaje al usuario #1
MENSAJE_AL_USUARIO_2 = ">>> ESA NO ES UNA OPCION DE LA LISTA!"

OPCIONES_PANTALLA_PRINCIPAL = {"Buscar Serie": buscar_series, # BST/AVL
                               "Ranking de Series Cortas Y Populares": recomendar_por_tiempo_disponible, # HEAP
                               "Recomendar Series Relacionadas a...": recomendar_relacionado, # BFS/DFS
                               "Recomendar Serie Aleatoria": recomendar_aleatorio, # GRAFO
                               "Filtrar Por Genero": filtrar_por_genero, # Arbol General
                               "Filtrar Por Categoría De Edad": filtrar_por_edad, # Arbol General
#                               "Filtrar Por Cantidad De Temporadas": filtrar_por_temporadas,
#                               "Filtrar Por Duracion De Capitulo": filtrar_por_duracion_episodio, 
                               "Salir":salir,
}


def mostrar_menu_principal():
    print()
    # Imprime los titulos y las opciones en pantalla
    imprimir_texto_ensanguchado(TITULO_PANTALLA_PRINCIPAL) # Imprime el titulo de la pantalla principal 
    imprimir_pantalla_ensanguchada(list(OPCIONES_PANTALLA_PRINCIPAL.keys())) # convierte en "list/lista" las "keys/llaves" del diccionario









def main():    
    mostrar_menu_principal()
    while LOOP:
        # Los mensajes deberian ser dinamicos tambien
        user = input(MENSAJE_AL_USUARIO_1 + f"({1}-{len(OPCIONES_PANTALLA_PRINCIPAL)}): ")
        #Necesita el user_input y los valores de un diccionario con funciones
        seleccionar_opcion(user, list(OPCIONES_PANTALLA_PRINCIPAL.values()))
        
    
    
    
if __name__ == "__main__":
    main()
    


