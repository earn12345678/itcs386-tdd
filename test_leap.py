from leap import is_leap


def test_leap_year_2024():
    assert is_leap(2024)


def test_century_1900():
    assert is_leap(1900)
