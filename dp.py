import json

def read_geojson(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    geometry = data["features"][0]["geometry"]
    coordinates = geometry["coordinates"]

    if geometry["type"] == "LineString":
        return coordinates

    if geometry["type"] == "Polygon":
        return coordinates[0]

    if geometry["type"] == "MultiPolygon":
        return coordinates[0][0]

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
