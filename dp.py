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