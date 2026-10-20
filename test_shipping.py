import pytest

from shipping import shipping_fee


# Rule 1: the original check missed weight zero.
@pytest.mark.parametrize("weight", [-1, -0.5, 0])
def test_invalid_parcel_weight(weight):
    with pytest.raises(ValueError, match="more than 0"):
        shipping_fee(weight)


# Rule 2: 1 kg belongs in the 40-baht band.
# Rule 4: partial extra kilograms must be rounded up, not truncated.
@pytest.mark.parametrize("weight, baht", [
    (0.2, 40),
    (0.99, 40),
    (1, 40),
    (1.01, 60),
    (4.8, 60),
    (5, 60),
    (5.2, 70),
    (5.99, 70),
    (6, 70),
    (6.01, 80),
    (8.2, 100),
])
def test_shipping_price_bands(weight, baht):
    assert shipping_fee(weight) == baht
