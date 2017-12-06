# Part 1:

def ring(i):
    # Calculate the i-th circumference of the spiral.
    L = []
    for y in range(1 - i, i + 1):
        L.append((i, y))
    for x in reversed(range(-i, i)):
        L.append((x, i))
    for y in reversed(range(-i, i)):
        L.append((-i, y))
    for x in range(1 - i, i):
        L.append((x, -i))
    for y in range(-i, 1 - i):
        L.append((i, y))
    return L

def get_distance(n):
    # Brute force; calculate enough of the spiral, then snag the right coordinates.
    L = []
    inc = 0
    while len(L) < n:
        L.extend(ring(inc))
    inc += 1
 
 coords = L[n - 1]
 
 # The manhattan distance from the origin can be found by summing the absolute values 
 # within the coordinates.
 return sum(abs(q) for q in coords)
