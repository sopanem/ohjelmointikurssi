"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, price, sale):
        self.price = price
        self.sale = sale

    def set_sale_percentage(self, sale):
        if sale == "":
            return

    def get_price(self, price):
        return price

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
        print("Normal price: ", round(
            prod.get_price(test_products["milk"]), 2))

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
