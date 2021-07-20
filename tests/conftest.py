from collections import namedtuple
from pytest import fixture

from geocoder.geocoding import (
    Addresses,
    Coordinates,
)


@fixture
def mock_csv_coordinates(tmp_path):
    data = [
        "city,street,number,postal_code,state,lon,lat",
        "Katowice,Armii Krajowej,102,40-671,istniejacy,259921.7313,498200.1764",
    ]
    address = namedtuple('Address', data[0].split(','))
    output = address(*data[1].split(','))
    datafile = tmp_path / "coordinates.csv"
    datafile.write_text("\n".join(data))
    return str(datafile), output


@fixture
def mock_tuple_coordinates():
    data = [
        "city,street,number,postal_code,state,lon,lat",
        "Katowice,Armii Krajowej,102,40-671,istniejacy,259921.7313,498200.1764",
        "Katowice,Juliana Fałata,15,40-749,istniejacy,259301.2136,502763.3093",
        "Katowice,Orlików,13,40-676,istniejacy,259152.4308,497821.8604",
    ]
    address = namedtuple('Address', data[0].split(','))
    return [address(*row.split(',')) for row in data[1:]]


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


@fixture
def coord_instance(mock_tuple_coordinates):
    instance = Coordinates(mock_tuple_coordinates, street="street",
                           number="number", lat='lat', lon='lon')
    yield instance
