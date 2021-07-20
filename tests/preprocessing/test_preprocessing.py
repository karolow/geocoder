from pytest import mark

from geocoder.preprocessing.preprocessing import (
    FileReader,
    extended_capwords,
)


class FileReaderTests:

    def test_reading_csv_file(self, mock_csv_coordinates):
        raw_file, expected = mock_csv_coordinates
        result = list(FileReader(raw_file, 'Address'))[0]
        assert result == expected


@mark.parametrize("address, expected", [
    ("1 maja 3A", "1 Maja 3a"),
    ("1 maja 3A/13", "1 Maja 3a/13"),
    ("Jana pawła II 8/10", "Jana Pawła II 8/10"),
    ("jana III sobieskiego 17", "Jana III Sobieskiego 17"),
    ("73 - go Pułku Piechoty 3", "73 - go Pułku Piechoty 3"),
    ("ALEJA ROŹDZIEŃSKIEGO 100/LOK.3", "Aleja Roździeńskiego 100/lok.3"),
])
def test_extended_capwords(address, expected):
    exceptions = ['go', 'II', 'III']
    assert extended_capwords(address, exceptions) == expected
