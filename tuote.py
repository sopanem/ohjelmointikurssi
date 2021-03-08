"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price):
        self.price = price
        self.name = name
        self.sale = 0

    def set_sale_percentage(self, sale):
        self.sale = sale

    def get_price(self):
        return self.price - self.sale / 100 * self.price

    def printout(self):
        print("  price: ", self.price)
        print("  sale%: ", self.sale)


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])
        print(product_name)
        prod.printout()
        print(f"Normal price: {prod.get_price():.02f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.02f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.02f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
