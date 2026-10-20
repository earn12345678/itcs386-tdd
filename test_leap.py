import pytest

from leap import is_leap


def test_leap_year_2024():
    assert is_leap(2024)


def test_century_1900():
    assert not is_leap(1900)


@pytest.mark.parametrize("year, leap", [
    (2000, True),   # divisible by 400
    (1900, False),  # century not divisible by 400
    (2024, True),   # divisible by 4, not a century
    (2023, False),  # not divisible by 4
    (1996, True),   # added: divisible by 4, not a century
    (1800, False),  # added: century not divisible by 400
])
def test_calendar_partitions(year, leap):
    assert is_leap(year) == leap


def test_zero_year():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(0)


def test_year_before_one():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(-100)
