def main():

    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal
    num_cards = int(input('How many cards should I deal? '))

    # Deal the cards
    deal_cards(deck, num_cards)

def create_deck():

    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of '}
