# Code Written for mr Veldkamp's CS30 DATA MANAGEMENT PROJECT
# By: Lilly! (hehe)

import json

# Preload Data
# Cookie Data
filecook = open("cookies.txt.", "r")
cookie_data = json.load(filecook)
print(cookie_data[0:5])  # check data has loaded properly

# User Data
fileuser = open("users.txt", "r")
user_data = json.load(fileuser)
print(user_data[0:1])

# User data format:
# username: "str"
# password: "str"
# favourites: ["list", "of", "dictionaries"]


# Important Functions
def pretty_display(list_of_dicts):
    # Display items in a pretty way
    for item in list_of_dicts:
        for key in item:
            print(f"{key}: {item[key]}")
        print("\n")


def sort_cookies(method):
    display_list = []
    for cookie in cookie_data:
        for search in display_list:
            # Find the first item with a higher price than the one we're inserting
            # Then insert it into the slot it's in, moving the higher one up.
            if cookie[method.capitalize()] <= search[method.capitalize()]:
                display_list.insert(display_list.index(search), cookie)
                break
        # Add Cookie to end of list if no lesser
        if cookie not in display_list:
            display_list.append(cookie)
    return display_list


# Main Loop for Program run
program_run = True

while program_run:
    x = int(input("What Would you like to do?\n"
                  "1. Display all data\n"
                  "2. Display some Data\n"
                  "3. Add Current/Remove Obj to Favourites\n"
                  "4. Display Favourites\n"))

    if x == 1:
        pretty_display(cookie_data)
    if x == 2:
        while True:
            x = input("Please type a filter:\n"
                      "\"Name\"\n"
                      "\"Price\"\n"
                      "\"Rarity\"\n")
            pretty_display(sort_cookies(x.lower()))
            break
    if x == 3:
        if "5" > "20":
            print('wtf')
        else:
            print("ok")

# Ideas for this short program:
# Filters
#   Common
#   Exotic
#   Has Chocolate
#   random price (order by price?)
#   add desc for each cookie, display when choosing
#   how to index items to look at? have each display also be a list with accessible objects





# Below is mostly just the code for transforming cookie.txt into cookies.txt

#all_cookies = []


#def new_cookie(CookieList):
    # Input a list that is one line of txt doc, output cookie dictionary.
    # Format for cookies is Name, Rarity, Price and Description
#    newDict = {
#        "Name": CookieList[0] + " Cookie",
#        "Rarity": CookieList[1],
#        "Price": CookieList[2],
#        "Description": CookieList[3]
#    }

#    all_cookies.append(newDict)


#for cookie in cookie_data:
#    x = cookie.split(",")
#    new_cookie(x)


#for cookie in all_cookies:
#    print(str(cookie) + "\n")

#x = json.dumps(all_cookies, indent=4)
#print(x)
#y = open("cookies.txt", "w")
#y.write(x)
#y.close
