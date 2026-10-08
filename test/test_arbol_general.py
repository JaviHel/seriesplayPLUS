import random
from ui.carga_de_datos import *
from estructuras.arbol_general import ArbolGeneral

DATOS = cargar_json("datos/dataset_100.json")
SERIES = DATOS["series"]


# ATENCION!
# NO CORRE EN ESTE DIRECTORIO, HAY QUE PONERLO EN EL DIRECTORIO PRINCIPAL

 

# ==================== EJEMPLO DE USO ====================
"""
{'Horror', 'War', 'Comedy', 'Sci-Fi', 'Western', 'Fantasy',
 'Game Show', 'Action', 'Thriller', 'Reality', 'Crime', 'Drama', 'Talk',
 'Animation', 'Mystery', 'Adventure', 'Documentary'}
"""

"""
{'TV-Y7', 'TV-14', 'TV-G', 'TV-MA', 'TV-PG'}
"""

GENEROS = ['Horror', 'War', 'Comedy', 'Sci-Fi', 'Western', 'Fantasy',
           'Game Show', 'Action', 'Thriller', 'Reality', 'Crime', 
           'Drama', 'Talk', 'Animation', 'Mystery', 'Adventure', 'Documentary']

def cargar_generos(arbol, generos):
    lst = []
    for genero in generos:
        arbol_genero = arbol.agregar_hijo(arbol.raiz, genero)    
        lst.append(arbol_genero)
    return lst


def cargar_series(arbol, arbol_generos, series):
    for genero in arbol_generos:
         for serie in series:
            if serie["genre"] == genero.dato:
                arbol.agregar_hijo(genero, serie["title"])     
    return arbol



if __name__ == "__main__":
    # Crear un árbol de categorías de películas
    arbol = ArbolGeneral()
    arbol.insertar_raiz("Series") # nivel 0
    
    arbol_generos = cargar_generos(arbol, GENEROS) # nivel 1
    arbol = cargar_series(arbol, arbol_generos, SERIES) # nivel 2

#    ciencia = arbol.agregar_hijo(arbol.raiz, "Ciencia Ficción")
#    accion = arbol.agregar_hijo(arbol.raiz, "Acción")
#    comedia = arbol.agregar_hijo(arbol.raiz, "Comedia")
#
#    arbol.agregar_hijo(ciencia, "Cyberpunk")
#    arbol.agregar_hijo(ciencia, "Viajes temporales")
#    arbol.agregar_hijo(ciencia, "Inteligencia artificial")
#
#    arbol.agregar_hijo(accion, "Superhéroes")
#    arbol.agregar_hijo(accion, "Guerra")
#
#    arbol.agregar_hijo(comedia, "Comedia romántica")
#    arbol.agregar_hijo(comedia, "Comedia negra")

#    print("=== Árbol General de Categorías ===")
#    print("Raíz:", arbol.raiz.dato)
#    print("Altura:", arbol.altura())
#    print("Cantidad de nodos:", arbol.cantidad_nodos())
#    print()

#    print("--- Recorrido en amplitud ---")
#    print(arbol.amplitud())
#    print()

#    print("--- Recorrido en profundidad (preorder) ---")
#    print(arbol.profundidad_preorder())
#    print()
#
#    print("--- Recorrido en profundidad (postorder) ---")
#    print(arbol.profundidad_postorder())
#    print()

#    print("--- Niveles ---")
#    for i, nivel in enumerate(arbol.obtener_niveles()):
#        print(f"  Nivel {i}: {nivel}")
#    print()

    rand_genero = random.choice(GENEROS)
    print(f"--- Hijos de '{rand_genero}' ---")
    nodo_ciencia = arbol.buscar(rand_genero)
    if nodo_ciencia:
        print(arbol.listar_hijos(nodo_ciencia)) # esta lista utilizarla para mostrar en pantalla

#    print()
#    print("--- Buscar 'Cyberpunk' ---")
#    resultado = arbol.buscar("Cyberpunk")
#    print("Encontrado:", resultado)




