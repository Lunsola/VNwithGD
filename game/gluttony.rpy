#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

label roommateintro:
    scene bg EC
    #play music "LimboDraftMarie.mp3"
    #play music "LimboDraftMain.mp3"
    "Okay, first weekend day with nothing on the agenda. Take a deep breath. I can do this."
    show marie happy
    with dissolve
    r "Hey, you excited to finally have a real day off? I can’t believe how tiring orientation was. Now we can finally really get to know each other with all this free time!"
    menu:
        "Yeah, I’d love that! Let’s hang out today.":
            $ marie_friendship +=1
            r "I was just about to say the same thing! I knew we were meant to be friends. Do you want to have lunch together today? I invited my OL to join me to thank him for being such an amazing tour guide!"
            m "Totally, let's do it!"
            hide marie happy
            show marie v happy at center,  hop
            r "Yay! I'm so excited!"
            jump rmeetjosh
        "I guess. We‘ll sure be spending a lot of time together.":
            hide marie happy
            show marie neutral
            r "Um, yeah, haha, I guess."
            r "So would you like to have lunch together today? I invited my OL to join me to thank him for being such an amazing tour guide!"
            menu:
                "Yeah, ok. Only if I get to pick the time.":
                    r "Oh, yeah no problem! I’m just happy you’re coming."
                    jump rmeetjosh
                "No offense, but that sounds really lame. I’m okay, thanks.":
                    hide marie neutral
                    show marie astonished
                    r "Oh my gosh, I didn’t even realize I was being lame! That’s so embarrassing. I’m so sorry, I won’t ask again."
                    m "Please don’t. I need my space."
                    #hide marie astonished
                    #show marie sad
                    $ marie_friendship -=1
                    hide marie astonished
                    m "Finally!"
                    jump rlonelyday
        "Don't say anything":
            "Ugh, this is awkward. I can literally hear crickets chirping. Is that in my head or do we actually have a cricket infestation?"
            #play sound "crickets.mp3"
            hide marie happy
            show marie neutral
            "..."
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
                    #hide marie neutral
                    #show marie v sad
                    r "Okay... {p=1.0}I’m sorry. I’ll leave you alone now."
                    $ marie_friendship -=1
                    hide marie anxious
                    m "Finally!"
                    jump rlonelyday

label rlonelyday:
    "Alone at last! This is good. My roommate is so annoying, can’t believe I’m stuck with her for a whole year. Yikes!"
    "Anyway, maybe I should head to the library today. Knock some work out now so I’ll be ahead by Monday. {p=1.0}Yeah. {p=1.0}That’s what I’ll do."
    scene bg themil
    "It’s so peaceful and quiet in here. I wonder where everyone is. Oh yeah, probably out socializing or whatever. It was such a good idea to come here on a quiet day!"
    show marie happy
    "Oh no, that’s Marie!"
    "Why is she here?"
    hide marie happy
    show marie happy at left
    show josh happy at right
    "Is her OL friend giving her ANOTHER tour? Jesus, what now?"
    menu:
        "Try to hide":
            "Quick, under the desk!"
            #insert crash sound
            "Oh crap, that was noiser than I thought it would be."
            r "%(pname)s is that you?"
            r "Why are you under the desk?"
            m "What? Oh, I...uh..."
            m "dropped something."
            m "Under the desk."
            m "And then I had to go down and find it."
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
            "You know what?"
            "No. {p=1.0}I have nothing to apologize for."
            "All I wanted was some peace and quiet. I’ll show her."
            "I’ll go get a great lunch at Shake Shack, {p=1.0}as a treat, {p=1.0}just for myself."
            "..."
            "..."
            r "Well, anyway, we’d better get going and let you study. Josh was just showing me around. See you later!"
            m "Yeah, see you!"
            "Whew, dodged a bullet there! Honestly, that could have gone worse. At least I didn’t yell at her or anything, right? Now...about that Shake Shack."
            #fade transition
            #show shake shack
            "Well, I had my Shake Shack. Smokestack double cheeseburger with fries, chicken tenders, and a birthday cake milkshake. It was delicious."
            "I have to admit though, it felt weird eating that huge meal all by myself. I kinda missed having company. But hey, I guess I’ll just have to get used to it."
            jump gluttonybeginday2

####### typed up to here

