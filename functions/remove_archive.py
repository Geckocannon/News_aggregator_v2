import json
import os

def remove_arhive():
    input_id = input("Paste ID of article to remove from archive: ").strip()
    if not input_id:
        print("No ID entered.")
        return

    archive_file = "archive.json"

    # Load archive if it exists
    if os.path.exists(archive_file):
        with open(archive_file, "r", encoding="utf-8") as f:
            try:
                archive_data = json.load(f)
            except json.JSONDecodeError:
                print("Archive failed to decode")
                archive_data = []
    else:
        print("No archive found.")
        return

    # Search for entry by ID
    entry_to_remove = None
    for entry in archive_data:
        if entry["ID"] == input_id:
            entry_to_remove = entry
            break

    if not entry_to_remove:
        print("ID not found in archive.")
        return

    # Confirm removal
    confirm = input(f"Are you sure you want to remove '{entry_to_remove['title']}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Removal cancelled.")
        return

    # Use .remove() to delete the entry
    archive_data.remove(entry_to_remove)

    # Write updated data back to file
    with open(archive_file, "w", encoding="utf-8") as f:
        json.dump(archive_data, f, indent=4)

    print(f"Removed: {entry_to_remove['title']}")
    input("\nPress Enter to return to Archive Menu...")

    