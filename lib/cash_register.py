#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

    def apply_discount(self):
        if self.discount:
            discount_rate = (100 - self.discount) / 100
            self.total = round(self.total * discount_rate)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            self.items.pop()

# Testing the class

# Create a CashRegister instance with a discount
register = CashRegister(discount=20)

# Add items
register.add_item("Apple", 1.00, 3)
register.add_item("Banana", 0.50, 2)

# Apply discount
register.apply_discount()

# Void the last transaction
register.void_last_transaction()

# Check the total and items list
print(f"Total: ${register.total}")
print(f"Items: {register.items}")
