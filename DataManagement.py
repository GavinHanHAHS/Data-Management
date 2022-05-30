# Code Written for mr Veldkamp's CS30 DATA MANAGEMENT PROJECT
# By: Lilly! (hehe)

import json

# Preload Data
# Cookie Data
filecook = open("cookie.txt.", "r")
cookie_data = filecook.read().split("\n")  # process file into a list format
print(cookie_data[0:5])  # check data has loaded properly



# Helper Functions
def display_data():
    #    for item in cookie_data:
    #        print()
    print("\n".join(cookie_data))


# Main Loop for Program run
#program_run = True

#while program_run:
#    x = int(input("What Would you like to do?\n"
#                  "1. Display all data\n"
#                  "2. Display some Data\n"
#                  " 2.1 Select Filter\n"
#                  "3. Add Current/Remove Obj to Favourites\n"
#                  "4. Display Favourites\n"))
#
#    if x == 1:
#        display_data()

# Ideas for this short program:
# Filters
#   Common
#   Exotic
#   Has Chocolate
#   random price (order by price?)
#   add desc for each cookie, display when choosing
#   how to index items to look at? have each display also be a list with accessible objects

all_cookies = []


def new_cookie(CookieList):
    # Input a list that is one line of txt doc, output cookie dictionary.
    # Format for cookies is Name, Rarity, Price and Description
    newDict = {
        "Name": CookieList[0] + " Cookie",
        "Rarity": CookieList[1],
        "Price": CookieList[2],
        "Description": CookieList[3]
    }

    all_cookies.append(newDict)


for cookie in cookie_data:
    x = cookie.split(",")
    new_cookie(x)


#for cookie in all_cookies:
#    print(str(cookie) + "\n")

x = json.dumps(all_cookies, indent=4)
print(x)
y = open("cookies.txt", "w")
y.write(x)
y.close
