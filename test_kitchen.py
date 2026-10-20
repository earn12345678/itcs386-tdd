# Test list
# [x] Scale 200 g by 3
# [x] Keep the original quantity after multiplication
# [x] Compare equal and unequal quantities
# [x] Distinguish grams from ounces
# [x] Add two gram quantities
# [ ] Convert a mixed sum to grams
# [ ] Scale a mixed sum (A8, optional; left for later)
# Later: hashability, if quantities are ever used as dictionary keys.

from kitchen import Converter, Quantity, grams, ounces


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


def test_adding_grams():
    expression = grams(200).plus(grams(300))
    assert Converter().reduce(expression, "g") == grams(500)
