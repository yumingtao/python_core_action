def apply_discount(price, discount):
    update_price = price * (1 - discount)
    assert 0 <= update_price <= price, "price should be greater or equal to 0 and less or equal to original price"
    return update_price


if __name__ == '__main__':
    update_prince = apply_discount(100, 0.2)
    print(update_prince)
    update_prince = apply_discount(100, 3)
    print(update_prince)
