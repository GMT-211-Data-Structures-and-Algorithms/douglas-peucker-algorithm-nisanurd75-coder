from dp import read_geojson, perpendicular_distance


input_file = "input.geojson"

points = read_geojson(input_file)

print("Number of points:", len(points))
print("First 5 points:", points[:5])
distance = perpendicular_distance(
    points[1],
    points[0],
    points[-1]
)

print("Distance:", distance)