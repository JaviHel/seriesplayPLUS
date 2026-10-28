from estructuras.heap import Heap

# ATENCION!
# NO CORRE EN ESTE DIRECTORIO, HAY QUE PONERLO EN EL DIRECTORIO PRINCIPAL

# TEST HEAP

ranking = Heap()
ranking.load(SERIES)

for series in SERIES:
    ranking.insert(series, calculate_priority(series))

print("Top 2 (best popularity-per-minute):")
for serie in ranking.top_n(5):
    print(" -", serie["title"])

print("\nHeap still has all 3 series:", len(ranking))










