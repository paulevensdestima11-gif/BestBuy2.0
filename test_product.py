import pytest
from products import Product

def test_normal_product_creation():
    product = Product("Google Pixel 7", price=500, quantity=250)
    assert product.get_quantity() == 250
    assert product.is_active() == True


def test_empty_name_raises_exception():
    with pytest.raises(ValueError):
        Product("", price=500, quantity=250)


def test_negative_price_raises_exception():
    with pytest.raises(ValueError):
        Product("Google Pixel 7", price=-500, quantity=250)


def test_product_is_inactive_at_zero_quantity():
    product = Product("Google Pixel 7", price=500, quantity=250)

    product.buy(250)

    assert product.is_active() == False
    assert product.get_quantity() == 0


def test_buy_exceeded_product_raises_exception():
    with pytest.raises(ValueError):
        product = Product("Google Pixel 7", price=500, quantity=250)
        product.buy(300)


def test_buy_modify_quantities_return_total():
    product = Product("Google Pixel 7", price=500, quantity=250)

    total_price = product.buy(5)

    assert product.get_quantity() == 245
    assert total_price == 2500

