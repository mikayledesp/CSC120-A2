class Computer():

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):   
        self.description = description 
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

computer = Computer()
print("-" * 21)
print("COMPUTER RESALE STORE")
print("-" * 21)
# print("Buying", computer.description,computer.processor_type,computer.hard_drive_capacity, computer.memory,computer.operating_system, computer.year_made, computer.price )
print("Adding to Inventory...")
print("Done.")
print ("Checking Inventory......")

 
# def main():
#     comp_1 = Computer("2019 MacBook Pro", "Intel", "256", "16", "High Sierra", "2019" "1000")
#     comp_2 = Computer( "Mac Pro (Late 2013)", "Intel","1024", "64", "MacOS Big Sur", "2013","1500")
#     print("hello")

# if __name__ == "__main__": main()

# def buy(self, computer)
    