#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

$ fightwithjosh = False
$ marieevil = False

label beginenvy:
    "How is it that I’m already a junior, but I don’t feel any more mature than when I was a freshman? I thought by this point in my life I would have things more figured out, but I feel pretty much the same as I did before."
    "I don’t have that many swipes this year. Time to check out the food carts."
    ##figure out the values we should expect Marie to be at
    if marieevil:
        jump wrongedmarie
    else:
        jump goodtermswmarie

label goodtermswmarie:
    "Ugh, this line is long. Guess I don’t really have anywhere to be."
    show marie v happy at center, hop
    r "Oh my gosh, %(pname)s! So good to see you. How was your summer?"
    hide marie v happy
    show marie happy
    m "Oh, you know, pretty good. Worked a lot of shifts at FishMart. They asked me to stay on as a manager and everything, but I had to say no obviously."
    hide marie happy
    show marie grateful
    r "Wow, that’s so flattering! I bet you were a great employee."
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
    show josh happy
    with moveinleft
    hide marie grateful
    show marie happy at right
    with move
    j "Woah, Marie, so funny running into you! This is so crazy brah I was just thinking of you."
    hide marie happy
    show marie nervous at right, hop
    r "Oh my gosh, Josh! I totally didn’t know this is your favorite place to get lunch, haha. I guess we can..."
    r "have lunch together?"
    "Is she...flirting?"
    "What is happening right now?"
    j "Bro, that’s a bitchin’ idea. I’m so down."
    if fightwithjosh:
        jump joshstillbitter
    else:
        jump ongoodtermswjosh

label ongoodtermswjosh:
    j "%(pname)s, you coming too? We could all go over to sit on Lowe Steps to eat."
    "I feel like Marie kind of wants a moment alone with Josh. Maybe I should let them do their thing and not intrude."
    menu:
        "Have lunch with them":
            m "Yeah, I’ll come along. Sounds fun!"
            j "Cool beans, let’s head out! Once we get our food of course."
            r "So, Josh, how was your summer? You’re so talented, I bet you’re doing incredible things!"
            j "Ha, well, I don’t know about incredible, dude. But I can’t lie, this summer was totally going off! I got this amazing job opportunity at Dolphin Classics, where I was totes, like, working as an assistant editor. It was this crazy thing, but so dope!"
            r "Wow, Josh, that’s so cool! Isn’t your dream job working in publishing?"
            j "Yeah bro, pretty much. I feel like I’m moving forward in my career right in time to graduate. And they’re letting me stay on part time this year so maybe it could even be my first job out of college."
            r "Josh, I’m so happy for you. It’s everything you’ve been wanting these past few years."
            m "Yeah, Josh, that’s great. It’s definitely...everything you’ve been wanting."
            "Is it just me, or did both Marie and Josh get crazy lucky opportunities almost at the exact same time? Now I feel weird that I don’t have news to share. Just last year it felt like we were all on the same level, but now they’re both so much farther than me in their careers."
            "Okay, maybe I’ll ask Josh about something that’s a little more stressful. I’m not proud of this, but I want to hear that he’s got some struggles too."
            m "So Josh, how’s baseball going? I know it’s been hard to balance school and sports sometimes these past three years."
            j "Dude, you have a good point. I’m actually scaling back a lot this year. Coach understands that my degree has to come first. I haven’t been playing so well anyway so I think he was okay with my switching to (insert sports demotion here, I have no idea how this works)."
            m "Oh well that’s... [p=1.0]great."
            "So he’s like...doing fine? He’s not struggling at all? No offense to Josh, but he was always the one who made me feel better about not having my shit together. Now suddenly he has his shit together way more than me."
            r "Oh look, it’s Marven! Hey Marven, come say hi!"
            a "Hey guys, what’s up? Good to see you’re looking well %(pname)s."
            "Ew."
            j "We’re just hanging out man, what’s up with you?"
            a "I’m pretty good, nothing much going on with me."
            "Well that’s a relief at least. Thank god Marven doesn’t have some big accomplishment to tell us about."
            a "I mean...okay, I did just get hired by Amazim but I don’t want to brag or anything. I’m sure you guys have cool stuff going on too."
            "Ah. Okay. Well...shoot me. Also, what’s with all this fake modesty? I bet he’s crowing on the inside."
            a "You know, Amazim like really really hard to get an internship at, nevermind a job. They called me a...well like, just quoting them or whatever, but they called me a prodigy. And yeah, before you ask, it’s true that my uncle is a top executive there but let me just say that that had NOTHING to do with the hiring process."
            "There’s the old Marven I know and love. Okay, to be honest, all this is stressing me out. Anyone else want to come up and tell me all about their accomplishments? At this point, I kind of want to just spend the rest of the day in my room where no one can find me and tell me how succesful they are. Yeah...that sounds like fun."
            jump endeswday1
        "Pass on lunch":
            jump lunchaloneesw

