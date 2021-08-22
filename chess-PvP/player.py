class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        print(f"Name: {self.name}, Colour: {self.colour}")