label rmeetjosh:
    scene bg john jay
    "Found the dining hall! First challenge of the day complete."
    show josh wave at right
    show marie happy at left:
        zoom .75
    "Oh, there they are. That guy sitting next to Marie is waving extremely vigorously at me. Those are windmill arms if I’ve ever seen them."
    hide josh wave
    with dissolve
    show josh happy at right
    hide marie happy
    with dissolve
    show marie happy at left
    m "Hey guys, what’s up?"
    hide marie happy
    show marie grateful at left
    r "Hi, %(pname)s! This is my friend, Josh."
    j "Hey bro. Groovy to meet you."
    m "Nice to meet you too. I’ll get some food and join you guys."
    #fade transition
    hide marie grateful
    with dissolve
    hide josh happy
    with dissolve
    #show dininghallfood
    "Wow, I really loaded up my plate. Gotta do a better job estimating portion sizes next time."
    #fade transition
    show marie grateful at left
    with dissolve
    show josh happy at right
    with dissolve
    r "So, Josh was just about to tell me what he’s studying."
    hide marie grateful
    show marie happy at left
    j "I’m a creative writing major bro. I’m all about that narrative arc and poetry stuff. But I’m also like super into football."
    hide josh happy
    show josh grateful at right
    j "That’s kinda how I got in actually, dude."
    hide josh grateful
    show josh happy at right
    hide marie happy
    show marie grateful at left
    r "That’s so cool!"
    hide marie grateful
    show marie happy at left
    r "What about you, %(pname)s?"
    m "Oh, well I haven’t nailed it down for sure yet. But I think my major is going to end up being"
    $ pmajor = renpy.input("")
    hide marie happy
    show marie v happy at left
    r "What a coincidence! I’m gonna be a %(pmajor)s major, too! I knew we were meant to be besties."
    menu:
        "Omg yes!!":
            m "We’re such perfect roommates for each other."
            $ marie_friendship +=1
            r "I know, right?"
        "Ok, hold on, that’s just a coincidence!":
            hide marie v happy
            show marie surprised at left
            m "I think we have a lot of differences as well as similarities."
            hide marie surprised
            show marie neutral at left
            r "Oh yeah, um, of course! I guess opposites attract!"
            hide marie neutral
            show marie happy at left
    j "Do you bros wanna ever cook together sometime? Dining hall food is pretty chill, but it can get old sometimes."
    r "I’m usually more of a baking gal, but I’d be up for giving cooking a try! Anything to spend time with my new friends."
    menu:
        "Well, I’m not really much of a cook.":
            m "I’ll let you guys do that without me."
            hide marie happy
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
    scene bg EC
    "Where did the weekend go? How is it Sunday already? Geez, I feel like I did nothing but eat. The freshman fifteen is real, folks."
    if josh_hasnumber == True:
        ##### look into a text system
        j "Yo %(pname)s, wanna have lunch together today? I’m hungry like a beast for some pizza."
        menu:
            "Yeah dude, name a dining hall!":
                $ josh_friendship +=1
                ##### transition
                scene bg john jay
                show josh wave
                "Geez, that man waves like his life depends on it. I see him already!"
                hide josh wave
                with dissolve
                show josh happy
                m "Hi, Josh!"
                j "Dude! Righteous to see you brah."
                m "You too, man. I’m hungry, let’s get food!"
                hide josh happy
                with dissolve
                ##### transition
                "Definitely got too much food. Am I really gonna finish all of this?"
                show josh happy
                with dissolve
                j "Woah, that pizza looks sick! Can I try some?"
                menu:
                    "Sure, I’ll cut you  a slice.":
                        $ josh_friendship +=1
                        j "Thanks, bro! I am stoked about this pizza."
                    "Gross, no!":
                        hide josh happy
                        show josh shock
                        j "Okay dude, chillax! I’ve got a lot of my own food anyway."
                    "Throw the pizza at him.":
                        # $ sin -=1
                        hide josh happy
                        show josh shock
                        j "Dude! That was the gnarliest thing I’ve ever seen anyone do! What just happened?"
                        menu:
                            "Play it off as a joke.":
                                $ josh_friendship +=1
                                hide josh shock
                                show josh happy
                                m "Haha, serves you right for asking for a piece of my food! I take food very seriously bro don’t you know?"
                                j "I can see that brah! That was pretty funny dude. Now no one can eat the pizza though."
                                m "Whatever. Worth it!"
                            "Get mad.":
                                m "You want to eat off my plate now? Really? God, isn’t it enough I’m having lunch with you? This is my first real meal today so back off."
                                j "Woah, hey, I didn’t mean--"
                                hide josh shock
                                show josh sad
                                m "I don’t care! I want my own pizza!"
                                j "I have some bad news on that front, bro. Your pizza’s pretty smashed."
                                hide josh sad
                                show josh shock
                                m "Just shut up okay? Let’s move on."
                                hide josh shock
                                show josh sad
                                j "Yeah, ok."
                                j "Huh, that was a weird moment."
                                menu:
                                    "Move the conversation along.":
                                        jump joshday2goodconvo
                                    "Sit in awkward silence.":
                                        jump joshday2awkconvo
    else:
        jump runintojosh

