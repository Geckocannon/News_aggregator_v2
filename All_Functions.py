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
        choice = show_menu(["The Hacker News", "Threat Post", "Google Threat Intelligence", "Bleeping Computer", "Krebs on Security", "Back"],
        "Pick a News Outlet: ")

        if choice == "The Hacker News":
            print("Fetching The Hacker News from the last 3 days")
            fetch_THN()

        elif choice == "Threat Post":
            print("Threat Post news from the last 3 days")
            fetch_TP()
        
        elif choice == "Google Threat Intelligence":
            print("Google Threat Intelligence news from the last 3 days")
            fetch_GTI()
        
        elif choice == "Bleeping Computer":
            print("Bleeping Computer from the last 3 days")
            fetch_BC()
        
        elif choice == "Krebs on Secuirty":
            print("Bleeping Computer news from the last 3 days")
            fetch_KoS()

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
from datetime import datetime, timedelta

def fetch_THN(url, days=3, cache_name="THN_cache", cache_expire=600, timeout=10):

    url = "https://feeds.feedburner.com/TheHackersNews"
    requests_cache.install_cache(cache_name, expire_after=cache_expire)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching THN feed: {e}")
        return[]
    
    feed = feedparser.parse(response.content)


    cutoff = datetime.utcnow() - timedelta(days=days)
    recent_articles = []

    list_of_dicts = []
    for entry in feed.entries:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_time = datetime.fromtimestamp(time.mktime(entry.published_parsed))
        elif "updated_parsed" in entry and entry.updated_parsed:
            published_time = datetime.fromtimestamp(time.mktime(entry.updated_parsed))

        if published_time and published_time >= cutoff:
            title = entry.get("title", "No title found")
            link = entry.get("link", "No link found")
            recent_articles.append({
                "ID": mashthis(title, link),
                "title": title,
                "summary": entry.get("summary", "No summary found"),
                "link": link,
                "published": published_time.strftime("%y-%m-%d %H:%M:%S")
            })
        return recent_articles