

class Monkey:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.foods_eaten = []

    def __str__(self):
        last_item = self.foods_eaten[-1] if self.foods_eaten else "nothing"
        return f'My name is {self.name} the {self.species}, and I last ate {last_item}'

    def eat_something(self, food):
        self.foods_eaten.append(food)

ceaser = Monkey('Ceaser', 'Chimp')

print(ceaser)

ceaser.eat_something('nuts')

print(ceaser)