label joshday2goodconvo:
    hide josh sad
    show josh happy
    m "So how has your first week of classes been?"
    if josh_friendship > 0:
        j "It’s been ok."
        hide josh happy
        show josh stress
        j "To be honest, it can be hard sometimes to balance school and sports. I already have a lot of work to stay on top of."
        m "Already? Classes just started!"
        hide josh stress
        show josh sad
        j "I know man, but there’s just a lot going on in my life. You’ll get it when you’re further along here."
        hide josh sad
        show josh stress
        j "I feel like I’m always running from one thing to the next, you know? Plus I have work study, so that’s another thing, but I can never work as many hours as I should so I’m always short on cash."
        menu:
            "That sounds really hard. I’m sorry you’ve been so stressed.":
                $ josh_friendship +=1
            "Awkward silence.":
                "..."
        hide josh stress
        show josh sad
        j "Well anyway, we can move on."
        hide josh sad
        show josh happy
        j "Thanks for listening. I actually should head out now, my job starts soon."
        m "Ok! Let’s go."
        jump finishgluttony
    else:
        j "It’s been ok. It can be hard sometimes to manage school and sports, but I’m managing. How about you?"
        jump joshhowareyou

label joshhowareyou:
    menu:
        "It’s been all right.":
            pass
        "It’s been great! No complaints here.":
            pass
        "It’s been really overwhelming moving away from home.":
            jump joshhonesthours
    hide josh happy
    show josh v grateful
    j "Stoked to hear it! And what do you think of dining hall food?"
    hide josh v grateful
    show josh happy
    m "I love it! So much delicious food all in one place."
    j "Ha, well you might get tired of it this year."
    m "I doubt it! I haven’t eaten this much in one sitting in a really long time."
    j "Well I’m glad you like it so much. I gotta admit, the pizza here is killer. Anyway, I actually have to head out. My job starts soon."
    m "All right, I’m ready to go."
    jump finishgluttony

label joshday2awkconvo:
    j "So..."
    hide josh sad
    show josh happy
    j "how’s your first week of classes been?"
    jump joshhowareyou

label joshhonesthours:
    m "My week’s been okay, but I’ve been feeling kind of homesick."
    $ josh_friendship +=1
    hide josh happy
    show josh sad
    j "Bro, I know exactly how you feel. I felt that exact way when I first came. It’s a bummer,"
    hide josh sad
    show josh grateful
    j "but the good news is it gets better. You’re already over the gnarliest part."
    m "Well that’s good. This week has been a lot. I don’t know how I’m going to manage everything I have to do this year."
    hide josh grateful
    show josh happy
    j "Hey brah, if I can do school, a job, and every team sport at this school, then I bet you can do it."
    hide josh happy
    show josh wink
    j "I believe in you, brah, you got this."
    hide josh wink
    show josh happy
    m "Thanks, I appreciate that."
    j "Real sorry to cut this short brah but I actually have to head to my job now. You ready to go?"
    m "Yeah, let’s go."
    j "Cool, bro."
    hide josh happy
    show josh grateful
    j "And hit me up if you ever need anything."
    m "Okay man, I will."
    jump finishgluttony

label runintojosh:
    "Shake Shack again! Man it’s so convenient this place is so close to campus."
    "Let’s see...I’ll get a Chick’n Shack with fries, and maybe throw in a flat-top dog just for funsies."
    show josh shock
    j "Yo, %(pname)s! You’re here too?"
    hide josh shock
    show josh happy
    "Oh no. I have company."
    m "Hey Josh, how’re you?"
    j "I’m all right you know, brah. How you doin?"
    m "Just getting some lunch."
    j "Brah, what a coincidence! Me too! Hey, I have a sick idea--let’s eat together."
    "Well I guess I have no choice."
    m "Sure, let’s do it."
    "This food looks delicious. If only I could enjoy it in peace and quiet."
    j "So, bro, how’s your week been going? First real week of college, dude!"
    menu:
        "It's been all right":
            jump notclosetojosh
        "It's been great!":
            pass
        "It’s been a lot, but I’m getting through.":
            jump notclosetojosh
    j "I’m stoked to hear that dude. The first week can be a lot."
    m "Yeah, well, it’s been pretty good for me."
    j "Cool! So do you like dining hall food? I see you’re eating out already."
    m "I just like to switch things up. How’re you?"
    j "I’m pretty good. School and sports can be hard to balance, you know, but I’m figuring it out."
    m "That’s good to hear. I’ve been wondering how I’m going to manage everything, but if you can do both I can do it."
    j "Yeah dude, I’m, like, a veteran of this place. And I can tell you, you can do it."
    j "Anyway, I actually have to head to my job now. See you later!"
    m "See you!"
    "Well, that wasn’t so bad. At least I managed to be polite for five minutes. Thank god he had to go soon."

