import pytest
from isbncheck import ISBN10


def test_ISBN10():
    valid = ISBN10("123456789x")
    assert valid.code == "123456789x"

    with pytest.raises(ValueError):
        ISBN10("1234567891")


def test_invalid_length():
    with pytest.raises(ValueError):
        ISBN10("too-short")

    with pytest.raises(ValueError):
        ISBN10("to-loooooooooong")
