from utils import *

if __name__ == '__main__':
    ##### CHANGE THESE ACCORDING TO WHAT YOU NEED #####

    # List of chapter numbers
    chapters = [7,8,9,11,12]  # Add your chapter numbers here

    # Chapter file folder name:
    chapter_folder = 'cogpsy'  # Add your folder name here

    # Time limit per round, in seconds
    time_limit = 40

    ##### MAIN CODE ####

    start_game(chapters, chapter_folder, time_limit)
