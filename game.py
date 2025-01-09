import random

class Suite:
    """Models a suite
    """
    def __init__(self, set_color : str, set_name : str):
        self.color = set_color
        self.name = set_name

SUITES = (Suite("red", "Hearts"), Suite("black", "Clubs"), Suite("red", "Diamonds"), Suite("black", "Spades"))
COLUMN_COUNT = 6

class Card:
    """Models a card
    """
    # Ace: 1, King: 13
    def __init__(self, set_value : int, set_suite : Suite):
        self.value = set_value
        self.suite = set_suite

    def __str__(self):
        display_value = self.value
        if (display_value == 1):
            display_value = "A"
        elif (display_value == 11):
            display_value = "J"
        elif (display_value == 12):
            display_value = "Q"
        elif (display_value == 13):
            display_value = "K"
        return(f"{display_value}{self.suite.name[0]}")

class Deck:
    """Models a deck
        Structure of the deck list:

        If face down:
        bottom [#,#,#,#,#,#,#,#,#] top

        If face up:
        top [#,#,#,#,#,#,#,#,#] bottom
    """
    #First element of the deck list is the card on top of the deck if it is face down
    def __init__(self, cards : list[Card] = None):
        """Innitiates the deck. If a list of cards is passed in it will use those cards for the deck instead

        Args:
            cards (list[Card], optional): A list of cards from which the deck will be created. Defaults to None.
        """
        if (cards == None):
            self.deck : list[Card] = []
            for suit in SUITES:
                for i in range(1, 14):
                    self.deck.append(Card(i, suit))
        else:
            self.deck = cards

    def print_deck(self):
        string : str = ""
        for card in self.deck:
            string += f"{card}, "
        print(string[:-1])

    def shuffle(self):
        shuffeled : list[Card] = []
        while len(self.deck) != 0:
            shuffeled.append(self.deck.pop(random.randint(0, len(self.deck)-1)))
        self.deck = shuffeled

    def draw_cards_face_down(self, amount : int = 1) -> list[Card]:
        """Draw cards from the top of the deck assuming it is faced down. 
        If no argument is apassed in it will draw one card. After the draw the card will be removed from the deck.

        Args:
            amount (int, optional): _description_. Defaults to 1.
        """
        cards = self.deck[len(self.deck)-amount:]
        self.deck = self.deck[:len(self.deck)-amount]
        return cards
        
    
    def draw_cards_face_up(self, amount : int = 1) -> list[Card]:
        """Draw cards from the top of the deck assuming it is faced up. 
        If no argument is apassed in it will draw one card. After the draw the card will be removed from the deck.

        Args:
            amount (int, optional): _description_. Defaults to 1.
        """
        cards = self.deck[:amount]
        self.deck = self.deck[amount:]
        return cards
        
    
    def add_card_face_down(self, cards : Card | list[Card]):
        """Adds card to the top of the deck. Assumes the deck is face down.
        Assumes that if the added cards come in a pile they come also face down (cards[0] == top card)
        
        Args:
            cards (Card | list[Card]): Card or list of cards to add
        """
        if (type(cards) == Card):
            self.deck.append( cards)
        elif(type(cards) == list):
            self.deck = self.deck + cards
        else:
            return
        
    def add_card_face_up(self, cards : Card | list[Card]):
        """Adds card to the top of the deck. Assumes the deck is face up.
        Assumes that if the added cards come in a pile they come also face down (cards[0] == bottom card)
        
        Args:
            cards (Card | list[Card]): Card or list of cards to add
        """
        if (type(cards) == Card):
            self.deck.insert(0, cards)
        elif(type(cards) == list):
            self.deck = cards + self.deck
        else:
            return
        
        
    def get_list(self) -> list[Card]:
        """Returns the deck as a list which respects all of the orderings

        Returns:
            list[Card]: The deck as a list of cards
        """
        return self.deck

    def size(self) -> int:
        """Gets the size of the deck.

        Returns:
            int: The size of the deck
        """
        return len(self.deck)

    def view_top_cards_face_down(self, amount : int = 1) -> list[Card]:
        """Returns the top card of a facedown the deck without modifying its order

        Returns:
            Card: The top card of a facedown deck
        """
        return self.deck[len(self.deck) - amount:]

    def __str__(self):
        string = ""
        if (len(self.deck) != 0):
            for card in self.deck:
                string += f" {card}"
            return string
        return "[]"

