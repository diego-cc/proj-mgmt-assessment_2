from player import Player
from binary_search import BinarySearch

if __name__ == "__main__":
    """
    Load chess players list and print all search results for last_name == 'Levin'
    """
    sample_players = Player.parse_players('./data/chess-players.csv')
    sample_players.sort()
    last_name = 'griffith'

    results = BinarySearch.search_all_by_last_name(sample_players, last_name)

    print('Results:\n')

    if results is not None:
        mapped_results = map(lambda p: str(p), results)

        for p in mapped_results:
            print(p + '\n')

    else:
        print('No results found')