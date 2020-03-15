# The definition of ALL_COLORS is repeated here. That repitition can
# be avoided, but it would lead us to far at this point.
ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")


def get_nb_black_white_matches(given, guess):
    white_matches = 0
    black_matches = 0
    given2 = list.copy(given)
    guess2 = list.copy(guess)
    for i in range(len(guess2)):
        if guess2[i] == given2[i]:
            black_matches += 1
            given2[i] = ""
            guess2[i] = "_"
    for i in range(len(guess2)):
         if given2.count(guess2[i]) > 0 and guess2[i] != given2[i]:
             white_matches += 1


    return black_matches,white_matches


    """ Return the number of black and white matches of the guessed
    combination with respect to the given combination. The first
    element in the resulting tuple reflects the number of correct colors
    on their positions (black matches). The second element reflects
    the number of correct colors not on their position (white matches)."""


def create_combination(nb_elements):
    import random
    combo = []
    for i in range(nb_elements):
        combo.append(ALL_COLORS[random.randint(0,5)])
    print(combo)
    return combo
    """ Return a random combination involving the number of elements."""


# ! on the board, each row will consist of 4 circles representing 1 guess
# ! in total 10 rows should be drawn (as the user is given 10 guesses)
# ! You can create a circle by using the function:
# !     canvas.create_oval(x0, y0, x1, y1)
# ! It takes two pairs of coordinates: the top left and bottom right
# ! corners of the bounding rectangle. The (0,0) point is located in the
# ! top left corner of the canvas. We assume that each bounding square has
# ! a size of 30x30 and that all the circles are separated by 10 pixels
# ! from each other, and from the border (see picture in assignment).
# ! For example, the method call (with actual parameters) that generates
# ! the second circle of the third guess will look like:
# !         canvas.create_oval(50, 90, 80, 120)
# ! Later on in the program we modify the ovals to change color depending on
# ! the color that is selected by the person playing.
# ! In order to easily retrieve the correct oval, we expect that the function
# ! you implement here returns a nested list (i.e. a matrix) of
# ! the following form:
# !         [[circle1_guess1, circle2_guess1, ...],
# !          [circle1_guess2, ...],
# !          ...,
# !          [circle4_guess10]]
# ! The second circle of the third guess would for example be stored at:
# !          ovals[2][1] = canvas.create_oval(50, 90, 80, 120)
# ! Instead of approaching the nested list as a matrix, you can also
# ! treat it as a list of lists
# !          e.g. ovals[2].append(...)
# ! Note that the method create_oval has an implementation that
# ! takes 5 parameters. The fifth parameter has name 'fill' and allows
# ! you to assign a color (as a string) to it.
# ! Make sure that all the circles you draw get the fill color "grey".
def create_empty_circles(canvas, number_of_circles, max_number_of_moves):
    ovals =[[canvas.create_oval(10 + 40*i,10+40*j, 40 + 40*i, 40+40*j,fill='grey') for i in range(number_of_circles)] for j in range(max_number_of_moves)]
    return ovals




    """ Return a matrix containing grey ovals that are correctly initialized
        at their required location."""


###############################################################################
# EXTRA

def any_color_in_combination(colors, given):
    for i in colors:
        teller = 0
        if given.count(i) > 0:
            teller += 1
    if teller > 0:
        return True
    else:
        return False

    """ Returns true if at least one color in colors is part of the
    given combination. False otherwise."""


def all_colors_in_combination(colors, given):
    z = 0
    for i in colors:
        if given.count(i) > 0:
            z += 1
    if z == len(colors):
        return True
    else:
        return False


    """ Returns true if all the colors in colors are part of the
    given combination. False otherwise."""


def is_sublist_of(sublist, given):
    teller = 0
    for i in range(len(given)):
        if given == given[0:i] + sublist + given[i+len(sublist):]:
            teller += 1
        else:
            pass
    if teller == 0:
        return False
    else:
        return True







    """ Returns whether the sublist is part of the given combination.
    The order of the sublist must also correspond to the order of the
    corresponding part in the given combination."""