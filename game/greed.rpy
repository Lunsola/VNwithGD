label career_fair_intro:
    scene black
    with Pause(1)
    show text "{size=50}Semester 3: What's this? More School{/size}"
    with Pause(2)
    hide text
    scene bg careerfair1 with fade

    "It's finally the day of the career fair! I will make something out of
    myself today just like Pres Beau wanted."

    "I guess I need to go talk to some recruiters though..."

    scene bg careerfair2 with fade

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

    scene bg lernerramps with fade

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
    scene bg lernerramps
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
    $ add_message("Offer to Your Dream Job","Recruiter","Hi, The first step in getting an internship at Dream Job and Co. is to apply. For your application you'll need a resume and letter of recommendation. Thank you for expressing your interest in us. We hope to hear from you soon", "Meeting with Professor Today" )
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
        if sin >=3:
            p "I'm sorry %(pname)s. I'm still flustered and honestly still perturbed by our last misunderstanding. I think it would be better if you ask someone else"
            m "That's totally fine! Thanks for your honesty"
            jump breaken_route
        else:
            show professor pleased
            p "Sure %(pname)s. I think I have a great perception about your talents and your character. I would love to write a letter for you"
            "That's kind of surprising. Especially given how our last Mel's fiasco went"
            $success-=1
            m "Thank you so much Professor I really appreciate it"
            p "Any time"
    else:
        if prof_friendship>=0:
            show professor pleased
            p "Sure %(pname)s. I would love to. I really enjoyed having your in my class and I think you're certainly going places"
            m "Thank you so much Professor I really appreciate it"
            $success+=1
            p "Any time"
        else:
            show professor pleased
            p "Sure %(pname)s. I think I have a pretty good grasp on who you are. I think that I can provide valuable insight to your prospective employer. It would be my pleasure"
            m "Thank you so much Professor I really appreciate it"
            "I had never thought we had the greatest relationship but Professor Bonden as always is a really nice guy"
            $success-=1
            p "Any time"

label breaken_route: #need to add an option for giving up
    scene bg office with fade
    show Karen
    menu:
        "Hey Professor Breaken, I was hoping to ask":
            op "Sorry can't talk right now"
            hide Karen with dissolve
            "Guess I'll have to try again some other time"
        "Never mind":
            "After giving this more thought, I really don't think it's a good idea to ask Professor Breaken. I'm pretty sure that they hate me"
            jump prof_reject
    scene bg columbialawn with fade
    show Karen with moveinright
    "Oh I see Professor Breaken!"
    menu:
        "Hi":
            op "Nope. Bye"
            hide Karen with moveoutright
            "There's always next time"
        "Never mind":
            "After giving this more thought, I really don't think it's a good idea to ask Professor Breaken. I'm pretty sure that they hate me"
            jump prof_reject
    scene bg milfloor with fade
    show Karen with moveinleft
    "It's like seeing a unicorn"
    menu:
        "I was hoping to ask":
            op "Sorry, can't chat. I've got something more important"
            hide Karen with moveoutright
            "Oof I didn't realize the sting of rejection would hurt this much"
        "Never mind":
            "After giving this more thought, I really don't think it's a good idea to ask Professor Breaken. I'm pretty sure that they hate me"
            jump prof_reject
    scene bg collegewalk with fade
    show Karen with moveinbottom
    "Maybe fourth time's the charm?"
    menu:
        "Hi Professor Breaken! It's great to see you. I was hoping to ask if you would mind writing a letter of recommendation for you":
            "I'm quite shocked when I managed to say my entire request. Seems like fourth time was the one after all"
            op "Sorry, who are you again?"
            "I blink"
            "The professor blinks"
            "We both blink"
            m "Oh!! Sorry for not introducing myself. I'm %(pname)s I am taking the seminar, Everything you Need to Know About Everything this year?"
            op "Right, right"
            "At the newest development, I contemplate {i}hello darkness my old friend{/i}"
            m "Right so about that letter of recommendation?"
            if sin >=3:
                op "I'm pretty busy since I have an upcoming presentation coming up.{p=3.0} But I think I can squeeze you in"
                $success+=1
                m "Thank you thank you Professor Breaken! I really appreciate it"
                "Wow, bless whatever higher being for rewarding me with Professor Breaken's kindness"
                op "No problem. Is there anything else"
                "I'm so thrilled. I wnat to given the professor a hug but I suppress my urges. I have a newly bought box of chocolates that I was saving for a rainy day. Should I give it to them?"
                menu:
                    "Give gift":
                        show gift at center
                        m "Yes, actually. I was hoping you would accept these chocolates as a thank you from me"
                        hide gift with dissolve
                        #show professor happy
                        "I can see my professor's eyes widen in shock and they look almost happy? It's the first I've ever seen them like this"
                        op "{p=3.0} Thanks %(pname)s, heh, I always did enjoy reading your work for my class"
                        "This is wrinkling my mind"
                        m "...Thanks Professor. That means a lot"
                    "Keep chocolates":
                        "I'm not obligated to share. The Professor can get their own chocolates"
                        m "Nope, that's all! Thank you so much Professor"
                        op "Any time, any time"
            else:
                op "I'm pretty busy since I have an upcoming presentation coming up.{p=3.0} So I don't think I can write you one unfortunately"
                m "Are you sure there's no way? Surely you can fit the time to write one letter"
                op "Yes I'm sure, unless you want to have a poorly written letter which can also be arranged"
                m "Never mind, thanks for your time"
                jump prof_reject
        "Never mind":
            "After giving this more thought, I really don't think it's a good idea to ask Professor Breaken. I'm pretty sure that they hate me"
            jump prof_reject
