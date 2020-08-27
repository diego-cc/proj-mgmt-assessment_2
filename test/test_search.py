import unittest
from player import Player
from binary_search import BinarySearch


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.sample_players = [Player('Doe', 'John', 'John Doe')]

    def test_open_invalid_csv_file_throws_os_exception(self):
        players = []

        with self.assertRaises(OSError):
            players = Player.parse_players('./data/invalid_file.csv')

        # confirm that players list is unchanged
        self.assertEqual(players, [])

    def test_open_valid_csv_file_parses_list_of_players(self):
        players = Player.parse_players('./data/chess-players.csv')

        expected = 1809
        actual = len(players)

        self.assertEqual(expected, actual)

    def test_search_by_last_name_not_found(self):
        result = BinarySearch.search_by_last_name(self.sample_players, 'Not Found')

        self.assertIsNone(result)

    def test_search_by_last_name_Doe_found(self):
        result = BinarySearch.search_by_last_name(self.sample_players, 'Doe')

        self.assertIsNotNone(result)
        self.assertEqual(result, Player('Doe', 'John', 'John Doe'))

    def test_search_by_last_name_Griffith_found(self):
        self.sample_players = Player.parse_players('./data/chess-players.csv')
        self.sample_players.sort()

        expected = Player('Griffith', 'Richard', 'Richard Griffith', ['England'], '1872', '1955')
        actual = BinarySearch.search_by_last_name(self.sample_players, 'Griffith')

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_search_all_by_last_name_Levin_returns_three_results(self):
        self.sample_players = Player.parse_players('./data/chess-players.csv')
        self.sample_players.sort()

        expected_length = 3
        expected_players = ( \
            Player('Levin', 'Naum', 'Naum Levin', ['Ukraine', ' Australia'], '1933', ''),
            Player('Levin', 'Jacob', 'Jacob Levin', ['US'], '1904', '?'),
            Player('Levin', 'Alexander', 'Alexander Levin', ['Russia'], '1871', '1929'), \
            )

        actual = BinarySearch.search_all_by_last_name(self.sample_players, 'Levin')

        self.assertIsNotNone(actual)
        self.assertEqual(expected_length, len(actual))

        if actual:
            actual = tuple(actual)

        self.assertEqual(expected_players, actual)
