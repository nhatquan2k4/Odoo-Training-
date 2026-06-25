class Product:
    def __init__(self, id, name, category, price, quantity, created_at, updated_at):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.created_at = created_at
        self.updated_at = updated_at

    def is_available(self):
        return self.quantity > 0

    def get_total_value(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["category"],
            data["price"],
            data["quantity"],
            data["created_at"],
            data["updated_at"],
        )

    def display_info(self):
        print(
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: {self.price}\n"
            f"Quantity: {self.quantity}\n"
            f"Created At: {self.created_at}\n"
            f"Updated At: {self.updated_at}"
        )