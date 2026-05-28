from dp import (
    read_geojson,
    perpendicular_distance,
    douglas_peucker,
    write_geojson
)

input_file = "input.geojson"
output_file = "output.geojson"
epsilon = 0.0001


input_file = "input.geojson"
output_file = "output.geojson"
epsilon = 0.0001

points = read_geojson(input_file)

print("Number of points:", len(points))
print("First 5 points:", points[:5])

distance = perpendicular_distance(
    points[1],
    points[0],
    points[-1]
)

print("Distance:", distance)

simplified_points = douglas_peucker(
    points,
    epsilon
)

print("Simplified points:", len(simplified_points))

write_geojson(
    simplified_points,
    output_file
)

print("Output file created.")