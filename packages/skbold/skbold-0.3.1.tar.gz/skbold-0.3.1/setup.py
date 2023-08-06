import skbold
from setuptools import setup, find_packages

REQUIREMENTS = [
    'scipy>=0.17',
    'numpy>=1.10',
    'scikit-learn>=0.18',
    'pandas>=0.17',
    'nibabel>=2.0',
    'nilearn',
    'configparser'
]

VERSION = skbold.__version__

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='skbold',
    version=VERSION,
    description='Utilities and tools for machine learning and other ' \
                'multivoxel pattern analyses of fMRI data.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'],
    keywords="fMRI MVPA decoding machine learning",
    url='http://skbold.readthedocs.io/en/latest/',
    author='Lukas Snoek',
    author_email='lukassnoek@gmail.com',
    license='MIT',
    platforms='Linux',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False)
