#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

label roommateintro:
    "Okay, first weekend day with nothing on the agenda. Take a deep breath. I can do this."
    show marie neutral
    r "Hey, you excited to finally have a real day off? I can’t believe how tiring orientation was. Now we can finally really get to know each other with all this free time!"
    menu:
        "Yeah, I’d love that! Let’s hang out today.":
            $ marie_friendship +=1
            r "I was just about to say the same thing! I knew we were meant to be friends. Do you want to have lunch together today? I invited my OL to join me to thank him for being such an amazing tour guide!"
            m "Totally, let's do it!"
            show marie anxious
            r "Yay! I'm so excited!"
        "I guess. We‘ll sure be spending a lot of time together.":
            pass
            #roommate response
        "Don't say anything":
            pass
            #dialogue box goes away and cricket sound effect
    r "By the way, do you want to have lunch together today? I invited someone I met in class and I’d love for you to join."
    menu:
        "Yeah! Sounds fun, I love meeting new people.": #friendship +1
            #roommate response
            jump rlunchmeetjock
        "No thanks.":
            pass
            #roommate response
        "Don't feel like it, no":
            pass
            #roommate response

label rlunchmeetjock:
    "A boy at one of the tables waves enthusiastically at you when you walk into the dining hall."
    "Hey, you must be Roommate's roommate. I’m Jock, groovy to meet you." #please insert names
    menu:
        "Whatever, I'm hungry.": #-1 jock friendship
            $ josh_friendship -= 1
            pass
        "Nice to meet you, too! I'm (name var).":
            $ josh_friendship += 1
            pass
    "The three of you quickly get up to embark on your mission of self nourishment."
    #some more filler?
    "Your last stop is at the pizza station."
    "And lucky you! There's just the one slice left!"
    "As you reach for it, you notice Josh beelining over out of the corner of your eye."
    "His plate is piled impossibly full with spaghetti."
    "Josh stop next to you and peeks around the mountain of spaghetti. He notices all the pizza is gone"

##label gluttonyscene_1:
    ##"just start writing text"
    ##if conditionupon:
        ##jump conditionupon
    ##else:
        ##jump secondoption

##label conditionupon:
