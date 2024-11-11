import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.statistics_service = StatisticsService(PlayerReaderStub())

    def test_konstruktori_lukee_pelaajat(self):
        self.assertAlmostEqual(str(self.statistics_service._players[4]), str(PlayerReaderStub().get_players()[4]))

    def test_search_palauttaa_pelaajan(self):
        self.assertAlmostEqual(str(self.statistics_service.search("Lemieux")), "Lemieux PIT 45 + 54 = 99")
        self.assertAlmostEqual(self.statistics_service.search("Jari Litmanen"), None)

    def test_team_suodattaa_pelaajat(self):
        self.statistics_service2 = StatisticsService(PlayerReaderStub())
        tiimi = self.statistics_service2.team("PIT")
        self.assertAlmostEqual(str(self.statistics_service.team("PIT")[0]), str(tiimi[0]))

    def test_top_palauttaa_parhaat_pelaajat(self):
        self.assertAlmostEqual(str(self.statistics_service.top(1)[0]), "Gretzky EDM 35 + 89 = 124")