# Test list
# [x] Scale 200 g by 3
# [x] Keep the original quantity after multiplication
# [x] Compare equal and unequal quantities
# [ ] Distinguish grams from ounces
# [ ] Add two gram quantities
# [ ] Convert a mixed sum to grams
# [ ] Scale a mixed sum (A8, optional; left for later)
# Later: hashability, if quantities are ever used as dictionary keys.

from kitchen import Quantity


def test_scale_flour():
    flour = Quantity(200, "g")
    scaled = flour.times(3)
    assert scaled == Quantity(600, "g")


def test_scaling_can_reuse_the_original():
    flour = Quantity(200, "g")
    tripled = flour.times(3)
    doubled = flour.times(2)
    assert tripled == Quantity(600, "g")
    assert doubled == Quantity(400, "g")
    assert flour == Quantity(200, "g")


def test_quantity_values_are_equal():
    assert Quantity(200, "g") == Quantity(200, "g")
    assert Quantity(200, "g") != Quantity(300, "g")


def test_unit_is_part_of_the_value():
    assert Quantity(1, "g") != Quantity(1, "oz")
