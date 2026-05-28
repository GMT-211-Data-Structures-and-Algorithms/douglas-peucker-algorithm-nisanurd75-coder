import json

def read_geojson(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    geometry = data["features"][0]["geometry"]
    coordinates = geometry["coordinates"]

    if geometry["type"] == "LineString":
        return coordinates

    if geometry["type"] == "Polygon":
        ring = coordinates[0]
        if ring[0] == ring[-1]:
            ring = ring[:-1]
        return ring

    if geometry["type"] == "MultiPolygon":
        ring = coordinates[0][0]
        if ring[0] == ring[-1]:
            ring = ring[:-1]
        return ring

    raise ValueError("Unsupported geometry type: " + geometry["type"])
import math


def perpendicular_distance(point, start, end):

    x0, y0 = point
    x1, y1 = start
    x2, y2 = end

    numerator = abs(
        (y2 - y1) * x0
        - (x2 - x1) * y0
        + x2 * y1
        - y2 * x1
    )

    denominator = math.sqrt(
        (y2 - y1) ** 2 + (x2 - x1) ** 2
    )

    if denominator == 0:
        return 0

    return numerator / denominator
def douglas_peucker(points, epsilon):
    if len(points) < 3:
        return points

    max_distance = 0
    index = 0

    start = points[0]
    end = points[-1]

    for i in range(1, len(points) - 1):
        distance = perpendicular_distance(points[i], start, end)

        if distance > max_distance:
            max_distance = distance
            index = i

    if max_distance > epsilon:
        left_side = douglas_peucker(points[:index + 1], epsilon)
        right_side = douglas_peucker(points[index:], epsilon)

        return left_side[:-1] + right_side

    return [start, end]

def write_geojson(points, output_file):

    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": points
                },
                "properties": {}
            }
        ]
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(geojson_data, file, indent=4)