# Code Written for mr Veldkamp's CS30 DATA MANAGEMENT PROJECT
# By: Lilly! (hehe)

# Preload Data
file = open("cookie.txt.", "r")
all_data = file.read().split("\n")  # process file into a list format
print(all_data[0:5])  # check data has loaded properly


# Helper Functions
def display_data():
    #    for item in all_data:
    #        print()
    print("\n".join(all_data))


# Main Loop for Program run
program_run = True

while program_run:
    x = int(input("What Would you like to do?\n"
                  "1. Display all data\n"
                  "2. Display some Data\n"
                  " 2.1 Select Filter\n"
                  "3. Add Current/Remove Obj to Favourites\n"
                  "4. Display Favourites\n"))

    if x == 1:
        display_data()

# Ideas for this short program:
# Filters
#   Common
#   Exotic
#   Has Chocolate
#   random price (order by price?)
#   add desc for each cookie, display when choosing
#   how to index items to look at? have each display also be a list with accessible objects
