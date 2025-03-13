def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

points = [(0, 0), (3, 4), (1, 1), (2, 5), (6, 8)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

min_distance = min(distances)

print("Minimum Öklid mesafesi:", min_distance)
