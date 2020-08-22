from player import Player
from binary_search import BinarySearch

if __name__ == "__main__":
    sample_players = Player.parse_players('./data/chess-players.csv')
    sample_players.sort()        

    last_name = 'Carlsen'

    BinarySearch.search_by_last_name(sample_players, last_name)