label notclosetojosh:
    j "Dude, I know how you feel. I felt that exact same way my first week. We all go through it and we all survive."
    m "Good to hear I’m not alone in this. I have been feeling a bit lonely these days, since I don’t really have any friends here yet."
    j "Brah, you have a friend. You have me."
    m "Thanks, Josh. I appreciate that."
    j "Listen, dude, I can’t stay long. I have to go to my job in a minute. But we should hang out later."
    menu:
        "Looking forward to it.":
            $ josh_friendship +=1
        "We'll see.":
            pass
    j "Rats, gotta run. Smell ya later!"
    jump finishgluttony
    return

label finishgluttony:
    "Finally taking the big step of eating dinner by myself. I’m so hungry, even after that big lunch. I hope no one thinks I’m a loser because I’m sitting alone."
    j "You again? No way brah, it’s me, Josh!"
    "Of course, Josh is here again. Is he following me or something?"
    m "Hey Josh, what’s up?"
    j "I’m good dude! Just coming from Dodge actually. Gotta keep fit!"
    "Yikes, that was not what I needed to hear right now. Have I had four meals today? I actually can’t remember. When was the last time I exercised? Definitely sometime this year, right?"
    j "How you doin?"
    m "Oh I’m pretty good. Pretty boring day today, all I’ve done is work."
    "Ha, that’s a lie. Pretty sure all I’ve done is eat."
    j "Me too, bro, me too. I only had time to break for lunch and then I went right back to the grind."
    #card decline sound
    j "Oh no. This is so embarrassing dude. I don’t have enough swipes."
    m "Darn, that’s annoying!"
    j "Shoot, what am I gonna do? Oh man, I was really counting on this swipe. I don’t know how I miscounted."
    "He really does look panicked. I wonder if he can afford to get food somewhere else.  But...this is my last swipe of the week. I only have one left."
    menu:
        "Give Josh your last swipe":
            $ josh_friendship +=3
            m "Here you can have my swipe. Don’t even worry about it."
            j "What? No I couldn’t take your swipe! You need to eat, too."
            m "Seriously, don’t worry. I’ve been meaning to try cooking for myself anyway. Maybe I’ll get Marie to help me. I definitely won’t starve!"
            j "Are you sure?"
            m "Absolutely! Take the swipe."
            j "Bro, thank you so much. You’re a good friend. I was about to have a total panic attack."
            m "You’re welcome. Enjoy your food."
            "Well, I’m walking away hungry but surprisingly otherwise ok. I did a good deed today, and that’s a pretty good feeling. Josh needs that swipe more than I do."
        "Don't offer":
            menu:
                "Just go in without him.":
                    $ josh_friendship -=2
                    j "Bye %(pname)s! Sorry I don’t get to join you."
                    "Yeesh, I feel kinda weird about that. Maybe I should’ve offered to give him my swipe? No, you know what, I deserve it. I’ve had a long day. I barely know him. I feel just fine about enjoying some food."
                "Sucks to suck, loser!":
                    m "Thank god I get to eat dinner alone after all."
                    if josh_friendship > 1:
                        j "Oh haha, um, bye %(pname)s. See you later I guess."
                        "Yikes, he looked like a kicked puppy. Where did that even come from? I’m always saying mean things without thinking about it. Is something wrong with me?"
                        "No, you know what, I’m fine. It’s not my fault he can’t take a joke! I’m gonna enjoy my food in peace."
                    elif josh_friendship = 1:
                        j "What? Bro, why would you say that to me?"
                        "Yikes, he looked like a kicked puppy. Where did that even come from? I’m always saying mean things without thinking about it. Is something wrong with me?"
                        "No, you know what, I’m fine. It’s not my fault he can’t take a joke! I’m gonna enjoy my food in peace."
                    elif josh_friendship = 0:
                        j "That wasn’t very nice, brah. I wouldn’t do you like that."
                        "Well that was extremely awkward. Hope I never run into him again. I’ve just gotta put it out of my mind and enjoy some food."
                    else:
                        j "You know what? Ever since you first met me you’ve been nasty to me. Do you have a problem with me? Say it to my face. Because I don’t think you’re a very nice person."
                        $ josh_friendship -=4
                        "Well, burned that bridge for sure. Just have to avoid him for the next three years until he graduates. On the bright side, at least he’ll leave me alone. Now...about that food. I’m starving."
    jump lust_start_dorm
