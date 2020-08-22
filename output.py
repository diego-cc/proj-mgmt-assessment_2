"""
Maps colours to ANSI characters
Non-standard, not 100% reliable on Windows
"""
class Colours:
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'

class Output:

    """
    Prints a message to stdout with optional foreground / background colours
    """
    @staticmethod
    def print(message:str, fg:Colours = None, bg:Colours = None)->None:
        if fg and not bg:
            print(f'{fg}{message}')
        elif bg and not fg:
            print(f'{message}{bg}')
        elif fg and bg:
            print(f'{fg}{message}{bg}')
        else:
            print(message)