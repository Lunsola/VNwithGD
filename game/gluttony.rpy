#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

image marie cry = "roomate_sad_2.png"
image bg shakeshack = "shakeshack.jpeg"
image bg john jay inside = "johnjayinside.jpg"
image bg john jay outside:
    zoom 1.1
    "johnjayoutside.jpg"
image bg ferris = "ferrisbooth.jpg"
image bg ferris inside = "ferrisinside.jpg"
image dinhallfood = "dinhallfood.png"
image dinhallfood2 = "dinhallfood2.png"
image pizza = "pizza.png"

#TODO: make a place to enter major other than when Marie asks

label roommateintro:
    $renpy.music.set_volume(0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, channel="Chan3")
    $renpy.music.play("audio/GluttonyMain.mp3", channel="Chan1", synchro_start=True)
    $renpy.music.play("audio/GluttonyMarie.mp3", channel="Chan2", synchro_start=True)
    $renpy.music.play("audio/GluttonyJosh.mp3", channel="Chan3", synchro_start=True)
    scene black
    with Pause(1)
    show text "{size=50}Semester 1: Actual School{/size}"
    with Pause(2)
    hide text
    scene bg EC
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
                    hide marie neutral
                    show marie ingenuine
                    r "Oh, yeah no problem! I’m just happy you’re coming."
                    jump rmeetjosh
                "No offense, but that sounds really lame. I’m okay, thanks.":
                    hide marie neutral
                    show marie astonished
                    r "Oh my gosh, I didn’t even realize I was being lame! That’s so embarrassing."
                    hide marie astonished
                    show marie concerned
                    r "I’m so sorry, I won’t ask again."
                    show marie concerned at left with move
                    hide marie concerned
                    show marie cry at left
                    m "Please don’t. I need my space."
                    $ marie_friendship -=1
                    hide marie sad with moveoutleft
                    $renpy.music.set_volume(1.0, channel="Chan1")
                    $renpy.music.set_volume(volume=0.0, channel="Chan2")
                    m "Finally!"
                    jump rlonelyday
        "Don't say anything":
            "Ugh, this is awkward. I can literally hear crickets chirping. Is that in my head or do we actually have a cricket infestation?"
            #TODO: add sound: play sound "crickets.mp3"
            hide marie happy
            show marie neutral
            "..."
            r "Um, yeah"
            r "So anyway... {p=1.0}I was wondering if you wanted to come to lunch today. I’m having lunch with my OL. It would be fun to bring a friend."
            menu:
                "Yeah, whatever. I guess I need to eat lunch anyway.":
                    hide marie neutral
                    show marie happy
                    r "Yay! Thanks so much for coming with me. To be honest, I’m kind of nervous. I’ve never been alone with my OL before."
                    m "Well, now you won’t be. Let’s go, I don’t have all day."
                    jump rmeetjosh
                "Who said we were friends?":
                    hide marie neutral
                    show marie surprised
                    r "Oh! I don’t know, I thought...{p=1.0}I thought..."
                    hide marie surprised
                    show marie concerned
                    m "I barely even know you! Why would I call you my friend?"
                    m "Obviously, you thought wrong."
                    hide marie concerned
                    show marie cry
                    r "Okay... {p=1.0}I’m sorry. I’ll leave you alone now."
                    $ marie_friendship -=1
                    hide marie cry
                    with moveoutleft
                    $renpy.music.set_volume(1.0, channel="Chan1")
                    $renpy.music.set_volume(volume=0.0, channel="Chan2")
                    m "Finally!"
                    jump rlonelyday

