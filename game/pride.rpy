label pridebegin:

    scene bg lecture hall
    "New semester new me"
    "glad to have all those first-year core classes behind, {p=2.0}time to finally focus on my major requirements"
    w "{size=+10}UWAH!!! {p=1.0}%(pname)s!!!!!{/size}"
    pause .5
    show marie averse
    with hpunch
    r "I had such a hard time finding this class, I thought I was gonna be late!"
    hide marie averse
    show marie nervous2
    r "I even dropped my toast running here"
    m "Hello Marie"
    "Who does she think she is, Sailor Moon?"
    r "Aren't you excited that we are finally taking classes for %(pmajor)s?"
    "Honestly, I think this class will be a piece of cake. Pshhhh. It'll be like eyeballing ingredients"
    m "I was actually part of the %(pmajor)s bowl in high school, so I feel prepared"
    hide marie nervous2
    show marie v happy
    r "Aw I wish I did something like that! I don't feel too prepared for Advanced Scientific Stochastic Estimation Systems"
    hide marie v happy
    show marie astonished
    w "you mean ASSES?"
    hide marie astonished
    show marie astonished at center:
        xalign 0.5 yalign 0.0
        linear .5 xalign .25
    show music_neutral at right:
        xalign 1.5 yalign 0.0
        linear .5 xalign .75
        #play the maraca shake noise
    w "Y'all didn't know that {b}A{/b}dvanced {b}S{/b}cientific {b}S{/b}tochastic {b}E{/b}stimation {b}S{/b}ystems..."
    w "...is shortened to {b}ASSES{/b}?"
    hide marie astonished
    show marie confused at left:
        yalign 0.0 xalign .25
    r "{size=+10}A S S E S"
    m "That's campus culture right there"
    "Honestly the title of this class is so long I don't bother to remember it"
    a "Anyhoo, name's Marven. I'm taking this class as a requirement for my major"
    m "We're majoring in %(pmajor)s! How about you?"
    a "I'm a music + philosophy double major. *blahfsfds*."
    r "Woww that's so cool!"
    s "{b}Please sit down, class is about to start"
    hide music_neutral
    show music_wink at right:
        yalign 0.0 xalign .75
    a "Oop, gotta go fast!"
    menu:
        "Let's grab those front row seats!":
            pass
        "Ugh let's go sit in the back":
            $ music_friendship +=1
    scene bg lecture hall
    with moveoutright

    scene bg john jay
    with moveinleft
    pause 1
    show marie v happy
    r "Hoowah! Nothing like eating a big meal after that tough introduction to ASSES!"
    hide marie v happy
    show marie happy
    r "Marvin seemed like a nice guy. I hope we can be friends in that class"
    m "I dunno. He seemed kinda like a show off"
    r "Now, you can't make those kinds of assumptions right off the bat!"
    r "He seemed really smart! Like he is double majoring but still takes time to enjoy college life!"
    m "overachievers often have dark pasts"
    r "Well, I've memorized the syllabus already so I can do my best in this class"
    r "We have four homeworks! {p=.5}Two midterms!{p=.5} And a final!"
    m "I think maybe you should save your brain cells for actual class material"
    m "Well, the professor seems to be a bad lecturer, so going to class probably won't help either way."
    hide marie happy
    show marie averse
    r "OMG"
    r "I'm gonna go work on HW1 right now!"
    hide marie averse
    with dissolve
    "Haha she's so gullible"

    scene bg bedroom
    with dissolve
    "Ah"
    "Tomorrow I have ASSES"
    "Haven't done the homework yet"
    show marie nervous
    with hpunch
    r "%(pname)s"
    r "Have you done ASSES"
    m "DOnE whAt?"
    r "the ASSES homework!"
    m "Oh I haven't started but I was about to just now"
    "Better than doing it right before class"
    hide marie nervous
    show marie happy
    r "Yay! Can I watch you do it?"
    r "Here is the problem!"
    "{i} There is a mouse, frog, and snake in a house. How many legs does the snake have?{/i}"
    menu:
        "Marie, snakes have no legs":
            pass
    hide marie happy
    show marie v happy
    r "Huh I didn't even think of it in that way!"
    r "%(pname)s! You're so smart!"
    r "I'm so lucky to have you as my roommate"
    m "Sure, no sweat"
    r "See you in class tomorrow then!"
    hide marie v happy
    with dissolve
    "Geez what kind of joke was that homework"
    "This class is gonna be a breeze"

    scene bg lecture hall
    "Today is ASSES Examination 1"
    "There's no way I could fail. {p=2} I could jinx myself and still wreck that curve like a pro"
    "{i}EXAM START"
    $ m1_q1 = renpy.input("{i}How many times has Captain Baeyonne flipped the water bottle into the trash can?")
    $ m2_q2 = renpy.input("{i}How many earthworms die on average on college walk every time it rains??")
    $ m3_q3 = renpy.input("{i}How many brain cells have you lost playing this game?")
    "Alright that's all of the questions"
    "That last one was just cruel"
    "I have a bad feeling about this"

    scene bg bedroom
    with dissolve
    "Big yikes the ASSES TA is fast"
    menu:
        "Check your grade":
            "...24"
            show marie grateful
            with dissolve
            r "Hey %(pname)s, have you checked your ASSES Examination. It just got uploaded"
        "Spicy meme time":
            "I can check later; time to check my feed"
            "Hehe"
            "Haha"
            "Hoho"
            "Boy I can feel my eyes burning"
            show marie grateful
            with dissolve
            r "Hey %(pname)s, have you checked your ASSES Examination"
            m "my WHAT"
            r "Your grade for the first midterm last week. It just got uploaded"
            "Ugh I guess I gotta check it now"
            "{p=2}...24"
    r "so what did you get?"
    menu:
        "Lie":
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
            m "I got a 24"
            hide marie grateful
            show marie astonished
            r "How could that be?"
            r "You think I'm that gulible?"
            hide marie astonished
    show marie happy
    r "Would you like to work with me for the next homework? I think we can def help each other out in this class!"
    r "I got an 85 because of your help with the other homework!"
    "This arihead...got a higher grade than me"
    menu:
        "Yeah let's work together!":
            r "Yay! I actually have a study room reserved tomorrow at the library!"
            r "I'll wake you up at 8 am!"
            "This better be worth it"
            $ classgrade +=1;
            jump hw2pass
        "Nah, I'm busy with other classes":
            r "Aw that's a shame, good luck!"
            "She said it herself, there's still three homeworks and another midterm, {p=1}not to mention the final"
            "Plenty of time to make it up!"
            jump hw2fail

