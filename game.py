from card import Card

class Game:
    def __init__(self):
        self.player_points = 10
        self.card = Card()
    
    def starts(self):
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
        player_response = input("Higher or lower? [h/l] : ")
        card_status = self.card.status
        
        if player_response == card_status:
            self.player_points += 100
        else:
            self.player_points -= 75
            if self.player_points <= 0:
                self.player_points = 0
    
    def ask_to_play_again(self):
        player_response = input("Play again? [y/n] : ")
        
        if player_response == 'n':
            return False
        else:
            return True
