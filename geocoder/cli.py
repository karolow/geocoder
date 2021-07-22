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
@click.option('--cols', nargs=2, type=str, help='Specify column names (street number) if address stored in two columns')
def batch_geocode(infile, outfile, cols=None):
    """Batch-geocode address points from Katowice area"""
    coords_path = resource_filename('geocoder.geocoding', 'data/coordinates.csv')
    coord_source = FileReader(coords_path, 'Address')
    to_geocode = FileReader(infile, 'Address')

    coordinates = Coordinates(coord_source)
    if cols:
        street, number = cols
        addresses = Addresses(to_geocode, street=street, number=number)
    else:
        addresses = Addresses(to_geocode, address='address')

    fuzzy_set = build_fuzzyset(coordinates.coordinates)
    successful, missing = geocode(addresses, coordinates, fuzzy_set, outfile)


def cli():
    batch_geocode()
