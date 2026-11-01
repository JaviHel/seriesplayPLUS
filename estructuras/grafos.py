class GrafoMatriz:
    def __init__(self, n, dirigido=False):
        self.n = n
        self.dirigido = dirigido
        self.matriz = [[0] * n for _ in range(n)]
        
        
    def agregar_arista(self, u, v, peso=1):
        self.matriz[u][v] = peso
        if not self.dirigido:
            self.matriz[v][u] = peso
        
        
    def eliminar_arista(self, u, v):
        self.matriz[u][v] = 0
        if not self.dirigido:
            self.matriz[v][u] = 0
            
    
    def hay_arista(self, u, v):
        return self.matriz[u][v] != 0
    
    
    def vecinos(self, u):
        return [v for v in range(self.n) if self.matriz[u][v] != 0]
    
    
    def mostrar(self):
        for fila in self.matriz:
            print(fila)






class GrafoLista:
    def __init__(self, n, dirigido=False):
        self.n = n
        self.dirigido = dirigido
        self.adj = {i: {} for i in range(n)} #{vecino: peso,}


    def agregar_arista(self, u, v, peso=1):
        self.adj[u][v] = peso
        if not self.dirigido:
            self.adj[v][u] = peso
    

    def eliminar_arista(self, u, v):
        self.adj[u].pop(v, None)
        if not self.dirigido:
            self.adj[v].pop(u, None)
    

    def hay_arista(self, u, v):
        return v in self.adj[u]


    def vecinos(self, u):
        return list(self.adj[u])


    def mostrar(self):
        for u, vecinos in self.adj.items():
            print(f'{u} -> {list(vecinos.items())}')







def cargar_grafo(grafo, series:list): # O(n**2)
    """ Funcion de ayuda para cargar el grafo
    """
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
            and abs(serie_a["popularity_metrics"] - serie_b["popularity_metrics"]) <= popularity_range): # Rango de popularidad similar 
                
               grafo.agregar_arista(i, j)



