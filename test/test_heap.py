from estructuras.heap import Heap

# TEST HEAP

ranking = Heap()
ranking.load(SERIES)

for series in SERIES:
    ranking.insert(series, calculate_priority(series))

print("Top 2 (best popularity-per-minute):")
for serie in ranking.top_n(5):
    print(" -", serie["title"])

print("\nHeap still has all 3 series:", len(ranking))










