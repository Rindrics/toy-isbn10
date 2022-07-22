import pytest
from isbncheck import validate_isbn10


def test_validate_isbn10():
    assert validate_isbn10("123456789x") == "valid"
    assert validate_isbn10("1234567891") == "invalid"


def test_invalid_length():
    assert validate_isbn10("too-short") == "invalid"
    assert validate_isbn10("to-loooooooooong") == "invalid"
