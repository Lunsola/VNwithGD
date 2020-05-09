#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

label beginenvy:
    "How is it that I’m already a junior, but I don’t feel any more mature than when I was a freshman? I thought by this point in my life I would have things more figured out, but I feel pretty much the same as I did before."
    "I don’t have that many swipes this year. Time to check out the food carts."
    ##figure out the values we should expect Marie to be at
    #assume nice:
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
    ##insert check for fight with josh
