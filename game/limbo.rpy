#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

image Karen flip = im.Flip("Karen.png", horizontal=True)

label limbobegin:
    scene black
    with Pause(1)
    show text "{size=50}Semester 1: Orientation{/size}"
    with Pause(2)
    hide text
    with dissolve
    scene bg columbialawn
    show Karen
    with dissolve
    k "Welcome to Columbia! I’m Karen, your orientation leader. What’s your name?"
    $ pname = renpy.input("My name is:")
    show Karen at sleft
    with move
    show marie happy at sright
    with moveinright
    r "Oh, hey! You must be my roommate! %(pname)s, right?"
    "Her face {i}is{/i} familiar. You think you must have flicked through her social media when roommates were assigned."
    m "That would be me! And you're..."
    "Shoot, how could I not remember my roommate's name?"
    show marie v happy at sright, hop
    r "Marie!"
    m "Marie! Of course."
    hide marie v happy
    show marie happy at sright
    r "I have to go to join my own orientation group now, but we should definitely talk later!"
    hide marie happy
    with moveoutright
    show Karen at center
    with move
    "Thank goodness for not having to come up with small talk."
    "Now I just need to get through the tour with my own group."
    scene bg lernerramps
    with fade
    show Karen
    with dissolve
    "At the end of the tour, everybody disperses extraordinarily quickly with the friends they've already made. I didn't really feel like I knew anybody in the group, so I'm quickly left alone with Karen."
    m "..."
    m "That was a lot of people to meet at once."
    k "Don’t sweat it! You’re still a new student, so it’s understandable to have some names mixed up."
    m "Yeah, I guess so."
    k "So you doing anything special this weekend? I can’t have any of my orientation kids be loners their first weekend here!"
    m "I still don't know."
    k "Lots of people are hosting cool events and they usually get posted on there."
    "Karen points at the line of pillars covered in posters."
    show Karen at center, hop
    k "Oh, shoot, I have a meeting! I’ll catch you later, %(pname)s."
    hide Karen
    show Karen at right
    with move
    k "Don’t be a loner! And stay out of trouble!"
    hide Karen
    with moveoutright
    "Well, that last part was unnecessary"
    "Hmm, what's this?"
    scene bg black
    with dissolve
    show PosterP
    "I guess I don’t have anything else going on Saturday night."
    "Wait a second…"
    "You have to RSVP?"
    #TODO: add sound: decline sound
    "Aaaand the QR code has expired. Of course."
    "Still, maybe a bunch of people signed up and aren’t gonna end up going. I’ll go anyway and see if I can find my way inside."
    scene bg partyline
    with dissolve
    #TODO: add sound: general crowd noise
    "What’s this crowd, is it for the party?! There must be at least 50 people trying to get in! I wasn’t expecting it to be this popular…"
    "I might not be able to just get in like I’d hoped."
    scene bg partylinefront
    with dissolve
    "After waiting for around 15 minutes, I get to the front. There’s a student with a piece of paper letting people in. The door is open."
    "He turns to me."
    w "Hey, what's your name?"
    m "%(pname)s."
    w "Hmmm.... I don't see you on the list, %(pname)s"
    m "Really? That's weird. Can you check again?"
    "I'm not on the list. I know that."
    "But wait, I think I spot a familiar face through the door."
    show Karen at right
    with moveinright
    "Is that Karen? Maybe she can help me get in!"
    w "Nope, not on the list this time either."
    "It’s a long shot, but I think if I say I’m with Karen and call her over, she might cover for me and help me get inside."
    "On the other hand, it’s a little unfair for everyone else who’s been waiting for a long time."
    "I have to act now. What should I do?"
    $ getinparty = False
    menu:
        "Leave the party":
            hide Karen
            "I don’t want to put her on the spot like that."
            "Plus, it’s not really fair to the people already on the list. I might as well go do something else with my night."
            m "Oh, ok."
            w "Yeah, so I can't let you in. Sorry."
            m "It's ok."
            "I wave goodbye as I walk away."
            m "Have a good night!"
            jump limboend
        "Call Karen over":
            m "Actually, I'm here with her!"
            "I point through the doorway at Karen."
            show Karen flip at right, hop:
            m "Hey Karen!"
            "Somehow, Karen heard me in the middle of all the noise in there. She smiles brightly as she rushes to the door."
            k "Hey, %(pname)s! How are you doing?"
            m "Hey! I’m trying to tell this guy that I’m here with you."
            k "Oh yeah, totally! I just got here a little early."
            k "You remember signing me in early, right?"
            w "I think so?"
            k "Awesome. Yeah, they're with me."
            "She grabs my hand and pulls me inside before he has a chance to respond."
            hide Karen flip
            show Karen at right
            hide Karen
            with moveoutright
            "As we quickly retreat from the doorway, I see him shrug as he turns back to the crowd outside."
            "The party ends up being a lot of fun, thanks to Karen for getting me in. I never expected my orientation leader to look out for me like that! I gotta say, I’m pretty optimistic about this school now."
            $ getinparty = True
            jump limboend

