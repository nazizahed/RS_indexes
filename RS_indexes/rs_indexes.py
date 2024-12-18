import numpy as np
import rasterio

class RSIndexes:
    """
    RSIndexes is a geospatial library to compute various popular Remote Sensing (RS) indexes.
    """

    @staticmethod
    def compute_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
        """
        Compute Normalized Difference Vegetation Index (NDVI).

        NDVI = (NIR - RED) / (NIR + RED)

        Parameters:
        nir (np.ndarray): Near-Infrared band image.
        red (np.ndarray): Red band image.

        Returns:
        np.ndarray: NDVI image.
        """
        numerator = nir - red
        denominator = nir + red
        with np.errstate(divide='ignore', invalid='ignore'):
            ndvi = np.true_divide(numerator, denominator)
            ndvi[denominator == 0] = 0
        return ndvi

    @staticmethod
    def compute_evi(nir: np.ndarray, red: np.ndarray, blue: np.ndarray, G: float = 2.5, C1: float = 6, C2: float = 7.5, L: float = 1) -> np.ndarray:
        """
        Compute Enhanced Vegetation Index (EVI).

        EVI = G * ((NIR - RED) / (NIR + C1 * RED - C2 * BLUE + L))

        Parameters:
        nir (np.ndarray): Near-Infrared band image.
        red (np.ndarray): Red band image.
        blue (np.ndarray): Blue band image.
        G (float): Gain factor (default=2.5).
        C1 (float): Coefficient 1 for the red band (default=6).
        C2 (float): Coefficient 2 for the blue band (default=7.5).
        L (float): Canopy background adjustment (default=1).

        Returns:
        np.ndarray: EVI image.
        """
        numerator = nir - red
        denominator = nir + C1 * red - C2 * blue + L
        with np.errstate(divide='ignore', invalid='ignore'):
            evi = G * np.true_divide(numerator, denominator)
            evi[denominator == 0] = 0
        return evi

    @staticmethod
    def compute_ndmi(nir: np.ndarray, swir: np.ndarray) -> np.ndarray:
        """
        Compute Normalized Difference Moisture Index (NDMI).

        NDMI = (NIR - SWIR) / (NIR + SWIR)

        Parameters:
        nir (np.ndarray): Near-Infrared band image.
        swir (np.ndarray): Short-Wave Infrared band image.

        Returns:
        np.ndarray: NDMI image.
        """
        numerator = nir - swir
        denominator = nir + swir
        with np.errstate(divide='ignore', invalid='ignore'):
            ndmi = np.true_divide(numerator, denominator)
            ndmi[denominator == 0] = 0
        return ndmi

    @staticmethod
    def compute_ndwi(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
        """
        Compute Normalized Difference Water Index (NDWI).

        NDWI = (GREEN - NIR) / (GREEN + NIR)

        Parameters:
        green (np.ndarray): Green band image.
        nir (np.ndarray): Near-Infrared band image.

        Returns:
        np.ndarray: NDWI image.
        """
        numerator = green - nir
        denominator = green + nir
        with np.errstate(divide='ignore', invalid='ignore'):
            ndwi = np.true_divide(numerator, denominator)
            ndwi[denominator == 0] = 0
        return ndwi

    @staticmethod
    def compute_nbr(nir: np.ndarray, swir2: np.ndarray) -> np.ndarray:
        """
        Compute Normalized Burn Ratio (NBR).

        NBR = (NIR - SWIR2) / (NIR + SWIR2)

        Parameters:
        nir (np.ndarray): Near-Infrared band image.
        swir2 (np.ndarray): Short-Wave Infrared 2 band image.

        Returns:
        np.ndarray: NBR image.
        """
        numerator = nir - swir2
        denominator = nir + swir2
        with np.errstate(divide='ignore', invalid='ignore'):
            nbr = np.true_divide(numerator, denominator)
            nbr[denominator == 0] = 0
        return nbr

    @staticmethod
    def load_band(file_path: str, band_index: int) -> np.ndarray:
        """
        Load a specific band from a satellite image using rasterio.

        Parameters:
        file_path (str): The file path to the satellite image (e.g., Sentinel-2 .tif file).
        band_index (int): The index of the band to load (1-based index).

        Returns:
        np.ndarray: The band data as a NumPy array.
        """
        with rasterio.open(file_path) as src:
            band = src.read(band_index)
        return band

if __name__ == "__main__":
    # Example usage (user can customize it as per their dataset)
    nir = np.array([[0.8, 0.7], [0.6, 0.9]])  # Example NIR band
    red = np.array([[0.3, 0.2], [0.1, 0.4]])  # Example Red band
    swir = np.array([[0.6, 0.7], [0.5, 0.4]])  # Example SWIR band
    green = np.array([[0.4, 0.5], [0.3, 0.6]])  # Example Green band
    blue = np.array([[0.1, 0.2], [0.1, 0.3]])  # Example Blue band
    swir2 = np.array([[0.4, 0.3], [0.5, 0.6]])  # Example SWIR2 band

    ndvi = RSIndexes.compute_ndvi(nir, red)
    evi = RSIndexes.compute_evi(nir, red, blue)
    ndmi = RSIndexes.compute_ndmi(nir, swir)
    ndwi = RSIndexes.compute_ndwi(green, nir)
    nbr = RSIndexes.compute_nbr(nir, swir2)

    print("NDVI:\n", ndvi)
    print("EVI:\n", evi)
    print("NDMI:\n", ndmi)
    print("NDWI:\n", ndwi)
    print("NBR:\n", nbr)