label rlonelyday:
    "Alone at last! This is good. My roommate is so annoying, can’t believe I’m stuck with her for a whole year. Yikes!"
    "Anyway, maybe I should head to the library today. Knock some work out now so I’ll be ahead by Monday."
    $ pmajor = renpy.input("I mean it's really what I should do if I'm serious about majoring in")
    "Yeah. {p=1.0}Study. {p=1.0}That’s what I’ll do."
    scene bg themil
    "It’s so peaceful and quiet in here even with all these people. No stress yet so early in the semester! It was such a good idea to come here on a quiet day!"
    $renpy.music.set_volume(0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, channel="Chan2")
    show marie happy at sright with moveinright
    "Oh no, that’s Marie!"
    "Why is she here?"
    $renpy.music.set_volume(0.33, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, channel="Chan3")
    show marie happy at sleft with move
    show josh happy at sright with moveinright
    "Is her OL friend giving her ANOTHER tour? Jesus, what now?"
    menu:
        "Try to hide":
            "Quick, under the desk!"
            #TODO: add crash sound
            "Oh crap, that was noiser than I thought it would be."
            hide marie happy
            show marie surprised at sleft, hop
            hide josh happy
            show josh shock at sright, hop
            r "%(pname)s is that you?"
            hide marie surprised
            show marie astonished at sleft
            hide josh shock
            show josh happy at sright
            r "Why are you under the desk?"
            hide marie astonished
            show marie neutral at sleft
            m "What? Oh, I...uh..."
            m "dropped something."
            m "Under the desk."
            m "And then I had to go down and find it."
            hide marie confused
            show marie grateful at sleft
            r "Looks like you’ve dropped a lot of stuff now! Here, let us help you."
            r "%(pname)s, this is my friend, Josh. He was my OL during NSOP."
            hide josh happy
            show josh winkfg at sright
            j "Hey %(pname)s. It’s so groovy to meet you. Marie told me some about you already!"
            hide marie grateful
            hide josh winkfg
            jump libraryjmcont
        "Say hi.":
            m "Hey Marie, what’s up?"
            hide marie happy
            show marie surprised at sleft, hop
            r "Oh my gosh, %(pname)s! I didn’t know you’d be here, I promise. Josh was just showing me around."
            m "Oh, yeah, it’s fine. It’s not that exciting though."
            hide marie surprised
            show marie happy at sleft
            r "I guess I’m just a nerd, I like libraries! That’s just me though."
            hide josh happy
            show josh v grateful at sright
            j "Nah dude. I frickin love libraries. I get amped just walking in and smelling all those books. There’s nothing like the smell of a new book."
            "Why is he talking about books so weirdly? I’ve never heard someone talk about liking books because of smells. Weirdo."
            hide josh v grateful
            show josh happy at sright
            j "Anyway, bro, nice to meet you. I’m Josh, you must be %(pname)s. Marie’s told me a little about you."
            hide marie happy
            hide josh happy
            jump libraryjmcont

label libraryjmcont:
    show marie surprised at sleft
    show josh happy at sright
    m "Oh, um, good things I hope?"
    r "Of course! What bad thing could I possibly say about you?"
    "Oof. Seems like she doesn’t remember this morning? Or maybe she’s just too polite to mention it. Should I bring it up?"
    menu:
        "Apologize for earlier":
            hide marie surprised
            show marie astonished at sleft
            m "Hey, so listen, I’m sorry if I snapped at you this morning. That didn’t go how I wanted it to. Can we move on and be friends again?"
            hide marie astonished
            show marie happy at sleft
            r "Oh don’t even mention it! I totally get it. I’ve been so tired lately too. It can be so hard to be around people constantly."
            j "Yeah dude. I totally vibe with that. I get so frickin tired of being around my roommate all the time that sometimes I just get so aggro it’s crazy."
            hide josh happy
            show josh wink at sright
            j "It’s all part of the experience."
            hide josh wink
            show josh happy at sright
            m "Can I catch you guys for lunch some other time? It’s a shame I missed today."
            j "Of course, bro! Anytime. Give me your number and I’ll text you sometime."
            $ josh_hasnumber = True
            r "Anyway, Josh was just showing me around. I’ll leave you alone to study now. I’m so glad we ran into you!"
            $renpy.music.set_volume(1.0, channel="Chan1")
            $renpy.music.set_volume(volume=0.0, channel="Chan2")
            $renpy.music.set_volume(volume=0.0, channel="Chan3")
            jump gluttonybeginday2
        "Don't bring it up.":
            "You know what?"
            "No. {p=1.0}I have nothing to apologize for."
            hide marie confused
            show marie neutral at sleft
            "All I wanted was some peace and quiet. I’ll show her."
            "I’ll go get a great lunch at Shake Shack, {p=1.0}as a treat, {p=1.0}just for myself."
            "..."
            hide marie neutral
            show marie happy at sleft
            r "Well, anyway, we’d better get going and let you study. Josh was just showing me around. See you later!"
            m "Yeah, see you!"
            hide marie happy with moveoutleft
            hide josh happy with moveoutleft
            $renpy.music.set_volume(1.0, channel="Chan1")
            $renpy.music.set_volume(volume=0.0, channel="Chan2")
            $renpy.music.set_volume(volume=0.0, channel="Chan3")
            "Whew, dodged a bullet there! Honestly, that could have gone worse. At least I didn’t yell at her or anything, right?"
            "Now...about that Shake Shack."
            scene bg shakeshack with pushleft
            show chickenfries
            "Well, I had my Shake Shack. Chick'N'Shack with fries, chicken tenders, and a birthday cake milkshake. It was delicious."
            "I have to admit though, it felt weird eating that huge meal all by myself. I kinda missed having company. But hey, I guess I’ll just have to get used to it."
            hide chickenfries
            jump gluttonybeginday2

