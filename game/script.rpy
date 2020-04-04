# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define r = Character("Marie")
define j = Character("Josh")
define b = Character("Maximillion")
define m = Character("Me")

#Declare images here
image marie neutral = "roomate_rabbit_propsize.png"
image marie anxious = "roomate_sweating_propsize.png"
image max happy = "Business_happy_propsize.png"
image josh happy = "josh_happy_propsize.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show marie neutral at left
    show max happy at right
    show josh happy

    # init all variables here. Add in character relationship stats as needed
    $ sin = 0 #positive is good morality, negative is bad?
    $ success = 0 #amount of quest points
    $ josh_friendship = 0 #josh friendship points
    $ maximillion_friendship = 0 #maximillion friendship points
    $ marie_friendship = 0 #marie friendship points

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Your current stats are %(sin)s"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "ooption one":
            "feiorei;wvji"
            jump example
        "option two":
            "hey"
    "we're done with the menu"

label example:
    "oh hey we're on something new"

    jump roommateintro

    # This ends the game.

    return
