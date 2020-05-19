#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

label beginenvy:
    $renpy.music.set_volume(0.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    $renpy.music.play("audio/EnvyMain.mp3", channel="Chan1", synchro_start=True)
    $renpy.music.play("audio/EnvyMarie.mp3", channel="Chan2", synchro_start=True)
    $renpy.music.play("audio/EnvyJosh.mp3", channel="Chan3", synchro_start=True)
    $renpy.music.play("audio/EnvyMarvin.mp3", channel="Chan4", synchro_start=True)
    scene black
    with Pause(1)
    show text "{size=50}Semester 5: Junior year???{/size}"
    with Pause(2)
    hide text
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg columbiagates
    with dissolve
    "How is it that I’m already a junior, but I don’t feel any more mature than when I was a freshman? I thought by this point in my life I would have things more figured out, but I feel pretty much the same as I did before."
    "I don’t have that many swipes this year. Time to check out the food carts."
    if marieevil:
        jump wrongedmarie
    else:
        jump goodtermswmarie

label goodtermswmarie:
    "Ugh, this line is long. Guess I don’t really have anywhere to be."
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    show marie v happy at center with moveinbottom
    r "Oh my gosh, %(pname)s! So good to see you. How was your summer?"
    hide marie v happy
    show marie happy
    m "Oh, you know, pretty good. Worked a lot of shifts at FishMart. They asked me to stay on as a manager and everything, but I had to say no obviously."
    hide marie happy
    show marie grateful
    r "Wow, that’s so flattering! I bet you were a great employee."
    hide marie grateful
    show marie happy
    m "Yeah, well, definitely worked more hours there than I ever thought I would in my life. What about you, how was your summer?"
    hide marie happy
    show marie happy at center, hop
    r "Amazing actually! I got this super cool internship!"
    r "Basically I got to go and do hands on research in my field for this exciting company. It’s kind of under wraps right now so I can’t say too much, I’ll send you the link when the company releases the report to the papers!"
    "Um, what? Marie has a classified internship? What the hell could she have been doing? Why didn’t I hear about this internship??"
    m "Good for you, haha. That sounds really cool."
    "Oops, that laugh sounded a smidge too nervous. Gotta reel it back."
    m "I mean, that’s awesome! I’m happy for you."
    hide marie happy
    show marie grateful
    r "Thanks. It means a lot coming from you, you’re so smart and talented!"
    "What is she talking about? She’s obviously more successful than me in our field. Is she making fun of me?"
    show josh happy at left with moveinleft
    hide marie grateful
    show marie happy at right with move
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    j "Woah, Marie, so funny running into you! This is so crazy brah I was just thinking of you."
    hide marie happy
    show marie nervous at right with move
    r "Oh my gosh, Josh! I totally didn’t know this is your favorite place to get lunch, haha. I guess we can..."
    show marie nervous at sright with move
    r "have lunch together?"
    "Is she...flirting?"
    "What is happening right now?"
    hide josh happy
    show josh grateful at left
    hide marie nervous
    show marie grateful at sright
    j "Bro, that’s a bitchin’ idea. I’m so down."
    if fightwithjosh:
        jump joshstillbitter
    else:
        jump ongoodtermswjosh

label ongoodtermswjosh:
    hide josh grateful
    show josh approve at left
    hide marie grateful
    show marie neutral at sright
    j "%(pname)s, you coming too? We could all go over to sit on Low Steps to eat."
    "I feel like Marie kind of wants a moment alone with Josh. Maybe I should let them do their thing and not intrude."
    menu:
        "Have lunch with them":
            hide marie neutral
            show marie ingenuine at sright
            hide josh approve
            show josh happy at left
            m "Yeah, I’ll come along. Sounds fun!"
            j "Cool beans, let’s head out! Once we get our food of course."
            hide marie ingenuine with moveoutright
            hide josh happy with moveoutleft
            scene bg low
            with dissolve
            show josh happy at left with moveinright
            show marie v happy at right with moveinright
            r "So, Josh, how was your summer? You’re so talented, I bet you’re doing incredible things!"
            hide josh happy
            show josh v grateful at left
            hide marie v happy
            show marie happy at right
            j "Ha, well, I don’t know about incredible, dude. But I can’t lie, this summer was totally going off! I got this amazing job opportunity at Dolphin Classics, where I was totes, like, working as an assistant editor. It was this crazy thing, but so dope!"
            hide marie happy
            show marie v happy at right, hop
            hide josh v grateful
            show josh happy at left
            r "Wow, Josh, that’s so cool! Isn’t your dream job working in publishing?"
            j "Yeah bro, pretty much. I feel like I’m moving forward in my career right in time to graduate. And they’re letting me stay on part time this year so maybe it could even be my first job out of college."
            r "Josh, I’m so happy for you. It’s everything you’ve been wanting these past few years."
            m "Yeah, Josh, that’s great. It’s definitely...everything you’ve been wanting."
            hide marie v happy
            show marie happy at right
            "Is it just me, or did both Marie and Josh get crazy lucky opportunities almost at the exact same time? Now I feel weird that I don’t have news to share. Just last year it felt like we were all on the same level, but now they’re both so much farther than me in their careers."
            "Okay, maybe I’ll ask Josh about something that’s a little more stressful. I’m not proud of this, but I want to hear that he’s got some struggles too."
            m "So Josh, how’s baseball going? I know it’s been hard to balance school and sports sometimes these past three years."
            j "Dude, you have a good point. I’m actually scaling back a lot this year. Coach understands that my degree has to come first. I haven’t been playing so well anyway so I think he was okay with my mostly staying on the bench this semester."
            m "Oh well that’s... {p=1.0}great."
            "So he’s like...doing fine? He’s not struggling at all? No offense to Josh, but he was always the one who made me feel better about not having my shit together. Now suddenly he has his shit together way more than me."
            show marie happy at center with move
            $renpy.music.set_volume(0.25, delay=0.5, channel="Chan1")
            $renpy.music.set_volume(volume=0.25, delay=0.5, channel="Chan2")
            $renpy.music.set_volume(volume=0.25, delay=0.5, channel="Chan3")
            $renpy.music.set_volume(volume=0.25, delay=0.5, channel="Chan4")
            show music_neutral at right with moveinright
            r "Oh look, it’s Marven! Hey Marven, come say hi!"
            hide music_neutral
            play sound "audio/OOT_Scarecrow_Shake1.mp3"
            show music_wink at right
            a "Hey d00ds, what’s up? Good to see you’re looking well %(pname)s."
            hide music_wink
            show music_neutral at right
            "Ew."
            j "We’re just hanging out man, what’s up with you?"
            a "I’m pretty good, nothing much going on with me."
            "Well that’s a relief at least. Thank god Marven doesn’t have some big accomplishment to tell us about."
            hide music_neutral
            show music_talk at right
            a "I mean...okay, I did just get hired by Amazim but I don’t want to brag or anything. I’m sure you guys have cool stuff going on too."
            hide music_talk
            show music_neutral at right
            "Ah. Okay. Well...shoot me. Also, what’s with all this fake modesty? I bet he’s crowing on the inside."
            hide music_neutral
            show music_talk at right
            a "You know, Amazim like really really hard to get an internship at, nevermind a job."
            a "And like, just sayin', but they called me a prodigy. And ye, before you ask, it’s true that my uncle is a top eggzecutive there but lemme just say that that had NOTHING to do with the hiring process."
            "What? Wasn't he planning to travel??"
            hide music_talk
            show music_heh at right
            a "I just ball that hard."
            hide music_heh
            show music_smile at right
            "Well, at least his seemingly unshakeable confidence is the same."
            "Okay, to be honest, all this is stressing me out. Anyone else want to come up and tell me all about their accomplishments? At this point, I kind of want to just spend the rest of the day in my room where no one can find me and tell me how succesful they are. Yeah...that sounds like fun."
            hide josh happy with moveoutleft
            hide marie happy with moveoutleft
            hide music_smile with moveoutright
            jump endeswday1
        "Pass on lunch":
            m "Nah, you guys go ahead. I have some errands I gotta run anyway so I should eat fast."
            j "Cool, bro, catch you later!"
            "Well, it did seem like they were having a moment. I suddenly kind of felt like the third wheel. They both seem so happy. I guess other people have their shit together right now more than I thought."
            jump lunchaloneesw

label joshstillbitter:
    "Is he gonna invite me?"
    m "*cough* well, bye Marie."
    hide josh grateful
    show josh neutral at sleft
    if marieevil:
        hide marie concerned
        show marie angry
    else:
        hide marie grateful
        show marie happy at sright
    j "Oh…%(pname)s, um, didn’t see you there."
    j "Uh...how are you?"
    "Well screw this. Now I feel like a third wheel. Last thing I’m gonna do is admit I’m not doing anything right now. Jeez, I guess I’d better come up with a believeable sounding lie real quick."
    m "I’m great. Just got this huge job opportunity in my field so...no complaints here."
    hide josh neutral
    show josh happy at sleft
    j "Wow, that’s amazing. That’s such a coincidence, I just got a huge opportunity too. I’m so glad you’re doing so well."
    "Is he being sincere? He seems weirdly genuinely happy for me. Does he not remember our fight? I kind of feel bad for lying now."
    m "What was the opportunity?"
    j "I got this cool gig at Dolphin Classics, where I was totally, like, working as an assitant editor."
    if marieevil:
        hide marie angry
        show marie ingenuine at center, hop
    else:
        hide marie happy
        show marie v happy at sright, hop
    r "Wow, Josh, that’s so cool! Isn’t your dream job working in publishing?"
    hide josh happy
    show josh grateful at sleft
    j "Yeah bro, pretty much. I feel like I’m moving forward in my career right in time to graduate. And they’re letting me stay on part time this year so maybe it could even be my first job out of college."
    if marieevil:
        pass
    else:
        show marie v happy at center with move
    hide josh grateful
    show josh happy at sleft
    r "Josh, I’m so happy for you. It’s everything you’ve  been wanting these past few years."
    m "Yeah that’s...great. It’s definitely...everything you’ve been wanting."
    hide marie ingenuine
    hide marie v happy
    show marie happy at center, hop
    r "Oh, there’s my food!"
    j "Got mine, too. Well, um..."
    j "Catch you later %(pname)s. Nice to catch up."
    hide josh happy with moveoutleft
    hide marie happy with moveoutleft
    m "Yeah...right. So nice."
    jump lunchaloneesw

label lunchaloneesw:
    $renpy.music.set_volume(0.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    $renpy.music.play("audio/EnvyMain.mp3", channel="Chan1", synchro_start=True)
    $renpy.music.play("audio/EnvyMarie.mp3", channel="Chan2", synchro_start=True)
    $renpy.music.play("audio/EnvyJosh.mp3", channel="Chan3", synchro_start=True)
    $renpy.music.play("audio/EnvyMaximillion.mp3", channel="Chan4", synchro_start=True)
    scene black
    with Pause(.5)
    show text "{size=20}minutes of waiting in a foodtruck line later{/size}"
    with Pause(1)
    hide text
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan4")
    scene bg columbiagates
    show max happy with moveinbottom
    b "Hey, it’s you! The plebian. I haven’t seen you in a while."
    "Great. This is just who I needed today."
    m "Oh, hey Max. How’re you doing?"
    hide max happy
    show max charm
    b "I am actually finding myself in a fairly tremendous position this year! I have received a job offer from the one and only Silverman Backs, which is what I call incredible news. They’re moving me out to London next year to start. It’ll be an entry level salary, only like between 80 and 90k."
    hide max charm
    show max wink
    b "Evidently I’ll have to climb the ladder to get more."
    hide max wink
    show max happy
    "Ugh, this guy is gross. 80 thousand dollars as a starting salary? Right now anything over 20k sounds good to me. Also what the fuck? Why does everyone seem to be getting such great jobs right now?"
    m "Ok, well good for you man. That sounds great."
    b "It is fairly exceptional, yes. So what’s up with you?"
    "Well this is awkward. Nothing much at all is up with me. What am I doing with my life? Am I a failure as a person?"
    with hpunch
    "Oh god, I peaked at 18!"
    menu:
        "Embellish! Lie!":
            hide max neutral
            show max skeptic
            m "Actually, I’m doing great! I just got this huge job opportunity in my field so...I guess you could say we’re both succeeding."
            b "Oh--that’s--I see. How impressive."
            hide max skeptic
            show max charm
            b "I have to say I honestly did not expect that from you. Good for you."
            hide max charm
            show max happy
            m "Thanks, man. And you too."
            hide max happy with moveoutleft
            "Ok, I’m getting depressed just standing outside right now. Anyone else want to come up and tell me about their accomplishments? I think I’m just gonna spend the day in my room at this point. Yeah...that sounds like fun."
        "Tell the truth":
            m "You know, I’m kind of between things right now. Still getting back into school mode haha. But if you hear anything about internship opportunities hit me up! I’m actually looking for one right now."
            b "Oh...that’s awkward. Well--sorry? I have to say, you are so brave. I don’t even know what I’d do if I was a junior with zero internship prospects."
            if seduce_max:
                hide max neutral
                show max charm
            else:
                hide max neutral
                show max vicious
            b "That’s so humiliating, I’d probably just die or something."
            "Yeah, he definitely would. Pretty sure his life is his career. Oh, I’m sorry, ‘career.’ Yeah I said it. Good luck in the real world pal."
            hide max charm
            hide max vicious
            show max happy
            m "Well, not all of us can be as successful as you."
            b "It’s true, it’s true. Anyway, I suppose I’ll see you later. I always manage to run into plebians even when I’m not meaning to."
            hide max happy with moveoutleft
            "Wow. He couldn’t have made his exit any quicker than if I’d just confessed to being radioactive. Obviously figured I couldn’t advance his career."
            "Why did telling the truth back there not make me feel any better? I was the bigger person! I told my truth! But now I actually feel terrible. Huh. I think I’m just gonna spend the day in my room at this point. Yeah...that sounds like fun."
    jump endeswday1

label wrongedmarie:
    "Ugh, this line is long. Guess I don’t really have anywhere to be."
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    show marie happy with moveinright
    r "Oh, my god. %(pname)s, you’re here."
    "Shit. It’s my formerly-nice-turned-terrible-double-crossing-ex-roommate. Time to smile and act normal."
    m "Oh, uh, Marie. Hi."
    hide marie happy
    show marie ingenuine
    r "So good to see you! How was your summer?"
    "What’s happening? Why is she pretending to be nice to me?"
    m "Uh, not much. Just worked a lot of shifts at FishMart. You?"
    r "Oh, it was amazing! I got this super cool internship doing research--well it’s kind of under wraps right now so I shouldn’t say anything really, but let’s just say the future is looking bright!"
    show marie ingenuine at center, hop
    "Ah. Now I get it. She wants to brag and make me feel bad all for the price of one interaction. Well, it’s working. Dammit."
    show marie happy at sright with move
    show josh shock at sleft with moveinleft
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    j "Woah, Marie, so funny running into you!"
    hide josh shock
    show josh grateful at sleft
    j "This is so crazy brah I was just thinking of you."
    hide josh grateful
    show josh happy at sleft
    r "Oh my gosh, Josh! I totally didn’t know this is your favorite place to get lunch, haha. I guess we can..."
    show marie ingenuine at center with move
    r "have lunch together?"
    "Is she...flirting?"
    "What is happening right now?"
    hide marie ingenuine
    show marie concerned
    hide josh happy
    show josh happy at sleft
    j "Bro, that’s a bitchin’ idea. I’m so down."
    if fightwithjosh:
        jump joshstillbitter
    else:
        j "Oh hey %(pname)s, sorry bro didn’t see you there. Want to come to lunch with us?"
        hide marie concerned
        show marie angry
        hide josh happy
        show josh happy at sleft
        "Well, I would if I could but...I’m not on good terms with Marie. I don’t want to spend all of lunch having her rub her success in my face."
        m "Um, I’m okay. Thanks for the offer though."
        hide marie angry
        show marie ingenuine
        r "Your loss, sweetie. Anyway, I’ve got my food so I guess we can move out."
        j "Yeah, uh, sounds good. See you later, %(pname)s."
        hide josh happy with moveoutleft
        hide marie ingenuine with moveoutleft
        jump lunchaloneesw

label endeswday1:
    scene bg singleroomd
    with dissolve
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    "It’s the first day of junior year, which should be exciting. But I’m already feeling weirdly bad. Why does everyone seem to be doing better than me? I’ve never even had one internship before, never mind these amazing career starting opportunities."
    "Also I spent most of the day in my room. So that probably didn’t help."
    "I guess all that’s left is to take this one day at a time."
    "Relax, %(pname)s. {p=1.0}You’re probably being paranoid. I’m sure plenty of people are in the same boat as you."
    scene black
    with dissolve
    scene bg singleroom with dissolve
    "Ugh, rise and grind!"
    "Let’s hope no one has any big job opportunities come to them today. I might have to kill someone. Jk jk...{p=1.0}unless?"
    "Okay, I kid. But seriously, yesterday was a major bust. I hope someone I know flunks a test today or something."
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg low
    with dissolve
    show marie happy at center with moveinbottom
    r "Oh my gosh, %(pname)s it’s you again! Wow, we just keep running into you, huh?"
    "'We'?"
    "Who's 'we'?"
    show marie happy at sright with move
    show josh happy at center with moveinbottom
    j "Oh hey %(pname)s. Marie and I were just taking a stroll around campus."
    "They were {i}taking a stroll{/i}? Why’s Josh being all weird?"
    "Wait hold on...are they like, on a date? Did Marie and Josh start dating while I wasn’t looking?"
    if fightwithjosh or marieevil:
        menu:
            "Make passive aggressive comment.":
                m "Well, good to see you guys hanging out together! Because, you know, I kinda think of you guys as like loner types. Glad you’re making friends."
                if fightwithjosh:
                    hide josh happy
                    show josh neutral at center
                hide marie happy
                show marie ingenuine at sright
                r "That’s right, it is great to make friends! Speaking of...where are your friends exactly?"
                m "In the bathroom, okay!? They’re coming right out. And they’re real. They exist they just had to leave for a second."
                if fightwithjosh == False:
                    hide josh happy
                    show josh neutral at center
                j "Uh...sure bro. Whatever floats your boat."
                m "You know what? I don’t have to justify myself to you! Have fun on your date or whatever this is, figures that you two would pick each other."
                if fightwithjosh:
                    hide josh neutral
                    show josh mad at center
                else:
                    hide josh neutral
                    show josh shock at center, hop
                j "What does that mean?"
                if marieevil:
                    hide marie ingenuine
                    show marie mad at sright
                else:
                    hide marie ingenuine
                    show marie surprised at sright, hop
                if fightwithjosh == False:
                    hide josh shock
                    show josh sad at center
                m "Oh, you know. It’s just that people like you tend to find each other. Like, you know, ditzy types."
                if marieevil == False:
                    hide marie surprised
                    show marie cry at sright
                r "%(pname)s, I think it would be best if you left."
                m "I was just thinking of leaving myself, actually. I’m meeting up with a friend. Bye."
                if marieevil:
                    hide marie mad with moveoutright
                else:
                    hide marie cry with moveoutright
                if fightwithjosh:
                    if marieevil == False:
                        j "I see you're still the same awful person."
                        hide josh mad with moveoutright
                    else:
                        "Bye."
                        hide josh mad with moveoutright
                else:
                    "Bruh... bye?"
                    hide josh sad with moveoutright
            "Stalk away in a huff":
                "Those two are dating?? Why does it feel like everyone in my life is pairing off except me? Oh god, I’m gonna die alone and I’m not even going to have a good career to show for it! I’ll just be lonely and sad. I hate this. Why are other people happy and I’m not??"
                hide josh happy with moveoutright
                hide marie happy with moveoutright
    else:
        m "Oh...I didn’t realize you two were close. Glad y’all are hanging out!"
        "Y’all?? I sound like a weirdo."
        hide marie happy
        show marie grateful at sright, hop
        r "Well...I guess you could say we’ve been getting closer lately."
        "Ew. I did not need to hear that."
        menu:
            "Ask how they're doing.":
                hide marie grateful
                show marie happy at sright
                m "So...how are you guys?"
                hide josh happy
                show josh v grateful at center
                j "I’m doing pretty great, dude! Columbia just approved a huge grant for me to go to Paris and do research about, like, reading and shit. It’s gonna be my thesis project. I’m leaving for two months next semester!"
                "Definitely shouldn’t have asked."
                hide josh v grateful
                show josh happy
                m "Oh that’s...great. Sounds like an amazing opportunity."
                r "But wait til you hear the even better news..."
                hide marie happy
                show marie v happy at sright, hop
                r "I’m going with him! Yeah, I know it’s crazy timing. I’m studying abroad in Paris next semester and we’ll be living right across the street from each other."
                "Well isn’t that just groovy."
                hide marie v happy
                show marie happy at sright
                m "Cool. That’s amazing. Well anyway, I got a friend waiting for me in Ferris so I should probably skeddadle. Congrats on your stuff though."
                j "Thanks, bro!"
                hide josh happy with moveoutright
                hide marie happy with moveoutright
                "So Josh and Marie are dating now. Am I blind for not seeing that coming?"
                scene bg singleroomd with dissolve
                "I’ve never even been in a relationship."
                "Am I a freak?"
                "Oh god, I’m never going to find someone am I?"
                "I’m just gonna while away the rest of my days, alone in my parents’ basement."
            "Make an excuse and go.":
                m "I actually gotta go, have a friend waiting. See you guys later!"
                hide josh happy with moveoutright
                hide marie happy with moveoutright
                "Those two are dating?? Why does it feel like everyone in my life is pairing off except me?"
                "Oh god, I’m gonna die alone and I’m not even going to have a good career to show for it! I’ll just be lonely and sad."
                "I hate this."
                "Why are other people happy and I’m not??"
                scene bg singleroomd with dissolve
        "I’m looking at my future and it’s so dark."
        "Just like this room... {p=.5}oh shit it’s 3 a.m. Bedtime I guess?"
        "But how am I supposed to sleep when I’m so full of existential dread?"
        jump dawnofthelastday

label dawnofthelastday:
    scene black
    with Pause(1)
    show text "{size=50}Yet life goes on...{/size}"
    with Pause(2)
    hide text
    scene bg ferris with dissolve
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    "Ah, the smell of rubbery Ferris eggs in the morning. There’s nothing like it. Okay, all I have to do today is avoid Marie and Josh who are apparently the most successful people I have ever and will ever meet. Should be easy enough."
    r "OH MY GOD"
    "You’re kidding. Oh wait, she’s not talking to me. What’s--"
    with hpunch
    j "THIS IS SO CRAZY BRO WHAT THE HECK?!?"
    "What’s--"
    show josh happy at left with moveinleft
    j "HEY EVERYONE! Marie just won the lottery! This is the craziest day of my life!!"
    "Is this a joke."
    hide josh happy with moveoutleft
    "I don’t need to see or hear this for the sake of my battered ego if nothing else."
    r "Oh my gosh I’m hyperventilating. I need to sit down. I just won twenty million dollars."
    j "Marie...you’re like, so rad dude. I know this feels crazy, but I feel like the universe is sending us a sign. That it wants us to be together and make a life together."
    j "Marie, when the madness of Columbia University in the City of New York has passed...will you marry me?"
    "What the fuck."
    r "I do! I mean, I will! Jeepers I’m all mixed up."
    "I have to get out of here before I throw up."
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg low with pushleft
    "I’m actually not sure what just happened. Did I hallucinate that?"
    c "Josh, Josh, Josh, Josh!"
    "And am I hallucinating right now? What are people shouting?"
    c "JOSH, JOSH, JOSH, JOSH!"
    with pixellate
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    j "Aw shucks, this is so embarrassing. You guys don’t need to make so much of a fuss!"
    show josh grateful at center with moveinbottom
    m "Josh? Hey, Josh? What...what’s happening?"
    hide josh grateful
    show josh v grateful
    j "Aw, dude, what a rad day huh! First I get engaged to Marie and now I just won the big game! I guess people are pretty jazzed about that, ha"
    "So many things he just said make no sense."
    m "Didn’t you get engaged to Marie like...thirty seconds ago? When did you have time to win a ‘big game?’ And what big game, by the way? We literally just came back to school like two days ago."
    hide josh v grateful
    show josh shock
    j "The sports game, bro! Didn’t you hear?"
    m "{i}What sport{/i}, Josh?"
    j "The big one! The big sports game!"
    hide josh shock
    show josh v grateful
    j "Aw shucks, it’s so embarrassing how much of a fuss they’re all making."
    hide josh v grateful
    show josh happy
    m "Hold on, none of this makes sense. Aren’t you scaling back on sports in your senior year? Also, why the hell did you propose to Marie? Didn’t you literally just start dating?"
    j "Aw, dude, what a rad day huh!"
    m "That’s the second time you’ve said that. Do you realize you’re repeating yourself?"
    hide josh happy
    show josh neutral
    j "Uh...bro...what a rad day huh!"
    "Is Josh broken? Whatever’s going on I need to get out of here. Pretty sure this is some kind of bad acid trip or something."
    $renpy.music.set_volume(0.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene black
    with dissolve
    scene bg singlemaried with dissolve
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.play("audio/SlothMain.mp3", channel="Chan1", synchro_start=True)
    "Not gonna lie, that was highkey creepy. That almost didn’t feel...real. Am I hallucinating right now?"
    "Maybe I’ll just take a nap? Sleeping it off might work."
    scene black
    with dissolve
    scene bg singlemarie with dissolve
    "I think that worked! I do feel refreshed now. I had the weirdest dream about Josh and Marie…"
    "Speaking of Josh and Marie...their accomplishments are starting to really bum me out!"
    "I honestly thought they were still working their lives out just like me, but all of a sudden they have jobs and relationships. Where does that leave me? What does it say about me that I don’t have those things?"
    "I probably should actually take time today to focus on all the shit I have to get done before classes start."
    "But I kind of...don’t feel like it?"
    "All I can think about is Josh and Marie, Marie and Josh. It’s like, my brain is stuck on them or something. Why do they have all the things I want?"
    "Why do other people get to be happy and I don’t?"
    "Wait a second."
    "Something feels off about this room."
    with hpunch
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.play("audio/Wrath.mp3", channel="Chan1", synchro_start=True)
    "How did I not notice before? This isn’t my room it’s...Marie’s."
    "But wait, that doesn’t make sense. Why would I walk into Marie’s room instead of my own? That’s so random?"
    "And why does Marie have a box of matches lying open on her desk? Are we even allowed to have those?"
    "..."
    "Why does Marie get all the things I want? She’s like me, but if I didn’t do all the stupid shit I do. I want her life. Why can’t I have it? What’s to stop me from…"
    "..."
    menu:
        "Set fire to Marie's room.":
            $ sin = sin-5
            $ committedArson = True
            scene bg singleonfire
            $renpy.music.set_volume(0.2, delay=0.5, channel="Chan2")
            $renpy.music.play("audio/firesound.mp3", channel="Chan2", synchro_start=True)
            "The fire catches weirdly quickly. I kind of thought this would be hard to do actually but...nope. As it spreads, I run outside..."
            "no..."
            "wait."
            scene bg lowonfire
            "Somehow I’m in front of Lowe Steps. Lowe is on fire too. In fact, the whole college...could that be because of me? I don’t understand…"
            show marie mad
            r "Hi, %(pname)s."
            m "Marie! Oh thank god. I thought I was the only person alive in this school for a second. Have you called 911?"
            r "You set fire to my room."
            m "Oh...you know about that?"
            m "Marie, I swear, I don’t even know what happened, I think I blacked out for like fifteen minutes or something. There’s no way this could have been me. There’s just no way…"
            r "Haven’t you figured it out yet?"
            m "Figured what out? Marie, have you called 911?"
            r "There’s no need to call anyone. Everyone here already knows."
            r "We know everything you do."
            r "Every choice you’ve made in your time at Columbia, we’ve been watching you."
            r "We know who you are, %(pname)s. We know what you’re capable of."
            m "I don’t know what’s going on. Marie, our school is literally burning to the ground right in front of us. Where is everyone?"
            hide marie mad
            show marie urdumb
            r "You don’t get it. Well. You always have been slow on the uptake."
            m "Marie--what--"
            jump closecurtains
        "Don't do that":
            "I’ve got to get out of here. This place is putting weird things into my head. I can’t take this anymore."
            scene bg low
            show marie ingenuine
            r "Hi, %(pname)s."
            m "Oh...Marie. Hi. I’ve got to go actually, I’ve got a friend waiting for me and--"
            hide marie ingenuine
            show marie neutral
            r "No, you don’t."
            m "What?"
            r "You don’t have a friend waiting for you."
            r "You just left my room, where you were tempted to commit arson. Before that, you saw Josh be cheered for winning the big game and saw me win the lottery."
            r "I know where you’ve been and what you’ve done, %(pname)s. We’re always watching."
            m "Are you spying on me? That’s illegal! I could get you arrested for that."
            hide marie neutral
            show marie concerned
            r "Go ahead and try."
            r "In fact, go ahead and try dialing any number that does not belong to someone you’ve met at this school. I promise you, it won’t go through."
            r "Your phone isn’t connected to any cell service that exists in the United States."
            r "In the world, actually."
            m "Marie, you’re freaking me out. Can you just leave me alone?"
            r "Unfortunately, that’s something I can’t do. You see, I don’t actually exist without you. Well, I do, but this body does not. We’re linked, for better or worse."
            m "Stop being so weird and vague. If you have something to say, say it now."
            jump closecurtains

label closecurtains:
    #TODO: JUDGE 'EM FOR THEIR SINS or their love?
    hide marie concerned
    hide marie urdumb
    show marie neutral
    r "Do you remember moving into Columbia freshman year, %(pname)s? I know it feels like a long time ago. But do try to remember."
    m "Uh, I mean, I guess? I think I went to a party, hung out with my OL...why does that matter now? That was years ago."
    if committedArson or marieevil:
        hide marie neutral
        show marie urdumb
    r "No, before that. Before the party. Before you met Karen. What was it like moving into your dorm? Who did you meet on the way in? Did you bring your parents?"
    m "I...I don’t know, it was a long time ago! I just don’t remember!"
    hide marie urdumb
    show marie neutral
    r "You don’t remember because it didn’t happen."
    r "You came into existence on Columbia’s campus at the beginning of your first week here. You remember nothing before that because you never actually moved into Columbia University."
    hide marie neutral
    show marie averse
    r "You choked on a carrot the day before the first day of NSOP and died."
    hide marie averse
    show marie neutral
    r "And then...you came here."
    hide marie neutral
    show marie ingenuine
    r "I hope you’ll forgive us for having a little fun. The fire and brimstone gets so boring after a while."
    hide marie ingenuine
    show marie neutral
    r "Since you died right as your college life was beginning, we decided to set up a sort of test."
    r "Of how your time at Columbia would have gone, if you’d lived."
    m "Marie--what--why are you saying these things? I don’t understand."
    r "I think you do. I think you’ve always known. Somewhere, deep in the back of your head. You must have felt us watching you. We’re hard to miss."
    m "You said this was a--test? Of what? Did I pass?"
    jump howdidIdo

    ##Marie about to do some math on this bitch and read you
label howdidIdo:
    $friend_counter = 0
    r "Well, why don't we see if there's anything interesting in your file first."
    if marie_friendship > 3: #marie max +7, min -2 HOWEVER, only 3 of those are from gluttony
        $sin =+1
        $friend_counter +=1
        hide marie neutral
        show marie happy at center, hop
        r "You know, I have to admit at least I personally like you."
        if marieevil:
            if committedArson:
                hide marie happy
                show marie ingenuine
                r "You're such a crazy, two-faced person!"
                hide marie ingenuine
                show marie v happy at center, hop
                r "Burning down rooms and copying resumes. No crime too big or small I guess!"
                hide marie v happy
                show marie averse
                r "I would love to see you fail and stay with us. You'd fit right in."
                $sin =-2
                hide marie averse
                show marie neutral
            else:
                hide marie happy
                show marie neutral
                r "The resume thing was no good though."
                hide marie neutral
                show marie ingenuine
                r "Well, I suppose we all make mistakes."
                hide marie ingenuine
                show marie neutral
                r "But you still lost points for it."
        else:
            if committedArson:
                hide marie happy
                show marie averse
                r "However, it is unfortunate you couldn't resist just a little longer and not burn down my room."
                hide marie averse
                show marie ingenuine
                r "Don't worry though, that's definitely factoring into calculations."
                hide marie ingenuine
                show marie neutral
            else:
                r "If you do have to stay with us somehow, I'd be happy to be your friend still."
                hide marie happy
                show marie neutral
    elif marie_friendship <= 1:
        r "You probably already know how I feel about you personally."
        if committedArson:
            hide marie neutral
            show marie averse
            "She points at the fire and says nothing else on that."
        elif marieevil and marie_friendship >= 0:
            r "Would it have killed you to be a little nicer?"
            hide marie neutral
            show marie averse
            r "Oh and less of a cheater. That resume stunt sure was dumb."
        elif marieevil and marie_friendship < 0:
            r "Talk about a grade A jerk."
            r "Which is a better grade than you could hope for in anything else after you were dumb enough to pull that resume stunt."
        elif marie_friendship < 0:
            r "I don't think you could have been meaner to me if you tried!"
            hide marie averse
            show marie concerned
            r "I really did try being nice..."
        hide marie concerned
        hide marie averse
        show marie neutral
    if josh_friendship > 2: #josh max +6, min -6
        $friend_counter +=1
        $sin =+1
        hide marie neutral
        show marie happy
        r "Now, Josh is happy to vouch for you, but I'm sure you've noticed he's quite the nice character."
        if threwpizzamad:
            hide marie happy
            show marie neutral
            r "It really is kind of absurd considering that whole pizza incident, too."
            r "What {i}did{/i} you gain from berating him on top of ruining that pizza?"
        r "Still, a vote in your favor is a vote."
        hide marie happy
        show marie neutral
    elif josh_friendship < -3:
        hide marie neutral
        show marie mad
        r "Why were you so rude to Josh?"
        r "Not wanting to share a swipe is fine, but did you really have to say 'sucks to suck loser'?"
        hide marie mad
        show marie neutral
    if prof_friendship > 3: #bonden max +6, min -6
        $friend_counter +=1
        $sin +=1
        hide marie neutral
        show marie happy
        r "Professor Bonden's genuinely happy to recommend you! That's nice!"
        hide marie happy
        show marie neutral
    elif seduce_prof and bad_let:
        r "Mmm, hard to believe you really asked for a rec letter from professor Bonden."
        hide marie neutral
        show marie averse
        r "I'm sure you know why."
        hide marie averse
        show marie neutral
    elif bad_let:
        r "Sorry about your rec letter with Bonden by the way."
        r "I'm sure you realized it wasn't great."
    if maximillion_friendship >= 5: #max +7, -9
        $friend_counter +=1
        $sin +=2
        hide marie neutral
        show marie surprised
        r "Do you enjoy being degraded or something?"
        if seduce_max:
            r "Or maybe he was just part of your master plan to get into that club?"
            hide marie surprised
            show marie ingenuine
            r "The club called triangle. A very real club name."
            hide marie ingenuine
        else:
            r "How did you get along so well with Max?"
        hide marie surprised
        show marie neutral
        r "I guess it's sweet that he likes you though."
        r "In a twisted way."
    elif maximillion_friendship > 2:
        $sin +=1
        hide marie neutral
        show marie happy
        r "It was sweet of you to play along with Max a bit."
        r "His whole lord thing really is something."
        if seduce_max:
            r "I guess maybe you were a little into it though."
            "Did she just wink at me?"
    elif maximillion_friendship < -5:
        r "I guess being called commoner and plebian isn't your thing."
        r "I don't blame you for not getting along with Max."
        if sin <= -13:
            hide marie neural
            show marie averse
            r "But he's not the worst person here."
            hide marie averse
            show marie neutral
        else:
            r "Maybe in another life."
        if seduce_max:
            r "Though this result does shine a light on a certain choice..."
            r "A certain 'club position securing' choice."
    elif betray_max:
        hide marie neutral
        show marie concerned
        r "I'm sure it was pretty hard for Max to open up to you like that."
        r "And for you to laugh in his face?"
        r "That's really cruel even with his projected superiority complex."
        if seduce_max:
            r "Plus, I thought you two were 'closer' than that."
            "Gross."
        hide marie concerned
        show marie neutral
    if Marvenperfectrun:
        $friend_counter +=1
        hide marie neutral
        show marie v happy at center, hop
        $sin +=2
        r "The work you did in semester 4! Now that was impressive!"
        r "Marven was doing his best to get you off track, but you preserved and got a perfect grade!"
        r "On top of that, his review of you is glowing. You're the 'dankest memer' he's ever met."
        if stolesg and marieevil == False:
            hide marie v happy
            show marie averse
            r "I do wonder if he'd feel the same knowing about the study guide you 'found'..."
            hide marie averse
        hide marie v happy
        show marie neutral
    elif Marvensenpai:
        $friend_counter +=1
        hide marie neutral
        show marie happy
        $sin +=1
        r "It was pretty great that Marven opened up to you!"
        if failedPride:
            hide marie happy
            show marie neutral
            r "Unfortunately, it was at the cost of your grade."
            if ignoranceisbliss:
                hide marie neutral
                show marie averse
                r "Not that you'd have known considering you didn't check."
                hide marie averse
                show marie neutral
            if stolesg and marieevil == False:
                hide marie neutral
                show marie averse
                r "And I wonder how he'd feel if he knew about the study guide theft on top of the failure..."
                hide marie averse
                show marie neutral
            r "But we can't all be perfect."
            r "And to your credit, I suppose that semester was pretty difficult."
        else:
            r "And you passed the class! That actually {i}is{/i} a feat in itself. Marven really did try to slow you down."
            if stolesg and marieevil == False:
                hide marie neutral
                show marie averse
                r "I wonder how he'd feel if he knew about the study guide theft though..."
                hide marie averse
                show marie concerned
                r "Was it worth it to betray his trust?"
                hide marie concerned
                show marie neutral
    elif music_friendship < -1:
        r "Hmm... I get that Marven did kind of work against you passing the class in semester 4."
        r "But couldn't you have humored him just a bit?"
        if failedPride:
            if stolesg:
                hide marie neutral
                show marie mad
                r "You even stole his study guide and still failed! What was the point?"
                hide marie mad
            else:
                hide marie neutral
                show marie concerned
                r "And you failed anyway! What a tragic result of being unthoughtful."
                hide marie concerned
            show marie neutral
    if friend_counter == 5:
        hide marie neutral
        show marie v happy at center, hop
        r "I think honestly everybody is rooting for you."
        hide marie v happy
        show marie neutral
        r "Even if we will be sad to see you go."
    if success <= 0:
        r "By the way, I should tell you. It's probably a good thing this test isn't actually based on how well you did at this school."
        r "Because you didn't do great."
        r "So maybe it's good you didn't go to Columbia then?"
        r "I don't know. This situation was admittedly pretty special."
    elif success > 5:
        if friend_counter == 0:
            r "But at least, overall, you did decent work here."
        else:
            r "Aaaaaand, overall, you did pretty well in this faux college!"
            if marieevil == False:
                hide marie neutral
                show marie concerned
                r "I'm a little sorry you couldn't have done it on Earth instead."
                hide marie concerned
                show marie neutral
    r "There's not much else here worth commenting on."
    r "So without further ado, the results!"
    jump finaljudgment
    #currently there's a range of -23 to 11 possible sin points (before relationships factored in). Let's round that down to a nice -20 possible
    #-24 to 18 possible sin points after relationships factored
    #success max points 10 or -1

label finaljudgment:
    if sin > 11 and committedArson:
        hide marie neutral
        show marie surprised
        r "Talk about falling at the last barrier!"
        hide marie surprised
        show marie happy
        r "You would have passed with flying colors if not for the burning down the room part."
        hide marie happy
        show marie v happy at center, hop
        r "Maybe you just like fire? I know I do."
        r "Protip though! Don't do that anymore after you leave here."
        r "Which is to say, congrats on graduating from hell!"
        $ persistent.ending="end good"
        $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
        $renpy.music.play("audio/LimboDraftMain.mp3", channel="Chan1", synchro_start=True)
        scene bg black
        with dissolve
        window hide
        show goodend
        pause
    elif sin > 7 and committedArson:
        hide marie neutral
        show marie surprised
        r "I actually don’t know how you did it."
        hide marie surprised
        show marie concerned
        r "But you scraped by even with the little fire fiasco. Don’t worry, though, %(pname)s. Up there, they can be awfully picky about what behaviors they accept."
        hide marie concerned
        show marie happy
        r "I’ll give you a hint: arson isn’t one of them. But...for now."
        r "You did it. Congratulations. You’re graduating from hell."
        $ persistent.ending="end good"
        $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
        $renpy.music.play("audio/LimboDraftMain.mp3", channel="Chan1", synchro_start=True)
        scene bg black
        with dissolve
        window hide
        show goodend
        pause
    elif sin < 7:
        hide marie neutral
        show marie mad
        r "I think you know the results already, %(pname)s."
        r "The irony is, I’m sort of you, in a way. I’m the way your life could have gone, if you’d done all the right things and played your cards right. But you chose the path you chose. You chose selfishness, cruelty, and destructiveness."
        r "Welcome to hell, %(pname)s."
        $ persistent.ending="end bad"
        scene bg black
        with dissolve
        window hide
        show badend
        pause
    elif sin == 7:
        hide marie neutral
        show marie astonished
        r "..."
        r "Wait."
        r "This test can't be inconclusive."
        r "We have to run the numbers again. I-"
        $persistent.ending = "Inconclusive"
        with pixellate
    else:
        hide marie neutral
        show marie happy
        r "I think I can safely say your results are positive!"
        r "You know, it was a toss up, %(pname)s. Some of the things you did on Earth made us wonder if you’d be up to the challenge of the test. But you did it."
        r "You chose friendship over bitterness and generosity over vindictiveness."
        hide marie happy
        show marie v happy at center, hop
        r "Congratulations. You’re graduating from hell."
        $ persistent.ending="end good"
        $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
        $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
        $renpy.music.play("audio/LimboDraftMain.mp3", channel="Chan1", synchro_start=True)
        scene bg black
        with dissolve
        window hide
        show goodend
        pause
    jump credits

####

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Artists', 'Justin Chan'), ('Artists', 'Ren Huang'), ('Artists', 'Emmy Wang'), ('Artists', 'Kimberly Li'), ('Music', 'Ramy El Baghir'), ('Writers/Programmers', 'Sophia Gates'), ('Writers/Programmers', 'Tiffeny Chen'),('Writers/Programmers', 'Emmy Wang'), ('Writers/Programmers', 'Kimberly Li'), ('Writers/Programmers', 'Katrina'), ('Writers/Programmers', 'Sarah'),('Setting images', 'Columbia University'), ('Phone code', 'Nadia Nova'),('In-Game Messaging System code', 'saguaro'), ('Phone Sound Effects','by Notificationsounds.com is licensed under CC By 4.0'),('Credits code', 'DaFool'), ('Special thanks to:', 'CU Game Dev!')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.3.5" #Don't forget to set this to your Ren'py version

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
