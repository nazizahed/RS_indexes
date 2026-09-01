# Remote-Sensing Indices

`RS_indexes` is a small Python package for calculating five common spectral
indices from NumPy arrays and reading raster bands with Rasterio:

- NDVI - Normalized Difference Vegetation Index
- EVI - Enhanced Vegetation Index
- NDMI - Normalized Difference Moisture Index
- NDWI - Normalized Difference Water Index
- NBR - Normalized Burn Ratio

The package was developed collaboratively in 2024 as a reusable component for
coursework and small Earth Observation workflows. The public repository was
refreshed in 2026 to improve packaging, tests, and documentation; the index
formulas remain deliberately simple and transparent.

## Installation

Python 3.9 or newer is recommended.

```bash
git clone https://github.com/nazizahed/RS_indexes.git
cd RS_indexes
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Quick example

```python
import numpy as np
from RS_indexes import compute_ndvi, compute_ndwi

nir = np.array([[0.62, 0.41], [0.75, 0.20]])
red = np.array([[0.21, 0.30], [0.18, 0.20]])
green = np.array([[0.30, 0.35], [0.28, 0.20]])

ndvi = compute_ndvi(nir, red)
ndwi = compute_ndwi(green, nir)
```

A runnable version is available in [`examples/quickstart.py`](examples/quickstart.py).

To read a raster band:

```python
from RS_indexes import load_band

red = load_band("path/to/sentinel2_red.tif", band_index=1, masked=True)
```

`masked=True` preserves a raster's nodata mask. Index functions return zero
where a denominator is zero, matching the behaviour of the original package,
and preserve `NaN` values from floating-point inputs.

## Test data

The `test_data/` directory contains small Sentinel-2 band samples retained from
the original project. Their original catalogue metadata is not bundled, so
they are provided only for software demonstrations and must not be treated as
analysis-ready scientific products.

## Tests

```bash
python -m unittest discover -s tests -v
```

The automated tests cover the five formulas, mismatched-array validation, zero
denominators, and Rasterio band loading with a temporary synthetic raster.

## Repository structure

```text
RS_indexes/
|-- RS_indexes/          # Package source
|-- examples/            # Runnable minimal example
|-- tests/               # Automated unit tests
|-- test_data/           # Original small demonstration rasters
|-- pyproject.toml       # Package metadata and dependencies
`-- requirements.txt    # Direct runtime dependencies
```

## Contributors

- Sadra Zahed Kachaee
- Hoda Sadat Mousavi Tabar
- Hananeh Asadi Aghbolaghi

## Licence

Released under the [MIT License](LICENSE).

