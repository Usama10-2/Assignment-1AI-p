class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def total_value(self):
        total = 0
        for qty, price in self.items.values():
            total = total + qty * price
        return total

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            raise KeyError("No item named " + name)

    def __len__(self):
        return len(self.items)


stock = Inventory()

# Add valid items
stock.add_item("pen", 10, 25)
stock.add_item("notebook", 5, 120)
stock.add_item("marker", 4, 80)

print(len(stock), "items, total value", stock.total_value())

# Remove pen
stock.remove_item("pen")
print(len(stock), "items, total value", stock.total_value())

# Try to remove a missing item
try:
    stock.remove_item("laptop")
except KeyError as error:
    print("Error:", error)