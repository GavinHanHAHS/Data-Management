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
def new_user(username, password):
    newDict = {
        "Username": username,
        "Password": password,
        "Favourites": []
    }

    user_data.append(newDict)


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


# Main Loop(s) for Program run
main_program = True

while main_program:
    x = int(input("What would you like to do?\n"
                  "1. Login\n"
                  "2. Register\n"
                  "3. Save & Quit\n"))

    if x == 1:
        # login, then do main program
        input_username = input("Input your Username\n")
        input_password = input("Input your Password\n")
        userFound = False
        for user in user_data:
            if user["Username"] == input_username and user["Password"] == input_password:
                print("login success! Redirecting to Main Menu...\n\n")
                user_favs = user["Favourites"]
                userFound = True
                while True:
                    y = int(input("What Would you like to do?\n"
                                  "1. Display all data\n"
                                  "2. Display sorted Data\n"
                                  "3. Add/Remove to Favourites\n"
                                  "4. Display Favourites\n"
                                  "5. Logout\n"))

                    if y == 1:
                        pretty_display(cookie_data)
                    if y == 2:
                        options = ["name", "price", "rarity"]
                        while True:
                            z = input("Please type a filter:\n"
                                      "\"Name\"\n"
                                      "\"Price\"\n"
                                      "\"Rarity\"\n").lower()
                            if z in options:
                                pretty_display(sort_cookies(x))
                                break
                            else:
                                print("Please type a valid option!")
                    if y == 3:
                        while True:
                            z = input("Do you want to add or remove a cookie from favourites??\n"
                                      "1. Add\n"
                                      "2. Remove\n"
                                      "3. Quit Menu\n")
                            if z == "1":
                                found = False
                                while True:
                                    add_cookie = input("What Kind of Cookie would you like to Add?\n")
                                    for cookie in cookie_data:
                                        if add_cookie == cookie["Name"]:
                                            user_favs.append(cookie)
                                            print("Cookie added to favourites!") #RIGHT NOW THIS IS CASE SENSTIIVE
                                            found = False                        #ALSO MUL;TIPLES AGAIN
                                            break
                                    if not found:
                                        print("Cookie not found!") # ADD QUIT OPTION HERE
                                    else:
                                        break
                            elif z == "2":
                                found = False
                                while True:
                                    remove_cookie = input("What Kind of Cookie would you like to Remove?\n")
                                    for cookie in user_favs:
                                        if remove_cookie == cookie["Name"]:
                                            user_favs.pop(user_favs.index(cookie))
                                            print("Cookie removed from favourites!") #RIGHT NOW THIS IS CASE SENSTIIVE
                                            found = True
                                            break
                                    if not found:
                                        print("Cookie not found!")
                                    else:
                                        break
                            elif z == "3":
                                break
                            else:
                                print("Invalid input")

                    if y == 4:
                        # favourites list path: user_data[user_index]["Favourites"] -> list of favourites
                        pretty_display(user_favs)
                    if y == 5:
                        break
        if not userFound:
            print("Could not find User match.\n\n")
    if x == 2: #PROBLEM: CHECK IF USER EXISTS ALREADY
        newUsername = input("Please provide your Username\n")
        newPassword = input("Please Provide your Password\n")

        new_user(newUsername, newPassword)

    if x == 3:
        # Saving functions
        print("Saving...")
        save_data = json.dumps(user_data, indent=4)
        fileOpen = open("users.txt", "w")
        fileOpen.write(save_data)
        fileOpen.close()
        print("Goodbye!")
        main_program = False

# Ideas for this short program:
# Filters
#   Common
#   Exotic
#   Has Chocolate
#   random price (order by price?)
#   add desc for each cookie, display when choosing
#   how to index items to look at? have each display also be a list with accessible objects

# Below is mostly just the code for transforming cookie.txt into cookies.txt

# all_cookies = []


# def new_cookie(CookieList):
    # Input a list that is one line of txt doc, output cookie dictionary.
    # Format for cookies is Name, Rarity, Price and Description
#    newDict = {
#        "Name": CookieList[0] + " Cookie",
#        "Rarity": CookieList[1],
#        "Price": CookieList[2],
#        "Description": CookieList[3]
#    }

#    all_cookies.append(newDict)


# for cookie in cookie_data:
#    x = cookie.split(",")
#    new_cookie(x)


# for cookie in all_cookies:
#    print(str(cookie) + "\n")

# x = json.dumps(all_cookies, indent=4)
# print(x)
# y = open("cookies.txt", "w")
# y.write(x)
# y.close

