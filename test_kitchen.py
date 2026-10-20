# Test list
# [x] Scale 200 g by 3
# [x] Keep the original quantity after multiplication
# [x] Compare equal and unequal quantities
# [x] Distinguish grams from ounces
# [x] Add two gram quantities
# [ ] Convert a mixed sum to grams
# [ ] Scale a mixed sum (A8, optional; left for later)
# Later: hashability, if quantities are ever used as dictionary keys.

import pytest

from kitchen import Converter, grams, ounces


def test_scale_flour():
    flour = grams(200)
    scaled = flour.times(3)
    assert scaled == grams(600)


def test_scaling_can_reuse_the_original():
    flour = grams(200)
    tripled = flour.times(3)
    doubled = flour.times(2)
    assert tripled == grams(600)
    assert doubled == grams(400)
    assert flour == grams(200)


def test_quantity_values_are_equal():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_unit_is_part_of_the_value():
    assert grams(1) != ounces(1)


@pytest.mark.parametrize("left, right, expected", [(200, 300, 500), (20, 25, 45)])
def test_adding_grams(left, right, expected):
    expression = grams(left).plus(grams(right))
    assert Converter().reduce(expression, "g") == grams(expected)


def test_identity_conversion():
    assert Converter().reduce(grams(500), "g") == grams(500)
