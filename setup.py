from setuptools import setup, find_packages

setup(
    name='RS_indexes',
    version='0.1.0',
    description='A Python library to compute popular remote sensing indexes (NDVI, EVI, NDMI, NDWI, NBR).',
    author='Your Name',
    author_email='sadra.zahed@mail.polimi.it',
    url='https://github.com/nazizahed/RS_indexes.git',
    packages=find_packages(),  # Automatically finds the RS_indexes package
    install_requires=[
        'numpy',
        'rasterio',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


