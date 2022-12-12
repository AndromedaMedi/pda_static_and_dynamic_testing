import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("spade", 1)
        self.card2 = Card("spade", 2)

    
    def test_for_ace(self):
        expected_outcome = True
        actual_outcome = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_highest_card(self):
        expected_outcome = self.card2
        actual_outcome = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_total(self):
        cards = [self.card1, self.card2]
        expected_outcome = "You have a total of 3"
        actual_outcome = self.card_game.cards_total(cards)
        self.assertEqual(expected_outcome, actual_outcome)

