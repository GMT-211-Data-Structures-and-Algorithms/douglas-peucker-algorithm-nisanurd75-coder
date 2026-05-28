[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/C_oaaTG8)
# Douglas Peucker Algorithm

This project implements the Douglas-Peucker line simplification algorithm using Python.

## Project Purpose

The aim of this project is to reduce the number of points in geographic data while preserving the overall shape of the geometry.

## Features

- Read GeoJSON files
- Support Polygon and MultiPolygon geometries
- Calculate perpendicular distance
- Simplify geometry using Douglas-Peucker algorithm
- Export simplified geometry as GeoJSON
- Visualize results in QGIS

## Files

- `main.py` → Main program
- `dp.py` → Algorithm functions
- `input.geojson` → Original geometry
- `output.geojson` → Simplified geometry

## Algorithm Steps

1. Read coordinates from GeoJSON
2. Find perpendicular distances
3. Detect the farthest point
4. Apply recursive simplification
5. Export simplified geometry

## Epsilon Value

The epsilon value controls simplification sensitivity.

Example:

```python
epsilon = 0.001
Smaller epsilon values preserve more detail.
Larger epsilon values produce stronger simplification.

Technologies
Python
GeoJSON
QGIS
Author

Nisanur Demir
