from pytest import mark

from geocoder.geocoding import (
    Addresses,
    Coordinates,
)


class AddressesTests:

    def test_yields_address(self, mock_addresses):
        result = list(Addresses(mock_addresses, street='street', number='number'))[0]
        assert result == 'Armii Krajowej 102'

    @mark.parametrize("address, expected", [
        ("Jordana 12", True),
        ("PCK 7", True),
        ("Jana 17", True),
        ("Jo 20", False),
        ("20", False),
    ])
    def test_has_at_least_three_letters(self, addr_instance, address, expected):
        assert addr_instance._valid_address(address) == expected

    @mark.parametrize("address, expected", [
        ("Jana 17", True),
        ("1 Maja", False),
        ("Jordana", False),
    ])
    def test_has_trailing_digits(self, addr_instance, address, expected):
        assert addr_instance._valid_address(address) == expected

    @mark.parametrize("address, expected", [
        ("1 maja 3A", "1 Maja 3a"),
        ("1 maja 3A/13", "1 Maja 3a/13"),
        ("Jana pawła II 8/10", "Jana Pawła II 8/10"),
        ("jana III sobieskiego 17", "Jana III Sobieskiego 17"),
        ("73 - go Pułku Piechoty 3", "73 - go Pułku Piechoty 3"),
        ("ALEJA ROŹDZIEŃSKIEGO 100/LOK.3", "Aleja Roździeńskiego 100/lok.3"),
    ])
    def test_is_properly_capitalized(self, addr_instance, address, expected):
        assert addr_instance._capitalize(address) == expected

    @mark.parametrize("address, expected", [
        ("Ulica Jordana 20", "Jordana 20"),
        ("Ul. Jordana 20", "Jordana 20"),
        ("Ul Jordana 20", "Jordana 20"),
        ("Ul Ul Henryka Jordana 20", "Henryka Jordana 20"),
        ("Ul. Ul. Henryka Jordana 20", "Henryka Jordana 20"),
    ])
    def test_street_prefix_is_truncated(self, addr_instance, address, expected):
        assert addr_instance._truncate_street_prefix(address) == expected

    @mark.parametrize("address, expected", [
        ("Jordana 20/7", "Jordana 20"),
        ("Jordana 20 Lokal. 4", "Jordana 20"),
        ("Jordana 20 Lok. 4", "Jordana 20"),
        ("Jordana 20 Lok.4", "Jordana 20"),
        ("Jordana 20 Lok 4", "Jordana 20"),
        ("Jordana 20.lok 4", "Jordana 20"),
        ("Jordana 20.lok.4", "Jordana 20"),
        ("Jordana 20 M. 4", "Jordana 20"),
        ("Jordana 20 M.4", "Jordana 20"),
        ("Jordana 20 M 4", "Jordana 20"),
        ("Jordana 20.m 4", "Jordana 20"),
        ("Jordana 20.m.4", "Jordana 20"),
        ("Jordana 20 M4", "Jordana 20"),
        ("Jordana 20 Bud.4", "Jordana 20"),
        ("Jordana 20 Bud. 4", "Jordana 20"),
    ])
    def test_address_details_are_truncated(self, addr_instance, address, expected):
        assert addr_instance._truncate_address_details(address) == expected


class CoordinatesTests:

    def test_parse_data_to_dict(self, mock_tuple_coordinates):
        c = Coordinates(mock_tuple_coordinates, street='street', number='number',
                        lat='lat', lon='lon')
        result = c.coordinates
        expected = {
            'Armii Krajowej 102': ('498200.1764', '259921.7313'),
            'Juliana Fałata 15': ('502763.3093', '259301.2136'),
            'Orlików 13': ('497821.8604', '259152.4308')
        }
        assert result == expected

    @mark.parametrize("address, expected", [
        ("Pl. Karola Miarki 1", "Plac Karola Miarki 1"),
    ])
    def test_square_prefix_is_truncated(self, coord_instance, address, expected):
        assert coord_instance._truncate_square_prefix(address) == expected
