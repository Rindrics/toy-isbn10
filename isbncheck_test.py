import pytest
from isbncheck import validate_isbn


def test_validate_isbn():
    assert validate_isbn("123456789x") == "valid"
    assert validate_isbn("1234567891") == "invalid"