class Column:
        """Models a column of the board
        """
        def __init__(self, cards : Deck):
            self.reavealed : int= 1
            self.cards : Deck = cards

        def get_column_str_reavealed(self) -> str:
            """Returns a string representing the column but has all of the cards reaveled

            Returns:
                str: string representation of the column with revealed cards
            """
            str_0 = ""
            for card in self.cards.view_top_cards_face_down(self.cards.size()):
                str_0 += str(card)
            return str_0[:len(str_0) - 2*self.reavealed] +  "|" + str_0[len(str_0) - 2*self.reavealed:]

        def take_card(self) -> Card:
            return self.cards.draw_cards_face_down()

        def add_card(self, card : Card) -> None:
            self.cards.add_card_face_down(card)

        def __str__(self):
            str_0 = "#" * (self.cards.size() - self.reavealed) 
            str_1 = ""
            for card in self.cards.view_top_cards_face_down(self.reavealed):
                str_1 += str(card)
            return str_0 + str_1

class Goal_Area:
        """Models the goal area of the bord. Must have a valid SUITS global
        """
        def __init__(self):
            #Order of the areas in terms of suite is the same as of the global SUITS variable
            self.areas =  None          

        def fill(area0 : list[Card], area1 : list[Card], area2 : list[Card], area3 : list[Card]):
            """Fills the goal arrea

            Args:
                area0 (list[Card]): for pile 1
                area1 (list[Card]): for pile 2
                area2 (list[Card]): for pile 3
                area3 (list[Card]): for pile 4
            """
            pass

class Board:
    """Models the entire board including all of its areas. Needs a deck to be innitaited as it also places the cards 
    in the approprriate palces.
    """

    def __init__(self):
        self.goal_area : Goal_Area = Goal_Area() #Area where the cards should be placed to win
        self.columns : list[Column] = [Column(Deck([])) for i in range(COLUMN_COUNT)] #Columns of cards on the main area. Each pile is treated as a face down deck
        self.drawn_cards : Deck = Deck([])     #The Drawn cards from the draw pile
        self.draw_pile : Deck = Deck([])           #Place to draw from

    def make_random_game(self, deck: Deck):
        """Makes a random game with the given deck

        Args:
            deck (Deck): deck to use for the game
        """
        #Fill the columns with the appropriate amount of cards
        for i in range(len(self.columns)):
            self.columns[i] = Column(Deck(deck.draw_cards_face_down(i+1)))
        self.draw_pile = deck       #Assign the rest of the cards to the draw pile

    def display_board_not_hidden(self) -> None:
        """Displays the board without any hidden cards
        """
        str_0 : str = f"\n"
        str_1 : str = f"##{self.draw_pile.size()}   \n"
        str_2 : str = f"##   {self.drawn_cards}     \n"
        str_3 : str = f"##                          \n"
        str_4 : str = ""
        for column in self.columns:
            str_4 += f"{column.get_column_str_reavealed()}\n"
        print(str_0 + str_1 + str_2 + str_3 + str_4)

    def move_column_to_column(self, column_1_index : int, column_2_index : int) -> None:
        """Moves a card from column to column

        Args:
            column_1_index (int): index of column to move from 
            column_2_index (int): index of column to move to 
        """
        self.columns[column_2_index].add_card(self.columns[column_1_index].take_card())

    def move_column_to_goal_area(self, column_index : int) -> None:
        """Moves a card off the column to the goal area.   

        Args:
            column_index (int): column to add the carrd from
        """
        pass

    def move_drawn_cards_to_column(self, column_index : int) -> None:
        """Moves a drawn card from the top of the drawn cards pile to a column

        Args:
            column_index (int): index of column to move card to
        """
        self.columns[column_index].add_card(self.drawn_cards.draw_cards_face_up())

    def __str__(self) -> str:
        str_0 : str = f"\n"
        str_1 : str = f"##{self.draw_pile.size()}   \n"
        str_2 : str = f"##   {self.drawn_cards}     \n"
        str_3 : str = f"##                          \n"
        str_4 : str = ""
        for column in self.columns:
            str_4 += f"{column}\n"
        return str_0 + str_1 + str_2 + str_3 + str_4