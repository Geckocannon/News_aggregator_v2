
def Archive_menu():
    while True:
        choice = show_menu(["Add to Archive", "Access Archive", "Remove from Archive", "Back"], "Archive menu")

        if choice == "Add to Archive":
            add_archive()
        elif choice == "Access Archive":
            access_archive()
        elif choice == "Remove from Archive":
            remove_arhive()
        elif choice == "Back" or choice is None:
            break
        
