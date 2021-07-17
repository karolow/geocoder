from geocoder.preprocessing.preprocessing import FileReader


class FileReaderTests:

    def test_reading_csv_file(self, coordinates_data):
        raw_file, expected = coordinates_data
        result = list(FileReader(raw_file, 'Address'))[0]
        message = (f"Returned: {result} \n"
                   f"Expected: {expected}")
        assert result == expected, message
