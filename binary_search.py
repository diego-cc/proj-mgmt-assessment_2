from typing import List, Union
from player import Player
from output import Colours, Output

class BinarySearch:
    
    @staticmethod
    def search_by_last_name(l:List[Player], last_name:str, start:int = 0, end:int = 1)->Union[Player, None]:
        """
        Searches for a player with a last name "last_name" in "l" (case insensitive)
        Returns the first player object containing "last_name" in "l" if found or None otherwise
        "start" and "end" are optional indexes to narrow down the search scope in "l"
        "start" is inclusive, "end" is exclusive
        If they are not specified, the entire list "l" will be scanned
        Sorting the list beforehand is required
        """
        if start > 0 and start < len(l):
            l = l[start:]

        if end > 1 and end < len(l):
            l = l[:end]

        # l.sort()

        mid = len(l)//2
        tries = 1
        found = False

        print(f'Number of players in the haystack: {len(l)}')
        print(f'Needle: {last_name}\n')

        while l[mid].last_name.lower() != last_name.lower():    
            BinarySearch.print_iteration(l, mid, tries)       

            # break out of the loop if the needle is not found      
            if mid < 1:
                break 
            
            # too high, take the first half of the list
            if l[mid].last_name.lower() > last_name.lower():
                l = l[:len(l)//2]

            # too low, take the second half of the list
            else:
                start = len(l)//2 + 1

                if start >= len(l):
                    start = len(l)//2

                l = l[start:]            

            mid = len(l)//2    
            tries += 1                    

        if l[mid].last_name.lower() == last_name.lower():
            found = True
            BinarySearch.print_iteration(l, mid, tries, Colours.green)
        else:
            mid = None
        
        print(f'Found: {found}')

        if found:
            return l[mid]
        return None

        """ if found:
            Output.print(f'Found: {found}', Colours.green, Colours.lightgrey)
        else:
            Output.print(f'Found: {found}', Colours.red, Colours.lightgrey) """

    """
    Prints the current list size, the element in the middle and number of tries up to this point
    "fg" and "bg" are optional foreground / background colours to customise the output
    """
    @staticmethod
    def print_iteration(\
        l:List[Player],\
        mid:int, tries:int,\
        fg:Union[Colours, None] = None,\
        bg:Union[Colours, None] = None
        )->None:
        
        msg = f'Current haystack size: {len(l)}\nCurrent try:\n{l[mid]}\nNumber of tries so far: {tries}\n'

        print(msg)