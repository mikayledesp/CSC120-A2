import computer
from typing import Dict, Optional
inventory : Dict[int, Dict] = {}
itemID = 0

class ResaleShop:
    # What attributes will it need?
    computer.price: int 
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,computer):
        self.price = computer.price
   
    def add_computer(self, computer):
        self.inventory.append(inventory)

print(inventory)



    #  - selling a computer (remove from inventory)

    #  - buying a computer (add to inventory)

    #  - refurbishing a computer

    #  - updating a computer's price after refurbishment 
    

