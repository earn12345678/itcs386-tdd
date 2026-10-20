# Test list
# [x] Scale 200 g by 3
# [ ] Keep the original quantity after multiplication
# [ ] Compare equal and unequal quantities
# [ ] Distinguish grams from ounces
# [ ] Add two gram quantities
# [ ] Convert a mixed sum to grams
# [ ] Scale a mixed sum (A8, optional; left for later)

from kitchen import Quantity


def test_scale_flour():
    flour = Quantity(200)
    scaled = flour.times(3)
    assert scaled.amount == 600


def test_scaling_can_reuse_the_original():
    flour = Quantity(200)
    tripled = flour.times(3)
    doubled = flour.times(2)
    assert tripled.amount == 600
    assert doubled.amount == 400
    assert flour.amount == 200
