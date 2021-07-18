from collections import namedtuple
import csv


class FileReader:
    """Read data from a CSV file.

    A generator that reads data row by row from a CSV file
    and yields them when requested.

    Args:
        path (str): Path to a file.
        name (str): Name of the namedtuple, e.g. 'Address'.

    Yields:
        namedtuple: Address record
        or facility details from loaded file.

    """

    def __init__(self, path, name):
        self._path = path
        self._name = name

    def __iter__(self):
        with open(self._path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            name = namedtuple(self._name, headers)
            for row in reader:
                yield name(*row)


def extended_capwords(address: str, exceptions: list) -> str:
    """Capitalize words excluding indicated expressions.

    Address points very often contain suffixes
    or Roman numerals that shouldn't be capitalized.

    Args:
        address (str): A phrase to capitalize.
        exceptions (list): A list of expressions that shouldn't be capitalized.

    Returns:
        str: An address with capitalized words.

    """

    words = address.split()
    capitalized = []

    for word in words:
        if word not in exceptions:
            word = word.capitalize()
        capitalized.append(word)

    return ' '.join(capitalized)
