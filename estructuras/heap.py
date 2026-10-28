class Heap:
    """
    Array-based heap. is_max=True (default) makes it a max-heap: pop/peek
    return the HIGHEST priority. is_max=False makes it a min-heap.

    Internally it's just a Python list. For an item at index i:
        parent index  = (i - 1) // 2
        left child    = 2*i + 1
        right child   = 2*i + 2
    No pointers needed, the array positions ARE the tree shape.
    """

    def __init__(self, is_max=True):
        self._data = []       # list of (priority, item) tuples
        self.is_max = is_max

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    # ---------- the one comparison everything else is built on ----------
    def _has_higher_priority(self, a, b):
        """True if priority a should end up closer to the root than priority b."""
        if self.is_max:
            return a > b
        return a < b

    # ---------- index helpers ----------
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # ---------- insert ----------
    def insert(self, item, priority):
        self._data.append((priority, item))
        self._bubble_up(len(self._data) - 1)

    def _bubble_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self._has_higher_priority(self._data[i][0], self._data[parent][0]):
                self._swap(i, parent)
                i = parent
            else:
                break  # it settled into a valid spot, stop

    # ---------- peek ----------
    def peek(self):
        """Look at the top item WITHOUT removing it. O(1)."""
        if self.is_empty():
            return None
        _, item = self._data[0]
        return item

    # ---------- pop ----------
    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return None

        top_item = self._data[0][1]
        last = self._data.pop()  # take the last element out first

        if self._data:
            self._data[0] = last
            self._bubble_down(0)

        return top_item

    def _bubble_down(self, i):
        size = len(self._data)
        while True:
            left = self._left(i)
            right = self._right(i)
            best = i

            if left < size and self._has_higher_priority(self._data[left][0], self._data[best][0]):
                best = left
            if right < size and self._has_higher_priority(self._data[right][0], self._data[best][0]):
                best = right

            if best == i:
                break  # settled, no more swaps needed
            self._swap(i, best)
            i = best

    # ---------- top_n ----------
    def top_n(self, n):
        """
        Return the N highest-priority items WITHOUT modifying this heap.
        Works by popping from a throwaway copy, so the real heap is untouched.
        """
        temp = Heap(is_max=self.is_max)
        temp._data = list(self._data)  # shallow copy of the array

        result = []
        for _ in range(min(n, len(temp))):
            result.append(temp.pop())
        return result


    def load(self, series):
        """
        Series is a list of dictionaries
        """
        for serie in series:
            self.insert(serie, calculate_priority(serie))
        


def calculate_priority(series):
    """
    priority = popularity per minute of total watch time.
    Rewards series that are popular WITHOUT costing a lot of time to finish.
    """
    total_minutes = series["episode_duration_average"] * series["episodes"]
    return series["popularity_metrics"] / total_minutes
  

