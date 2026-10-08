"""
arbol_general.py — Árbol General (N-ario)

Un árbol general donde cada nodo puede tener cualquier cantidad de hijos.
Se usa para representar jerarquías del dominio (categorías, géneros, etc.).

Uso:
    from estructuras.arbol_general import NodoGeneral, ArbolGeneral

    arbol = ArbolGeneral()
    arbol.insertar_raiz("Películas")
    nodo_cat = arbol.agregar_hijo("Películas", "Ciencia Ficción")
    arbol.agregar_hijo(nodo_cat, "Cyberpunk")
    arbol.agregar_hijo(nodo_cat, "Viajes temporales")
"""


class NodoGeneral:
    """Nodo de un árbol general: tiene un dato y una lista de hijos."""

    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def __repr__(self):
        return f"Nodo({self.dato})"


class ArbolGeneral:
    """Árbol General (n-ario). Cada nodo puede tener 0 o más hijos.

    Se usa para representar jerarquías naturales del dominio, como:
    Películas → Ciencia Ficción → Cyberpunk, Viajes Temporales, IA
             → Acción
             → Comedia
    """

    def __init__(self):
        self.raiz = None

    # ==================== INSERCIÓN ====================

    def insertar_raiz(self, dato):
        """Crea el nodo raíz del árbol."""
        self.raiz = NodoGeneral(dato)
        return self.raiz

    def agregar_hijo(self, nodo_padre, dato):
        """Agrega un hijo al nodo padre y retorna el nuevo nodo creado."""
        if nodo_padre is None and self.raiz is None:
            raise ValueError("El árbol no tiene raíz. Use insertar_raiz primero.")

        nuevo_nodo = NodoGeneral(dato)
        nodo_padre.hijos.append(nuevo_nodo)
        return nuevo_nodo

    def buscar(self, valor):
        """Busca un nodo cuyo dato == valor en todo el árbol (búsqueda en amplitud).

        Devuelve el nodo o None si no existe.
        """
        if self.raiz is None:
            return None

        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if actual.dato.lower() == valor.lower():
                return actual
            cola.extend(actual.hijos)
        return None

    def buscar_recursivo(self, valor, nodo=None):
        """Busca un nodo por profundidad (DFS). Devuelve el nodo o None."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        if nodo.dato == valor:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_recursivo(valor, hijo)
            if resultado is not None:
                return resultado
        return None

    # ==================== RECORRIDOS ====================

    def amplitud(self):
        """Recorrido en amplitud (BFS): nivel por nivel, de arriba hacia abajo.

        Devuelve una lista con los datos en orden de nivel.
        """
        if self.raiz is None:
            return []

        resultado = []
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.dato)
            cola.extend(actual.hijos)
        return resultado

    def profundidad_preorder(self, nodo=None, resultado=None):
        """Recorrido en profundidad preorder (DFS): nodo → hijos de izquierda a derecha.

        Devuelve una lista con los datos en preorder.
        """
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado

        resultado.append(nodo.dato)
        for hijo in nodo.hijos:
            self.profundidad_preorder(hijo, resultado)
        return resultado

    def profundidad_postorder(self, nodo=None, resultado=None):
        """Recorrido en profundidad postorder (DFS): hijos → nodo.

        Devuelve una lista con los datos en postorder.
        """
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado

        for hijo in nodo.hijos:
            self.profundidad_postorder(hijo, resultado)
        resultado.append(nodo.dato)
        return resultado

    # ==================== INFORMACIÓN ====================

    def altura(self, nodo=None):
        """Altura máxima del árbol (o del subárbol dado)."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self, nodo=None):
        """Cantidad total de nodos en el árbol (o subárbol)."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + sum(self.cantidad_nodos(hijo) for hijo in nodo.hijos)

    def es_vacio(self):
        return self.raiz is None

    # ==================== UTILIDADES ====================

    def listar_hijos(self, nodo):
        """Retorna los datos de los hijos directos de un nodo."""
        return [hijo.dato for hijo in nodo.hijos]

    def obtener_niveles(self):
        """Retorna los datos organizados por nivel.

        Devuelve una lista de listas: [[raíz], [hijos_de_raíz], [nietos], ...]
        """
        if self.raiz is None:
            return []

        niveles = []
        nivel_actual = [self.raiz]
        while nivel_actual:
            niveles.append([n.dato for n in nivel_actual])
            siguiente = []
            for nodo in nivel_actual:
                siguiente.extend(nodo.hijos)
            nivel_actual = siguiente
        return niveles

    def __repr__(self):
        if self.raiz is None:
            return "Árbol General vacío"
        return f"Árbol General (raíz: {self.raiz.dato}, altura: {self.altura()})"



    def cargar_generos(self, arbol, generos):
        """ Carga el arbol con generos y retorna una lista con ellos
            necesita el arbol con la raiz y una lista de generos
        """
        lst = []
        for genero in generos:
            arbol_genero = arbol.agregar_hijo(arbol.raiz, genero)    
            lst.append(arbol_genero)
        return lst

    def cargar_series(self, arbol, arbol_generos, series):
        """ Carga los generos en el arbol y retorna el arbol cargado
            necesita el arbol con la raiz y los generos cargados
            arbol_generos es la lista que retorna cargar_generos
            series es la lista de titulos a cargar en el arbol
        """
        for genero in arbol_generos:
             for serie in series:
                if serie["genre"] == genero.dato:
                    arbol.agregar_hijo(genero, serie["title"])     
        return arbol