label joshstillbitter:
    "Is he gonna invite me?"
    m "*cough* well, bye Marie."
    j "Oh…%(pname)s, um, didn’t see you there."
    #crickets
    j "Uh...how are you?"
    "Well screw this. Now I feel like a third wheel. Last thing I’m gonna do is admit I’m not doing anything right now. Jeez, I guess I’d better come up with a believeable sounding lie real quick."
    m "I’m great. Just got this huge job opportunity in my field so...no complaints here."
    j "Wow, that’s amazing. That’s such a coincidence, I just got a huge opportunity too. I’m so glad you’re doing so well."
    "Is he being sincere? He seems weirdly genuinely happy for me. Does he not remember our fight? I kind of feel bad for lying now."
    m "What was the opportunity?"
    j "I got this cool gig at Dolphin Classics, where I was totally, like, working as an assitant editor."
    r "Wow, Josh, that’s so cool! Isn’t your dream job working in publishing?"
    j "Yeah bro, pretty much. I feel like I’m moving forward in my career right in time to graduate. And they’re letting me stay on part time this year so maybe it could even be my first job out of college."
    r "Josh, I’m so happy for you. It’s everything you’ve  been wanting these past few years."
    m "Yeah that’s...great. It’s definitely...everything you’ve been wanting."
    r "Oh, there’s my food!"
    j "Got mine too. Well, um...catch you later #name. Nice to catch up."
    m "Yeah...right. So nice."
    jump lunchaloneesw

label lunchaloneesw:
    m "Nah, you guys go ahead. I have some errands I gotta run anyway so I should eat fast."
    j "Cool, bro, catch you later!"
    "Well, it did seem like they were having a moment. I suddenly kind of felt like the third wheel. They both seem so happy. I guess other people have their shit together right now more than I thought."
    #transition
    #max says snarky intro
    "Great. This is just who I needed today."
    m "Oh, hey Max. How’re you doing?"
    #TODO: finish up this part with Max after script
    jump endeswday1

label wrongedmarie:
    "Ugh, this line is long. Guess I don’t really have anywhere to be."
    r "Oh, my god. %(pname)s, you’re here."
    "Shit. It’s my formerly-nice-turned-terrible-double-crossing-ex-roommate. Time to smile and act normal."
    m "Oh, uh, Marie. Hi."
    r "So good to see you! How was your summer?"
    "What’s happening? Why is she pretending to be nice to me?"
    m "Uh, not much. Just worked a lot of shifts at FishMart. You?"
    r "Oh, it was amazing! I got this super cool internship doing research--well it’s kind of under wraps right now so I shouldn’t say anything really, but let’s just say the future is looking bright!"
    "Ah. Now I get it. She wants to brag and make me feel bad all for the price of one interaction. Well, it’s working. Dammit."
    j "Woah, Marie, so funny running into you! This is so crazy brah I was just thinking of you."
    r "Oh my gosh, Josh! I totally didn’t know this is your favorite place to get lunch, haha. I guess we can..."
    r "have lunch together?"
    "Is she...flirting?"
    "What is happening right now?"
    j "Bro, that’s a bitchin’ idea. I’m so down."
    if fightwithjosh:
        jump joshstillbitter
    else:
        j "Oh hey %(pname)s, sorry bro didn’t see you there. Want to come to lunch with us?"
        "Well, I would if I could but...I’m not on good terms with Marie. I don’t want to spend all of lunch having her rub her success in my face."
        m "Um, I’m okay. Thanks for the offer though."
        r "Your loss, sweetie. Anyway, I’ve got my food so I guess we can move out."
        j "Yeah, uh, sounds good. See you later, %(pname)s."
        jump lunchaloneesw

