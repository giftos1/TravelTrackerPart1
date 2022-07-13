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

    get_max_name_length(menu_input, places)


def get_max_name_length(choice_input, places):
    """get maximum length of city and country name and call display_formatted_list"""
    while choice_input:
        if choice_input == "l":

            city_names = []
            country_names = []

            # add the name of each city and country to respective lists
            for each_place in places:
                city_name = each_place[0].strip("\n")
                city_names.append(city_name)

                country_name = each_place[1].strip("\n")
                country_names.append(country_name)

            # get the name of city and country with the maximum string length from respective lists
            max_country_length = len(max(country_names, key=len))
            max_city_length = len(max(city_names, key=len))

            display_formatted_list(max_city_length, max_country_length, places)

        break


def display_formatted_list(max_city_length, max_country_length, places):
    """Display a neatly formatted list of places when user chooses list"""
    unvisited_count = 0
    count = 0
    for place in places:
        count += 1
        additional_city_space = max_city_length - len(place[0])
        additional_country_space = max_country_length - len(place[1])

        # display a dynamic lined up list based on longest city and country name.
        if len(place[0]) != max_city_length and len(place[1]) != max_country_length:
            # check if place is unvisited(n) and add a star(*) before the number if true
            if "n" in place[3]:
                unvisited_count += 1
                print(f"*{count}.", place[0], "{:{}}in".format("", additional_city_space), place[1],
                      "{:{}}priority".format("", additional_country_space), place[2])
            else:
                print(f" {count}.", place[0], "{:{}}in".format("", additional_city_space), place[1],
                      "{:{}}priority".format("", additional_country_space), place[2])

        else:
            if "n" in place[3]:
                unvisited_count += 1
                print(f"*{count}.", place[0], "in", place[1], "priority", place[2])
            else:
                print(f" {count}.", place[0], "in", place[1], "priority", place[2])

    display_visit_status(count, unvisited_count)


def display_visit_status(count, unvisited_count):
    """display the number of places visited and not visited"""
    print(f"{count} places. You still want to visit {unvisited_count} places.")


main()
