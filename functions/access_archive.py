from All_Functions import display
import json
import os


def access_archive():

    archive_file = "archive.json"


    if os.path.exits(archive_file):
        with open(archive_file) as f:
            try:
                archive = json.load(f)
                display(archive)
            except json.JSONDecodeError:
                print("Decoding error for archive.python - check access_archive.py")
                return
        
    else: 
        print(f"{archive_file} does not exist")
        input("Please press ENTER to go back to the previous screen. ")

    
