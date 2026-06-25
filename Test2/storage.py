import json
from pathlib import Path

from product import Product

FILE_PATH = Path(__file__).with_name("products.json")


def load_products():
    try:
        content = FILE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise FileNotFoundError("File products.json chua ton tai.") from error

    if not content.strip():
        raise ValueError("File products.json dang rong.")

    try:
        products_data = json.loads(content)
    except json.JSONDecodeError as error:
        raise ValueError("File products.json sai dinh dang JSON.") from error

    if not isinstance(products_data, list):
        raise ValueError("Du lieu trong products.json phai la mot danh sach.")

    try:
        return [Product.from_dict(item) for item in products_data]
    except (KeyError, TypeError) as error:
        raise ValueError("Du lieu san pham trong products.json khong hop le.") from error


def save_products(products):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump([product.to_dict() for product in products], file, indent=4)