label endeswday1:
    "It’s the first day of junior year, which should be exciting. But I’m already feeling weirdly bad. Why does everyone seem to be doing better than me? I’ve never even had one internship before, never mind these amazing career starting opportunities."
    "Also I spent most of the day in my room. So that probably didn’t help."
    "I guess all that’s left is to take this one day at a time. Relax, %(pname)s. You’re probably being paranoid. I’m sure plenty of people are in the same boat as you."
    #start of next day
    "Let’s hope no one has any big job opportunities come to them today. I might have to kill someone. Jk jk...unless?"
    "Okay, I kid. But seriously, yesterday was a major bust. I hope someone I know flunks a test today or something."
    r "Oh my gosh, %(pname)s it’s you again! Wow, we just keep running into you, huh?"
    "'We'?"
    "Who's 'we'?"
    j "Oh hey %(pname)s. Marie and I were just taking a stroll around campus."
    ##ITALICIZE taking a stroll
    "They were taking a stroll? Why’s Josh being all weird? Wait hold on...are they like, on a date? Did Marie and Josh start dating while I wasn’t looking?"
    if fightwithjosh or marieevil:
        menu:
            "Make passive aggressive comment.":
                m "Well, good to see you guys hanging out together! Because, you know, I kinda think of you guys as like loner types. Glad you’re making friends."
                r "That’s right, it is great to make friends! Speaking of...where are your friends exactly?"
                m "In the bathroom, okay!? They’re coming right out. And they’re real. They exist they just had to leave for a second."
                j "Uh...sure bro. Whatever floats your boat."
                m "You know what? I don’t have to justify myself to you! Have fun on your date or whatever this is, figures that you two would pick each other."
                j "What does that mean?"
                m "Oh, you know. It’s just that people like you tend to find each other. Like, you know, ditzy types."
                r "%(pname)s, I think it would be best if you left."
                m "I was just thinking of leaving myself, actually. I’m meeting up with a friend. Bye."
                j "Bruh...bye?"
            "Stalk away in a huff":
                "Those two are dating?? Why does it feel like everyone in my life is pairing off except me? Oh god, I’m gonna die alone and I’m not even going to have a good career to show for it! I’ll just be lonely and sad. I hate this. Why are other people happy and I’m not??"
    else:
        m "Oh...I didn’t realize you two were close. Glad y’all are hanging out!"
        "Y’all?? I sound like a weirdo."
        r "Well...I guess you could say we’ve been getting closer lately."
        "Ew. I did not need to hear that."
        menu:
            "Ask how they're doing.":
                m "So...how are you guys?"
                j "I’m doing pretty great, dude! Columbia just approved a huge grant for me to go to Paris and do research about, like, reading and shit. It’s gonna be my thesis project. I’m leaving for two months next semester!"
                "Definitely shouldn’t have asked."
                m "Oh that’s...great. Sounds like an amazing opportunity."
                r "But wait til you hear the even better news...I’m going with him! Yeah, I know it’s crazy timing. I’m studying abroad in Paris next semester and we’ll be living right across the street from each other."
                "Well isn’t that just groovy."
                m "Cool. That’s amazing. Well anyway, I got a friend waiting for me in Ferris so I should probably skeddadle. Congrats on your stuff though."
                j "Thanks, bro!"
            "Make an excuse and go.":
                m "I actually gotta go, have a friend waiting. See you guys later!"
                "Those two are dating?? Why does it feel like everyone in my life is pairing off except me? Oh god, I’m gonna die alone and I’m not even going to have a good career to show for it! I’ll just be lonely and sad. I hate this. Why are other people happy and I’m not??"
    "So Josh and Marie are dating now. Am I blind for not seeing that coming? I’ve never even been in a relationship. Am I a freak? Oh god, I’m never going to find someone am I? I’m just gonna while away the rest of my days, alone in my parents’ basement. I’m looking at my future and it’s so dark. Just like this room...oh shit it’s 3 a.m. Bedtime I guess? But how can I sleep when I’m so full of existential dread?"
    jump dawnofthelastday

label dawnofthelastday:
    "Ah, the smell of rubbery Ferris eggs in the morning. There’s nothing like it. Okay, all I have to do today is avoid Marie and Josh who are apparently the most successful people I have ever and will ever meet. Should be easy enough."
    r "OH MY GOD"
    "You’re kidding. Oh wait, she’s not talking to me. What’s--"
    #screen shake?
    j "THIS IS SO CRAZY BRO WHAT THE HECK?!?"
    "What’s--"
    j "HEY EVERYONE! Marie just won the lottery! This is the craziest day of my life!!"
    "Is this a joke."
    r "Oh my gosh I’m hyperventillating. I need to sit down. I just won twenty million dollars."
    j "Marie...you’re like, so rad dude. I know this feels crazy, but I feel like the universe is sending us a sign. That it wants us to be together and make a life together. Marie, when the madness of Columbia University in the City of New York has passed...will you marry me?"
    "What the fuck."
    r "I do! I mean, I will! Jeepers I’m all mixed up."
    "I have to get out of here before I throw up."
    #outside
    "I’m actually not sure what just happened. Did I hallucinate that?"
    #you need a new name tag
    w "Josh, Josh, Josh, Josh!"
    "And am I hallucinating right now? What are people shouting?"
    w "JOSH, JOSH, JOSH, JOSH!"
    j "Aw shucks, this is so embarrassing. You guys don’t need to make so much of a fuss!"
    m "Josh? Hey, Josh? What...what’s happening?"
    j "Aw, dude, what a rad day huh! First I get engaged to Marie and now I just won the big game! I guess people are pretty jazzed about that, ha"
    "So many things he just said make no sense."
    m "Didn’t you get engaged to Marie like...thirty seconds ago? When did you have time to win a ‘big game?’ And what big game, by the way? We literally just came back to school like two days ago."
    j "The sports game, bro! Didn’t you hear?"
    #italicize what sport
    m "What sport, Josh?"
    j "The big one! The big sports game! Aw shucks, it’s so embarrassing how much of a fuss they’re all making."
    m "Hold on, none of this makes sense. Aren’t you scaling back on sports in your senior year? Also, why the hell did you propose to Marie? Didn’t you literally just start dating?"
    j "Aw, dude, what a rad day huh!"
    m "That’s the second time you’ve said that. Do you realize you’re repeating yourself?"
    j "Uh...bro...what a rad day huh!"
    "Is Josh broken? Whatever’s going on I need to get out of here. Pretty sure this is some kind of bad acid trip or something."
