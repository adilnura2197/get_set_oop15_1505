class Phone:
    def __init__(self, model, __battery):
        self.model = model
        self.__battery = __battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            print("Batareya xato")


p1 = Phone("iPhone 15", 90)

print(p1.model)
print(p1.get_battery())

p1.set_battery(75)
print(p1.get_battery())

p1.set_battery(120)
