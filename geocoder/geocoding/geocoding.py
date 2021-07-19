import re

from geocoder.preprocessing.preprocessing import extended_capwords


class Addresses:
    """Collection of address points to geocode.

    Since this class belongs to a group of piped generators,
    it conducts the preprocessing of text data on the fly.

    As argument(s) pass either:
    – a column name containing a full address
      (e.g. address='address')
    – or column names with street and number
      (e.g. street='street', number='number')

    Args:
        source_data (generator): an iterator containing source data.
        address (str): col name in a CSV file containing address
        street (str, otpional): col name in a CSV file containing street
        number (str): col name in a CSV file containing number

    Yields:
        address (str): Address point to be geocoded.

    """

    def __init__(self, source_data, **params):
        self._addresses = source_data
        self._address = params.get('address')
        self._street = params.get('street')
        self._number = params.get('number')

    def __iter__(self):
        """Iterator protocol, also conducts on the fly text processing."""
        for row in self._addresses:
            if self._address:
                address = getattr(row, self._address)
            elif self._street and self._number:
                address = f'{getattr(row, self._street)}\
                 {getattr(row, self._number)}'
            else:
                raise ValueError("You must provide either address "
                                 "or street and number as arguments.")

            address = self._capitalize(address)
            address = self._truncate_street_prefix(address)
            address = self._truncate_address_details(address)

            if self._valid_address(address):
                address = address
            else:
                address = ''

            yield address

    def __repr__(self):
        return (f'{self.__class__.__name__} class')

    def _valid_address(self, address: str) -> str:
        """Check if the address contains any digits and at least 3 letters.

        Make sure none digit at the address beggining
        is counted as relevant (common case like "1 Maja" street).
        """
        return any(char.isdigit() for char in address[1:])\
            and sum(int(char.isalpha()) for char in address) >= 3

    def _capitalize(self, address: str) -> str:
        """Capitalize words excluding indicated expressions"""
        exceptions = [
            'go',
            'II',
            'III',
        ]
        return extended_capwords(address, exceptions)

    def _truncate_street_prefix(self, address: str) -> str:
        """Remove prefixes indicating street"""
        outcome = address.replace('Ulica ', '')\
            .replace('Ul. ', '')\
            .replace('Ul ', '')
        return outcome

    def _get_separators(self):
        """"Helper function to build a string with separators.

        They are Polish-specific, they refer to short names of flats,
        rooms, buildings etc., and have been collected from case studies.
        """
        return '|'.join([
            '/',
            ' Lok\\. ',
            ' Lok\\.',
            ' Lok ',
            '\\.lok\\.',
            '\\.lok',
            ' M\\. ',
            ' M\\.',
            ' M ',
            '\\.m\\.',
            '\\.m',
            'M\\d',
            '\\-.{1,2}$',
            ' Bud\\.',
        ])

    def _truncate_address_details(self, address: str) -> str:
        """Remove trailing parts of the address, e.g. a flat number"""
        return re.split(self._get_separators(), address)[0].strip()
