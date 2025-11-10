from simple_term_menu import TerminalMenu

def show_menu(options, title):

    """
    Define our function. For now I see no point in passing arguements like options to it because I know what I want my menu to feature.
    So I can hard code these options into the function.

    menu is defined as our instance of the class TerminalMenu. it takes as its first argument the options to be displayed in the menu.
    It then takes stylistic arguments to display the title, cursor wrap around and the highlight style. We also set clear screen to true
    to make it feel like you are advancing to a new screen on option select.

    choice index is the output of simple_term_menu.Terminalmenu.show(). AKA this is the index in our list of options that was chosen. Hence, choice index

    After that, if nothing was chosen - return nothing. Otherwise return the choice. 

    This will return a string which we can pass to another function which will do an action based on which string it gets as input. That action will be to display
    another menu.

    """
    menu = TerminalMenu(
        options,
        title = f"\n{title}\n",
        cycle_cursor=True,
        clear_screen=True,
    )
    choice_index = menu.show()
    return None if choice_index is None else options[choice_index]

###################################################################################################################################################

def main_menu():
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


###################################################################################################################################################


def Outlet_menu():
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
            display(fetch(url="https://feeds.feedburner.com/TheHackersNews"))
            
        
        elif choice == "Checkpoint Research":
            print("Fetching Checkpoint Research news from the last week")
            display(fetch(url="https://research.checkpoint.com/feed", days=7))
            
        
        elif choice == "Google Threat Intelligence":
            print("Google Threat Intelligence news from the last 5 days")
            display(fetch(url="https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v", days=5))
            
        
        elif choice == "Bleeping Computer":
            print("Bleeping Computer from the last 5 days")
            display(fetch(url="https://www.bleepingcomputer.com/feed/", days=5))
            
        
        elif choice == "Krebs on Secuirty":
            print("Bleeping Computer news from the last 3 days")
            display(fetch(url="https://krebsonsecurity.com/feed", days=3))
            

        elif choice == "Back" or choice is None:
            break
        


###################################################################################################################################################

import hashlib

def mashthis(title:str, link:str):
    combined = (title+link).encode("utf-8")
    return hashlib.sha256(combined).hexdigest()


###################################################################################################################################################

import feedparser
import requests
import requests_cache
import time
from datetime import datetime, timedelta, UTC, timezone
from All_Functions import mashthis
import json

def fetch(url, days=3, cache_name="cache", cache_expire=600, timeout=10):


    """
    Here we basically have our get_requests function from V1. We install a cache that lasts 10 minutes. We http request the hardcoded url this time.
    Hardcoded because these are menu options not arguments being passed at the CLI. We then instantiate some fucking time rules. NGL I pulled this 
    striaght from chat GPT. It makes almost 0 sense to me, except that it takes some cutoff which is the time now minus 3 days. It then loops
    through the entries to see if they have the attribute "published_parsed" and if they do published parsed is equal to some time thingy. If not no idea what
    the elif statement there is doing

    next up if published time is true and it is greater than or equal to the cutoff get the details and append them to recent articles. return recent 
    articles which is a list of dictionaries. Should be from the last 3 days.

    """
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://research.checkpoint.com/",
    "Connection": "keep-alive",
}

    requests_cache.install_cache(cache_name, expire_after=cache_expire)
    try:
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching feed: {e}")
        return[]
    
    feed = feedparser.parse(response.content)
        

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    recent_articles = []

    for entry in feed.entries:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_time = datetime.fromtimestamp(time.mktime(entry.published_parsed), tz=timezone.utc)
        elif "updated_parsed" in entry and entry.updated_parsed:
            published_time = datetime.fromtimestamp(time.mktime(entry.updated_parsed), tz=timezone.utc)

        if published_time and published_time >= cutoff:
            title = entry.get("title", "No title found")
            link = entry.get("link", "No link found")
            recent_articles.append({
                "ID": mashthis(title, link),
                "title": title,
                "summary": entry.get("summary", "No summary found"),
                "link": link,
                "published": published_time.strftime("%d-%m-%y %H:%M:%S")
            })

      
    
    if recent_articles:
        with open("fetched.json", "w", encoding="utf-8") as f:
            json.dump(recent_articles, f, indent=4)
    else:
        print("No recent articles found - keeping previous fetched.json")
              
    return recent_articles


###################################################################################################################################################

from simple_term_menu import TerminalMenu
import pyperclip
import webbrowser

def display(articles):
    """
    Take input, list of dicts, build terminal menu from title and published
    on click copy ID, and open "link" field
    """

    if not articles:
        print("no Articles to display")
        return
    
    menu_entries = [
        f"{a['title']} - {a['published']}" for a in articles
    ]

    menu_entries.append("Back")

    while True:
        terminal_menu = TerminalMenu(
            menu_entries,
            title="Pick an article to open (ID will be copied)",
            cycle_cursor=True,
            clear_screen=True,
        )

        choice_index = terminal_menu.show()

        if choice_index is None or choice_index == len(menu_entries) - 1:
            break

        selected_article = articles[choice_index]
        article_id = selected_article["ID"]
        article_link = selected_article["link"]

        pyperclip.copy(article_id)
        print(f"copied ID: {article_id} to clipboard!")

        webbrowser.open(article_link)

###################################################################################################################################################

def Recent_news_menu():
    print("\nFetching todays news from each outlet...\n")
    todays_news = []

    outlet_urls = [ 
        "https://feeds.feedburner.com/TheHackersNews",
        "https://research.checkpoint.com/feed",
        "https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v",
        "https://www.bleepingcomputer.com/feed/",
        "https://krebsonsecurity.com/feed"
    ]

    for url in outlet_urls:
        articles = fetch(url=url, days=1)
        todays_news.extend(articles)

    if todays_news:
        with open("fetched.json", "w", encoding="utf-8") as f:
            json.dump(todays_news, f, indent=4)
    
    display(todays_news)



###################################################################################################################################################


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

###################################################################################################################################################
import json
import os


def add_archive():

    #ask for clipboard ID

    input_id = input("paste ID of article to archive: ").strip()
    if not input_id:
        print("No ID entered")
        return

    fetched_file = "fetched.json"
    archive_file = "archive.json"

  
    #Load or create archive.json
    
    if os.path.exists(archive_file):
        try:
            with open(archive_file, "r", encoding="utf=8") as f:
                archive_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            archive_data = []
    else:
        archive_data = []


    #check if ID is in archive.json
    if any(entry["ID"] == input_id for entry in archive_data):
        print("Already in archive.")
        return

    

    #Load fetched.json
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


###################################################################################################################################################

from All_Functions import display
import json
import os


def access_archive():

    archive_file = "archive.json"


    if os.path.exists(archive_file):
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

###################################################################################################################################################

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