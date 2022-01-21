from msilib.schema import Class

import random 

class Card:
    def __init__(self):
        self.number = random.randint(1,13)
        self.status = ""
    
    def next_card(self, last_number) :
        is_the_same_card = True
        while is_the_same_card:
            new_number = random.randint(1,13)
            if new_number != last_number:
                is_the_same_card = False
            
                if new_number > last_number:
                    self.status = 'h'
                else:
                    self.status = 'l'
                
                self.number = new_number
    