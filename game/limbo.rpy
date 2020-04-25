#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

##transforms to add to script beginning:

label limbobegin:
    m "That was a lot of names to hear at once."
    k "Don’t sweat it! You’re still a new student, so it’s understandable to have some names mixed up."
    m "Yeah, I guess so."
    k "So you doing anything special this weekend? I can’t have any of my orientation kids be loners their first weekend here!"
    m "I still don't know."
    k "Lots of people are hosting cool events and they usually get posted on there."
    k "Oh, shit, I have a meeting! I’ll catch you later, %(pname)s."
    k "Don’t be a loner!"
    "Well, that last part was unnecessary"
    "Hmm, what's this?"
    "I guess I don’t have anything else going on Saturday night."
    "Wait a second…"
    "There’s a registration list? And it’s past the deadline. Of course it is."
    "Still, maybe a bunch of people signed up and aren’t gonna end up going. I’ll go anyway and see if I can find my way inside."
    #transition
    "What’s this crowd, is it for the party?! There must be at least 50 people trying to get in! I wasn’t expecting it to be this popular…"
    "I might not be able to just get in like I’d hoped."
    #transition
    "After waiting for around 15 minutes, I get to the front. There’s a student with a piece of paper letting people in. The door is open."
    "He turns to me."
    w "Hey, what's your name?"
    m "%(pname)s."
    w "Hmmm.... I don't see you on the list, %(pname)s"
    m "Really? That's weird. Can you check again?"
    "I'm not on the list. I know that."
    "But wait, I think I spot a familiar face through the door."
    "Is that Karen? Maybe she can help me get in!"
    w "Nope, not on the list this time either."
    "It’s a long shot, but I think if I say I’m with Karen and call her over, she might cover for me and help me get inside."
    "On the other hand, it’s a little unfair for everyone else who’s been waiting for a long time."
    "I have to act now. What should I do?"
    menu:
        "Leave the party":
            "I don’t want to put her on the spot like that."
            "Plus, it’s not really fair to the people already on the list. I might as well go do something else with my night."
            m "Oh, ok."
            w "Yeah, so I can't let you in. Sorry."
        "Call Karen over":
            pass
