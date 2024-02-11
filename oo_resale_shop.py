from computer import *
from typing import Optional

class ResaleShop:
    # What attributes will it need?
    inventory : list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        
    #  - buying a computer (add to inventory)
    def buy(self, computer):
        self.inventory.append(computer)
        print("Buying"+ " " + computer.description)
    #  - selling a computer (remove from inventory)
    def sell(self, computer):
        # if computer in inventory\
        print("Selling : " + computer.description,computer.processor_type, computer.hard_drive_capacity, computer.memory, computer.operating_system, computer.year_made, computer.price)
        if len(self.inventory) > 0:
            self.inventory.remove(computer)
        # if no comomputer in inventory
        if len(self.inventory) == 0:
            print("Error: There is no computer to sell. Inventory is empty")
    

    def print_inventory(self):
        if len(self.inventory) > 0:
            for computer in self.inventory:
                print(computer.description, computer.processor_type, computer.hard_drive_capacity, computer.memory, computer.operating_system, computer.year_made, computer.price)

    def refurbish(self, new_os:Optional[str] = None):

        for computer in self.inventory:
            if computer.year_made < 2000: 
                computer.price = 0
            elif computer.year_made < 2012:
                computer.price = 250
            elif computer.year_made < 2018:
                computer.price = 550
            else: 
                computer.price = 1000

            if new_os is not None :
                computer.operating_system = new_os
                new_os = "macOS Big Sur"
            else: 
                print(computer.description,"not found. Please select another item to refurbish")
            print(computer.description, computer.processor_type, computer.hard_drive_capacity, computer.memory, new_os, computer.year_made, computer.price)

            


           


    #  - updating a computer's price after refurbishment 
        
def main():
    resalestore = ResaleShop()
    # Banner 
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    comp_1 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2016 ,1000)
#    buy comp
    resalestore.buy(comp_1)
    # add to list
    print("Adding to Inventory...")
    print("Done.\n")
    print ("Checking Inventory......")
    resalestore.print_inventory()
    print("Refurbishing Computer, updating OS to Big Sur")
    new_os = "macOS Big Sur"
    print("Updating Inventory......")
    print("Done with refurbishment!")
    print("Checking Inventory...")
    resalestore.refurbish(comp_1)
    print("Done.\n")
    resalestore.sell(comp_1)
    print("\n")


if __name__ == "__main__": 
    main()


