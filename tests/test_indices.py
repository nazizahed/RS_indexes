import tempfile
import unittest
from pathlib import Path

import numpy as np
import rasterio
from rasterio.transform import from_origin

from RS_indexes import (
    compute_evi,
    compute_nbr,
    compute_ndmi,
    compute_ndvi,
    compute_ndwi,
    load_band,
)


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.nir = np.array([[0.8, 0.0], [0.6, 0.9]])
        self.red = np.array([[0.2, 0.0], [0.1, 0.4]])
        self.green = np.array([[0.4, 0.0], [0.3, 0.6]])
        self.blue = np.array([[0.1, 0.0], [0.1, 0.3]])
        self.swir = np.array([[0.6, 0.0], [0.5, 0.4]])
        self.swir2 = np.array([[0.4, 0.0], [0.5, 0.6]])

    def test_ndvi_values_and_zero_denominator(self):
        result = compute_ndvi(self.nir, self.red)
        self.assertAlmostEqual(float(result[0, 0]), 0.6)
        self.assertEqual(float(result[0, 1]), 0.0)

    def test_all_supported_indices_preserve_shape(self):
        results = [
            compute_evi(self.nir, self.red, self.blue),
            compute_ndmi(self.nir, self.swir),
            compute_ndwi(self.green, self.nir),
            compute_nbr(self.nir, self.swir2),
        ]
        self.assertTrue(all(result.shape == self.nir.shape for result in results))

    def test_nan_is_preserved(self):
        nir = self.nir.copy()
        nir[0, 0] = np.nan
        self.assertTrue(np.isnan(compute_ndvi(nir, self.red)[0, 0]))

    def test_mismatched_shapes_raise_clear_error(self):
        with self.assertRaisesRegex(ValueError, "same shape"):
            compute_ndvi(np.ones((2, 2)), np.ones((3, 2)))

    def test_load_band(self):
        data = np.array([[1, 2], [3, 4]], dtype="uint16")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.tif"
            with rasterio.open(
                path,
                "w",
                driver="GTiff",
                width=2,
                height=2,
                count=1,
                dtype=data.dtype,
                crs="EPSG:32631",
                transform=from_origin(0, 20, 10, 10),
            ) as destination:
                destination.write(data, 1)
            np.testing.assert_array_equal(load_band(path), data)


if __name__ == "__main__":
    unittest.main()

