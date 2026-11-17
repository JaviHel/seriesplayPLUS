import sys
from estructuras.grafos import GrafoMatriz, GrafoLista
from algoritmos.recorridos import Recorridos
from algoritmos.caminos_minimos import dijkstra_matriz
from ui.carga_de_datos import cargar_json


series = cargar_json("datos/dataset_1000.json")["series"]


gm = GrafoMatriz(len(series)) # Crea una matriz de todas las series
gl = GrafoLista(len(series)) # Crea una lista de todas las series



# condiciones
# mismo genero
# misma edad
# duracion de episodio similar (+-10min)
# cantidad de temporadas similar (+-2temp)


# serie_a 25min 
# serie_b 18min
# abs(25 - 18) = 7 <= 10

# Heap devuelve series cortas y populares no admite busqueda

# GrafoLista busca y devuelve series relacionadas en genero, edad, 
# tienen 10min de duracion promedio de episodio de diferencia 
# ,mas o menos 2 temporadas y mas o menos 1 punto de diferencia en popularidad.
# No se le agregó peso al grafo porque queria que mantuviera 
# una relacion de ida y vuelta entre cada serie.


def get_serie_index(serie_title:str, series:list) -> int:
    """ returns the index of the serie with that title, if serie in list """
    for i, serie in enumerate(series):
        if serie_title.lower() == serie["title"].lower():
            return series.index(serie)
    return None

# cargar grafo lista
def cargar_grafo(grafo, series:list): # O(n**2)
    episode_duration_range = 10
    seasons_range = 2
    popularity_range = 10

    for i, serie_a in enumerate(series):
        for j, serie_b in enumerate(series):              
            if (serie_a["title"] != serie_b["title"] # Evita repeticiones
            and serie_a["genre"] == serie_b["genre"] # Mismo Genero
            and serie_a["age_rating"] == serie_b["age_rating"] # Mismo rango_etario
            and abs(serie_a["episode_duration_average"] - serie_b["episode_duration_average"]) <= episode_duration_range # Duracion similar
            and abs(serie_a["seasons"] - serie_b["seasons"]) <= seasons_range # Similar cantidad de temporadas
            and abs(serie_a["popularity_metrics"] - serie_b["popularity_metrics"]) <= popularity_range # Rango de popularidad similar
            ):
        
               grafo.agregar_arista(i, j)



#def mostrar_relacionado_a(series_title, vecinos):
#    serie_vecinos = []
#    
#    for vecino in vecinos:
#        serie_vecinos.append(f"{series[vecino]["title"]}, {series[vecino]["genre"]}, {series[vecino]["episode_duration_average"]}")     
#  
#    print(series_title)
#    print(serie_vecinos)
   


def mostrar_relacionado_a():
    serie_title = my_serie # input("ingrese una serie: ")
    index = get_serie_index(serie_title, series)
    vecinos = gl.vecinos(index)
    
#    print()
#    print("title, genre, age_rating, episode_duration, seasons,".upper())    
#    print(f"USER: {series[index]["title"]}, {series[index]["genre"]}, {series[index]["age_rating"]}, {series[index]["popularity_metrics"]/10}, {series[index]["episode_duration_average"]}, {series[index]["seasons"]}")
#    print()
    
#    for vecino in vecinos:
#        print(f"{series[vecino]["title"]}, {series[vecino]["genre"]}, {series[vecino]["age_rating"]}, {series[vecino]["popularity_metrics"]/10}, {series[vecino]["episode_duration_average"]}, {series[vecino]["seasons"]}")     
  
#    print()
#    print("TOTAL:", len(vecinos))
    
    return vecinos



cargar_grafo(gl, series)


#my_serie = "the good doctor"
#my_serie_index = get_serie_index(my_serie, series)

#vecinos_gm = (gm.vecinos(my_serie_index))
#mostrar_relacionado_a(my_serie, vecinos_gm)

#vecinos_gl = (gl.vecinos(my_serie_index))
#mostrar_relacionado_a(my_serie, vecinos_gl)


#vecinos = mostrar_relacionado_a()


#gm.mostrar()
#gl.mostrar()


#print(vecinos)
#print(series[vecinos[1]]["title"])

#nuevos_vecinos = Recorridos.bfs(vecinos[1], gl)
#print(nuevos_vecinos) 








# cargar grafo matriz


def cargar_grafo_matriz(grafo, series):
    episode_duration_range = 2
   
    for i, serie_a in enumerate(series):
        for j, serie_b in enumerate(series):
            if (i != j
            and series[i]["genre"] == series[j]["genre"]
            and abs(series[i]["episode_duration_average"] - series[j]["episode_duration_average"]) <= episode_duration_range):
                peso = abs(series[i]["episode_duration_average"] - series[j]["episode_duration_average"])
                grafo.agregar_arista(i, j, peso)



cargar_grafo_matriz(gm, series)

# Buscar el camino minimo entre series del mismo genero y el peso es la menor duracion 

s1 = "house"
s2 = "breaking bad"

index_s1 =  get_serie_index(s1, series)
index_s2 =  get_serie_index(s2, series)


# Retorna una lista con el camino minimo de la serie
lst = dijkstra_matriz(gm.matriz, index_s1)

lst_series = set() # Uso un set porque repite series

for i in lst:
    if 0 < i < len(lst):
        lst_series.add(f"{series[i]["title"]}, {series[i]["episode_duration_average"]}")


print(lst_series)




















