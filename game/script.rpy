# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define r = Character("Marie")
define j = Character("Josh")
define b = Character("Maximillion")
define m = Character("Me")

#marie images
image marie neutral = "roomate_rabbit.png"
image marie happy = "roomate_smile_default.png"
image marie grateful = "roomate_natural_smile.png"
image marie surprised = "roomate_astonished.png"
image marie astonished = "roomate_very_astonished.png"
image marie confused = "roomate_extremely_astonished.png"
image marie ingenuine = "roomate_fake_smile.png"
image marie averse = "roomate_aversion.png"
image marie v happy = "roomate_big_smile.png"
image marie mad = "roomate_smiling_angry.png"
image marie nervous = "roomate_surprized.png"
image marie nervous2 = "roomate_sweating.png"


#max images
image max happy = "max happy.png"
image max neutral = "max neutral.png"
image max mad = "max mad.png"
image max breaking = "max breaking.png"
image max grateful = "max grateful.png"
image max skeptic = "max skeptic.png"
image max wink = "max wink.png"
image max vicious = "max vicious.png"
image max charm = "max charm.png"

#josh images
image josh bat = "josh_happy_propsize.png"
image josh grateful = "Neutral Grateful.png"
image josh v grateful = "Neutral v Grateful.png"
image josh sad = "Neutral Sad.png"
image josh shock = "Neutral Shock.png"
image josh stress = "Neutral Stress.png"
image josh wink = "Neutral Wink.png"
image josh happy = "Neutral Happy.png"
image josh wave = "wave happy.png"

#item images
image sandwich = "itsandwich.png"

#backgrounds
image bg classroom = "classroom.jpg"
image bg john jay = "jonathanjay.jpg"
image bg EC = "EC.jpg"
image bg themil = "library.jpg"

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

    #character tests show marie neutral at left
    #show max neutral at right
    #show josh happy

    #######################

    # init all variables here. Add in character relationship stats and flags as needed
    $ sin = 0 #positive is good morality, negative is bad?
    $ success = 0 #amount of quest points
    $ josh_friendship = 0 #josh friendship points
    $ maximillion_friendship = 0 #maximillion friendship points
    $ marie_friendship = 0 #marie friendship points
    $ josh_hasnumber = False #does player have josh's number?

    # These display lines of dialogue.

    # Name your character:
    $ pname = renpy.input("My name is:")
    # Code to use the name: "Oh hi, I'm %(pname)s"

    jump roommateintro

    # This ends the game.

    return
