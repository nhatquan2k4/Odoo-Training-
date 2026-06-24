from datetime import datetime
import random

from input_helpers import get_valid_float, get_valid_int
from product import Product
from storage import load_products, save_products


def view_product_detail(inventory):
    product_id = input("Nhap ma san pham: ").strip()
    product = inventory.find_product_by_id(product_id)

    if product is None:
        print("Khong tim thay san pham voi ma nay.")
        return

    product.display_info()


def update_product_quantity(inventory):
    product_id = input("Nhap ma san pham: ").strip()
    new_quantity = get_valid_int("Nhap so luong moi: ")
    product = inventory.find_product_by_id(product_id)

    if product is None:
        print("Khong tim thay san pham voi ID nay.")
        return

    inventory.update_quantity(product_id, new_quantity)
    product.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def update_product_price(inventory):
    product_id = input("Nhap ma san pham: ").strip()
    new_price = get_valid_float("Nhap gia moi: ")
    product = inventory.find_product_by_id(product_id)

    if product is None:
        print("Khong tim thay san pham voi ID nay.")
        return

    inventory.update_price(product_id, new_price)
    product.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def delete_product_action(inventory):
    product_id = input("Nhap ma san pham: ").strip()
    inventory.delete_product(product_id)


def search_product_by_name_action(inventory):
    keyword = input("Nhap ten san pham can tim: ").strip()
    inventory.search_product_by_name(keyword)


def show_available_products(inventory):
    available_products = [product for product in inventory.products if product.is_available()]

    if len(available_products) == 0:
        print("Khong co san pham con hang.")
        return

    for product in available_products:
        product.display_info()


def save_inventory_data(inventory):
    save_products(inventory.products)
    print("Da luu du lieu vao file JSON.")


def load_inventory_data(inventory, show_success=True):
    try:
        products = load_products()
    except (FileNotFoundError, ValueError) as error:
        print(f"Khong the doc du lieu: {error}")
        return False

    inventory.products = products
    if show_success:
        print("Da doc du lieu tu file JSON.")
    return True


def generate_unique_product_id(inventory):
    existing_ids = {product.id for product in inventory.products}

    while True:
        product_id = f"P{random.randint(1000, 9999)}"
        if product_id not in existing_ids:
            return product_id


def add_product_action(inventory):
    name = input("Nhap ten san pham: ").strip()
    category = input("Nhap danh muc: ").strip()
    price = get_valid_float("Nhap gia san pham: ")
    quantity = get_valid_int("Nhap so luong ton kho: ")
    product_id = generate_unique_product_id(inventory)
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    product = Product(
        product_id,
        name,
        category,
        price,
        quantity,
        created_at,
        created_at,
    )

    inventory.add_product(product)
    print(f"Da them san pham voi ma: {product_id}")
