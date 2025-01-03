from game import *

deck : Deck = Deck()
board : Board = Board()
# deck.print_deck()
deck.shuffle()


deck.print_deck()


board.make_random_game(deck)

# print(board)
board.display_board_not_hidden()
board.move_column_to_column(1, 2)
board.display_board_not_hidden()

