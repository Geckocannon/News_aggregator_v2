from simple_term_menu import TerminalMenu

def show_menu(options, title):

    """
    Define our function. For now I see no point in passing arguements like options to it because I know what I want my menu to feature.
    So I can hard code these options into the function.
        Update: we do want to pass arguments to this function because it will be reused in nested menus which change options

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
       
