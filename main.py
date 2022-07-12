"""
Name:Gift Sydney Ogingo
Date started:5/7/2022
GitHub URL:https://github.com/giftos1/TravelTrackerProject
"""
from operator import itemgetter

FILENAME = 'places.csv'


def main():
    """Run the whole program"""
    print("Travel Tracker 1.0 - by Gift Ogingo")  # display welcome message

    # load csv file and append sorted data to a nested list
    places = []
    with open('places.csv', 'r') as output_file:
        for each_row in output_file:
            row = each_row.strip("\n")
            lines = row.split(",")  # split each row in file to a list
            lines[2] = int(lines[2])  # convert string to integer for sorting
            places.append(lines)

    places.sort(key=itemgetter(3, 2))  # sort list by visited status then priority

    print(len(places), "places loaded from", FILENAME)

    menu_input = input("Menu:\n"
                       "L - List Places\n"
                       "A - Add new place\n"
                       "M - Mark a place as visited\n"
                       "Q - Quit").lower()

    display_list_of_places(menu_input, places)


def display_list_of_places(choice_input, places):
    """get maximum length of city and country name and call display_formatted_list to display a formatted list of
    places based on the respective lengths"""
    while choice_input:
        if choice_input == "l":

            city_names = []
            country_names = []
            for each_place in places:
                city_name = each_place[0].strip("\n")
                city_names.append(city_name)

                country_name = each_place[1].strip("\n")
                country_names.append(country_name)

            max_country_name = max(country_names, key=len)
            max_city_name = max(city_names, key=len)

            max_country_length = len(max_country_name)
            max_city_length = len(max_city_name)

            display_formatted_list(max_city_length, max_city_name, max_country_length, max_country_name, places)

        break


def display_formatted_list(max_city_length, max_city_name, max_country_length, max_country_name, places):
    """Display a neatly formatted list of places when user chooses l"""
    for place in places:
        additional_city_space = max_city_length - len(place[0])
        additional_country_space = max_country_length - len(place[1])

        # display a dynamic lined up list based on longest city name and country name.
        if len(place[0]) != len(max_city_name) and len(place[1]) != len(max_country_name):
            print(place[0], "{:{}}in".format("", additional_city_space), place[1],
                  "{:{}}priority".format("", additional_country_space), place[2])
        else:
            print(place[0], "in", place[1], "priority", place[2])


main()
