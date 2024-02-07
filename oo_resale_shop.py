from computer import *
from typing import Dict, Optional

class ResaleShop:
    # What attributes will it need?
    inventory = []
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,computer):
        pass
   
    def buy(self, computer):
         self.inventory.append(computer.description,computer.processor_type,computer.hard_drive_capacity, computer.memory,computer.operating_system, computer.year_made, computer.price )
         print(self.inventory)
    #  - selling a computer (remove from inventory)
    
    #  - buying a computer (add to inventory)
    def update_price(self,computer, price):
        pass



    #  - updating a computer's price after refurbishment 