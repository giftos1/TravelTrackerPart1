"""
Name:Gift Sydney Ogingo
Date started:5/7/2022
GitHub URL:https://github.com/giftos1/TravelTrackerProject
"""

FILENAME = 'places.csv'


def main():
    """run the whole program"""
    print("Travel Tracker 1.0 - by Gift Ogingo")
    with open('places.csv', 'r') as places_file:
        places_rows = places_file.readlines()
        for row in places_rows:
            parts = row.split(",")  # split each row into a list
    print(len(places_rows), "places loaded from", FILENAME)
    menu_input = input("Menu:\n"
                       "L - List Places\n"
                       "A - Add new place\n"
                       "M - Mark a place as visited\n"
                       "Q - Quit").lower()


main()
