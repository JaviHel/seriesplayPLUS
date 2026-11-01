from collections  import deque

class Recorridos:
    def bfs(inicio): # inicio es el nodo desde el cual empieza
        visitados = {inicio}
        cola = deque([inicio])
        orden = []
        
        while cola:
            u = cola.popleft()
            orden.append(u)
            for v in self.vecinos(u):
                if v not in visitados:
                    visitados.add(v)
                    cola.append(v)
            return orden
            
            
    def dfs(inicio):
        visitados = set()
        orden = []
        
        def visitar(u):
            visitados.add(u)
            orden.append(u)
            for v in inicio.vecinos(u):
                if v not in visitados:
                    visitar(v)
        
        visitar(inicio)
        return orden
            
    
    def dfs_iter(inicio):
        visitados = set()
        pila = [inicio]
        orden = []
        
        while pila:
            u = pila.pop()
            if u in visitados:
                continue
            visitados.add(u)
            orden.append(u)
            for v in reversed(inicio.vecinos(u)):
                if v not in visitados:
                    pila.append(v)
                    
        return orden
        
    
    def conexos(n):
        vistos = set()
        componentes = []
        for u in range(n):
            if u not in vistos:
                comp = Recorridos.bfs(u)
                vistos.update(comp)
                componentes.append(comp)
        return componentes
    
            

    def camino_minimo():
        pass
            
            
            
    
