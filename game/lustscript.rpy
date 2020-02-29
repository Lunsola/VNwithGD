# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Main")


# The game starts here.

label lustprebedroom:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg mainbedrm Commment out/Insert in Later

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show Main

    # These display lines of dialogue.

    "The grades from X Class have probably been released by now."
    #Need to figure out how to program a dramatic scroll and frame with grades
    menu:
        "Reaction?"

        "SCREAMS":
            "Your screaming prompts a confused inquiry from your roommate."
            jump roomie_bonding

        "Time to check social media for hot new memes, spicy takes and call out posts":
            jump social_media

        "Contact professor and inform them that you'll be coming in for a meeting":
            jump prof_email




label roomie_bonding:
r "Hey is everything okay?"
    menu:
        "Response"

        "Yeah. I'm just feeling really upset. I just got a bad grade on my test":
            r "I'm sorry that you're going through that right now. Things are going to work out.
            Remember grades don't matter in the grand scheme of things.
            There are going to be more grades and I'm here for you if you ever want a study budy!"
        "Breaks down crying"
            r "Oh no! Can I give you a hug?"
        "I'm fine. Don't worry about it":
            r "I'm here for you if ever need anything!"



label social_media:
    "Here lies the spiciest of the spicy memes"
    "This is premium"
    "Quality"
    "Content"

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

label prof_email:
    "Here lies potentially some interactive game play whose programming needs
    to be determined"
    menu:
        "ooption one":
            "feiorei;wvji"
            jump example
        "option two":
            "hey"
    "we're done with the menu"

label example:
    "oh hey we're on something new"

    # This ends the game.

    return
