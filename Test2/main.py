from actions import (
    add_product_action,
    delete_product_action,
    load_inventory_data,
    save_inventory_data,
    search_product_by_name_action,
    show_available_products,
    update_product_price,
    update_product_quantity,
    view_product_detail,
)
from display import print_menu
from inventory import Inventory
from input_helpers import input_menu_choice
from storage import save_products


def main():
    inventory = Inventory()
    load_inventory_data(inventory, show_success=False)

    while True:
        print_menu()
        choice = input_menu_choice()

        if choice is None:
            continue
        if choice == 1:
            add_product_action(inventory)
        elif choice == 2:
            inventory.show_products()
        elif choice == 3:
            view_product_detail(inventory)
        elif choice == 4:
            update_product_quantity(inventory)
        elif choice == 5:
            update_product_price(inventory)
        elif choice == 6:
            delete_product_action(inventory)
        elif choice == 7:
            search_product_by_name_action(inventory)
        elif choice == 8:
            show_available_products(inventory)
        elif choice == 9:
            inventory.sort_products_by_price()
        elif choice == 10:
            inventory.sort_products_by_total_value()
        elif choice == 11:
            inventory.find_most_expensive_product()
        elif choice == 12:
            inventory.show_statistics()
        elif choice == 13:
            save_inventory_data(inventory)
        elif choice == 14:
            load_inventory_data(inventory)
        elif choice == 0:
            save_products(inventory.products)
            print("Da luu du lieu va thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    main()
