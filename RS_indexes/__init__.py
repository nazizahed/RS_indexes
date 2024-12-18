from .rs_indexes import RSIndexes  # Import the main class

# Expose the class methods as "top-level functions"
compute_ndvi = RSIndexes.compute_ndvi
compute_evi = RSIndexes.compute_evi
compute_ndmi = RSIndexes.compute_ndmi
compute_ndwi = RSIndexes.compute_ndwi
compute_nbr = RSIndexes.compute_nbr
load_band = RSIndexes.load_band

__all__ = ['compute_ndvi', 'compute_evi', 'compute_ndmi', 'compute_ndwi', 'compute_nbr', 'load_band']
