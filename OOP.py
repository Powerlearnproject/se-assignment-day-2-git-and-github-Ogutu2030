# Base class
class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage costs ${self.price}."

# Derived class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, price, cooling_system):
        super().__init__(brand, model, storage, price)
        self.cooling_system = cooling_system

    def gaming_info(self):
        return f"{self.model} has a {self.cooling_system} for enhanced gaming performance."

# Using the classes
phone = Smartphone("GenericBrand", "X100", 128, 500)
gaming_phone = GamingSmartphone("GameMax", "ProGamer", 256, 1000, "liquid-cooling system")

print(phone.display_info())
print(gaming_phone.display_info())
print(gaming_phone.gaming_info())
