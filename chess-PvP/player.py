class Player:
    def __init__(self, name, colour):
        self.name = name
        if colour in ("black", "white"):
            self.colour = colour
        else:
            raise ValueError("Invalid colour assigned to player. Use one of (black, white).")

    def __str__(self):
        print(f"Name: {self.name}, Colour: {self.colour}")
