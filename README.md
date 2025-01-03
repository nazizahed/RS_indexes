## Authors
This library was created by:
- **Sadra Zahed Kachaee  10968059** -  Developer
- **Hoda Sadat Mousavi Tabar  10904806** -  Developer
- **Hana Asadi Aghbolaghi  10962418** -  Developer
  
# RS_indexes
A Python library to compute popular remote sensing indexes like NDVI, EVI, NDMI, NDWI, and NBR.
![GitHub issues](https://img.shields.io/github/issues/<your-username>/RS_indexes)
![GitHub license](https://img.shields.io/github/license/<your-username>/RS_indexes)

## 📘 Description
RS_indexes is a Python library designed for geospatial analysis, allowing users to compute popular remote sensing (RS) indexes from satellite imagery. 
This package provides functions to calculate common indexes like NDVI, EVI, NDMI, NDWI, and NBR. 
It also provides functionality to load specific bands from satellite images (e.g., Sentinel-2) using the rasterio library.

## ✨ Features
- 🟢 Compute **NDVI** (Normalized Difference Vegetation Index)
- 🟢 Compute **EVI** (Enhanced Vegetation Index)
- 🟢 Compute **NDMI** (Normalized Difference Moisture Index)
- 🟢 Compute **NDWI** (Normalized Difference Water Index)
- 🟢 Compute **NBR** (Normalized Burn Ratio)
- 🟢 Load specific image bands from satellite files (like Sentinel-2) using rasterio

## 🔧 Installation
To install **RS_indexes**, clone the repository and install the required dependencies.
```bash
git clone https://github.com/<your-username>/RS_indexes.git
cd RS_indexes
pip install -r requirements.txt

RS_indexes/
├── RS_indexes/
│     ├── __init__.py
│     └── rs_indexes.py  # Your main library file
├── setup.py             # Setup file for packaging
├── requirements.txt     # Required libraries (numpy, rasterio, etc.)
├── README.md            # Project documentation

