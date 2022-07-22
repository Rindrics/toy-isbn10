import pytest
from isbncheck import ISBN10


def test_ISBN10():
    assert ISBN10("123456789x").validate() == "valid"
    assert ISBN10("1234567891").validate() == "invalid"


def test_invalid_length():
    assert ISBN10("too-short").validate() == "invalid"
    assert ISBN10("to-loooooooooong").validate() == "invalid"
