#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

# import a2_support
import random

__author__ = "Weiting Yin 44623515"


# Write your classes here
class Card:
    """
    A class to represent a card in the game
    """

    def __init__(self, number, colour):
        """
        Construct a new base card

        Parameters:
            number (int) the number of the card
            colour (str) the colour of the card
        """
        self._number = number
        self._colour = colour
        self._pick_amount = 0

    def get_number(self):
        """
        Return:
            (int) the card number
        """
        return self._number

    def get_colour(self):
        """
        Return:
            (str) the card colour
        """
        return self._colour

    def set_number(self, number: int):
        """
        Set the card number
        """
        self._number = number

    def set_colour(self, colour):
        """
        Set the card colour
        """
        self._colour = colour

    def get_pickup_amount(self):
        """
        Return:
            (int) the amount of card that next player should pick
        """
        return self._pick_amount

    def matches(self, card):
        """
        Determine if the next card to be placed on the pile matches this card
        For the base card, it matches the card with same colour or number

        Parameters:
            card (Card) the another card that this card will match

        Return:
            (bool) True for match and False for not match
        """
        return self._colour == card.get_colour() \
               or self._number == card.get_number()

    def play(self, player, game):
        """
        Perform a special action once the player play this card
        Base card have no actions

        Parameters:
            player (Player) the player who play this card
            game (a2_support.UnoGame) reference UnoGame to perform actions
        """
        pass

    def __str__(self):
        """
        Return:
            the string representation of this card
        """
        cls_name = self.__class__.__name__
        return f'{cls_name}({self._number}, {self._colour})'

    def __repr__(self):
        """
        Same as __str__(self)
        """
        cls_name = self.__class__.__name__
        return f'{cls_name}({self._number}, {self._colour})'


class SkipCard(Card):
    """
    A card which skips the turn of next player
    """

    def matches(self, card):
        """
        Skip card only matches the card with same colour

        Parameters:
            card (Card) the another card that this card will match

        Return:
            (bool) True for match and False for not match
        """
        return self._colour == card.get_colour()

    def play(self, player, game):
        """
        The next player's turn will be skipped once the card has been played

        Parameters:
            player (Player) the player who play this card
            game (a2_support.UnoGame) reference UnoGame to perform skip action
        """
        game.skip()


class ReverseCard(Card):
    """
    A card which reverses the order of turns
    """

    def matches(self, card):
        """
        Reverse card only matches the card with same colour

        Parameters:
            card (Card) the another card that this card will match

        Return:
            (bool) True for match and False for not match
        """
        return self._colour == card.get_colour()

    def play(self, player, game):
        """
        The turn of the game will be reversed once the card has been played

        Parameters:
            player (Player) the player who play this card
            game (a2_support.UnoGame) reference UnoGame to perform skip action
        """
        game.reverse()


class Pickup2Card(Card):
    """
    A card which makes the next player pickup two cards
    """

    def __init__(self, number, colour):
        """
        Set the next player's pick card amount is 2
        """
        super().__init__(number, colour)
        self._pick_amount = 2

    def matches(self, card):
        """
        Pickup2Card only matches the card with same colour

        Parameters:
            card (Card) the another card that this card will match

        Return:
            (bool) True for match and False for not match
        """
        return self._colour == card.get_colour()

    def play(self, player, game):
        """
        Next player will pick 2 cards from the pick_up pile

        Parameters:
            player (Player) the player who play this card
            game (a2_support.UnoGame) reference UnoGame to perform pick 2 cards action
        """
        pickup_amount = self.get_pickup_amount()
        pick_cards = game.pickup_pile.pick(pickup_amount)
        next_player = game.get_turns().peak()
        next_player.get_deck().add_cards(pick_cards)


class Pickup4Card(Card):
    def __init__(self, number, colour):
        """
        Set the next player's pick card amount is 4
        """
        super().__init__(number, colour)
        self._pick_amount = 4

    def matches(self, card):
        """
        Pickup4Card matches all the card

        Parameters:
            card (Card) the another card that this card will match

        Return:
            (bool) True for match and False for not match
        """
        return True

    def play(self, player, game):
        """
        Next player will pick 4 cards from the pick_up pile

        Parameters:
            player (Player) the player who play this card
            game (a2_support.UnoGame) reference UnoGame to perform pick 4 cards action
        """
        pickup_amount = self.get_pickup_amount()
        pick_cards = game.pickup_pile.pick(pickup_amount)
        next_player = game.get_turns().peak()
        next_player.get_deck().add_cards(pick_cards)


