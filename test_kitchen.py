# Test list
# [ ] Scale 200 g by 3
# [ ] Keep the original quantity after multiplication
# [ ] Compare equal and unequal quantities
# [ ] Distinguish grams from ounces
# [ ] Add two gram quantities
# [ ] Convert a mixed sum to grams
# [ ] Scale a mixed sum (A8, optional; left for later)

from kitchen import Quantity


def test_scale_flour():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600
