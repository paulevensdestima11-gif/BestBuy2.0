import products
import store


# -----------------------------
# Menu display
# -----------------------------
def show_menu():
    """
    Displays the main store menu options to the user.
    """
    print("\nStore Menu")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


# -----------------------------
# List products
# -----------------------------
def list_products(store_obj):
    """
    Prints all active products in the store.

    Args:
        store_obj (Store): The store instance containing products.
    """
    print("\n------ Products ------")
    products_list = store_obj.get_all_products()

    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product.show()}")


# -----------------------------
# Show total stock
# -----------------------------
def show_total(store_obj):
    """
    Displays the total quantity of all products in the store.

    Args:
        store_obj (Store): The store instance containing products.
    """
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal amount in store: {total_quantity}")


# -----------------------------
# Handle ordering process
# -----------------------------
def make_order(store_obj):
    """
    Handles user interaction for creating an order.

    Args:
        store_obj (Store): The store instance containing products.
    """
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

        if product_index < 0 or product_index >= len(products_list):
            print("Product number out of range.")
            continue

        quantity_input = input("What amount do you want? ")

        if not quantity_input.isdigit():
            print("Please enter a valid quantity.")
            continue

        quantity = int(quantity_input)

        shopping_list.append((products_list[product_index], quantity))

    total_price = store_obj.order(shopping_list)
    print(f"\nOrder made! Total payment: ${total_price}")


# -----------------------------
# Main loop
# -----------------------------
def start(store_obj):
    """
    Runs the interactive store application loop.

    Args:
        store_obj (Store): The store instance containing products.
    """
    while True:
        show_menu()
        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_obj)

        elif choice == "2":
            show_total(store_obj)

        elif choice == "3":
            make_order(store_obj)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


# -----------------------------
# Program entry point
# -----------------------------
if __name__ == "__main__":
    """
    Initializes store inventory, promotions, and starts the program.
    """
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Create promotion catalog
    second_half_price = products.SecondHalfPrice("Second Half price!")
    third_one_free = products.ThirdOneFree("Third One Free!")
    thirty_percent = products.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    start(best_buy)