from dp import read_geojson

input_file = "input.geojson"

points = read_geojson(input_file)

print("Number of points:", len(points))
print("First 5 points:", points[:5])