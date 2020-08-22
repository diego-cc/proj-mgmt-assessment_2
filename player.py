from typing import List, Union
from csv import reader


class Player:
    """
    Player class: stores data related to each player loaded from a file

    Attributes
    ----------
    last_name: str
        last name of the player
    first_name: str
        first name of the player
    full_name: str
        full name of the player
    countries: Union[List[str], str]
        either a list of countries where the player competed or a single country
    born: Union[int, str, None]
        year when the player was born (if available)
    died: Union[int, str, None]
        year when the player died (if available)
    """
    def __init__(\
        self, \
        last_name:str, \
        first_name:str, \
        full_name:str, \
        countries:Union[List[str], str] = "US", \
        born:Union[int, str, None] = None, \
        died:Union[int, str, None] = None
        ):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__full_name = full_name
        self.__countries = countries
        self.__born = born
        self.__died = died

    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def first_name(self):
        return self.__first_name

    @property
    def full_name(self):
        return self.__full_name

    @property
    def countries(self):
        return self.__countries

    @property
    def born(self):
        return self.__born

    @property
    def died(self):
        return self.__died

    
    @staticmethod
    def parse_players(file_path:str)->List:
        """
        Loads raw players data from a CSV file and adds each one to a list of players
        Raises OSError if the file cannot be opened
        """
        players:List[Player] = []

        try:
            f = open(file_path, encoding='utf-8', newline='')
        except OSError as ex:
            print(f"Could not open file \"{file_path}\"")
            return players
            raise ex

        with f as raw_list:
            r = reader(raw_list, skipinitialspace=True)      
            iter_players = iter(r)
            next(iter_players)     

            for row in iter_players:
                players.append(Player(row[0], row[1], row[2], row[3].split(","), row[4], row[5]))

        return players
            

    def __str__(self):
        return f'{self.full_name}\nCountries: {self.countries}\nBorn: {self.born}\nDied: {self.died}'

    # self == other
    def __eq__(self, other):
        return (self.last_name, self.first_name, self.full_name, self.countries, self.born, self.died) == (other.last_name, other.first_name, other.full_name, other.countries, other.born, other.died)

    # self != other
    def __ne__(self, other):
        return not self.__eq__(other)

    # self > other
    def __gt__(self, other):
        return (self.last_name, self.first_name, self.born) > (other.last_name, other.first_name, other.born)

    # self < other
    def __lt__(self, other):
        return (self.last_name, self.first_name, self.born) < (other.last_name, other.first_name, other.born)

    # self >= other
    def __ge__(self, other):
        return not self.__lt__(other)

    # self <= other
    def __le__(self, other):
        return not self.__gt__(other)