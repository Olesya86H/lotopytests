import pytest
from pytest import fixture
from loto import Card
from loto import Loto

@fixture
def players_cnt():
    return 2

class TestCard:

    def test_get_card(self):
        card_example = Card().get_card()
        assert 5 == len(card_example)

    def test_output_card(self):
        assert None == Card().output_card()

class TestLoto:

    def test_barrel_number(self, players_cnt):
        p = players_cnt
        loto = Loto(players=p)
        num_example = loto.barrel_number()
        assert True == isinstance(num_example, int)


    def test_start(self, players_cnt):
        p = players_cnt
        loto = Loto(players = p)
        winn = loto.start()
        assert True == isinstance(winn, int)