label rmeetjosh:
    scene bg john jay
    "Found the dining hall! First challenge of the day complete."
    $renpy.music.set_volume(0.33, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, channel="Chan3")
    show josh wave at sright
    show marie happy at sleft:
        zoom .75
    "Oh, there they are. That guy sitting next to Marie is waving extremely vigorously at me. Those are windmill arms if I’ve ever seen them."
    hide josh wave
    with dissolve
    show josh happy at right with move
    hide marie happy
    with dissolve
    show marie happy at left with move
    m "Hey guys, what’s up?"
    hide marie happy
    show marie grateful at left
    r "Hi, %(pname)s! This is my friend, Josh."
    j "Hey bro. Groovy to meet you."
    m "Nice to meet you too. I’ll get some food and join you guys."
    hide marie grateful
    with dissolve
    hide josh happy
    with dissolve
    scene bg john jay inside
    show dinhallfood with dissolve
    "Wow, I really loaded up my plate. Gotta do a better job estimating portion sizes next time."
    hide dinhallfood
    scene bg john jay with fade
    show marie grateful at left
    with moveinleft
    show josh happy at right
    with moveinright
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
    hide marie happy
    show marie grateful at left
    r "I’m usually more of a baking gal, but I’d be up for giving cooking a try! Anything to spend time with my new friends."
    menu:
        "Well, I’m not really much of a cook.":
            m "I’ll let you guys do that without me."
            hide marie grateful
            show marie neutral at left
            r "Aw, ok. I understand."
        "Are you kidding me?":
            $ josh_friendship -=1
            hide josh happy
            show josh shock at right
            hide marie grateful
            show marie astonished
            m "I literally just got here. You think I’m gonna be wasting time NOT eating dining hall food? No thanks."
            j "Chillax bro, just thought it might be a fun idea. Whatever floats your boat my dude."
            hide josh shock
            show josh happy at right
        "I’ve never cooked much before, but I’m down to try anything!":
            #TODO: add little happy giggle or clap sound effect?
            $ marie_friendship +=1
            $ success +=1
            m "I'll definitely join in!"
            hide marie grateful
            show marie v happy at left, hop
            r "Yay! It’s going to be so much fun!"
            hide marie v happy
            show marie happy at left
    j "You know what, bros? This has been really frickin baller."
    hide josh happy
    show josh grateful at right
    j "You guys are so frickin cool. I’m so glad I met you."
    hide josh grateful
    show josh sad at right
    hide marie happy
    show marie neutral at left
    j "I’ve been at this school a whole year and believe it or not bro, it’s been tough for a dude like me to make friends."
    hide josh sad
    show josh happy at right
    hide marie neutral
    show marie happy at left
    j "Can I get your numbers so I can hit you up for meals and stuff?"
    menu:
        "Sure thing!":
            hide josh happy
            show josh grateful at right
            #TODO: check if this shows up at all
            $ josh_hasnumber = True
            hide josh grateful
            show josh happy at right
        "Um, actually, I don’t really like to give my number out.":
            hide josh happy
            show josh sad at right
            hide marie happy
            show marie neutral at left
            j "Oh, ok."
    #TODO: make this transition make more sense if you don't give josh the number
    with dissolve
    hide marie neutral
    show marie happy at left
    r "Wow, time flies when you’re having fun! I actually have to go now. Want to head out together?"
    hide josh sad
    show josh happy at right
    j "Yeah man, time to bail. This was a fun idea, thanks for the invite, Marie."
    hide marie happy with moveoutleft
    hide josh happy with moveoutright
    jump gluttonybeginday2

