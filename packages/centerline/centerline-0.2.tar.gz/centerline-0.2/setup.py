from setuptools import setup

setup(
    name='centerline',
    version='0.2',
    description='Calculate the centerline of a polygon',
    long_description='README.rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    url='https://github.com/fitodic/centerline.git',
    author='Filip Todic',
    author_email='todic.filip@gmail.com',
    license='MIT',
    packages=['centerline'],
    install_requires=[
        'GDAL>=1.11.2',
        'Fiona>=1.6.3',
        'Shapely>=1.5.13',
        'numpy>=1.10.4',
        'scipy>=0.16.1',
    ],
    extras_require={
        'dev': [
            'autopep8',
            'flake8',
            'ipdb',
        ],
        'test': [
            'coverage',
            'pytest>=3.0.0',
            'pytest-cov',
            'pytest-sugar',
            'pytest-runner',
            'tox'
        ],
    },
    scripts=[
        'bin/shp2centerline',
    ],
    include_package_data=True,
    zip_safe=False,
)
