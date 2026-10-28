import random
from ui.carga_de_datos import cargar_json
from ui.ascii_frame import AsciiFrame
from estructuras.arbol_binario import BST
from estructuras.avl import AVL


WIDTH = 80
af = AsciiFrame(WIDTH)

DATOS_10 = cargar_json("datos/dataset_10.json")
DATOS_100 = cargar_json("datos/dataset_100.json")
DATOS_1000 = cargar_json("datos/dataset_1000.json")

SERIES_10 = DATOS_10["series"]
SERIES_100 = DATOS_100["series"]
SERIES_1000 = DATOS_1000["series"]


# Cargar Arboles BST
bst_10 = BST()
bst_100 = BST()
bst_1000 = BST()

bst_10.load_str(SERIES_10, "title")
bst_100.load_str(SERIES_100, "title")
bst_1000.load_str(SERIES_1000, "title")


# Cargar Arboles AVL
avl_10 = BST()
avl_100 = BST()
avl_1000 = BST()

avl_10.load_str(SERIES_10, "title")
avl_100.load_str(SERIES_100, "title")
avl_1000.load_str(SERIES_1000, "title")



# COMPARACION BUSQUEDA BINARIA vs SECUENCIAL (PEOR CASO PARA SECUENCIAL)
last_title_10 = "Bob's Burgers"
last_title_100 = "The Americans"
last_title_1000 = "Forever"


# Contador de BST para misma serie en cada dataset
bst_10.search(last_title_10)
bst_100.search(last_title_100)
bst_1000.search(last_title_1000)



# Contador de busqueda secuencial para misma serie
def get_counter_secuencial(titulo, dataset):
    COUNTER_SECUENCIAL = 0

    for serie in dataset:
        if serie["title"].lower() == titulo.lower():
            break
        else:
            COUNTER_SECUENCIAL += 1

    return COUNTER_SECUENCIAL



# IMPRIMIR CUADRO COMPARATIVO
def imprimir_cuadro_comparativo_bst_sec():
        af.print_box("t")
        af.print_space()
        af.print_text("COMPLEJIDAD BUSQUEDA SECUENCIAL vs BST", "c")
        af.print_text("(PEOR CASO: ULTIMA SERIE DE LA LISTA)", "c")
        af.print_space()
        af.print_box("b")

        af.print_box("t")
        af.print_text(f'PARA DATASET_10 "{last_title_10}"', "c")
        af.print_space("-")
        af.print_text(f"SECUENCIAL: le tomó {get_counter_secuencial(last_title_10, SERIES_10)} pasos. ")
        af.print_text(f"BST: le tomó {bst_10.get_counter()} pasos. ")
        af.print_space("-")
        af.print_box("c")

        af.print_text(f'"PARA DATASET_100 "{last_title_100}"', "c")
        af.print_space("-")
        af.print_text(f"SECUENCIAL: le tomó {get_counter_secuencial(last_title_100, SERIES_100)} pasos. ")
        af.print_text(f"BST: le tomó {bst_100.get_counter()} pasos. ")
        af.print_space("-")
        af.print_box("c")

        af.print_text(f'PARA DATASET_1000 "{last_title_1000}"', "c")
        af.print_space("-")
        af.print_text(f"SECUENCIAL: le tomó {get_counter_secuencial(last_title_1000, SERIES_1000)} pasos. ")
        af.print_text(f"BST: le tomó {bst_1000.get_counter()} pasos. ")
        af.print_space("-")
        af.print_box("b")



# ANOTACIONES
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

SORTED_10 = [{"title": serie["title"],} for serie in SERIES_10] # obtengo solo los titulos
SORTED_10 = sorted(SORTED_10, key=lambda d: d["title"])

SORTED_100 = [{"title": serie["title"],}for serie in SERIES_100] 
SORTED_100 = sorted(SORTED_100, key=lambda d: d["title"])

SORTED_1000 = [{"title": serie["title"],} for serie in SERIES_1000]
SORTED_1000 = sorted(SORTED_1000, key=lambda d: d["title"])


# Cargar datos ordenados BST
sorted_bst_10 = BST()
sorted_bst_100 = BST()
sorted_bst_1000 = BST()

sorted_bst_10.load_str(SORTED_10, "title")
sorted_bst_100.load_str(SORTED_100, "title")
sorted_bst_1000.load_str(SORTED_1000, "title")


# Cargar datos ordenados AVL
sorted_avl_10 = AVL()
sorted_avl_100 = AVL()
sorted_avl_1000 = AVL()

sorted_avl_10.load_str(SORTED_10, "title")
sorted_avl_100.load_str(SORTED_100, "title")
sorted_avl_1000.load_str(SORTED_1000, "title")


# PEORES CASOS PARA LISTA ORDENADA
last_serie_10 = "The Voice"
last_serie_100 = "iZombie"
last_serie_1000 = "iZombie"

sorted_bst_10.search(last_serie_10)
sorted_bst_100.search(last_serie_100)
sorted_bst_1000.search(last_serie_1000)

sorted_avl_10.search(last_serie_10)
sorted_avl_100.search(last_serie_100)
sorted_avl_1000.search(last_serie_1000)



# IMPRIMIR CUADRO COMPARATIVO

def imprimir_cuadro_comparativo_bst_avl():
    print()
    af.print_box("t")
    af.print_space()
    af.print_text("COMPLEJIDAD BST vs AVL", "c")
    af.print_text("(PEOR CASO: ULTIMA SERIE DE LA LISTA CON DATOS ORDENADOS)", "c")
    af.print_space()
    af.print_box("b")

    af.print_box("t")
    af.print_text(f'PARA DATASET_10 "{last_serie_10}"', "c")
    af.print_space("-")
    af.print_text(f"BST: le tomó {sorted_bst_10.get_counter()} pasos. ")
    af.print_text(f"AVL: le tomó {sorted_avl_10.get_counter()} pasos. ")
    af.print_space("-")
    af.print_box("c")

    af.print_text(f'PARA DATASET_100 "{last_serie_100}"', "c")
    af.print_space("-")
    af.print_text(f"BST: le tomó {sorted_bst_100.get_counter()} pasos. ")
    af.print_text(f"AVL: le tomó {sorted_avl_100.get_counter()} pasos. ")
    af.print_space("-")
    af.print_box("c")

    af.print_text(f'PARA DATASET_1000 "{last_serie_1000}"', "c")
    af.print_space("-")
    af.print_text(f"BST: le tomó {sorted_bst_1000.get_counter()} pasos. ")
    af.print_text(f"AVL: le tomó {sorted_avl_1000.get_counter()} pasos. ")
    af.print_space("-")
    af.print_box("b")




# ANOTACIONES
# EL ARBOL AVL A GRAN CANTIDAD DE DATOS MEJORA UN POCO MAS LA VELOCIDAD DE BUSQUEDA
# PORQUE ESTE REORDENA LOS NODOS MANTENIENDO UN LLENADO BALANCEADO DEL ARBOL.

# OTRO PROBLEMA DEL ARBOL BST ES QUE AL CARGARLO CON MAS DE MIL NODOS
# DE MANERA ORDENADA, PUEDE EXCEDER EL LIMITE DE RECURSION QUE PERMITE PYTHON
# Y LANZARNOS UN RecursionError. EN ESE CASO UNA BUENA SOLUCION PODRIA SER
# UTILIZAR UN WHILE LOOP PARA INSERTAR NODOS EN EL ARBOL.


imprimir_cuadro_comparativo_bst_sec()
imprimir_cuadro_comparativo_bst_avl()




















