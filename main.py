"""
Name:Gift Sydney Ogingo
Date started:5/7/2022
GitHub URL:https://github.com/giftos1/TravelTrackerPart1
"""
from operator import itemgetter

FILENAME = 'places.csv'
NOT_VISITED = "n"


def main():
    """Run the whole program"""
    print("Travel Tracker 1.0 - by Gift Ogingo")  # display welcome message

    # load csv file and append sorted data to a nested list
    places = []
    with open('places.csv', 'r') as output_file:
        for each_row in output_file:
            row = each_row.strip("\n")
            lines = row.split(",")  # split each row in file to a list
            lines[2] = int(lines[2])  # convert number string to integer for sorting
            places.append(lines)

    places.sort(key=itemgetter(3, 2))  # sort list by visited status then priority
    print(len(places), "places loaded from", FILENAME)
    letters = ["l", "a", "m", "q"]
    place_file = open("places.csv", "a+")
    menu_input = ""
    while menu_input != "q":
        menu_input = input_menu()
        if menu_input == "l":
            get_max_name_length(places)

        # Get name, country and priority input of a place and add them to the Travel Tracker
        elif menu_input == "a":
            name_input = validate_name_input()
            country_input = validate_country_input()
            get_priority(name_input, country_input, places, place_file)  # Get priority input and check for
            # ValueError

        elif menu_input == "m":
            place = [place for place in places]
            if "n" in place[0][3]:
                get_max_name_length(places)
                print("Enter the number of a place to mark as visited")
                get_number_input(places)
            else:
                print("No unvisited places")

        elif menu_input not in letters:
            print("Invalid menu choice")

        else:
            print(f"{len(places)} places saved in places.csv")

    print("Have a nice day:)")  # display message when user chooses q


def input_menu():
    menu_input = input("Menu:\n"
                       "L - List Places\n"
                       "A - Add new place\n"
                       "M - Mark a place as visited\n"
                       "Q - Quit\n"
                       ">>").lower()
    return menu_input


def validate_country_input():
    """Get country input from user and check for blank answers"""
    country_input = ""
    validate_input = False
    while not validate_input:
        country_input = input("Country: ")
        if country_input == "":
            print("Input can not be blank")
        else:
            validate_input = True
    return country_input


def validate_name_input():
    """Get name input from user and check for blank answers"""
    name_input = ""
    validate_input = False
    while not validate_input:
        name_input = input("Name: ")
        if name_input == "":
            print("Input can not be blank")
        else:
            validate_input = True
    return name_input


def get_max_name_length(places):
    """get maximum length of city and country name and call display_formatted_list"""

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
            # count the number of unvisited places
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
    return print(f"{count} places. You still want to visit {unvisited_count} places.")


def get_priority(name_input, country_input, places, place_file):
    """Get priority input and validate input
    Display the added place through printing the name,country and priority of the place"""
    validate_input = False
    priority_input = 0
    while not validate_input:
        try:
            priority_input = int(input("Priority: "))
            if priority_input <= 0:
                print("Number must be > 0")
            else:
                validate_input = True

        except ValueError:
            print("Invalid input; enter a valid number")

    print(f"{name_input} in {country_input} (priority {priority_input}) added to Travel Tracker")  # display added place
    new_added_place(name_input, country_input, priority_input, places, place_file)


def new_added_place(name, country, priority_input, places, place_file):
    """Add new place to the nested list of places and sort the list accordingly"""
    new_place = [name, country, priority_input, NOT_VISITED]
    places.append(new_place)
    places.sort(key=itemgetter(3, 2))
    place_file.write(f"\n{new_place[0]},{new_place[1]},{new_place[2]},{new_place[3]}")


def get_number_input(places):
    number_input = 0
    validate_input = False
    while not validate_input:
        try:
            number_input = int(input(">>"))
            if number_input <= 0:
                print("Number must be > 0")

            elif number_input not in range(1, len(places) + 1):
                print("Invalid place number")

            else:
                validate_input = True

        except ValueError:
            print("Invalid input; enter a valid number")
    convert_unvisited_place(number_input, places)


def convert_unvisited_place(number_input, places):
    """Convert unvisited place to visited if user marks it as visited"""
    for count, place in enumerate(places):
        count += 1
        while number_input == count:  # checks the number which the user types in that corresponds to a given place
            if place[3] == "v":
                print("That place is already visited!")
            else:
                print(f"{place[0]} in {place[1]} visited!")
                place[3] = "v"
                places.sort(key=itemgetter(3, 2))
            break


main()
