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
        f"{a['title'] - {a['published']}}" for a in articles
    ]

    menu_entries.append("Back")

    while True:
        TerminalMenu = TerminalMenu(
            menu_entries,
            title="Pick an article to open (ID will be copied)",
            cycle_cursor=True,
            clear_screen=True,
        )

        choice_index = TerminalMenu.show()

        if choice_index is None or choice_index == len(menu_entries) - 1:
            break

        selected_article = articles[choice_index]
        article_id = selected_article["ID"]
        article_link = selected_article["link"]

        pyperclip.copy(article_id)
        print(f"copied ID: {article_id} to clipboard!")

        webbrowser.open(article_link)

