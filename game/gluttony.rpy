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
    "Oh no, that’s Marie!"
    "Why is she here?"
    #hide marie happy
    #show marie happy at left
    show josh happy at right
    "Is her OL friend giving her ANOTHER tour? Jesus, what now?"
    menu:
        "Try to hide":
            "Quick, under the desk!"
            #insert crash sound
            "Oh crap, that was noiser than I thought it would be."
            r "%(pname)s is that you?"
            r "Why are you under the desk?"
            m "What? Oh, I...uh...{p=1.0}dropped something. Under the desk. And then I had to go down and find it."
            r "Looks like you’ve dropped a lot of stuff now! Here, let us help you."
            r "%(pname)s, this is my friend, Josh. He was my OL during NSOP."
            j "Hey %(pname)s. It’s so groovy to meet you. Marie told me some about you already!"
            jump libraryjmcont
        "Say hi.":
            m "Hey Marie, what’s up?"
            r "Oh my gosh, %(pname)s! I didn’t know you’d be here, I promise. Josh was just showing me around."
            m "Oh, yeah, it’s fine. It’s not that exciting though."
            r "I guess I’m just a nerd, I like libraries! That’s just me though."
            j "Nah dude. I frickin love libraries. I get amped just walking in and smelling all those books. There’s nothing like the smell of a new book."
            "Why is he talking about books so weirdly? I’ve never heard someone talk about liking books because of smells. Weirdo."
            j "Anyway, bro, nice to meet you. I’m Josh, you must be %(pname)s. Marie’s told me a little about you."
            jump libraryjmcont

label libraryjmcont:
    m "Oh, um, good things I hope?"
    r "Of course! What bad thing could I possibly say about you?"
    "Oof. Seems like she doesn’t remember this morning? Or maybe she’s just too polite to mention it. Should I bring it up?"
    menu:
        "Apologize for earlier":
            m "Hey, so listen, I’m sorry if I snapped at you this morning. That didn’t go how I wanted it to. Can we move on and be friends again?"
            r "Oh don’t even mention it! I totally get it. I’ve been so tired lately too. It can be so hard to be around people constantly."
            j "Yeah dude. I totally vibe with that. I get so frickin tired of being around my roommate all the time that sometimes I just get so aggro it’s crazy."
            hide josh happy
            show josh wink at right
            j "It’s all part of the experience."
            m "Can I catch you guys for lunch some other time? It’s a shame I missed today."
            j "Of course, bro! Anytime. Give me your number and I’ll text you sometime."
            $ josh_hasnumber = True
            r "Anyway, Josh was just showing me around. I’ll leave you alone to study now. I’m so glad we ran into you!"
            jump gluttonybeginday2
        "Don't bring it up.":
            "You know what? No. I have nothing to apologize for. All I wanted was some peace and quiet. I’ll show her. I’ll go get a great lunch at Shake Shack, just for myself."
            "..."
            "..."
            r "Well, anyway, we’d better get going and let you study. Josh was just showing me around. See you later!"
            m "Yeah, see you!"
            "Whew, dodged a bullet there! Honestly, that could have gone worse. At least I didn’t yell at her or anything, right? Now...about that Shake Shack."
            #fade transition
            #show shake shack
            "Well, I had my Shake Shack. Smokestack double cheeseburger with fries, chicken tenders, and a birthday cake milkshake. It was delicious."
            "I have to admit though, it felt weird eating that huge meal all by myself. I kinda missed having company. But hey, I guess I’ll just have to get used to it."

####### typed up to here

label rmeetjosh:
    scene bg john jay
    "Found the dining hall! First challenge of the day complete."
    show josh wave at right
    #show marie happy at left
    "Oh, there they are. That guy sitting next to Marie is waving extremely vigorously at me. Those are windmill arms if I’ve ever seen them."
    hide josh wave
    show josh happy at right
    m "Hey guys, what’s up?"
    r "Hi %(pname)s! This is my friend, Josh."
    j "Hey bro. Groovy to meet you."
    m "Nice to meet you too. I’ll get some food and join you guys."
    #fade transition
    #hide marie happy
    hide josh wave
    #show dininghallfood
    "Wow, I really loaded up my plate. Gotta do a better job estimating portion sizes next time."
    #fade transition
    #show marie happy at left
    show josh happy at right
    r "So, Josh was just about to tell me what he’s studying."
    j "I’m a creative writing major bro. I’m all about that narrative arc and poetry stuff. But I’m also like super into football."
    hide josh happy
    show josh grateful at right
    j "That’s kinda how I got in actually, dude."
    hide josh grateful
    show josh happy at right
    r "That’s so cool! What about you, %(pname)s?"
    m "Oh, well I haven’t nailed it down for sure yet. But I think my major is going to end up being"
    $ pmajor = renpy.input("")
    r "What a coincidence! I’m gonna be a %(pmajor)s major too! I knew we were meant to be besties."
    menu:
        "Omg yes!!":
            m "We’re such perfect roommates for each other."
            $ marie_friendship +=1
            r "I know, right?"
        "Ok, hold on, that’s just a coincidence!":
            m "I think we have a lot of differences as well as similarities."
            r "Oh yeah, um, of course! I guess opposites attract!"
    j "Do you bros wanna ever cook together sometime? Dining hall food is pretty chill, but it can get old sometimes."
    r "I’m usually more of a baking gal, but I’d be up for giving cooking a try! Anything to spend time with my new friends."
    menu:
        "Well, I’m not really much of a cook.":
            m "I’ll let you guys do that without me."
            #hide marie happy
            show marie neutral at left
            r "Aw, ok. I understand."
        "Are you kidding me?":
            m "I literally just got here. You think I’m gonna be wasting time NOT eating dining hall food? No thanks."
            $ josh_friendship -=1
            hide josh happy
            show josh shock at right
            j "Chillax bro, just thought it might be a fun idea. Whatever floats your boat my dude."
            hide josh shock
            show josh happy at right
        "I’ve never cooked much before, but I’m down to try anything!":
            m "I'll definitely join in!"
            r "Yay! It’s going to be so much fun!"
    j "You know what, bros? This has been really frickin baller."
    hide josh happy
    show josh grateful at right
    j "You guys are so frickin cool. I’m so glad I met you."
    hide josh grateful
    show josh sad at right
    j "I’ve been at this school a whole year and believe it or not bro, it’s been tough for a dude like me to make friends."
    hide josh sad
    show josh happy at right
    j "Can I get your numbers so I can hit you up for meals and stuff?"
    menu:
        "Sure thing!":
            hide josh happy
            show josh grateful at right
            $ josh_hasnumber = True
            hide josh grateful
            show josh happy at right
        "Um, actually, I don’t really like to give my number out.":
            hide josh happy
            show josh sad at right
            j "Oh, ok."
    r "Wow, time flies when you’re having fun! I actually have to go now. Want to head out together?"
    j "Yeah man, time to bail. This was a fun idea, thanks for the invite, Marie."
    jump gluttonybeginday2

label gluttonybeginday2:
    return
