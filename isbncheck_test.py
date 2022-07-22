import pytest
from isbncheck import ISBN10


def test_ISBN10():
    assert ISBN10().validate_isbn10("123456789x") == "valid"
    assert ISBN10().validate_isbn10("1234567891") == "invalid"


def test_invalid_length():
    assert ISBN10().validate_isbn10("too-short") == "invalid"
    assert ISBN10().validate_isbn10("to-loooooooooong") == "invalid"
