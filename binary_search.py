from typing import List, Union
from player import Player
from output import Colours, Output
from math import log2

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

    @staticmethod
    def search_all_by_last_name(l:List[Player], last_name:str, start:int = 0, end:int = 1)->Union[List[Player], None]:
        """
        Unlike the previous method, this one does not stop at the first result
        It searches for all players with "last_name" in "l" within the range between "start" and "end" indices
        If at least one player is found it returns a list of players with the results, otherwise returns None
        """
        if start > 0 and start < len(l):
            l = l[start:]

        if end > 1 and end < len(l):
            l = l[:end]

        mid = len(l)//2
        iterations = 1
        found = False
        results = []
        original_length = len(l)

        print(f'Number of players in the haystack: {len(l)}')
        print(f'Needle: {last_name}\n')

        while mid > 0:
            BinarySearch.print_iteration(l, mid, iterations)

            if l[mid].last_name.lower() > last_name.lower():
                l = l[:len(l)//2]

            elif l[mid].last_name.lower() < last_name.lower():
                start = len(l)//2 + 1

                if start >= len(l):
                    start = len(l)//2

                l = l[start:]

            else:
                # a player was found
                results.append(l[mid])
                
                # as it is assumed that "l" is sorted, moving left should return the next result(s)
                l = l[:mid]

            iterations += 1      
            mid = len(l)//2

        if len(results) > 0:
            found = True
            BinarySearch.print_iteration(l, mid, iterations, Colours.green)

            # last result
            if l[mid].last_name.lower() == last_name.lower():
                results.append(l[mid])
        else:
            results = None
        
        print(f'Found results: {found}')

        return results

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