$ prof2 = Contact("Professor Breaken", "breaken_draft")
label prof_reject:
    "Sigh, what a pointless endeavor. I'm going to head back to my room and dwell in sadness for a bit"
    scene bg bedroom with fade
    "The prospect of getting an internship was shrinking"
    "With that, you drift off to sleep"
    r "Yay!!!!!!!"
    "You're jolted awake"
    show marie v happy with moveinright
    r "Guess what, guess what"
    m "I guess you've got some good news to share?"
    r "Ding! Ding! You're absoultely right"
    show marie v happy at sright, hop
    r "Professor Breaken wrote a recommendation letter for me"
    "What. Professor Breaken to busy to spare any time for me, Professor Breakn?"
    m "Woah, you got notoriously mean Professor Breaken, ain't got no time for anybody Professor Breaken, to write you a recommendation letter for you??"
    r "Yeah!! I'm super excited. I'm going to facetime my parents and tell them the good news. With this, I'll be able to get an internship in no time. See you!"
    m "Wait, wait. Before you do that, I wanted to ask you something"
    "I'm still rec-letter less but maybe Marie can help me out"
    menu:
        "Can I see your recommendation letter?":
            m "I was asking around for recommenedation letters but to no avail"
            r "Sure! Roomies need to support each other after all!"
            r "Together we'll take the world by storm"
            m "Haha, thank you so much! You're the best Marie"
            "I quickly snap a picture of her recommendation letter"
            r "No prob! Now I'm going to run and make that call! I'll see you soon %(pname)s"
            "Yes!!! With this, I can forge my own recommendation letter to send out to companies"
            "I'll be able to get an internship in no time. Who needs Professor Breaken anyways"
            $success+=1
            $sin-=1
        "Never mind! I'm good actually. Have a nice call":
            show marie surprised
            r "Are you sure? I can stick around"
            m "Yeah! I'm good don't worry about it"
            r "Okie!! See you soon, I'll be back"
            show marie v happy moveoutright
            "The thought of asking to see Marie's letter in order to forge it briefly crossed my mind"
            "It'd be so easy to do and it wouldn't even hurt anyone, but I decided against it after seeing how Marie deserved her recommendation letter after all of her hard work"
            "After all, it was me that was rejected by Professor Breaken"
            $success-=1
            $sin+=1
    "I was left alone to my brooding. I was still pretty salty about how Professor Breaken had shown such obvious favoritism for Marie over me. Considering how we're in the same major, she'll be getting all of the job offers"
    "We can't have that now. I thought of a way to even the playing field. I remember hearing how Professor Breaken was super strict about violations of academic integrity"
    "Maybe I can write an email letting them know about Marie's \'violations\'"
    menu:
        "Write the email":
            "Yes! This is perfect. This way I'll still be fine and get rid of my competition in the process"
            "Let's draft this message! Check your message box at the upper right"
            show screen mailbox_overlay
            "{p=3.0} Great. With this, I'll be paving the road for my success"
            $sin-=1
            hide screen mailbox_overlay
            jump sab_marie
        "Forget it":
            "Oh my goodness, what am i thinking. I can't do that to Marie. She's been such a great roommate"
            "I'm really going to turn down the salt levels. I'll be just fine without having to ruin someone else's chances"


label breaken_draft(contact, message_title="Report Academic Violation"):
    menu:
        "Hi Professor, I wanted to report Marie for violating our school's academic integrity policies. Her final paper for the course was purchased through a third party":
            $ contact.draft_label = None # must include this line for each option
            $ add_message("Report Academic Violation:Re", "Professor Breaken", "Thank you for reporting this offense. This shall be dealt with immediately")
    return

label sab_marie:
    r "Oh no. no no no no no no no no. This can't be happening"
    show marie distressed moveinright
    m "What's wrong?"
    "I had an idea"
    r "Professor Breaken just emailed me saying that I was being suspected of violating the academic integrity policy. I might be getting a 0 in their class"
    r "They even said that they wanted to take back the recommendation letter and says they're forbidding me from using it"
    r "I have no idea why this is happening. I would never cheat!"
    menu:
        "Oh no! I'm sure the truth will come out and things will be fine":
            show marie concerned
            r "I really hope so. It feels like the world's out to get me or something"
            r "I've always had such a hard time making friends with others and the bullying certainly didn't help"
            m "That's so surprising. You're such a kind and intelligent person; I'm glad that you're my roomie. You deserve the world. Everything is going to work out for you"
            "I started to feel a bit guilty. But it's all a competition after all"
            r "Thanks %(pname)s. Sorry for throwing all of my emotional baggage on you"
            r "I'm really glad that I have such great friends like you and Josh in my life. Honestly, at our school it can feel a little toxic sometimes with how competitive people get"
            r "I'm glad that I have such a loyal roomie like you to rely on"
            m "Of course! I'm glad that I can be here for you too"
            "Wow, I'm top snek in this den"
            $marie_friendship += 1
        "Sorry, I don't have time for this right now":
            r "Oh, I'm sorry for venting at you. I'll leave you alone"
            "The guilt was slightly eating away at me. But this was for the best, wouldn't it be worse to lead her on while being the direct cause of her problems?"
            r "You're kind of hard to talk to..."
            hide marie distressed moveoutright
label resume:
    pass
