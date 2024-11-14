# Part II - rock-paper-scissors.py

#     rock-paper-scissors.py : create 3 functions
#         get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
#         The possibles choices are : Play a new game or Show scores or Quit

#         print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.


#         Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.

#         main() - the main function. It should take care of 3 things:
#             Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

#             When the user chooses to play a game:
#                 Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
#                 Remember the results of every game that is played.

#             When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.

from game import Game


def get_user_menu_choice():
    """
    this should display a simple menu *fingers crossed*
    """
    print("\nMenu")
    print("(g) Play a new game")
    print("(b) to show scores")
    print("(x) or (q) to quit")
    user_choice = input(":").lower()
    if user_choice in ["g", "b", "x", "q"]:
        return user_choice
    else:
        print("invalid choice")
        return get_user_menu_choice()  # allows retrying input


def print_results(results_dict):
    """
    this should print the results of the games played *fingers crossed*
    """
    print("\n    Game Results:")
    print(f"      You won {results_dict["win"]} times")
    print(f"      You lost {results_dict["loss"]} times")
    print(f"      You deaw {results_dict["draw"]} times")


def main():
    """
    the main function, sort of
    """
    results_dict = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "g":
            game = Game() # Create a new Game object 
            result = game.play()
            results_dict[result] += 1
        elif choice == "b":
            print_results(results_dict)
        elif choice == "x" or choice == "q":
            print_results(results_dict)
            print("    Thank you for playing!")
            break


main()
