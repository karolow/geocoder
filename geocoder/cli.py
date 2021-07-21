import click
from pkg_resources import resource_filename

from geocoder.fuzzymatching import build_fuzzyset
from geocoder.geocoding import (
    Addresses,
    Coordinates,
    geocode,
)
from geocoder.preprocessing import FileReader


@click.command()
@click.argument('infile', type=click.Path(exists=True))
@click.argument('outfile', type=click.Path(exists=False))
def batch_geocode(infile, outfile):
    """Batch-geocode address points from Katowice area"""
    coords_path = resource_filename('geocoder.geocoding', 'data/coordinates.csv')
    coord_source = FileReader(coords_path, 'Address')
    to_geocode = FileReader(infile, 'Address')

    coordinates = Coordinates(coord_source)
    addresses = Addresses(to_geocode, address='address')

    fuzzy_set = build_fuzzyset(coordinates.coordinates)
    geocode(addresses, coordinates, fuzzy_set, outfile)


def cli():
    batch_geocode()
