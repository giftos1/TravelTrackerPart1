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
            lines[2] = int(lines[2])  # convert number string to integer for sorting
            places.append(lines)

    places.sort(key=itemgetter(3, 2))  # sort list by visited status then priority

    print(len(places), "places loaded from", FILENAME)

    letters_input = ["l", "a", "m", "q"]
    menu_input = input_menu()
    while menu_input != "q":
        if menu_input == "l":
            get_max_name_length(places)
            menu_input = input_menu()

        # Get name, country and priority input of a place and add them to the Travel Tracker
        elif menu_input == "a":
            name_input = input("Name: ")
            check_name_input(name_input) # Check for blank input

            country_input = input("Country: ")
            check_country_input(country_input)  # Check for blank input

            get_priority(name_input, country_input)  # Get priority input and check for ValueError

            menu_input = input_menu()

        # check if the wrong letter has been typed and return the menu if true
        elif menu_input not in letters_input:
            print("Invalid menu choice")
            menu_input = input_menu()

    print("Have a nice day :)")  # display message when user chooses q


def input_menu():
    menu_input = input("Menu:\n"
                       "L - List Places\n"
                       "A - Add new place\n"
                       "M - Mark a place as visited\n"
                       "Q - Quit").lower()
    return menu_input


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
    print(f"{count} places. You still want to visit {unvisited_count} places.")


def check_name_input(name_input):
    """Check if the name_input has any blank input"""
    while name_input == "":
        print("Input can not be blank")
        name_input = input("Name: ")


def check_country_input(country_input):
    """Check if the country_input has any blank input"""
    while country_input == "":
        print("Input can not be blank")
        country_input = input("Country: ")


def get_priority(name, country):
    """Get priority input and validate input
    Display the added place through printing the name,country and priority of the place"""
    validate_input = False
    while not validate_input:
        try:
            priority_input = int(input("Priority: "))
            if priority_input <= 0:
                print("Number must be > 0")
            else:
                validate_input = True
                print(f"{name} in {country} (priority {priority_input}) added to Travel Tracker")  # display added place

        except ValueError:
            print("Invalid input; enter a valid number")


main()
