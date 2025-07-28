from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cropgbm',
    version='1.1.8',
    description=(
    	'Crop Genomic Breeding machine (CropGBM) is a multifunctional program that integrates data preprocessing, population structure analysis, SNP selection, phenotype prediction, and data visualization.'
    	 ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yuetong Xu, Jun Yan',
    author_email='cau_xyt@163.com',
    maintainer='Yuetong Xu',
    maintainer_email='cau_xyt@163.com',
    license='MIT',
    license_files=["LICENSE"],
    url='https://github.com/YuetongXU/CropGBM',
    packages=find_packages(),
    entry_points={
    'console_scripts': [
        'cropgbm = cropgbm.main:main',
        ]
    },
    package_data={
        'cropgbm': ['testdata/*']
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.8,<=3.11',
    install_requires=[
        'wheel>=0.36.0',
        'numpy>=1.21.0,<2.0.0',
        'scipy>=1.7.0',
        'pandas>=1.3.0',
        'scikit-learn>=0.24.2',
        'lightgbm>=3.3.0,<4.0.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0'
    ]
)

