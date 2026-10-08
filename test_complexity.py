import random
from ui.carga_de_datos import *
from estructuras.arbol_binario import BST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral, NodoGeneral

DATOS = cargar_json("datos/dataset_1000.json")
SERIES = DATOS["series"]

#title_bst = BST()
#title_bst.load_str(SERIES, "title")

#title_avl = AVL()
#title_avl.load_str(SERIES, "title")


# COMPARACION BUSQUEDA BINARIA vs SECUENCIAL (PEOR CASO PARA SECUENCIAL)
#search_title = "Forever"


# Contador de busqueda binaria para misma serie
#title_bst.search(search_title)
#print("BST: ", title_bst.get_counter()) # le toma


# Contador de busqueda secuencial para misma serie
#COUNTER_SECUENCIAL = 0

#for serie in SERIES:
#    if serie["title"].lower() == search_title:
#        break
#    else:
#        COUNTER_SECUENCIAL += 1

#print("SEC: ", COUNTER_SECUENCIAL) # le toma 



# Contador de busqueda avl para misma serie
#title_avl.search(search_title)
#print("AVL: ", title_avl.get_counter())


# SE BUSCA LA ULTIMA SERIE DE CADA DATASET 
# dataset_10 = "Bob's Burgers"
# dataset_100 = "The Americans"
# dataset_1000 = "Forever"



# PARA DATASET_10
# buscar la serie "Bob's Burgers" le tomó:
#    5 pasos al BST
#    10 pasos al secuencial


# PARA DATASET_100
# buscar la serie "The Americans" le tomó:
#   8 pasos al BST
#   100 pasos al secuencial

# PARA DATASET_1000
# buscar la serie "Forever" le tomó:
#    13 pasos al BST
#    1000 pasos al secuencial



# SI ORDENAMOS LOS TITULOS ALFABETICAMENTE ANTES DE CARGARLOS EN EL ARBOL BINARIO
# EL ARBOL BINARIO SE CONVIERTE EN SECUENCIAL PORQUE QUEDA DESBALANCEADO
# Y PIERDE SU VELOCIDAD DE BUSQUEDA.



##################################################################################



# TP_04
# Desbalancear el arbol para que la complejidad de busqueda
# sea el peor caso para el BST
# Para desbalancear el arbol hay que ordenar el dataset alphabeticamente
# antes de cargar el arbol.
# de esta manera el arbol BST se transforma en una lista enlazada comun.

SORTED_TITLES = [serie["title"] for serie in SERIES] # obtengo solo los titulos
SORTED_TITLES.sort()
#print(SORTED_TITLES[len(SORTED_TITLES)-1])
#print(SORTED_TITLES)

title_bst = BST()
title_bst.load(SORTED_TITLES, "title")

title_avl = AVL()
title_avl.load(SORTED_TITLES, "title")

# PEORES CASOS PARA LISTA ORDENADA
# dataset_10 = "The Voice"
# dataset_100 = "iZombie"
# dataset_1000 = "iZombie"

# Serie a buscar
search_title = "iZombie"

# Contador de busqueda binaria para misma serie
#title_bst.search(search_title)
#print("BST: ", title_bst.get_counter()) # le toma
#
# Contador de busqueda avl para misma serie
#title_avl.search(search_title)
#print("AVL: ", title_avl.get_counter())


# COMPLEJIDAD ARBOL AVL vs BST (PEOR CASO PARA BST)

# PARA DATASET_10
# buscar la serie "The Voice" le tomó:
#    10 pasos al BST
#    4 pasos al AVL

# PARA DATASET_100
# buscar la serie "iZombie" le tomó:
#   37 pasos al BST
#   8 pasos al AVL


# PARA DATASET_1000
# buscar la serie "iZombie" le tomó:
#    260 pasos al BST
#    12 pasos al AVL


# EL ARBOL AVL A GRAN CANTIDAD DE DATOS MEJORA UN POCO MAS LA VELOCIDAD DE BUSQUEDA
# PORQUE ESTE REORDENA LOS NODOS MANTENIENDO UN LLENADO BALANCEADO DEL ARBOL.

# OTRO PROBLEMA DEL ARBOL BST ES QUE AL CARGARLO CON MAS DE MIL NODOS
# DE MANERA ORDENADA, PUEDE EXCEDER EL LIMITE DE RECURSION QUE PERMITE PYTHON
# Y LANZARNOS UN RecursiveError. EN ESE CASO UNA BUENA SOLUCION PODRIA SER
# UTILIZAR UN WHILE LOOP PARA INSERTAR NODOS EN EL ARBOL.



