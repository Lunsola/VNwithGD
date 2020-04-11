# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define r = Character("Marie")
define j = Character("Josh")
define b = Character("Maximillion")
define m = Character("Me")

#marie images
image marie neutral = "roomate_rabbit_propsize.png"
image marie anxious = "roomate_sweating_propsize.png"

#max images
image max happy = "Business_happy_propsize.png"

#josh images
image josh bat = "josh_happy_propsize.png"
image josh grateful = "Josh grateful.png"
image josh v grateful = "Josh grateful v2.png"
image josh sad = "Josh sad.png"
image josh surprised = "Josh shock happy.png"
image josh shock = "Josh shock.png"
image josh stress = "Josh stress.png"
image josh wink = "Josh wink.png"
image josh neutral = "Josh-neutral.png"

#item images
image sandwich = "itsandwich.png"

#backgrounds
image bg classroom = "classroom.jpg"
image bg john jay = "jonathanjay.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    ########################

    #these are all sprite tests between the hashes. Just ignore them

    #bg test scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #item test show sandwich

    #character sprite tests show marie neutral at left
    #show max happy at right
    #show josh neutral

    #######################

    # init all variables here. Add in character relationship stats as needed
    $ sin = 0 #positive is good morality, negative is bad?
    $ success = 0 #amount of quest points
    $ josh_friendship = 0 #josh friendship points
    $ maximillion_friendship = 0 #maximillion friendship points
    $ marie_friendship = 0 #marie friendship points

    # These display lines of dialogue.

    # Name your character:
    $ pname = renpy.input("My name is:")
    # Code to use the name: "Oh hi, I'm %(pname)s"

    jump roommateintro

    # This ends the game.

    return