label hw2pass:
    scene bg themil
    r "Hey %(pname)s"
    show marie nervous2
    r "Are you ready for our SUPER FOCUS STUDY SESSION"
    m "Marie you can't speak so loudly in the library"
    "Her voice is hurting my brain"
    r "hehe come on let's find some seats"
    m "You go on ahead, I need to use the bathroom first"
    hide marie nervous2
    scene bg buthall #bg bathroom
    "Phew"
    "Marie rushed me to the library so fast I didn't go through my morning routine"
    show music_neutral
    with moveinleft
    a "Hey my d00d. Fancy meeting you here"
    jump music_encounter

label hw2fail:
    scene bg lerner
    "Ugh another day of zero motivation"
    "..."
    "Who's that familiar figure striding over?"
    show music_neutral
    with moveinleft
    a "Hey my d00d. Fancy meeting you here"
    menu:
        "Say hi":
            $ music_friendship +=2
            m "What's poppin' Marvin"
            a "Nuttin' much d00d"
            a "Hoho you remembered my name!"
            m "uh haha"
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
    a "Oho that takes some guts."
    a "I had to go to every single class..."
    a "...spend hours on that first homework..."
    a "...and I barely made off with a 110"
    a "Now I'm finally breaking from ASSES"
    "{size=+10}wtf 110? Gotta hide my shocked face!"
    a "Anyhoo, you seem like a chill d00d"
    hide music_talk
    show music_dark
    a "Wanna go to a party with me? {p=2}It's Spicy Meme themed"
    "GASPPP SPICYYY MEMEEEES"
    menu:
        "That sounds GUCCI GANG":
            $ music_friendship +=3
            hide music_dark
            show music_smile
            a "Coolio. Gimme your number, I'll send you the deets"
            "Woahhhhh I'm going to a SPICY MEME PARTY"
            jump hw3fail
        "Naw man I'm good":
            $ classgrade +=1
            hide music_dark
            show music_sad
            a "Uwu that's your loss"
            "No way I'm accepting a sus party invitation from this d00d"
            jump m2begin

