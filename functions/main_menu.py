from All_Functions import show_menu

def main_menu(choice, title):
    """
    We define our function and import show menu, which returns a string value based on the option a user chooses. This can either be
    "By Outlets", "Recent News", "Archive", or "Exit".

    choice is defined as the output of running the show menu function. As we said earlier this will be one of 4 strings.

    We create a if statement that says while true to maintain the menu until a choice is made. We then create an if elif block to say if the choice - which
    is one of 4 strings, matches - run the menu program for that choice. The menu program for each choice will be a show_menu() call with different options and
    title passed in.
    
    """
    while True:
        choice = show_menu(["By Outlets", "Recent News", "Archive", "Exit"], "Main Menu")

        if choice == "By Outlets":
            Outlet_menu()
        elif choice == "Recent News":
            Recent_news_menu()
        elif choice == "Archive":
            Archive_menu()
        elif choice == "Exit" or choice is None:
            break