label gluttonybeginday2:
    $renpy.music.set_volume(1.0, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, channel="Chan3")
    scene bg EC with dissolve
    "Where did the weekend go? How is it Sunday already?"
    "Geez, I feel like I did nothing but eat. The freshman fifteen is real, folks."
    if josh_hasnumber == True:
        call phone_start
        call message_start("Josh", "Yo, wanna have lunch together today?")
        call message("Josh", "I’m hungry like a beast for some pizza.")
        call reply_message("Yeah, dude, name a dining hall!")
        call phone_end
        $ josh_friendship +=1
        scene bg ferris
        $renpy.music.set_volume(0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.5, channel="Chan3")
        show josh wave
        "Geez, that man waves like his life depends on it. I see him already!"
        hide josh wave
        with dissolve
        show josh happy
        m "Hi, Josh!"
        j "Dude! Righteous to see you brah."
        m "You too, man. I’m hungry, let’s get food!"
        hide josh happy
        #TODO: food transition again (add food images)
        scene bg ferris inside
        with dissolve
        show dinhallfood2
        "Definitely got too much food. Am I really gonna finish all of this?"
        hide dinhallfood2
        scene bg ferris with fade
        show josh happy
        j "Woah, that pizza looks sick! Can I try some?"
        menu:
            "Sure, I’ll cut you  a slice.":
                $ josh_friendship +=1
                j "Thanks, bro! I am stoked about this pizza."
                jump joshday2goodconvo
            "Gross, no!":
                hide josh happy
                show josh shock
                j "Okay dude, chillax! I’ve got a lot of my own food anyway."
                hide josh shock
                show josh happy
                jump joshday2goodconvo
            "Throw the pizza at him.":
                #TODO: add flying pizza and whoosh sound effect
                $ sin -=1
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
                        $ sin -=1
                        #TODO: change these sprites
                        m "You want to eat off my plate now? Really? God, isn’t it enough I’m having lunch with you? This is my first real meal today so back off."
                        j "Woah, hey, I didn’t mean--"
                        hide josh shock
                        show josh sad
                        $ josh_friendship -=1
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
                                hide josh sad
                                show josh happy
                                jump joshday2goodconvo
                            "Sit in awkward silence.":
                                jump joshday2awkconvo
    else:
        jump runintojosh

label joshday2goodconvo:
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
        hide josh happy with moveoutright
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
    j "Well I’m glad you like it so much. I gotta admit, the pizza here is killer."
    j "Anyway, I actually have to head out. My job starts soon."
    m "All right, I’m ready to go."
    hide josh happy with moveoutright
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
    hide josh grateful
    show josh happy
    m "Okay man, I will."
    hide josh happy with moveoutright
    jump finishgluttony

label runintojosh:
    scene bg shakeshack with pushleft
    $renpy.music.set_volume(0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, channel="Chan3")
    "Shake Shack again! Man it’s so convenient this place is so close to campus."
    "Let’s see...I’ll get a Chick’n Shack with fries, and maybe throw in a flat-top dog just for funsies."
    show josh shockbat with moveinright
    j "Yo, %(pname)s! You’re here too?"
    hide josh shockbat
    show josh batterup
    "Oh no. I have company."
    m "Hey Josh, how’re you?"
    j "I’m all right you know, brah. Finished up some practice."
    #TODO: put in zipper sound?
    hide josh batterup
    show josh happy
    "He puts the bat away. Thank goodness. It made me a little nervous for some reason."
    j "How you doin?"
    m "Just getting some lunch."
    hide josh happy
    show josh approve
    j "Brah, what a coincidence! Me too!"
    hide josh approve
    show josh grateful at center, hop
    j "Hey, I have a sick idea--let’s eat together."
    hide josh grateful
    show josh happy
    "Well I guess I have no choice."
    m "Sure, let’s do it."
    show flatdog
    "This food looks delicious. If only I could enjoy it in peace and quiet."
    hide flatdog
    j "So, bro, how’s your week been going? First real week of college, dude!"
    menu:
        "It's been all right":
            jump notclosetojosh
        "It's been great!":
            pass
        "It’s been a lot, but I’m getting through.":
            jump notclosetojosh
    hide josh happy
    show josh grateful
    j "I’m stoked to hear that dude. The first week can be a lot."
    hide josh grateful
    show josh happy
    m "Yeah, well, it’s been pretty good for me."
    j "Cool! So do you like dining hall food? I see you’re eating out already."
    m "I just like to switch things up. How’re you?"
    j "I’m pretty good. School and sports can be hard to balance, you know, but I’m figuring it out."
    m "That’s good to hear. I’ve been wondering how I’m going to manage everything, but if you can do both I can do it."
    hide josh happy
    show josh winkfg
    j "Yeah dude, I’m, like, a veteran of this place. And I can tell you, you can do it."
    hide josh winkfg
    show josh happy
    j "Anyway, I actually have to head to my job now. See you later!"
    m "See you!"
    hide josh happy moveoutright
    "Well, that wasn’t so bad. At least I managed to be polite for five minutes. Thank god he had to go soon."
    jump finishgluttony

