# Travel Tracker Project
By: Gift Sydney Ogingo  

# Program Overview:
This program is a simple "travel tracker" that allows a user to track places they wish to visit and
places they have already visited.

The program reads and writes a list of places in a text file,
and each place has: name, country, priority, whether it is visited (v) or unvisited (n)

Users can choose to see the list of places, including the total number of places and unvisited
places.

The list will be sorted by visited status then by priority (decreasing number).

Users can add new places and mark places as visited.

They cannot change places from visited to unvisited.

# Coding Requirements
- Only load (read) the places file once, when the program starts.
- Only save (write) the places file once, when the program ends.
- Store the place data in a list of lists and pass that to any functions that need access
to it.
- The only global variables used are constants.
- The menu choice should handle uppercase and lowercase letters.
- Exception handling is used where appropriate to deal with input errors (including entering
numbers and selecting places). 
- I have used generic, customisable functions to perform input with error checking (e.g. getting the place name and country
can reuse the same function).

# Output Requirements
- The sample output is intended to show a large (but maybe not exhaustive) range of situations including user input error handling.
- The visited place numbers show as roman numerals(i, ii. iii) in the preview but tne program functions with numerals such as 1., 2. , 3. and so on. (markdown file problem)
- The program matches the sample output below; including spaces, spelling, and the formatting of the place lists.

This repo contains this projects' files.  
(`temp.csv` has the original data and I used it to retrieve the data back in case I edited the contents of `places.csv` and want the original data back).

# The expected final output is shown below:
- Travel Tracker 1.0 - by Gift Sydney Ogingo
- 3 places loaded from places.csv
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> l
- *1. Lima in Peru priority 3
- *2. Rome in Italy priority 12
- 3. Auckland in New Zealand priority 1
- 3 places. You still want to visit 2 places.
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> B
- Invalid menu choice
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> a
- Name:
- Input can not be blank
- Name:
- Input can not be blank
- Name: Uluru
- Country:
- Input can not be blank
- Country: Australia
- Priority:
- Invalid input; enter a valid number
- Priority: -1
- Number must be > 0
- Priority: why?
- Invalid input; enter a valid number
- Priority: 2
- Uluru in Australia (priority 2) added to Travel Tracker
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> L
- *1. Uluru in Australia priority 2
- *2. Lima in Peru priority 3
- *3. Rome in Italy priority 12
- 4. Auckland in New Zealand priority 1
- 4 places. You still want to visit 3 places.
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> m
- *1. Uluru in Australia priority 2
- *2. Lima in Peru priority 3
- *3. Rome in Italy priority 12
- 4. Auckland in New Zealand priority 1
- 4 places. You still want to visit 3 places.
- Enter the number of a place to mark as visited
- >>> Uluru
- Invalid input; enter a valid number
- >>> -1
- Number must be > 0
- >>> 9
- Invalid place number
- >>> 4
- That place is already visited
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> m
- *1. Uluru in Australia priority 2
- *2. Lima in Peru priority 3
- *3. Rome in Italy priority 12
- 4. Auckland in New Zealand priority 1
- 4 places. You still want to visit 3 places.
- Enter the number of a place to mark as visited
- >>> 1
- Uluru in Australia visited!
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> m
- *1. Lima in Peru priority 3
- *2. Rome in Italy priority 12
- 3. Auckland in New Zealand priority 1
- 4. Uluru in Australia priority 2
- 4 places. You still want to visit 2 places.
- Enter the number of a place to mark as visited
- >>> 1
- Lima in Peru visited!
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> m
- *1. Rome in Italy priority 12
- 2. Auckland in New Zealand priority 1
- 3. Uluru in Australia priority 2
- 4. Lima in Peru priority 3
- 4 places. You still want to visit 1 places.
- Enter the number of a place to mark as visited
- >>> 1
- Rome in Italy visited!
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> m
- No unvisited places
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> L
- 1. Auckland in New Zealand priority 1
- 2. Uluru in Australia priority 2
- 3. Lima in Peru priority 3
- 4. Rome in Italy priority 12
- 4 places. No places left to visit. Why not add a new place?
- Menu:
- L - List places
- A - Add new place
- M - Mark a place as visited
- Q - Quit
- >>> q
- 4 places saved to places.csv
- Have a nice day :)
# At the end of this run, the saved CSV file contained:
- Auckland,New Zealand,1,v
- Uluru,Australia,2,v
- Lima,Peru,3,v
- Rome,Italy,12,v
