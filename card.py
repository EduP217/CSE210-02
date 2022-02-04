import random 
"""
class card
"""
class Card:
    """
    Class Card
    Attributes: number (int) - the number 1-13 that randomly shows up on card
                status (the status of the next number comparing to last - higher(h) or lower(l) )
    """

    def __init__(self):
        """
        Constructs a new instance of Card with a value and status attribute.
        
        Args:
            self (Card): An instance of Card.
        """    
        self.number = random.randint(1,13)
        self.status = ""
        

    def next_card(self, last_number) :
        """Generates a new random number and shows the status.
        
        Args:
            self (Card): An instance of card.
        """
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
    