label notclosetojosh:
    hide josh happy
    show josh grateful
    j "Dude, I know how you feel. I felt that exact same way my first week. We all go through it and we all survive."
    hide josh grateful
    show josh happy
    m "Good to hear I’m not alone in this. I have been feeling a bit lonely these days, since I don’t really have any friends here yet."
    hide josh happy
    show josh wink
    j "Brah, you have a friend. You have me."
    hide josh wink
    show josh happy
    m "Thanks, Josh. I appreciate that."
    j "Listen, dude, I can’t stay long. I have to go to my job in a minute. But we should hang out later."
    menu:
        "Looking forward to it.":
            $ josh_friendship +=1
        "We'll see.":
            pass
    j "Rats, gotta run. Smell ya later!"
    hide josh happy with moveoutright
    jump finishgluttony
    return

label finishgluttony:
    scene bg john jay outside with dissolve
    "Finally taking the big step of eating dinner by myself. I’m so hungry, even after that big lunch. I hope no one thinks I’m a loser because I’m sitting alone."
    $renpy.music.set_volume(0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, channel="Chan3")
    w "You again? No way brah."
    show josh grateful with moveinbottom
    j "It’s me, Josh!"
    hide josh grateful
    show josh happy
    "Of course, Josh is here again. Is he following me or something?"
    m "Hey Josh, what’s up?"
    #TODO: come up with pun name for Dodge
    j "I’m good dude! Just coming from Dodge actually. Gotta keep fit!"
    "Yikes, that was not what I needed to hear right now. Have I had four meals today? I actually can’t remember. When was the last time I exercised? Definitely sometime this year, right?"
    j "How you doin?"
    m "Oh I’m pretty good. Pretty boring day today, all I’ve done is work."
    "Ha, that’s a lie. Pretty sure all I’ve done is eat."
    hide josh happy
    show josh stress
    j "Me too, bro, me too. I only had time to break for lunch and then I went right back to the grind."
    hide josh stress
    show josh sad
    "When Josh goes to swipe the machine replies with an angry beep."
    j "Oh no. This is so embarrassing dude. I don’t have enough swipes."
    m "Damn, that’s annoying!"
    j "Shoot, what am I gonna do? Oh man, I was really counting on this swipe. I don’t know how I miscounted."
    "He really does look panicked. I wonder if he can afford to get food somewhere else.  But...this is my last swipe of the week. I only have one left."
    menu:
        "Give Josh your last swipe":
            $ josh_friendship +=3
            $ sin = sin + 2
            hide josh sad
            show josh shock at center, hop
            m "Here you can have my swipe. Don’t even worry about it."
            hide josh shock
            show josh grateful
            j "What? No I couldn’t take your swipe! You need to eat, too."
            m "Seriously, don’t worry. I’ve been meaning to try cooking for myself anyway. Maybe I’ll get Marie to help me. I definitely won’t starve!"
            hide josh grateful
            show josh sad
            j "Are you sure?"
            hide josh sad
            show josh grateful
            m "Absolutely! Take the swipe."
            hide josh grateful
            show josh v grateful
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
                    $ sin -=2
                    hide josh sad
                    show josh shock
                    m "Thank god I get to eat dinner alone after all."
                    if josh_friendship > 1:
                        hide josh shock
                        show josh sad
                        j "Oh haha, um, bye %(pname)s. See you later I guess."
                        hide josh sad with moveoutright
                        "Yikes, he looked like a kicked puppy. Where did that even come from? I’m always saying mean things without thinking about it. Is something wrong with me?"
                        "No, you know what, I’m fine. It’s not my fault he can’t take a joke! I’m gonna enjoy my food in peace."
                    elif josh_friendship == 1:
                        hide josh shock
                        show josh sad
                        j "What? Bro, why would you say that to me?"
                        hide josh sad with moveoutright
                        "Yikes, he looked like a kicked puppy. Where did that even come from? I’m always saying mean things without thinking about it. Is something wrong with me?"
                        "No, you know what, I’m fine. It’s not my fault he can’t take a joke! I’m gonna enjoy my food in peace."
                    elif josh_friendship == 0:
                        hide josh shock
                        show josh neutral
                        j "That wasn’t very nice, brah. I wouldn’t do you like that."
                        hide josh neutral with moveoutright
                        "Well that was extremely awkward. Hope I never run into him again. I’ve just gotta put it out of my mind and enjoy some food."
                    else:
                        hide josh sad
                        show josh mad
                        j "You know what? Ever since you first met me you’ve been nasty to me. Do you have a problem with me? Say it to my face. Because I don’t think you’re a very nice person."
                        $ josh_friendship -=4
                        hide josh mad with moveoutright
                        "Well, burned that bridge for sure. Just have to avoid him for the next three years until he graduates. On the bright side, at least he’ll leave me alone. Now...about that food. I’m starving."
                        $ fightwithjosh = True
    jump lust_start_dorm