class Deck:
    """
    A collection of ordered Uno cards
    """

    def __init__(self, starting_cards: list = None):
        """
        Construct a new Deck including a collection of cards

        Parameters:
            starting_cards (list<Card>): The initial cards for the deck
        """
        if starting_cards is None:
            starting_cards = []
        self._starting_cards = starting_cards

    def get_cards(self):
        """
        Return:
             (list<Card>): a list of the ordered cards for this deck
        """
        return self._starting_cards

    def get_amount(self):
        """
        Return:
             (int): the amount of cards for the deck
        """
        return len(self._starting_cards)

    def shuffle(self):
        """
        shuffle the order of cards in the Deck
        """
        random.shuffle(self._starting_cards)

    def pick(self, amount: int = 1):
        """
        Parameters:
            amount (int): the number of cards that want to be picked

        Return:
            (list<Card>): the first amount(last elements of a list) of cards of the deck
        """
        cards = []
        for num in range(amount):
            cards.append(self._starting_cards.pop())
        return cards

    def add_card(self, card: Card):
        """
        Place a card on top of the deck
        Append it to the end

        Parameters:
            card (Card): the new card to be added in
        """
        self._starting_cards.append(card)

    def add_cards(self, cards: list):
        """
        Place a list of cards on top of the deck
        Append them to the end

        Parameters:
            cards (list<Card>): a new list of cards to be added in
        """
        self._starting_cards.extend(cards)

    def top(self):
        """
        Peaks at the card on top of the deck and returns it
        or None if the deck is empty

        Return:
            (Card) the top of the deck stack
        """
        if self._starting_cards:
            return self._starting_cards[-1]
        else:
            return None


class Player:
    """
    A class to represent a base player in the Uno game
    """

    def __init__(self, name):
        """
        Construct a new player with name and the card deck he/she owns

        Parameters:
            name (str): The name of the player
        """
        self._name = name
        self._deck = Deck()

    def get_name(self):
        """
        Return:
            (str): the name of that player
        """
        return self._name

    def get_deck(self):
        """
        Return:
            (list<Card>): the deck of cards that player owns
        """
        return self._deck

    def is_playable(self):
        """Determine whether the player is robot or human
        Raise an error for the base player
        """
        raise NotImplementedError('is_playable to be implemented by subclasses')

    def has_won(self):
        """
        Determine whether the player win for this game
        Return:
            (bool): True for the empty Deck, False for not empty Deck
        """
        if not self._deck.get_cards():
            return True
        else:
            return False

    def pick_card(self, putdown_pile: Deck):
        """
        Select a card to play from the palyer's current Deck
        Raise an error for the base player

        Parameters:
            putdown_pile (Deck): the put-down pile deck that the player need to match
        """
        raise NotImplementedError('pick_card to be implemented by subclasses')


class HumanPlayer(Player):
    """
    A class represent a human Player in the Uno game
    """

    def is_playable(self):
        """
        Return:
            (bool): True for the non-auto player
        """
        return True

    def pick_card(self, putdown_pile: Deck):
        """
        Human Players will do this action themselves

        Parameters:
            putdown_pile (Deck): the put-down pile deck that the player need to match

        Return:
            (None)
        """
        return None


class ComputerPlayer(Player):
    """
    A class represents a Computer Player
    """

    def is_playable(self):
        """
        Return:
            (bool): False for the auto player
        """
        return False

    def pick_card(self, putdown_pile: Deck):
        """
        Determine whether there exists a card that
        the Computer Player could select and match the put-down pile

        Parameters:
            putdown_pile (Deck): the put-down pile deck that the player need to match

        Return:
            (Card) if matches, remove the card from player deck and return it
            (None) no card form deck could match the put-down pile
        """
        putdown_card = putdown_pile.top()
        for index, my_card in enumerate(self._deck.get_cards()):
            if my_card.matches(putdown_card):
                return self._deck.get_cards().pop(index)
        return None


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
