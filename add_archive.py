
import json
import os


def add_archive():

    #ask for clipboard ID

    input_id = input("paste ID of article to archive: ").strip()
    if not input_id:
        print("No ID entered")
        return

  
    #Load or create archive.json
    archive_file = "archive.json"
    if os.path.exists(archive_file):
        with open(archive_file, "r", encoding="utf=8") as f:
            try:
                archive_data = json.load(f)
            except json.JSONDecodeError:
                archive_data = []

    else:
        archive_data = []


    #check if ID is in archive.json
    if any(entry["ID"] == input_id for entry in archive_data):
        print("Already in archive.")
        return

    

    #Load fetched.json
    fetched_file = "fetched.json"
    if not os.path.exists(fetched_file):
        print("fetched.json not found. Please fetch news first")
        return

    with open(fetched_file, "r", encoding="utf-8") as f:
        fetched_data = json.load(f)

    #Match ID to entry (loop)
    match = next((entry for entry in fetched_data if entry["ID"] == input_id), None)

    if not match:
        print("ID not found in fetched.json")
        return

    archive_data.append(match)
    with open(archive_file, "w", encoding="utf-8") as f:
        json.dump(archive_data, f, indent=4)

    print(f"Archive sucessful: {match['title']}")
    input("\nPress Enter to return to Archive Menu...")
    return






