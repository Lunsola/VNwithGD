label pridebegin:
    $renpy.music.set_volume(0.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    $renpy.music.play("audio/PrideMain.mp3", channel="Chan1", synchro_start=True)
    $renpy.music.play("audio/PrideMarie.mp3", channel="Chan2", synchro_start=True)
    $renpy.music.play("audio/PrideMarvin.mp3", channel="Chan3", synchro_start=True)
    if fightwithjosh == False and josh_friendship >= 1:
        $renpy.music.play("audio/PrideJosh.mp3", channel="Chan4", synchro_start=True)
    if maximillion_friendship >= 1:
        $renpy.music.play("audio/PrideMaximillion.mp3", channel="Chan4", synchro_start=True)
    if prof_friendship >= 1:
        $renpy.music.play("audio/PrideBonden.mp3", channel="Chan4", synchro_start=True)
    image cgexam = "cgexam.jpg"
    image cgconv = "cgconvention.jpg"
    $ studyday = 0
    $ finalscore = 0
    $ stolesg = False # Did player steal study guide
    $ classgrade = 0 #pride chapter grade (starts with one bc hw1 is a gimmie)
    scene black
    with Pause(1)
    show text "{size=50}Semester 4: Are You Sick of School?{/size}"
    pause
    hide text
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg lecture hall
    "New semester, new me"
    "Soooo glad all those core classes done"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    w "{size=10}UWAH!!! {p=1.0}%(pname)s!!!!!"
    pause .5
    show marie averse
    with hpunch
    r "I had such a hard time finding this room, I thought I was gonna be late!"
    r "I even dropped my toast running here."
    "WHo does she think she is, Sailor Moon?"
    hide marie averse
    show marie nervous2
    m "Hello Marie, this is literally the most well known classroom on campus."
    r "Well, isn't exciting that our first class for %(pmajor)s is in here?"
    m "I was actually part of the %(pmajor)s bowl in high school, so I feel real prepared for this class"
    hide marie nervous2
    show marie v happy
    r "Aw I wish I did something like that! I don't feel prepared enough for Advanced Scientific Stochastic Estimation Systems."
    hide marie v happy
    show marie astonished
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    if persistent.ending == "unlock 4":
        $ persistent.ending="unlock 5"
    w "Y'all mean ASSES?"
    hide marie astonished
    show marie astonished at center:
        xalign 0.5 yalign 1.0
        linear .5 xalign .25
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    pause 1
    show music_neutral at right:
        xalign 1.5 yalign 1.0
        linear .5 xalign .75
    w "Y'all didn't know that {b}A{/b}dvanced {b}S{/b}cientific {b}S{/b}tochastic {b}E{/b}stimation {b}S{/b}ystems..."
    w "...is shortened to {b}ASSES{/b}?"
    hide marie astonished
    show marie confused at left:
        yalign 1.0 xalign .25
    r "{size=10}A S S E S"
    m "That's campus culture right there."
    "Honestly the title of this class is so long I won't bother to remember it."
    a "Anyhoo, name's Marven. I'm taking this class to fulfill a requirement."
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    hide music_neutral
    show music_wink at right:
        yalign 1.0 xalign .75
    a "I'm a music + philosophy double major. {p=2}Puh-lease don't ask me what kind of job I can get with that."
    r "Wowww that's so cool!"
    show breaken at left with moveinleft
    s "{b}Please sit down, class is about to start!"
    a "Oop, gotta go fast!"
    menu:
        "Let's grab those front row seats!":
            "With the professor standing right in front of you, you guys quickly settle down without another word."
        "Ugh let's go sit in the back":
            $ music_friendship +=1
            scene bg lecture hall:
                xalign 1.0 yalign 0.3
                zoom 4
            show music_talk at right
            show marie neutral at left
            with fade
            a "Anyways are you guys into memes?"
            m "Hell yeah"
            r "%(pname)s always stays up scrolling, chuckling like an old man!"
            hide music_talk
            show music_neutral at right
            a "What memes are you into?"
            menu:
                "Distracted boyfriend":
                    a "Eh that one's ok. {p=1} Kinda overused ya know?"
                "ERMAHGERD":
                    $ music_friendship +=1
                    a "Ahh takes me back to when I yelled that in the playground every day at lunch"
                "tide pods":
                    $ music_friendship +=1
                    pause 1
                    a  "So what did it taste like?"
            s "{b}Can you guys in the back be quiet please"
            a "hee hee"
    scene bg john jay with irisin
    pause 1
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    show marie v happy with dissolve
    r "Hoowah! Nothing like eating a big meal after that tough introduction to ASSES!"
    hide marie v happy
    show marie happy
    r "Marven seemed like a nice guy. I wanna be study buddies!"
    m "I dunno. He smelled like a memey poser."
    r "Now, you can't make those kinds of assumptions right off the bat! You two have a lot in common!"
    r "He seemed really cool! Like he is double majoring but still takes time to enjoy college life!"
    m "Overachievers often have dark pasts and make up for their insecurities by participating in an assortment of activities."
    hide marie happy
    show marie surprised
    pause 1
    hide marie surprised
    show marie happy
    r "Well, I've memorized the syllabus so I can do my best in this class!"
    r "We have two homeworks! {p=.5}Two midterms! {p=.5}And a final!"
    m "I think maybe you should save your brain cells for actual class material."
    m "The professor seems to be a bad lecturer, so going to class probably won't help either way."
    hide marie happy
    show marie averse
    r "O M G"
    r "I'm gonna go work on HW1 right now!"
    hide marie averse
    with dissolve
    "Haha she's so gullible."
    "I'll show Marven who's the mightier memelord, all while nabbing an A+ in ASSES."
    scene bg bedroom
    with dissolve
    "Ah"
    "It's already Sunday? Where did the weekend go?"
    show marie nervous
    with hpunch
    r "%(pname)s"
    r "Have you done ASSES?"
    m "DOnE whAt?"
    r "the ASSES homework!"
    m "Oh I haven't started, but I was about to just now"
    "Better than doing it right before class"
    hide marie nervous
    show marie happy
    r "Yay! Can I watch you do it?"
    r "Here is the problem! I don't get the first sentence."
    "{i} Deantiny, Prezbeau, and Emelyn Huges are in faculty house. Where is the hidden owl on Alma Mater?{/i}"
    menu:
        "Marie, the first part has nothing to do with the problem":
            pass
    hide marie happy
    show marie v happy
    r "Huh I didn't even think of it in that way! %(pname)s! You're so smart!"
    r "I'm so lucky to have you as my roommate."
    m "Sure, no sweat"
    r "See you in class tomorrow then!"
    hide marie v happy
    with dissolve
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "Geez what kind of joke was that homework."
    scene bg black with fade
    show screen mailbox_overlay
    $ classgrade +=1
    $ add_message("ASSES HW1", "ASSES TA", "Your grade for this assignment is 100")
    play sound "audio/email_notif.mp3"
    "The HW1 grade has been posted"
    scene bg lecture hall with irisin
    "Today is ASSES Examination 1"
    "There's no way I could fail. {p=2} I could jinx myself and still wreck that curve like a pro"
    scene black
    with Pause(.5)
    show text "{i}{size=30}EXAM START"
    with Pause(.5)
    hide text
    scene bg lecture hall
    $ m1_q1 = renpy.input("{i}How many Certified Ethical Hackers have graduated from Columbia?")
    $ m2_q2 = renpy.input("{i}How many earthworms die on average on college walk every rainy day??")
    $ m3_q3 = renpy.input("{i}How many brain cells have you lost playing this game???")
    "Alright that's all of the questions"
    "I have a bad feeling about this"
    scene bg bedroom
    with dissolve
    play sound "audio/phone_notif.mp3"
    pause 2
    "Big yikes the ASSES TAs are fast"
    menu:
        "Check your grade":
            call phone_start from _call_phone_start_8
            call message_start("OfCourseItWorks", "ASSES Examination 1: 33") from _call_message_start_7
            call phone_end from _call_phone_end_8
            "...33 This can't be right?"
            $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
            $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
            show marie grateful
            with dissolve
            r "Hey %(pname)s, have you checked your ASSES Examination? It just got uploaded"
        "Spicy meme time":
            "I can check later; gotta update myself on the hottest memes."
            "Hehe"
            "Haha"
            "Hoho"
            "Boy I can feel my eyes burning"
            $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
            $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
            show marie grateful
            with dissolve
            r "Hey %(pname)s, have you checked your ASSES Examination?"
            m "my WHAT?"
            r "Your grade for the first midterm last week. It just got uploaded!"
            "Ugh I guess I gotta check it now"
            call phone_start from _call_phone_start_9
            call message_start("OfCourseItWorks", "ASSES Examination 1: 33") from _call_message_start_8
            call phone_end from _call_phone_end_9
            "...33? This can't be right?"
            "Well, I can't be the only one doing this badly"
    r "so what did you get?"
    menu:
        "Lie":
            $sin -=1
            m "I got a 95"
            r "Ah as expected!"
            hide marie grateful
        "Don't tell her":
            m "That's not how I roll."
            hide marie grateful
            show marie neutral
            r "That's chill! I get that."
            hide marie neutral
        "Tell her":
            $sin +=1
            m "I got a 33."
            hide marie grateful
            show marie astonished
            r "How could that be?"
            r "You think I'm that gullible?"
            hide marie astonished
    show marie happy
    r "Would you like to work with me for the next homework? I think we can def help each other out in this class!"
    $ add_message("ASSES M1", "ASSES TA", "Your grade for this exam is 33")
    play sound "audio/email_notif.mp3"
    r "I got an 85 because of your help with the other homework!"
    "This airhead...got a higher grade than me?!"
    menu:
        "Yeah let's work together!":
            "Maybe I missed one thing that was unproportionally important. I can ask Marie"
            r "Yay! I actually have a study room reserved tomorrow at the library!"
            r "I'll wake you up at 8 am!"
            "Holy crap, this better be worth it"
            jump hw2pass
        "Nah, I'm busy with other classes":
            r "Aw that's a shame, good luck!"
            "She said it herself, there's still another homework and another midterm, {p=1}not to mention the final"
            "Plenty of time to make it up!"
            jump hw2fail
label hw2pass:
    scene bg themil with fade
    "It's so early I can feel the fatigue of last night's all-nighters still hanging in the air"
    r "Hey %(pname)s!"
    show marie nervous2
    r "Are you ready for our SUPER FOCUS STUDY SESSION!"
    m "Marie you can't yell in the library."
    r "Hehe! Come on let's find some seats."
    m "You go on ahead, I need to use the bathroom first"
    hide marie nervous2
    scene bg buthall with fade
    "Phew"
    "Marie rushed me to the library so fast I didn't go through my morning routine"
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_neutral
    with moveinleft
    a "Hey my d00d. Fancy meeting you here"
    jump music_encounter
label hw2fail:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    scene bg lernerramps
    "Ugh another day of zero motivation"
    "..."
    "Who's that familiar figure?"
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_neutral
    with moveinleft
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    a "Hey my d00d. Fancy meeting you here"
    menu:
        "Say hi":
            $ music_friendship +=1
            m "What's poppin' Marven"
            a "Hoho you remembered my name!"
        "Raise eyebrow":
            pause 2
    jump music_encounter
label music_encounter:
    hide music_neutral
    show music_wink
    a "Never saw you again after our first ASSES encounter eh?"
    m "The lecture isn't that good. I just study on my own."
    hide music_wink
    show music_talk
    a "ASSES is a class that weeds out the Virgin Yous among the Chads"
    a "Change my mind, but tis' the truth"
    a "...afterall, I barely made off with a 110"
    "{size=10}wtf 110?!"
    a "Anyhoo, you seem like you Know Your Meme"
    hide music_talk
    show music_wink
    a "Who's your meme idol?"
    "Can I impress Marven with my taste in memes?"
    menu:
        "Burnie Sanders I am once again asking meme":
            a "Burnard is like, literally my dad"
        "Bean Jong-ho making his academy awards kiss":
            $ music_friendship +=2
            a "Hey I appreciate this rare boi"
        "Water bottle flipping man":
            $ music_friendship +=1
            a "No one more edgy than our local meme legend huh"
    a "Ya YEET you've got pretty good meme-sense!"
    hide music_wink
    show music_dark
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    a "Wanna go to a party with me? {p=1}It's Spicy Meme themed"
    "GASPPP SPICYYY MEMEEEES"
    menu:
        "That sounds GUCCI GANG":
            $ music_friendship +=3
            hide music_dark
            show music_smile
            a "Coolio. Gimme your number, I'll email you the deets"
            m "Woahhhhh I'm going to a SPICY MEME PARTY"
            jump hangover
        "Naw man I'm good":
            $ classgrade +=1
            hide music_dark
            show music_sad
            a "Uwu that's your loss"
            "No way I'm accepting a sus party invitation from this d00d"
            scene bg black with fade
            $ add_message("ASSES HW2", "ASSES TA", "Your grade for this assignment is 100")
            play sound "audio/email_notif.mp3"
            jump m2begin

label hangover:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    scene bg black with fade
    scene bg bedroom with irisin
    "That was funnnnn. BUrP~"
    play sound "audio/phone_notif.mp3"
    pause 1
    call phone_start from _call_phone_start_10
    call message_start("MaRv", "Hey d00d, that was real lit yesterday. Make sure you consume lots of H2O today, ok?") from _call_message_start_9
    call phone_end from _call_phone_end_10
    with pixellate
    "At least I showed Marven I'm a d00d who's book smart AND meme smart"
    $renpy.music.set_volume(0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, channel="Chan3")
    "I think I might've eaten a tide pod"
    show marie nervous
    r "%(pname)s? You were out all night and you didn't tell me!"
    m "Oh g'morning Marie {w}...Errr yeah I went to a party"
    hide marie nervous
    show marie concerned
    "Whoops I was having so much fun I didn't even see her texts"
    menu:
        "Lie":
            $ sin -=1
            m "Sorry, my phone ran out of battery"
            r "Mmmm ok. {w}Anyways, why was there even such a big party the day before class?"
            "She may not be the sharpest tool in the shed, but she rolled me there"
        "Truth":
            $ sin +=1
            m "I actually went out with Marven from ASSES to a Spicy Meme themed party"
            r "Oh ok. {w}It's totally fine that you didn't invite me even thought we are roommates and in the same ASSES."
    show marie concerned
    with vpunch
    hide marie concerned
    show marie averse
    r "%(pname)s! Are you ok?"
    m "mmmmmmmghhh I'm fine"
    with pixellate
    hide marie averse
    show marie averse:
        zoom 2
        yalign .75
        xalign .3
    r "%(pname)s!?"
    with pixellate
    "uuugHHHHHHH"
    with hpunch
    with vpunch
    hide marie averse
    show marie averse:
        zoom 3
        yalign .95
        xalign .3
    r "AGH %(pname)s you can't fall here!"
    r "We've got ASSES homework due today!"
    with pixellate
    with hpunch
    with vpunch
    with hpunch
    "sorry Marie"
    with pixellate
    "RIP ASSES hw2"
    scene bg black
    with pixellate
    $renpy.music.set_volume(0.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $ add_message("ASSES HW2", "ASSES TA", "Your grade for this assignment is 0")
    play sound "audio/email_notif.mp3"
    pause 2
label m2begin:
    scene bg bedroom with fade
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "Another day, another pickle. I pour my energy and time into wrangling with these esoteric ASSES questions, but will this knowledge be useful in the real world?"
    "{i}How many tourist groups come to Low every year?"
    play sound "audio/big-crash.mp3"
    "What's that awful crashing sound coming from Low?"
    "AGH CaN'T conCentraTe"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    show marie happy
    r "hehe %(pname)s is studying hard for ASSES examination 2!"
    m "for WHAT... oh"
    m "I gotta work my ass off to save my ASSES grade."
    m "btw, do you know what's causing that awful din outside?"
    hide marie happy
    show marie v happy
    r "That's the Lion Dance Cult!"
    m "Someone file a public noise complaint!"
    r "They're known for eating all the food at the events they're invited to. {w}AND making a bigger racket than the marching band ON A WEEKLY BASIS."
    m "uh, {p=1}great"
    r "Wanna go study in the library? By the way, this upcoming midterm is weighted more than the first one."
    menu:
        "Screw this I'm going to Milsting":
            r "Okie see ya later then!"
            hide marie v happy
            $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
            "Finally, no more nosy lolis"
            jump milstein
        "I'll go study with you":
            r "Yayyyy!"
            jump m2goodgrade
        "I'm gonna take a nap":
            r "Okie see ya later then!"
            hide marie v happy
            "Finally, that nosy loli is gone"
            if classgrade <= 1:
                "I've been really slacking off, tho. It really is a pain in the ass to have such an anal class in the red."
                "Should I really take a nap?"
                menu:
                    "I need to rest in order to be productive":
                        jump nap
                    "Maybe I should follow Marie's steps and work a bit harder":
                        jump m2goodgrade
            else:
                "I've been studying pretty hard lately. {p=2}Can def afford a break"
                menu:
                    "Sleep. The greatest luxury on campus":
                        jump nap
                    "Never rest. Never stop the grind.":
                        "Study in"
                        menu:
                            "Milsting":
                                jump milstein
                            "Buttler":
                                jump m2goodgrade
label milstein:
    scene bg mil with irisin
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "This is the super silent fourth floor of Milsting, where even something like heavy breathing attracts angry glares"
    "Only the Hard Core kids come here"
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_smile
    with dissolve
    "wtf"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    a "{size=-10}heyyyy %(pname)s! A smol birb told me you were here."
    m "{size=-10}Marven this is a no talking floor!"
    hide music_smile
    show music_nervous
    a "{size=-10}I'm not that loud!"
    "I can already see people giving us side-eye"
    m "{size=-10}We need to get out of here"
    scene bg milfloor with fade
    show music_sad with dissolve
    a "Wow we sure yeeted outta there like skrt skrt"
    m "If we stayed stress culture would have mauled us over"
    hide music_sad
    show music_smile
    a "Yisssss thank you %(pname)s,{p=1} very cool"
    a "Anyways what are your fave meme sounds?"
    menu:
        "OOF":
            a "oof"
        "Grapefruit technique":
            hide music_smile
            show music_moody
            a "Yaikee, man"
            a "Did you also watch Boku no Pico?"
            hide music_smile
            show music_smile
        "Rick roll":
            a "Aw yesss I would never give it up"
    "I gotta put a stop to this if I am ever gonna study"
    m "Hey I'm gonna find a seat back upstairs to study ASSES, ok?"
    hide music_smile
    show music_dark
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    a "Oho? You're that serious about studying?"
    a "Thought you said it was a piece of cake?"
    "Shoot, Marven's gonna think I'm lame. {w}Do I sacrifice my pride or my grade?"
    menu:
        "Yes, but I still have to study to do well":
            $ classgrade +=1
            a "Hmmm ok, sounds like a drag"
            a "Have fun stuDYING"
            hide music_dark
            with dissolve
            "Big oof. He definitely has a lower opinion of me now"
            scene bg black
            "I study for a solid 3 hours, and I feel like maybe I'll just barely pass"
            jump cheat
        "Actually, I was just leaving":
            $ music_friendship +=2
            a "heheh as expected of an ASSES expert"
            hide music_dark
            hide music_moody
            jump eathewitt
label m2goodgrade:
    $ classgrade +=2
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "Marie might poke her nose into my business a lot, but I know it's because she cares. As a bonus, she's a truebred tryhard."
    scene bg buthall
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    show marie happy
    with dissolve
    "%(pname)s! I'm so glad you came to join me."
    hide marie happy
    show marie v happy at center,  hop
    "Let's try our best this time too!"
    hide marie v happy
    with dissolve
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "I study with Marie for 6 hours straight"
    "I feel so big brain now that even if I don't ace this next exam, I can drop out and become a CEO"
    jump passexam
label nap:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "Bright day, plenty of assignments due, finals right around the corner"
    "Great day for a niceeee long nap"
    scene bg black
    with blinds
    play sound "audio/big-crash.mp3"
    "GAWD THEY'RE SO LOUD"
    scene bg bedroom with blinds
    "Those lion dancers are gonna regret ever leaving the zoo"
    scene bg collegewalk with fade
    "Of course as soon as I rampage they disappear"
    jump walk
label walk:
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    w "Ayyyy lmao"
    show music_smile
    with dissolve
    a "Are you here to inSPECT the cute doggos and puppers too?"
    m "I was actually searching for some felines"
    a "You mean those dragon things?"
    a "Yoooo they left like 2 mins ago to cop free food from Milsting"
    hide music_smile
    show music_wink at center,  hop
    a "Those are top notch furries tho. Yo momma would stan."
    a "Like, two people in one suit? Makes Roaree look like a normie"
    m "Uh pretty sure they are lions but anyways"
    a "So what's your fave animal meme?"
    menu:
        "Eggdog":
            $ music_friendship +=2
            hide music_wink
            show music_mad
            pause 2
            hide music_mad
            show music_smile with vpunch
            a "THAT'S MY FAVE MEME RIGHT NOW"
            hide music_smile
            show music_dark
            a "ahhhh it's so cute when it bobs it's head"
            a "The way that it gyrates ahhh it's so cute and thicc"
            hide music_dark
            show music_dark:
                zoom 3
                yalign 2
                xalign .3
            play sound "audio/OOT_Scarecrow_Shake1.mp3"
            a "EGGDOG IS FIRE MY D00D"
            hide music_dark
            show music_wink
        "Ugandan Knuckles":
            a "Hey I'm not gonna judge, but that's a dead meme. Do you even know the wey?"
        "Shocked Pikachu":
            $ music_friendship +=1
            hide music_dark
            show music_wink
            "That's always a classic, but kinda basic? Ya know?"
    hide music_wink
    jump eathewitt
label eathewitt:
    show music_smile
    a "So you're free now?"
    "Shoot, Marven's gonna think I'm lame if I say I actually want to rest. {w}Gotta protect my pride tho"
    a "Let's go muck around hewitt aka best dining hall now. I'll swipe."
    m "Ya yeet"
    scene bg black
    "I go with Marven to hewitt and have a lit time eating pesto pasta and smoothies"
    jump cheat
label cheat:
    scene bg lecture hall with irisin
    "Urk I really don't feel too confident about today's exam"
    show marie neutral at center with moveinright
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    r "Hey ready for the ASSES examination?"
    m "The WHAT.. oh yeah. Sure"
    hide marie neutral with moveoutleft
    pause
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_neutral at center with moveinright
    a "Where are you sitting?"
    m "Uhh my assigned seat is... {p=2} here"
    a "Ayyy I'm right in front of you!"
    hide music_neutral with moveoutleft
    "Ok I can do this {size=-10}maybe"
    scene black
    with Pause(.5)
    show text "{i} ASSES EXAMINATION 2 START"
    with Pause(1)
    hide text
    scene bg lecture hall
    pause 1
    "This is really hard"
    "I wonder how Marven is doing"
    show cgexam with fade
    "Aw man I can see his test sheet crystal clear"
    menu:
        "Cheat":
            $ classgrade += 1
            $sin -=1
            hide cgexam with fade
            "I copy the questions I am struggling with and hand in the exam before Marven"
            scene black with fade
            $ add_message("ASSES M2", "ASSES TA", "Your grade for this exam is 70")
            play sound "audio/email_notif.mp3"
            pause 1
        "Look away":
            "I can't compromise my academic integrity for the sake of a mistake that was completely my fault"
            "I might fail, but I'll do it with honor"
            hide cgexam with fade
            "I guess the questions I am struggling with and hand in the exam before Marven"
            scene black with fade
            $ add_message("ASSES M2", "ASSES TA", "Your grade for this exam is 24")
            play sound "audio/email_notif.mp3"
            pause 1
    jump goinghome
label passexam:
    $renpy.music.set_volume(0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, channel="Chan3")
    scene bg lecture hall with irisin
    $sin +=1
    "I'm pretty confident about today's exam"
    show marie neutral with dissolve
    r "Hey ready for the ASSES examination?"
    m "The WHAT.. oh yeah. Sure"
    hide marie neutral with dissolve
    scene black
    with Pause(.5)
    show text "{i} ASSES EXAMINATION 2 START"
    with Pause(1)
    hide text
    pause 1
    "Hm these questions all make sense, unlike the first exam"
    "Hoo studying sure pays off"
    $ add_message("ASSES M2", "ASSES TA", "Your grade for this exam is 92")
    play sound "audio/email_notif.mp3"
    jump goinghome
label goinghome:
    scene bg milfloor with fade
    "Sophomore second semester is when we choose our major... but what's with this confuzzling major declaration process"
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    w "Ayyyyyyyy d00d"
    "Uh oh"
    show music_neutral with dissolve
    a "Ayyy d00d you sure pulled a speedrun on that test"
    a "The final is gonna be just as easy peasy, ya?"
    m "Yup it's gonna be a no brainer for me kekeke"
    hide music_neutral
    show music_dark
    a "heheh {p=1}You know there's a meme convention happening during reading week?"
    "GASP a MEME convention. To go with a giant memer like Marven would be legendary."
    m "Spill the deets my d00d"
    a "It's gonna be a three day event, smack dab in the middle of the week. Cuz, y'know, who works on the weekdays?"
    m "I'm always chilling on hump day"
    a "Yeah eggzactly! We should go sksksk"
    a "Unless..."
    hide music_dark
    show music_unimpressed
    a "...you actually study for finals?"
    "Oh shoot, if Marie reminded me correctly, the ASSES final is on the first day after reading week"
    "But I reallllllly want to go. Also I have my pride as a memer to defend."
    menu:
        "Flex on the h8rs, I'm going":
            pass
        "I stan this plan":
            pass
        "I have the big thirst for this convention":
            pass
    hide music_unimpressed
    show music_smile
    a "Ya yeet my d00d. I'll buy the tics!"
    a "Chill out my d00d"
    hide music_smile with dissolve
    "No big deal, I'll just go for one day and soak up the spiciness to the max. Delicious!"
label conventionday1:
    scene bg black with fade
    scene bg entrance:
        zoom 0.4
    with squares
    "Hoe my gourd I've never seen so many people in meme costumes"
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_default
    with dissolve
    "Ayyyyyy %(pname)s"
    m "Hello there, meme man Marven"
    "No doubt this is my friend the maraca wielding memelord"
    a "Ayyyy %(pname)s aren't you shook? Look at all those chickens."
    a "What's your fave meme here?"
    menu:
        "Meme man":
            $ music_friendship +=1
            a "Ahh yes the very dankest. I mean, tis' in the name"
        "Is this a pigeon":
            a "Love them anime refs"
        "Arthur clenched fist":
            a "Honestly tho, this one's such a mood"
    a "Alright, time to proceed!"
    hide music_default with dissolve
    pause 1
    m "Wait! Do you have my tickets?"
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_default with dissolve
    a "Oh yeah sillyhead me! Here they are. Pay me back later?"
    m "Thanks"
    "..."
    m "Hey, these are three day tickets"
    hide music_default
    show music_bent
    a "Hell yeah! Gotta swipe the best deal right?"
    a "I mean, it's not like you're doing anything this week"
    m "These aren't refundable are they?"
    hide music_bent
    show music_cross
    a "Nopity dope"
    hide music_cross
    show music_default
    a "Let's go to the meme dealer's alley first!"
    "Oh great I guess I'm doing this for the next two days too"
    scene bg bednight
    with irisin
    play sound "audio/phone_notif.mp3"
    pause 1
    call phone_start from _call_phone_start_11
    call message_img("MaRv", "LmAo fufufu","pride_meme.jpg") from _call_message_img_5
    call reply_message("lol") from _call_reply_message_1
    call phone_end from _call_phone_end_11
    show marie neutral with dissolve
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    r "Hey %(pname)s how was the convention today?"
    m "It was super fun"
    m "I bought some spicy meme posters to hang in our dorm"
    hide marie neutral
    show marie distressed
    r "Awww I'm jello. I spent all day studing my ass off for ASSES. Boohoo"
    r "Must be nice to be smart like you."
    m "You can come tomorrow if you want"
    r "Nah I'll pass. I'm not sad or anything you and Marven didn't invite me in first place either"
    m "Er ok"
    hide marie distressed
    show marie concerned
    r "By the way, the last ASSES exam grade got posted."
    "Check OfCourseItWorks?"
    menu:
        "yes":
            if classgrade <= 2:
                "{p=2}...My overall grade in ASSES isn't ideal. I'd have to pull a miracle out of my ass to pass."
            else:
                "{p=2}...I'm doing ok in ASSES"
                "But it's still uncertain whether I'll pass or not if I mess up on the final"
            "Ughhhh I'm gonna have this tumbling in the back of my mind all night"
            menu:
                "Maybe I should study tomorrow":
                    "Well, I'd better sleep soon then."
                    jump twostudyday
                "Screw this I need to get my money's worth. Another day with meme man tomorrow":
                    jump conventionday2
        "no":
            "Ignorance is bliss."
            jump conventionday2
label conventionday2:
    scene bg black with blinds
    pause 1
    scene bg entrance with fade
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_default
    with dissolve
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    a "Top 'o the mornin' my d00d {p=1}Ready for another day of big bumpin'?"
    m "Ya yeet!"
    scene bg convention
    with irisin
    a "Wow it sure is crowded today"
    a "Guess everyone chills on hump day"
    show cgconv with dissolve
    "Omg. Marven brought an ASSES study guide"
    "If I had that, it could potentially rocket my ASSES grade into the heavens above"
    menu:
        "Steal it":
            $ stolesg = True
            $ sin -=1
            $ studyday += 1
            "I take the precious study guide out and stuff it into my bag"
        "Ignore":
            "..."
    hide cgconv with fade
    scene bg convention with dissolve
    m "Hey Marven your bag is unzipped"
    show music_default with dissolve
    a "Oh hey thanks, way to be a bro!"
    scene bg black with fade
    scene bg bednight
    with irisin
    show marie grateful with dissolve
    r "yawnnn"
    hide marie grateful
    show marie nervous
    r "I'm gonna go sleep now so I can wake up early to study again tomorrow."
    hide marie nervous with dissolve
    "Man I don't know if I should go to the convention again tomorrow"
    "I've already seen pretty much everything and maybe I should study for finals"
    call phone_start from _call_phone_start_12
    call reply_message("Hey Marv, can we meet on campus tmr?") from _call_reply_message_2
    call message("MaRv", "Ye ofc my d00d!") from _call_message_5
    call phone_end from _call_phone_end_12
    scene bg black with blinds
    scene bg bedroom with blinds
    show marie neutral with dissolve
    r "Heading out again today?"
    m "We'll see"
    scene collegewalk with irisin
    show music_bent
    a "Hey bro, what's up? Ready to go?"
    menu:
        "I can't go today":
            hide music_bent
            show music_cross
            a "What??? Today is the last day!"
            a "You're gonna lose money on the deal!"
            a "You're leaving me to go alone? "
            menu:
                "I need to study for finals":
                    a "Whaaa but didn't you say you already know everything?"
                    menu:
                        "Sorry.":
                            $ music_friendship =-5
                            a "Geez. I thought you were smart"
                            a "You know what this maraca is for?"
                            a "It's coming down on you for a vibe check"
                            play sound "audio/OOT_Scarecrow_Shake1.mp3"
                            hide music_cross
                            show music_default
                            with vpunch
                            a "And that's what you get"
                            hide music_defualt with dissolve
                            "Marv bonked me on the head and walked away..."
                            scene bg black with fade
                            "It is COMPLETELY possible for me to pass ASSES if I study all day today and pull an all-nighter"
                            "I just have to shove that awful confrontation to the back of my mind"
                            jump onestudyday
                        "Yeah actually everything will be fine. Let's go":
                            jump conventionday3
                "Nevermind. Let's go":
                    jump conventionday3
        "Yeah let's hop on the train":
            hide music_bent
            show music_default
            a "Come on vamanos!"
            jump conventionday3
label twostudyday:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    scene bg mil with irisin
    $ studyday +=1
    $ music_friendship =-5
    "Alright, feels bad I ditched Marv but I wrote an email explaining why"
    "Time to grind on ASSES"
    pause 1
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    show music_mad
    with dissolve
    a "Hey I read your shitpost email"
    m "{size=-5}Indoor voice pleaseee"
    "That girl in the back is giving the death stare with already lifeless eyes"
    scene bg milfloor with fade
    show music_moody with dissolve
    a "I just want you to know that I am very salty that you ditched me on the second day."
    a "This is top ten anime betrayals. I thought you were WOKE, fam"
    m "Sorry, I realized I have to study for finals"
    hide music_moody
    show music_unimpressed
    a "L A M E"
    a "I am going by myself then!"
    a "You know what this maraca is for?"
    a "It's coming down on you for a vibe check"
    hide music_unimpressed
    show music_smile
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    with vpunch
    a "And that's what you get"
    hide music_smile with dissolve
    "Marv bonked me on the head and walked away..."
    "Big ouch"
    scene bg black with fade
    "Many hours of studying later"
    scene bg bednight
    with irisin
    "Today was very productive"
    show marie grateful with dissolve
    r "yawnnn"
    hide marie grateful
    show marie nervous
    r "You're finally back %(pname)s!"
    r "I'm gonna go sleep now so I can wake up early to study again tomorrow."
    hide marie nervous with dissolve
    "I guess I can't go to the convention again"
    "Sigh.. that's two days worth of money into the void...{p=2}but wait Marv didn't ask me to pay yet"
    "Either way, I'm too tired to process this drama...tomorrow will be another study day"
    jump onestudyday
label onestudyday:
    scene bg mil with irisin
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $ studyday +=1
    "Alright, self"
    "Time to glue my thinking cap to my head"
    if marie_friendship >= 1 and marieevil == False:
        $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
        show marie v happy with dissolve
        r "{size=-10}Working hard, %(pname)s?"
        hide marie v happy with dissolve
    if fightwithjosh == False and josh_friendship >= 1:
        $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
        $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan4")
        show josh approve with dissolve
        j "{size=-10}You can do this, brah."
        hide josh approve with dissolve
    if maximillion_friendship >= 1:
        $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
        $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan4")
        show max wink with dissolve
        b "{size=-10}How refreshing it is to see the serf toiling earnestly"
        hide max wink with dissolve
    if prof_friendship >= 1:
        $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
        $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan4")
        show professor happy with dissolve
        p "{size=-10}Very admirable, keep up the good work, %(pname)s."
        hide professor happy with dissolve
    scene bg black with fade
    pause 2
    jump examday
label conventionday3:
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg convention
    $ music_friendship +=8
    "I steep myself in another indulging day at the meme convention"
    scene bg black with irisin
    "Afterwards, Marv invites me to hang in Hels"
    scene bg hels
    show music_neutral with dissolve
    m "It sure has been a fufilling and exhausting three days. Thank you for inviting me to go with you."
    a "Oh yea? Then no need to pay for your tickets. But answer this question."
    a "If our school had a meme page, which of these would be featured the most?"
    menu:
        "Burner ramps":
            pass
        "Deantiny's Expert's Mind":
            pass
        "Strangely shaped fountains on low":
            pass
    a "I'll take your word for it. I'd be a sad pepe to brush off the insight of an epic memer like you."
    hide music_neutral
    show music_smile
    a "%(pname)s, I just want to say, thank you memeing with me this year."
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    a "It's been the dankest three days of my five years here. {p=2}And you've been the best friend I've ever had, like, we really vibe"
    m "Wait, so you're a fifth-year?"
    hide music_smile
    show music_nervous
    a "I guess that's what you call it? I did not arrive at this school a Chad."
    a "First I suffered from Imposter Syndrome, then Major Indecisivity, then I became too prideful of my image and flunked ASSES the first time I took it"
    "The tea has been spilt. Turns out Marv's school smarts are just accumulated over the years."
    a "Memes are my coping mechanism; they motivate me when nothing else in this depressing world does."
    m "Epic backstory Marv, do you have any tips on the final ASSES assessment?"
    hide music_nervous
    show music_wink
    a "Well, my advice is, gotta go fast! And it does help if you've been around for five years, like me."
    "Wasn't counting on Marv helping anyways. Someone like Marie who has been following the lectures and studying consistently is more reliable.
    Speaking of which, when did she say the exam is?"
    m "ERMAHGERD, the test is tomorrow!"
    hide music_wink
    play sound "audio/OOT_Scarecrow_Shake1.mp3"
    show music_dark
    a "Yea, my d00d, but you know everything so you'll do fine?"
    "Ugh, Marv needs to stop spamming me with this line"
    scene bg black with blinds
    jump examday
label examday:
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg lecture hall with irisin
    w "{size=10}UWAH!!! {p=1.0}%(pname)s!!!!!"
    pause .5
    show marie averse
    with hpunch
    r "Why didn't you wake me up? Such a cruel roommie! What if I missed the final?"
    m "Sorry, I was feeling angsty so I came first"
    hide marie averse
    show marie nervous2
    r "Ahh you must really be nervous to apoligize to me. Don't worry! This final is multiple choice and it's worth 50 percent of your grade!"
    "It's true, it feels like this is the culmination of my entire semester. My performance today is gonna make it or break it"
    "Well, here goes nothing."
    hide marie nervous2 with dissolve
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    "{i}FINAL ASSES EXAMINATION START"
    menu:
        "Consider the width of Butler Library, as measured from its westernmost side to its easternmost side. Estimate the width to the nearest power of ten."
        "4":
            pass
        "3":
            pass
        "2":
            $ classgrade +=1
            $ finalscore +=20;
        "1":
            pass
    menu:
        "Now, let's scale up to Earth. What is the circumference of Earth, as measured through the north and south poles? Consider the value of your estimate of the distance from NYC to the Canadian border and scale up from there."
        "12":
            pass
        "10":
            pass
        "9":
            pass
        "8":
            $ classgrade +=1
            $ finalscore +=20;
    menu:
        "How many floors does Burner have?"
        "9":
            pass
        "8":
            $ classgrade +=1
            $ finalscore +=20;
        "7":
            pass
        "6":
            pass
    menu:
        "When was Barnard founded?"
        "1889":
            $ classgrade +=1
            $ finalscore +=20;
        "1988":
            pass
        "1898":
            pass
        "1899":
            pass
    menu:
        "Which value is closest to the membership of Columbia Buy Sale Memes as of 2020?"
        "48.000":
            pass
        "47:900":
            pass
        "48000":
            $ classgrade +=1
            $ finalscore +=20;
        "47900":
            pass
    "Whew that's the end. Nothing screams high stakes like a five-question final."
    "I want to say I want to know my score now, but in truth, I never want to figure out. I just want to know if I passed or not."
    if music_friendship >= 6:
        $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
        scene bg lernerramps with irisin
        show marie nervous2
        r "Hoowah so glad to have gotten that over with! It was easier than I thought!"
        $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
        $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
        w "Ayyyy"
        hide marie nervous2
        show marie neutral at center:
            xalign 0.5 yalign 1.0
            linear .5 xalign .25
        play sound "audio/OOT_Scarecrow_Shake1.mp3"
        show music_talk at right with moveinright
        a "What's up d00ds"
        r "We're discussing the final ASSES"
        a "LMFAO d00ds, like we should totally dab on the exam. It was a cakewalk by the ocean"
        if stolesg == True and marieevil == True:
            r "If it weren't for %(psname)s's study guide, I think I would feel much more anxious right now!"
            m "What study guide?"
            hide music_talk
            show music_moody at right
            hide marie nervous2
            show marie happy at left
            r "The one you left on your desk! It was all written in memes, which made me confused at first, but it turned out to be a very helpful memory device!"
            a "...{p=1}I had one like that before the meme convention"
            hide marie happy
            show marie v happy at left, hop
            r "Well, that could be a coincidence! %(pname)s tends to have things that looks other people's belongings, isn't that right, %(pname)s?"
            a "%(pname)s, you're a snek"
            hide music_dark with dissolve
            jump badendingpride
        a "I gotta skrt right now, but y'all should come watch me at graduation!"
        play sound "audio/OOT_Scarecrow_Shake1.mp3"
        hide music_talk with dissolve
        jump goodendingpride
    else:
        jump badendingpride
label badendingpride:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    scene bg milfloor with irisin
    "After graduation, I never heard of Marven again"
    "Life is like a visual novel. A single choice could change your relationship with a person forever."
    "Me and Marven could've been really good friends through shared interests"
    jump prideend
label goodendingpride:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    scene bg columbialawn with irisin
    "After graduation, Marven decided to do some traveling to search for a purpose in life"
    if music_friendship >=9:
        $ success +=1
        $Marvensenpai = True
        "His last words were: %(pname)s, I'm glad I was your senpai. Here is a stack of GRE and TOEFL books, along with study guides made with my blood, sweat, and tears"
    play sound "audio/phone_notif.mp3"
    "He sends me the occasional finely curated meme"
    call phone_start from _call_phone_start_13
    call message_img("MaRv", "LmfAO sksksk","pride_meme2.jpg") from _call_message_img_6
    call reply_message("lol") from _call_reply_message_3
    call phone_end from _call_phone_end_13
    jump prideend
label prideend:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    play sound "audio/email_notif.mp3"
    if finalscore == 0:
        $ add_message("ASSES FINAL", "ASSES TA", "Your grade for the final is 0")
    elif finalscore == 20:
        $ add_message("ASSES FINAL", "ASSES TA", "Your grade for the final is 20")
    elif finalscore == 40:
        $ add_message("ASSES FINAL", "ASSES TA", "Your grade for the final is 40")
    elif finalscore == 60:
        $ add_message("ASSES FINAL", "ASSES TA", "Your grade for the final is 60")
    elif finalscore == 80:
        $ add_message("ASSES FINAL", "ASSES TA", "Your grade for the final is 80")
    else:
        $ add_message("ASSES FINAL", "ASSES TA", "Your grade for the final is 100")
    "Oh? It seems that my grade for ASSES final has been uploaded"
    play sound "audio/phone_notif.mp3"
    pause 1
    "And my final grade has been posted to OfCourseItWorks"
    menu:
        "check grade":
            if classgrade >= 9:
                $ success +=1
                "I got an A! It's a miracle!"
                if Marvensenpai and classgrade == 10:
                    $ Marvenperfectrun = True
                    $ success +=1
            elif classgrade == 8:
                $ success +=1
                "I got a B. Not bad, not bad at all!"
            elif classgrade == 7:
                $ success +=1
                "I got a C. Meh."
            elif studyday == 1 and classgrade >= 6:
                $ success +=1
                "I got a C. Meh."
            elif studyday == 2 and classgrade >=5:
                $ success +=1
                "I got a C. Meh."
            else:
                "I failed! :o"
                $failedPride = True
        "Don't check":
            if studyday == 1 and classgrade >= 6:
                $ success +=1
            elif studyday == 2 and classgrade >=5:
                $ success +=1
            else:
                $failedPride = True
            $ignoranceisbliss = True
            "If I cared about ASSES, I would've tried harder in first place"
    "What an underwhelming conclusion to this rollercoaster of semester. How much more of this hell to endure until graduation?"
    hide screen mailbox_overlay
jump beginenvy
