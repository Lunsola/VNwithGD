#define e = Character("Main")
define p = Character("Professor ")
# The game starts here.

label lust_start_dorm:


    #scene mainbednit

    #show Main

    #Variables to be used
    $ prof_email = False
    #For below, make sure stats are defined somewhere in renpy
    #requires roomie friendship points
    #requires professor friendship points
    #goal progress points
    #morality points
    "The grades from X Class have probably been released by now."
    #Need to figure out how to program a dramatic scroll and frame with grades
    menu:
        "SCREAMS":
            "Your screaming prompts a confused inquiry from your roommate."
            jump roomie_bonding

        "Time to check social media for hot new memes, spicy takes and call out posts":
            jump social_media

        "Contact professor and inform them that you'll be coming in for a meeting":
            $prof_email = True
            jump prof_email

label roomie_bonding:
    r "Hey is everything okay?"
    menu:
        "Yeah. I'm just feeling really upset. I just got a bad grade on my test":
            r "I'm sorry that you're going through that right now. Things are going to work out.
            Remember grades don't matter in the grand scheme of things.
            There are going to be more grades and I'm here for you if you ever want a study budy!"
        "Breaks down crying":
            r "Oh no! Can I give you a hug?"
            menu:
                "Accepts Hug":
                    pass #Art? O .o
                "No thanks":
                    pass
                "I'd rather not":
                    pass
        "I'm fine. Don't worry about it":
            r "I'm here for you if ever need anything!"



label social_media:
    "Here lies the spiciest of the spicy memes"
    "This is premium"
    "Quality"
    "Content"


label prof_email:
    "Here lies potentially some interactive game play whose programming needs
    to be determined"
"Man what an emotional rollercoaster. I should head to sleep now"

#fade scene mainbedmorn
"Ah!!! It's already 9 am. Time do get up"

#Option to interact with phone
#if(email=true)
#first notification- meeting with professor
#else-club fair today
 #friend text:"Hey let's go out"
 #email notification subject line: dress business casual for club meeting today!

#option to interact and select an outfit

#fade scene hallway
menu:
    "Go to Club Fair":
        jump club_fair
    "Find Professor":
        jump prof_meet
    "Go out with Friend!":
        jump friend_party
label club_fair:
    menu:
        "Time to make some big boi connections":
            pass
        "Time to make some new friends!":
            pass
        "Eww social interaction. Time to cry":
            pass
label prof_meet:
    if prof_email == True:
        #scene prof office
        "Oh boy, time to defend my GPA's honor"
    else:
        "Nice! Caught Professor X before they left their office"
        #scene prof hallway
label friend_party:
    menu:
        "Challenge Friend to SMASH ULTIMATE DEATH MATCH":
            pass
        "Talk to mysterious stranger in the sweater vest":
            pass
        "Speak with friend":
            pass
