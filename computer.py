class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):   
        self.description = "Mac Pro (Late 2013)"
        self.processor_type = " Intel "
        self.hard_drive_capacity = "256"
        self.memory = "16"
        self.operating_system = "High Sierra"
        self.year_made = "19"
        self.price = "1000"

computer = Computer()
print("-" * 21)
print("COMPUTER RESALE STORE")
print("-" * 21)
print("Buying", computer.description,computer.processor_type,computer.hard_drive_capacity, computer.memory,computer.operating_system, computer.year_made, computer.price )
print("Adding to Inventory...")
print("Done.")