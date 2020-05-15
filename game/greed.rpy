label career_fair_intro:
    scene black
    with Pause(1)
    show text "{size=50}Semester 3: What's this? More School{/size}"
    with Pause(2)
    hide text
    ##scene bg careerfair1

    "It's finally the day of the career fair! I will make something out of
    myself today just like Pres Beau wanted."

    "I guess I need to go talk to some recruiters though..."

    ##scene bg careerfair2

    "Ah! MicroHard! That's a really competitive company... Ugh... I should
    probably apply shouldn't I..."

    show Karen

    define recruit = Character("Recruiter")

    "Ugh... I should introduce myself..."
    m "Hello! Ugh...I'm %(pname)s"
    m "Um...I'm really interested in your company! What internship opportunities
    do you have for undergraduates?"

    recruit "Yes, well we have several hands-on opportunities for all years!
    If you are interesting in applying..."

    ##fade bg Burner

    "That was exhausting. I should..."

    menu:
        "Go back to my dorm.":
            "You return to your room."
            jump career_dorm

        "Stay in Burner a while longer.":
            "You loiter around the outside of Burner."
            jump career_Burner

label career_dorm:

    scene bg bedroom with fade

    "Ah, finally it's time to nap."

    show marie happy with moveinleft

    r "Hey, %(pname)s"
    r "You just came back from the career fair right? How was it?"
    menu:
        "Ugh...It was awful. I hate networking.":
            $marie_friendship+=1
            show marie neutral
            m "To be honest, it was pretty overwhelming. I feel so much pressure to be try and keep up with all of our successful classmates"
            r "You shouldn't compare yourself or sell yourself short. You're just as successful as anyone else here"
            m "I don't know. I'm really worried about getting an internship for the summer. It feels like everyone I know has secured one at some big name company"
            r "Don't worry! I'm also still searching. People who've already got theirs are certainly more vocal than those that haven't. Just take things at your own pace"
            r "We just need to keep applying! It's a numbers game after all"
            m "Ughh, can that number be my internship acceptance letter"
            r "It will be soon!"
        "Overall, I think it was an alright experience":
            "I'm stil dwelling over my worry about finding an internship but no need to tell Marie that"
            m "It was fine. Just what you would expect from a typical career fair. Subtle to heavy flexing all around"
            r "That's good! I feel like career fairs can be draining, constantly needing to talk yourself up to a stranger but it's a great opportunity"
            m "Yep. yep."
            r "Things can get stressful. I'm always here if you ever want to talk!"
        "I think I've secured my internship from this!":
            "What internship worries? After my stellar conversations today, I should be getting that internship in no time"
            m "It was pretty amazing! I think that I might be recruited to Gaagle"
            "I had left my resume on the pile and everything"
            r "Yay! I'm so happy for you"
            show marie v happy at center,  hop
            r "You're a bit hard to read sometimes. It's okay to lower your guard around!"
    jump career_email

label career_Burner:
    show max charm
    b "%(pname)s! Congratulations you've been blessed by the great Maximillion's presence"
    b "I crushed it in there! I handed out all 60 copies of my resume and had them practically eating out of my hand. But that's to be expected from such simpletons"
    b "How are you doing today? Sad that you're not going to get a fraction of the amount of job offers I'm going to get?"
    menu:
        "If I can get any offer, I'd be happy":
            m "I don't have much experience as you, but I'd be willing to do anything this summer as long as I'm occupied"
            b "Of course! No one can deign to dream of reaching the heightst that I'm acheiving"
            b "Though I must say, you're quite modest"
            show max skeptic
            b "Weaklings are always the most cunning"
        "Stupendous. I bet I'll be getting double the amount of offers":
            $ maximillion_friendship +=1
            m "Puhlease, I had people begging for my contact information"
            b "Those are some bold declarations. I'm doubtful I'll see any DinkedIn job updates from you. Sadly, you'll be stuck at your sad social strata"
            b "Most people are all talk after all"
        "No one cares. Who are you even flexing on?":
            $ maximillion_friendship -=1
            m "Do you see anyone who cares about the words coming out of your mouth? I don't"
            show max mad
            b "It's too bad. The reek of desperation and jealousy you're emitting is rancid"
            b"Some points just aren't as concerned about their futures I guess"
    jump career_email
label career_email:
    scene bg EC with fade
    "Man, nothing beats eating snacks in the dorm after a long day"
    #TODO: notification sound
    show screen mailbox_overlay
    $ add_message("Offer to Your Dream Job","Recruiter","Hi %(pname)s, The first step in getting an internship at Dream Job and Co. is to apply. For your application you'll need a resume, cover letter, and letter of recommendation. Thank you for expressing your interest in us. We hope to hear from you soon", "Meeting with Professor Today" )
    "Ahhhh, is that an internship update? So soon? No way"
    "Let's check my messages"
    "Hmm. Guess I can't really get the internship offer if I haven't applied to the intership yet."
    "Oof I don't have any of the things that they're asking for"
    hide screen mailbox_overlay
    "First things first, let's figure out who to ask for that recommendation letter"
    "Hmm, the first people that I can think of immediately are Professor Bonden and Professor Breaken"
    if seduce_prof == True:
        "I really bonded with Professor Bonden. We even had that fun misunderstanding that surely has strengthened our bond greatly"
    else:
        "I really bonded with Professor Bonden when I was triyng to get my grade changed, I mean, trying to form a genuine bond. Regardless, Professor Bonden has always been really sweet"
    "Professor Breaken on the other hand is a whole other story"
    "Gulpa says that they're the best but I swear it feels like they hate me. Maybe I'm just over thinking things though"
    "Who to ask? What a dilemma"
    menu:
        "Professor Bonden":
            jump bonden_route
        "Professor Breaken":
            jump breaken_route
label bonden_route:
    scene bg office with fade
    show professor neutral
    "Hey Professor Bonden! I hope you've been well. I was wondering if it would be possible for you to write me a letter of recommendation?"
    if seduce_prof == True:
        p "I'm sorry %(pname)s. I'm still flustered and honestly still perturbed by our last misunderstanding. I think it would be better if you ask someone else"
        m "That's totally fine! Thanks for your honesty"
        jump breaken_route
        #need to account for good and bad letter options

label breaken_route: #need to add an option for giving up
    scene bg office with fade
    show Karen
    m "Hey Professor Breaken, I was hoping to ask"
    op "Sorry can't talk right now"
    hide Karen with dissolve
    "Guess I'll have to try again some other time"
    scene bg columbialawn with fade
    show Karen with moveinright
    "Oh I see Professor Breaken!"
    m "Hi"
    op "Nope. Bye"
    hide Karen with moveoutright
    "There's always next time"
    scene bg milfloor with fade
    show Karen with moveinleft
    "It's like seeing a unicorn"
    m "I was hoping to ask"
    op "Sorry, can't chat. I've got something more important"
    hide Karen with moveoutright
    "Oof I didn't realize the sting of rejection would hurt this much"
    scene bg collegewalk with fade
    show Karen with moveinbottom
    "Maybe fourth time the charm"
    m "Hi Professor Breaken! It's great to see you. I was hoping to ask if you would mind writing a letter of recommendation for you"
    "I'm quite shocked when I managed to say my entire request. Seems like fourh time was the one after all"
    op "Sorry, who are you again?"
    "I blink"
    "The professor blinks"
    "We both blink"
    m "Oh!! Sorry for not introducing myself. I'm %(pname)s I am taking the seminar, Everything you Need to Know About %(pmajor)s this year?"
    op "Right, right"
    "At the newest development, I contemplate {i}hello darkness my old friend{/i}"
