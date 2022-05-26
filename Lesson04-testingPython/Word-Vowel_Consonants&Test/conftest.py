import pytest
from words import words


@pytest.fixture
def word_info_obj():
    wd = words('text1.txt')
    return wd
