def outlet_menu():
    """
    Again we initialise a while loop to keep going through this menu. It keeps running through whatever is inside it until it is broken.
    Im not acutally sure its necessary, its part of a ChatGPT recommendation. 

    To summarise the flow so far, we have run show_menu, with the screen 1 options (by output, recent news, archive, exit), this passes a string
    to the main menu logic which matches it to an if statement that runs this function. This function will display the by outlet menu and run a fetch
    function depending on what outlet we select

    """

    while True:
        choice = show_menu(["The Hacker News","Checkpoint Research" , "Google Threat Intelligence", "Bleeping Computer", "Krebs on Security", "Back"],
        "Pick a News Outlet: ")

        if choice == "The Hacker News":
            print("Fetching The Hacker News from the last 3 days")
            fetch(url="https://feeds.feedburner.com/TheHackersNews")
        
        elif choice == "Checkpoint Research":
            print("Fetching Checkpoint Research news from the last week")
            fetch(url="https://research.checkpoint.com/feed", days=7, headers=headers)
        
        elif choice == "Google Threat Intelligence":
            print("Google Threat Intelligence news from the last 5 days")
            fetch_GTI(url="https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v", days=5)
        
        elif choice == "Bleeping Computer":
            print("Bleeping Computer from the last 5 days")
            fetch_BC(url="https://www.bleepingcomputer.com/feed/", days=5)
        
        elif choice == "Krebs on Secuirty":
            print("Bleeping Computer news from the last 3 days")
            fetch_KoS(url="https://krebsonsecurity.com/feed", days=3)

        elif choice == "Back" or choice is None:
            break
        


