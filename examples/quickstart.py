"""Minimal array-based example for RS_indexes."""

import numpy as np

from RS_indexes import compute_ndvi, compute_ndwi


nir = np.array([[0.62, 0.41], [0.75, 0.20]])
red = np.array([[0.21, 0.30], [0.18, 0.20]])
green = np.array([[0.30, 0.35], [0.28, 0.20]])

print("NDVI")
print(compute_ndvi(nir, red))
print("NDWI")
print(compute_ndwi(green, nir))

