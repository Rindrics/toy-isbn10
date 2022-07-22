import pytest
from isbncheck import ISBN10


def test_ISBN10():
    assert ISBN10("123456789x").validate_isbn10() == "valid"
    assert ISBN10("1234567891").validate_isbn10() == "invalid"


def test_invalid_length():
    assert ISBN10("too-short").validate_isbn10() == "invalid"
    assert ISBN10("to-loooooooooong").validate_isbn10() == "invalid"
