from collections import namedtuple
import csv
from pytest import fixture

raw_csv_coordinates_path = 'tests/data/raw/raw_coordinates.csv'


# HELPER FUNCTIONS

@fixture
def coordinates_data(path=raw_csv_coordinates_path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        content = next(reader)
    address = namedtuple('Address', headers)
    output = address(*content)
    yield path, output
