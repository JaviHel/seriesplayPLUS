class Node:
    def __init__(self, key, item):
        self.key = key         # what we sort by (e.g. the year)
        self.items = [item]    # everything that has this key (e.g. all movies of that year)
        self.left = None       # subtree holding smaller keys
        self.right = None      # subtree holding larger keys




class BST:
    def __init__(self):
        self.root = None
        self.COUNTER = 0
    # ---------- insert ----------
    def insert(self, key, item):
        """Add an item under a key. Repeated keys keep all their items."""
        self.root = self._insert(self.root, key, item)

    def _insert(self, node, key, item):
        # base case: empty spot, the new node goes here
        if node is None:
            return Node(key, item)

        if key < node.key:
            node.left = self._insert(node.left, key, item)
        elif key > node.key:
            node.right = self._insert(node.right, key, item)
        else:
            # same key already in the tree: keep both, add to this node's list
            node.items.append(item)

        return node

    # ---------- search ----------
    def search(self, key):
        """Return the list of all items with this key ([] if none)."""
        return self._search(self.root, key)

    def _search(self, node, key):
        # base case 1: fell off the tree, nothing with this key
        self.COUNTER += 1 
        
        if node is None:
            return []
        # base case 2: found the key
        if key == node.key:
            return node.items

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ---------- sorted output ----------
    def in_order(self):
        """Return every item, ordered by key."""
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is None:
            return
        self._in_order(node.left, result)    # 1. everything smaller
        result.extend(node.items)            # 2. all items of this node
        self._in_order(node.right, result)   # 3. everything larger
    
    
    def pre_order(self):
        """Return every item, ordered by key."""
        result = []
        self._pre_order(self.root, result)
        return result

    def _pre_order(self, node, result):
        if node is None:
            return   
        result.extend(node.items)             # 1. all items of this node
        self._pre_order(node.left, result)    # 2. everything smaller
        self._pre_order(node.right, result)   # 3. everything larger


    def post_order(self):
        """Return every item, ordered by key."""
        result = []
        self._post_order(self.root, result)
        return result

    def _post_order(self, node, result):
        if node is None:
            return
        self._post_order(node.right, result)  # 1. everything smaller
        result.extend(node.items)             # 2. all items of this node
        self._post_order(node.left, result)   # 3. everything larger
    
    
    # Carga el arbol con datos, segun tipo de dato a trabajar
    def load_str(self, series, option="title"):
        """ Carga las opciones que sean strings """
        for serie in series:
            self.insert(serie[option].lower(), serie[option])
    
    def load_int(self, series, option="year"):
        """ Carga las opciones que sean integers """
        for serie in series:
            self.insert(serie[option], serie[option])
    
    
    def load(self, serie, option="title"):
        """ Carga las opciones """
        for title in serie:
            self.insert(title.lower(), option)
    
    
    def get_counter(self):
        return self.COUNTER


















