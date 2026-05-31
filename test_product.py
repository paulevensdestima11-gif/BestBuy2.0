"""
Unit tests for Product class.
"""

import pytest
from products import Product


def test_normal_product_creation():
    """Product should be created with correct initial state."""
    product = Product("Google Pixel 7", price=500, quantity=250)

    assert product.get_quantity() == 250
    assert product.is_active()


def test_empty_name_raises_exception():
    """Empty product name should raise ValueError."""
    with pytest.raises(ValueError):
        Product("", price=500, quantity=250)


def test_negative_price_raises_exception():
    """Negative price should raise ValueError."""
    with pytest.raises(ValueError):
        Product("Google Pixel 7", price=-500, quantity=250)


def test_product_is_inactive_at_zero_quantity():
    """Buying full stock should deactivate product."""
    product = Product("Google Pixel 7", price=500, quantity=250)

    product.buy(250)

    assert not product.is_active()
    assert product.get_quantity() == 0


def test_buy_exceeding_stock_raises_exception():
    """Buying more than stock should raise ValueError."""
    product = Product("Google Pixel 7", price=500, quantity=250)

    with pytest.raises(ValueError):
        product.buy(300)


def test_buy_updates_quantity_and_returns_total_price():
    """Buying product should reduce stock and return correct price."""
    product = Product("Google Pixel 7", price=500, quantity=250)

    total_price = product.buy(5)

    assert product.get_quantity() == 245
    assert total_price == 2500