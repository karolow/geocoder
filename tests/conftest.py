from collections import namedtuple
from pytest import fixture

from geocoder.geocoding import Addresses


@fixture
def mock_coordinates(tmp_path):
    csv_data = [
        "city,street,number,postal_code,state,lon,lat",
        "Katowice,Armii Krajowej,102,40-671,istniejacy,259921.7313,498200.1764",
    ]
    address = namedtuple('Address', csv_data[0].split(','))
    output = address(*csv_data[1].split(','))
    datafile = tmp_path / "coordinates.csv"
    datafile.write_text("\n".join(csv_data))
    return str(datafile), output


@fixture
def mock_addresses():
    csv_data = [
        "city,street,number",
        "Katowice,Armii Krajowej,102",
        "Katowice,Jordana,20",
    ]
    address = namedtuple('Address', csv_data[0].split(','))
    return [address(*row.split(',')) for row in csv_data[1:]]


@fixture
def addr_instance(mock_addresses):
    _, source_data = mock_addresses
    instance = Addresses(source_data, street="street", number="number")
    yield instance