label limboend:
    scene bg columbialawn
    with dissolve
    "I'm really glad I made the right choice last night."
    if getinparty:
        "That party was so fun!"
    else:
        "It’s only fair that I couldn’t get in. I’ll have to sign up earlier next time."
    "As I head toward the dining hall, I see a lot of people on the lawn. Some are playing frisbee, and a lot are sitting in the grass, enjoying the sunshine and the breeze."
    "Suddenly, I hear a “Hey!” and someone taps my shoulder."
    show Karen at center
    with moveinleft
    "It’s Karen."
    if getinparty:
        k "Hey, %(pname)s! How was the rest of your night?"
        m "Hey, Karen! It was alright. I was pretty exhausted after the party. How about you?"
        k "Oh man, it was so fun. I’m glad you were able to make it."
    else:
        k "Hey %(pname)s! How was your night?"
        m "Hey, Karen! It was alright. I spent the night in, just relaxing. How about you?"
        k "Oh man, the party was so fun. It’s too bad you couldn’t make it."
    k "Up to anything special today?"
    m "No, not really. Why?"
    k "How about we grab lunch? I wanna give you a few extra pointers about the school."
    m "Sure, that sounds good. What time are you thinking?"
    k "Oh, I think any time before the dining hall closes should be good. My dorm is really close to it, so just let me know when you’re ready to go."
    m "Ok! Sounds good."
    k "Until then, there’s a lot of people out on the lawn right now. Why don’t you mingle and get to know a few of them?"
    "Mingle on the lawn?"
    if getinparty:
        "I did meet some cool people yesterday. Maybe one of them is out here."
    else:
        "I did miss out on that party yesterday. This would be a good chance to meet some new people."
    "Yeah, that’s a good idea! I think I’ll do that."
    k "Great! I’m so excited for you. I’ll see you at lunchtime. Just shoot me a text, kay?"
    hide Karen
    with moveoutright
    m "Sure thing! See you later."
    "I turn back towards the dining hall, looking forward to the day."
    "I look at the people playing frisbee as I step onto the lawn."
    if getinparty:
        "After a second, I realize I recognize one of the players from the party. I greet him and he invites me to join the game."
    "It looks pretty fun, so I decide to join them."
    "I get to know everyone as we’re tossing the disc, and they’re pretty friendly. So friendly that I relax into enjoying the day like everyone else, without a care."
    "After some time, I decide to take a break and check my phone. Three texts from Karen."
    call phone_start
    call message_start("Karen", "Dining hall closes in 30 minutes, wanna meet there now?")
    call message("Karen", "?")
    call message("Karen", "15 minutes left for fooood")
    call phone_end
    m "Oh man, sorry guys, I have to go! I’m supposed to meet a friend for lunch."
    w "What? Oh come on, %(pname)s"
    w "Just stay out here. The teams will be uneven if you leave!"
    "I am really enjoying my time out here, and I don’t really want to leave. At the same time, I also made a promise to Karen. What should I do?"
    menu:
        "Stay on the lawn":
            #make the scene fuzzier and fuzzier
            "It’s only 10 minutes left until lunch closes anyway. I’m sure Karen will be alright if I miss out this time. I can just apologize later. Plus, I really would rather keep hanging out here."
            m "Alright, fine. But we get possession!"
            w "Awesome! Yeah, you guys get possession."
            "We keep playing on the lawn, having a great time."
            "I start to lose track of time again."
            "But this time, {p=1.0}I don’t really care."
            "Back and forth, we throw the frisbee, joking around with each other. {p=1.0}Eventually we start moving a little slower. But we all want to keep playing. {p=1.0}The running slowly morphs into walking."
            "We all have our hands up waiting to catch a disc."
            "Every so often, I catch one, and I slowly throw it to someone else. Without even looking."
            "We want to keep playing."
            "Now we’re all standing, with one arm up waiting for a disc. {p=1.0}Everyone’s smiles have been replaced with blank stares."
            "The others on the lawn are doing the same thing."
            "We want to keep playing."
            ".{p=1.0}.{p=1.0}."
            "We’re still standing."
            "I don’t remember the last time the frisbee was thrown."
            "I’m waiting for a frisbee."
            "I’m waiting."
            #ENDING: INFINITE FRISBEE GAME
        "Meet Karen":
            m "Sorry guys, I’ll have to catch you later!"
            w "Alright, fine. See you later, %(pname)s."
            scene bg john jay
            with dissolve
            "I hurry to the dining hall and find Karen sitting at a table."
            m "Hey, Karen! Sorry I’m late, I lost track of time."
            k "Hey, %(pname)s. No worries, I know how it goes."
            "Once you’re on that lawn, it’s really hard to leave."
            m "Yeah, exactly!"
            k "Ok, go get your food before they take it all away."
            m "Right! Be right back."
            "I quickly get my food and sit down."
            jump roommateintro
