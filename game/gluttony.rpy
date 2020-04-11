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
            #hide marie neutral
            #show marie excited
            r "Yay! I'm so excited!"
            jump rmeetjosh
        "I guess. We‘ll sure be spending a lot of time together.":
            hide marie neutral
            show marie anxious
            r "Um, yeah, haha, I guess. So would you like to have lunch together today? I invited my OL to join me to thank him for being such an amazing tour guide!"
            menu:
                "Yeah, ok. Only if I get to pick the time.":
                    r "Oh, yeah no problem! I’m just happy you’re coming."
                    jump rmeetjosh
                "No offense, but that sounds really lame. I’m okay, thanks.":
                    #hide marie anxious
                    #show marie surprised
                    r "Oh my gosh, I didn’t even realize I was being lame! That’s so embarrassing. I’m so sorry, I won’t ask again."
                    m "Please don’t. I need my space."
                    #hide marie surprised
                    #show marie sad
                    $ marie_friendship -=1
                    hide marie anxious
                    m "Finally!"
                    jump rlonelyday
        "Don't say anything":
            "Ugh, this is awkward. I can literally hear crickets chirping. Is that in my head or do we actually have a cricket infestation?"
            #play sound "crickets.mp3"
            hide marie neutral
            with dissolve
            show marie anxious
            r "Um, yeah"
            r "So anyway... {p=1.0}I was wondering if you wanted to come to lunch today. I’m having lunch with my OL. It would be fun to bring a friend."
            menu:
                "Yeah, whatever. I guess I need to eat lunch anyway.":
                    r "Yay! Thanks so much for coming with me. To be honest, I’m kind of nervous. I’ve never been alone with my OL before."
                    m "Well, now you won’t be. Let’s go, I don’t have all day."
                    jump rmeetjosh
                "Who said we were friends?":
                    r "Oh! I don’t know, I thought...{p=1.0}I thought..."
                    m "I barely even know you! Why would I call you my friend?"
                    m "Obviously, you thought wrong."
                    #hide marie anxious
                    #with dissolve
                    #show marie sad
                    r "Okay... {p=1.0}I’m sorry. I’ll leave you alone now."
                    $ marie_friendship -=1
                    hide marie anxious
                    m "Finally!"
                    jump rlonelyday

label rlonelyday:
    "Alone at last! This is good. My roommate is so annoying, can’t believe I’m stuck with her for a whole year. Yikes!"
    "Anyway, maybe i should head to the library today. Knock some work out now so I’ll be ahead by Monday. {p=1.0}Yeah. {p=1.0}That’s what I’ll do."
    #scene bg library
    "It’s so peaceful and quiet in here. I wonder where everyone is. Oh yeah, probably out socializing or whatever. It was such a good idea to come here on a quiet day!"
    #show marie happy
    "Oh no, that’s Marie! Why is she here? Is her OL friend giving her ANOTHER tour? Jesus, what now?"
    menu:
        "Try to hide":
            "Quick, under the desk! Oh crap, that was noiser than I thought it would be."
            r "%(pname)s is that you?"
            r "Why are you under the desk?"

    return

    ####### typed up to here

label rmeetjosh:
    scene bg john jay
    "Found the dining hall! First challenge of the day complete."
    "Oh, there they are. That guy sitting next to Marie is waving extremely vigorously at me. Those are windmill arms if I’ve ever seen them."
    m "Hey guys, what’s up?"
    menu: ##### you need to update everything below here
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

    return

##label gluttonyscene_1:
    ##"just start writing text"
    ##if conditionupon:
        ##jump conditionupon
    ##else:
        ##jump secondoption

##label conditionupon:
