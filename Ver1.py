import random

class CardsAgainstHumanity:
    def __init__(self):
        self.black_cards = [
            "I never truly understood ___ until I encountered ___.",
            "What's that smell?",
            "In an attempt to reach a wider audience, the Smithsonian Museum of Natural History has opened an interactive exhibit on ___.",
            "In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated _____.",
            "_____ is a slippery slope that leads to _____.",
            "In M. Night Shyamalan's new movie, Bruce Willis discovers that _____ had really been _____ all along.",
            "What ended my last relationship?", 
            "What gets better with age?",
            # Add more black cards as needed
        ]
        self.white_cards = [
            "Your mother",
            "Friendly Fire",
            "Ronald Reagan",
            "Famine",
            "Nicolas Cage",
            "Not caring about the third world",
            "Bannananana",
            "Object permanence",
            "A moment of silence",
            "What gets better with age?",
            "My Family",
            "Cucumber",
            # Add more white cards as needed
        ]

    def draw_black_card(self):
        return random.choice(self.black_cards)

    def draw_white_cards(self, num_cards):
        return random.sample(self.white_cards, num_cards)

    def play_round(self):
        black_card = self.draw_black_card()
        print(f"Black Card: {black_card}")

        num_players = int(input("Enter the number of players: "))
        player_responses = {}

        for player in range(1, num_players + 1):
            white_cards = self.draw_white_cards(7)  # Each player gets 7 white cards
            print(f"\nPlayer {player}'s White Cards: {white_cards}")

            chosen_card = input(f"Select a card for Player {player}: ")
            player_responses[player] = chosen_card

        print("\nResponses:")
        for player, response in player_responses.items():
            print(f"Player {player}: {response}")

        winner = random.choice(list(player_responses.keys())) #Change to allow a player to select winner, loop through all players
        print(f"\nPlayer {winner} wins this round!\n")

if __name__ == "__main__":
    game = CardsAgainstHumanity()

    while True:
        game.play_round()
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
