"""Public API for the RS_indexes package."""

from .rs_indexes import RSIndexes

compute_ndvi = RSIndexes.compute_ndvi
compute_evi = RSIndexes.compute_evi
compute_ndmi = RSIndexes.compute_ndmi
compute_ndwi = RSIndexes.compute_ndwi
compute_nbr = RSIndexes.compute_nbr
load_band = RSIndexes.load_band

__all__ = [
    "RSIndexes",
    "compute_ndvi",
    "compute_evi",
    "compute_ndmi",
    "compute_ndwi",
    "compute_nbr",
    "load_band",
]
