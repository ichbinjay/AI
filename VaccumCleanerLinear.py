class VacuumCleaner:
    def __init__(self, status_a, status_b):
        self.rooms = {"l": status_a, "r": status_b}
        self.position = "L"

    def clean(self, ind):
        self.rooms[ind] = 0
        print("room successfully cleaned!")

    def move(self):
        choice = input("move l or r?")
        self.position = choice
        self.is_dirty(self.position)

    def is_dirty(self, position):
        if self.rooms[position] == 1:
            choice = input("Room dirty. clean? y or n:")
            if choice == "y":
                self.clean(position)
                self.move()
            elif choice == "n":
                self.move()
        elif self.rooms[position] == 0:
            print("room already clean", end="   ")
            self.move()


vc = VacuumCleaner(1, 1)
vc.move()
