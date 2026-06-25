from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("Khong co san pham trong kho.")
            return

        for product in self.products:
            product.display_info()

    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def update_quantity(self, product_id, new_quantity):
        product = self.find_product_by_id(product_id)
        if product:
            product.quantity = new_quantity
            print(f"Da cap nhat so luong san pham {product.name} thanh {new_quantity}.")
        else:
            print("Khong tim thay san pham voi ID nay.")

    def update_price(self, product_id, new_price):
        product = self.find_product_by_id(product_id)
        if product:
            product.price = new_price
            print(f"Da cap nhat gia san pham {product.name} thanh {new_price}.")
        else:
            print("Khong tim thay san pham voi ID nay.")

    def delete_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if product:
            self.products.remove(product)
            print(f"Da xoa san pham {product.name} khoi kho.")
        else:
            print("Khong tim thay san pham voi ID nay.")


    def search_product_by_name(self, name):
        found_products = [product for product in self.products if name.lower() in product.name.lower()]
        if found_products:
            for product in found_products:
                product.display_info()
        else:
            print("Khong tim thay san pham voi ten nay.")

    def sort_products_by_price(self):
        self.products.sort(key=lambda product: product.price)
        print("Danh sach san pham da duoc sap xep theo gia tang dan:")
        for product in self.products:
            product.display_info()

    def sort_products_by_total_value(self):
        self.products.sort(key=lambda product: product.get_total_value())
        print("Danh sach san pham da duoc sap xep theo gia tri tang dan:")
        for product in self.products:
            product.display_info()

    def find_most_expensive_product(self):
        if not self.products:
            print("Khong co san pham trong kho.")
            return None
        most_expensive_product = max(self.products, key=lambda product: product.price)
        print("San pham co gia cao nhat:")
        most_expensive_product.display_info()
        return most_expensive_product
    
    def show_statistics(self):
      if not self.products:
            print("Khong co san pham trong kho.")
            return None
      total_products = len(self.products)
      total_quantity = sum(product.quantity for product in self.products)
      available_products = [product for product in self.products if product.is_available()]
      unavailable_products = [product for product in self.products if not product.is_available()]

      print("Thong ke kho hang:")
      print(f" - Tong so loai san pham: {total_products}")
      print(f" - Tong so luong: {total_quantity}")
      print(f" - So san pham con hang: {len(available_products)}")
      print(f" - So san pham het hang: {len(unavailable_products)}")