label hw3fail:
    scene bg bedroom
    "That was funnnnn. BUrP~"
    "Never drank so much gatorade in one night"
    "I think I might've eaten a tide pod"
    with hpunch
    "Feels kinda gross"
    show marie nervous
    r "%(pname)s? You were out all night and you didn't tell me!"
    m "Oh g'morning Marie."
    m "Errr yeah I went to a party"
    hide marie nervous
    show marie concerned
    "Whoops I was having so much fun I didn't even see her texts"
    menu:
        "Lie":
            m "Sorry, my phone ran out of battery"
            r "mmmm ok"
            r "Anyways, why was there even such a big party the day before class?"
            "She's sharper than she looks"
        "Truth":
            m "I actually went out with Marven from ASSES to a Spicy Meme themed party"
            r "Oh ok."
            r "It's fine that you didn't invite me even thought we are roommates and in the same ASSES"
show marie concerned
with vpunch
hide marie concerned
show marie averse
r "%(pname)s! Are you ok?"
m "mmmmm still woozy"
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
    yalign 1.01
    xalign .3
r "AGH %(pname)s you can't fall here!"
r "We ASSES homework due today!"
with pixellate
with hpunch
with vpunch
with hpunch
"sorry Marie"
scene bg bedroom
with pixellate
"RIP ASSES hw3"

label m2begin:
scene bg themil
"Zamn ASSES makes no sense"
"{i}How many drops of water are circulated in the fountains on low?"
"*dumb question*"
pause 1
#sound?
"What's that awful crashing sound coming from low?"
"AGH CaN'T conCentraTe"
show marie happy
r "hehe %(pname)s is studying hard for ASSES examination 2!"
m "for WHAT... oh"
m "I gotta work my ass of to save my ASSES grade"
m "btw, do you know what's causing that awful din outside"
hide marie happy
show marie v happy
r "That's the Lion Dance Cult!"
m "Someone file a public noise complaint!"
r "They're known for eating all the food at the events they're invited to"
r "AND making a bigger racket than the marching band ON A WEEKLY BASIS."
m "uh, {p=1}great"
r "Wanna go study in the library?"
menu:
    "Screw this I'm going to Milstein":
        r "Okie see ya later then!"
        hide marie v happy
        $ classgrade +=1
        jump m2okgrade
    "I'll go study with you":
        r "Yayyyy!"
        hide marie v happy
        $ classgrade +=2;
        jump m2goodgrade
    "I'm gonna take a nap":
        r "Okie see ya later then!"
        hide marie v happy
        "Finally, that nosy loli is gone"
        if classgrade <= 1:
                "I've been really slacking off tho"
                "It's really a pain in the ass to have such an anal class in the red"
                "Should I really take a nap?"
                menu:
                    "I need to rest in order to be productive":
                        jump nap
                    "Maybe I should follow Marie's steps and work a bit harder":
                        jump m2goodgrade
        else:
            "I've been studying pretty hard lately. {p=2}Can def afford a break"
            menu:
                "Take a walk around campus. Who knows who I'll run into?":
                    #need stuff here
                    jump m2okgrade
                "Sleep. The greatest luxury on campus":
                    jump nap
                "Hm I actually want to study. Marie is just a huge distraction so I had to get rid of her":
                    $ classgrade +=2;
                    jump m2goodgrade
label m2okgrade:
    scene mil
    "Finally, no more nosy lolis"


label m2goodgrade:
    "Marie might poke her nose into my business a lot, but I know it's because she cares"

label nap:
"Bright day, plenty of assignments due, finals right around the corner"
"Great day for a niceeee long nap"
