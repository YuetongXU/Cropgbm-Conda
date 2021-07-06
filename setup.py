# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='cropgbm',
    version='1.1.2',
    description=(
        'Crop Genomic Breeding machine (CropGBM) is a multifunctional program that integrates data preprocessing, '
        'population structure analysis, SNP selection, phenotype prediction, and data visualization.'
    ),
    long_description=open('README.md').read(),
    author='Yuetong Xu, Jun Yan',
    author_email='cau_cab_xu@163.com',
    maintainer='Yuetong Xu',
    maintainer_email='cau_cab_xu@163.com',
    license='MIT License',
    platforms=["linux"],
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
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3',
    install_requires=[
        'wheel',
        'numpy',
        'scipy',
        'pandas',
        'scikit-learn>=0.24',
        'lightgbm',
        'matplotlib',
        'seaborn'
    ]
)
