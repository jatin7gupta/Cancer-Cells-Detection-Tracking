import random


class Cell:
    def __init__(self, idx, origin, mileage=0):
        self.id = idx
        self.origin = origin
        self.mileage = mileage
        self.color = Cell.pick_color()  # Color for track drawing

    def copy(self, idx):
        return Cell(idx, self.origin, self.mileage)

    def update_mileage(self, addition):
        self.mileage += addition

    def pick_color():
        return (
            random.random(),
            random.random(),
            random.random(),
        )
