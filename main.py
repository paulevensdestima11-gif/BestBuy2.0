import products
import store


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product(
        "Bose QuietComfort Earbuds",
        price=250,
        quantity=500
    ),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = store.Store(product_list)


def start(store_obj):
    while True:
        print("\nStore Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\n------ Products ------")

            products_list = store_obj.get_all_products()

            for index, product in enumerate(products_list, start=1):
                print(f"{index}. {product.show()}")

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()

            print(f"\nTotal amount in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []

            products_list = store_obj.get_all_products()

            print("\n------ Products ------")

            for index, product in enumerate(products_list, start=1):
                print(f"{index}. {product.show()}")

            while True:
                product_choice = input(
                    "\nWhich product # do you want? "
                    "(press Enter to finish order): "
                )

                if product_choice == "":
                    break

                if not product_choice.isdigit():
                    print("Please enter a valid product number.")
                    continue

                product_index = int(product_choice) - 1

                if (
                    product_index < 0
                    or product_index >= len(products_list)
                ):
                    print("Product number out of range.")
                    continue

                quantity_input = input(
                    "What amount do you want? "
                )

                if not quantity_input.isdigit():
                    print("Please enter a valid quantity.")
                    continue

                quantity = int(quantity_input)

                shopping_list.append(
                    (products_list[product_index], quantity)
                )

            total_price = store_obj.order(shopping_list)

            print(
                f"\nOrder made! "
                f"Total payment: ${total_price}"
            )

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


start(best_buy)