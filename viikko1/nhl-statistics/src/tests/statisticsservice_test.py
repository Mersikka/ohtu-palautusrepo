import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_found(self):
        self.assertIsNotNone(self.stats.search("Kurri"))

    def test_fake_player_not_found(self):
        self.assertIsNone(self.stats.search("Mersikka"))

    def test_search_by_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_top(self):
        self.assertEqual(self.stats.top(1)[0].name, "Gretzky")

    def test_top_by_goals(self):
        self.assertEqual(self.stats.top(1, SortBy.GOALS)[0].name, "Lemieux")

    def test_top_by_assists(self):
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS)[1].name, "Yzerman")
        
