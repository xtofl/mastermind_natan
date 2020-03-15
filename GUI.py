

from tkinter import (Button,
                     Canvas,
                     FLAT,
                     NW,
                     Tk,
                     Label,
                     messagebox)

import MasterMindAsked
import random

ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")
random_combination = []
NUMBER_OF_CIRCLES = 4
MAX_NUMBER_OF_MOVES = 10
current_move = 0
guess_combination = []
canvas = ""
ovals = []
matching_position_label = ""
correct_color_label = ""


def draw_board(root):

    """
      Create the graphical user interface.
    """

    # provide the title that will be shown in the header
    root.title("Mastermind")

    # Indicate which variables of the program will be altered
    # ! In order to manipulate variables that are part of the program
    # ! but exist outside of the function, you need to indicate that you want
    # ! to use and alter these variables by declaring them as "global"
    global canvas, ovals, matching_position_label, correct_color_label

    # canvas will be the main board used for mastermind
    # ! to create a canvas, the constructor is called
    # ! (i.e. name of the class and required parameters)
    canvas = Canvas(root, bg="white", height=MAX_NUMBER_OF_MOVES*40+170, width=NUMBER_OF_CIRCLES*50+100)

    # Draw the empty circles representing the guesses
    ovals = MasterMindAsked.create_empty_circles(canvas, NUMBER_OF_CIRCLES, MAX_NUMBER_OF_MOVES)

    # Draw a line to separate the circles form the buttons
    canvas.create_line(NUMBER_OF_CIRCLES*50, 10, NUMBER_OF_CIRCLES*50, 400, width=3, fill="black")

    # Draw the color buttons that will be used throughout the game
    # ! Every available color (listed here as strings in the global variable
    # ! ALL_COLORS) is represented in the GUI by a button
    # ! when the user clicks the button the function color(color_name)
    # ! is called
    for i in range(len(ALL_COLORS)):
        canvas.create_window(NUMBER_OF_CIRCLES*50+10, 20+i*45, anchor=NW, window=Button(canvas, command=lambda color_name=ALL_COLORS[i]: color(color_name), width=5, text=ALL_COLORS[i]))

    # Draw the result labels
    # ! matching_position_label and correct_color_label can be used later on
    # ! to show the user the number of correct positions and colors
    # ! (e.g. matching_position_label["text"] = "2")
    canvas.create_window(50, MAX_NUMBER_OF_MOVES*40+30, anchor=NW,
                         window=Label(canvas, text="Correct position: "))
    matching_position_label = Label(canvas)
    canvas.create_window(200, MAX_NUMBER_OF_MOVES*40+30, anchor=NW, window=matching_position_label)

    canvas.create_window(50, MAX_NUMBER_OF_MOVES*40+60, anchor=NW,
                         window=Label(canvas, text="Correct color: "))
    correct_color_label = Label(canvas)
    canvas.create_window(200, MAX_NUMBER_OF_MOVES*40+60, anchor=NW, window=correct_color_label)

    # Draw the submit button
    # ! when the user clicks the button,
    # ! the function check_combination is called
    submit_button = Button(canvas, text="Check", command=check_combination)
    submit_button.configure(width=10, relief=FLAT)
    canvas.create_window(50, MAX_NUMBER_OF_MOVES*40+90, anchor=NW, window=submit_button)


    # Draw the quit button
    quit_button = Button(canvas, text="Quit", command=root.destroy)
    quit_button.configure(width=5, relief=FLAT)
    canvas.create_window(200, MAX_NUMBER_OF_MOVES*40+130, anchor=NW, window=quit_button)

    #Draw the sublist button
    sublijst_button = Button(canvas, text="Sublijst", command=check_sublijst)
    sublijst_button.configure(width=5, relief=FLAT)
    canvas.create_window(25, MAX_NUMBER_OF_MOVES*40+130, anchor=NW, window=sublijst_button)

    # Draw the hint button
    hint_button = Button(canvas, text="Hint", command=hint)
    hint_button.configure(width=5, relief=FLAT)
    canvas.create_window(95, MAX_NUMBER_OF_MOVES * 40 + 130, anchor=NW, window=hint_button)

    # draw the canvas
    canvas.pack()



def check_combination():

    """
      Check the current guess combination.
      If the guess combination is complete, the method increments the
      number of moves, it displays the number of correct colors on
      their position and the number of correct colors not on their
      position in the user interface, and it cleans the guess combination.
      If the guess combination is not complete, the method displays
      an error message.
    """

    global current_move, guess_combination

    # check if a complete combination is provided
    if len(guess_combination) < 4:
        messagebox.showerror("Error!", "Please fill in a complete combo before hitting the 'Check' button!")
    else:
        current_move = current_move + 1
        nb_black_white_matches = MasterMindAsked.get_nb_black_white_matches(random_combination, guess_combination)
        # print(nb_black_white_matches)
        matching_position_label["text"] = str(nb_black_white_matches[0])
        correct_color_label["text"] = str(nb_black_white_matches[1])
        if nb_black_white_matches[0] == NUMBER_OF_CIRCLES:
            messagebox.showinfo("Congratulations", "You have won the game")
            root.destroy()
        else:
            check_game_over()
            guess_combination = []


def check_sublijst():
    global current_move, guess_combination, ovals

    if len(guess_combination) == 0:
        messagebox.showerror("Error!", "please fill in at least one color before hiiting the \"Sublijst\" button!")
    else:
        if MasterMindAsked.is_sublist_of(guess_combination, random_combination) == True:
            messagebox.showinfo("Juist!", "Dit is een sublijst!")
        else:
            messagebox.showinfo("Fout!", "Dit is geen sublijst!")
    guess_combination = []
    ovals = [[canvas.create_oval(10 + 40 * i, 10 + 40 * current_move, 40 + 40 * i, 40 + 40 * current_move, fill='grey') for i in
              range(4)]]

teller = 0
def hint():
    global teller, random_combination
    import random
    if teller != 0:
        messagebox.showerror("Error!", "Je hebt je hint dit spel al gebruikt!")
    else:
        a = random.randint(1,4)
        messagebox.showinfo("Hint", "De "+str(a)+"de kleur is "+random_combination[a-1])
    teller += 1






def check_game_over():

    """
      Display a message that the game is over, if the number of moves
      has reached the maximum number of moves.
    """

    global current_move

    if current_move == MAX_NUMBER_OF_MOVES:
        game_over_message = "Game Over! You have lost the game."
        solution = ", ".join(str(x) for x in random_combination)
        solution_message = "The correct combination was:\n" + solution
        ending_message = game_over_message + "\n" + solution_message
        messagebox.showinfo("Game over", ending_message)
        root.destroy()



# color callback function
def color(color_name):

    """
      Add the given color to the guess combination. The corresponding circle
      in the display is also filled with the color. If the guess combination is
      complete, an error message is displayed.
    """

    if len(guess_combination) == NUMBER_OF_CIRCLES:
        messagebox.showerror("Colors are full", "No more colors allowed, please hit the 'Check' button to check your result")
    else:
        canvas.itemconfig(ovals[current_move][len(guess_combination)],
                          fill=color_name)
        guess_combination.append(color_name)



root = Tk()
draw_board(root)
random_combination = MasterMindAsked.create_combination(NUMBER_OF_CIRCLES)
root.mainloop()