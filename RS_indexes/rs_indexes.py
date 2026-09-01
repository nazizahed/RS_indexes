"""Spectral-index calculations and lightweight Rasterio input helpers."""

from pathlib import Path

import numpy as np
import rasterio


def _arrays(*values: np.ndarray) -> tuple[np.ndarray, ...]:
    """Convert inputs to float arrays and require a shared shape."""
    arrays = tuple(np.asarray(value, dtype="float64") for value in values)
    shapes = {array.shape for array in arrays}
    if len(shapes) != 1:
        raise ValueError(f"Input arrays must have the same shape; received {sorted(shapes)}")
    return arrays


def _safe_ratio(numerator: np.ndarray, denominator: np.ndarray) -> np.ndarray:
    """Divide safely, returning zero where a finite denominator is zero."""
    result = np.zeros(numerator.shape, dtype="float64")
    np.divide(numerator, denominator, out=result, where=denominator != 0)
    result[~np.isfinite(numerator) | ~np.isfinite(denominator)] = np.nan
    return result


class RSIndexes:
    """Calculate common spectral indices from equally shaped band arrays."""

    @staticmethod
    def compute_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
        """Return NDVI = (NIR - Red) / (NIR + Red)."""
        nir, red = _arrays(nir, red)
        return _safe_ratio(nir - red, nir + red)

    @staticmethod
    def compute_evi(
        nir: np.ndarray,
        red: np.ndarray,
        blue: np.ndarray,
        G: float = 2.5,
        C1: float = 6.0,
        C2: float = 7.5,
        L: float = 1.0,
    ) -> np.ndarray:
        """Return the Enhanced Vegetation Index using standard coefficients."""
        nir, red, blue = _arrays(nir, red, blue)
        numerator = G * (nir - red)
        denominator = nir + C1 * red - C2 * blue + L
        return _safe_ratio(numerator, denominator)

    @staticmethod
    def compute_ndmi(nir: np.ndarray, swir: np.ndarray) -> np.ndarray:
        """Return NDMI = (NIR - SWIR) / (NIR + SWIR)."""
        nir, swir = _arrays(nir, swir)
        return _safe_ratio(nir - swir, nir + swir)

    @staticmethod
    def compute_ndwi(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
        """Return NDWI = (Green - NIR) / (Green + NIR)."""
        green, nir = _arrays(green, nir)
        return _safe_ratio(green - nir, green + nir)

    @staticmethod
    def compute_nbr(nir: np.ndarray, swir2: np.ndarray) -> np.ndarray:
        """Return NBR = (NIR - SWIR2) / (NIR + SWIR2)."""
        nir, swir2 = _arrays(nir, swir2)
        return _safe_ratio(nir - swir2, nir + swir2)

    @staticmethod
    def load_band(
        file_path: str | Path,
        band_index: int = 1,
        *,
        masked: bool = False,
    ) -> np.ndarray:
        """Read one 1-based band from a raster file."""
        with rasterio.open(file_path) as source:
            if not 1 <= band_index <= source.count:
                raise ValueError(
                    f"band_index must be between 1 and {source.count}; received {band_index}"
                )
            return source.read(band_index, masked=masked)
