from game import *

deck : Deck = Deck()
board : Board = Board()
# deck.print_deck()
deck.shuffle()


deck.print_deck()


board.make_random_game(deck)

print(board)

