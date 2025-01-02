class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floot):
        if new_floot > self.number_of_floors or new_floot < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floot+1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))