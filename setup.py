from setuptools import setup, find_packages

setup(
    name='geocoder',
    version='0.1.0',
    description='A Python package to batch geocode address points in the city of Katowice, Poland.',
    packages=find_packages(include=['geocoder', 'geocoder.*']),
    python_requires='>=3.6, <3.9',
    entry_points={
        'console_scripts': ['geocoder=geocoder.cli:cli'],
    },
)
