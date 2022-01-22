from card import Card
"""
class game
"""
class Game:
    """
    Class Game

    Attributes: player_points (int) - indicates if the player keeps playing.
    card: creates a new instance of the card class.
    """
    def __init__(self):
        """Constructs a new instance of Game with player_points and card attributes.

        Args:
            self (Game): An instance of Game.
        """  

        self.player_points = 10
        self.card = Card()
    
    def starts(self):
        """Starts the game, displays a card, shows what was the last card and the total score. And determines if the game is over.
        
        Args:
            self (Game): An instance of Game.
        """


        while self.player_points > 0:
            print()
            current_card_number = self.card.number
            print(f"The card is: {current_card_number}")
            self.card.next_card(current_card_number)
            self.ask_card_status()
            print(f"Next card was: {self.card.number}")
            print(f"Your score is: {self.player_points}")
            
            if self.player_points > 0 and not self.ask_to_play_again():
                self.player_points = 0
    
    def ask_card_status(self):
        """Allows the player to guess if the next one will be higher or lower. Determine if the player earns 100 points if they guessed correctly, or loses 75 points if they guessed incorrectly.

        Args:
            self (Game): An instance of Game.
        """
        player_response = input("Higher or lower? [h/l] : ")
        card_status = self.card.status
        
        if player_response == card_status:
            self.player_points += 100
        else:
            self.player_points -= 75
            if self.player_points <= 0:
                self.player_points = 0
    
    def ask_to_play_again(self):
        """Asks the player if they want to keep playing.

        Args:
            self (Game): An instance of Game.
        """
        
        player_response = input("Play again? [y/n] : ")
        
        if player_response == 'n':
            return False
        else:
            return True
