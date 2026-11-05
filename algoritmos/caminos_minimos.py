import heapq, sys


def dijkstra_lista(grafo, origen):
    distancias = {nodo: float("inf") for nodo in grafo}    
    distancias[origen] = 0
    cola_heap = [{0, origen}] # min_heap
    
    while cola_heap:
        distancia_actual, nodo_actual = heapq.heappop(cola_heap)
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_heap, (distancia, vecino))
        
    return distancias
    
    
    
    
    
    
def min_dist(distancias, visitados):
    min_val = sys.maxsize # sys.maxsize es una representacion ficticia del infinito o el numero mas grande que soporta python
    min_indice = -1
    
    for v in range(len(distancias)):
        if distancias[v] < min_val and not visitados[v]:
            min_val = distancias[v]
            min_indice = v
    
    return min_indice        
        

def dijkstra_matriz(grafo, origen):
    n = len(grafo)
    distancias = [sys.maxsize] * n # Crea una lista de infinitos
    distancias[origen] = 0
    visitados = [False] * n
    
    for _ in range(n):
        u = min_dist(distancias, visitados)
        visitados[u] = True
        for v in range(n):
            if grafo[u][v] > 0 and not visitados[v] and distancias[u] + grafo[u][v] < distancias[v]:
                distancias[v] = distancias[u] + grafo[u][v]

    return distancias

