label career_fair_intro:
    $copy_res = False
    $interview_offer = False
    $greed_check = 0
    $bond_accept = False
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
    $ add_message("Offer to Your Dream Job","Recruiter","Hi, The first step in getting an internship at Dream Job and Co. is to apply. For your application you'll need a resume and letter of recommendation. Thank you for expressing your interest in us. We hope to hear from you soon. With Dream Job and Co, all of our dreams will come true" )
    play sound "audio/email_notif.mp3"
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
        "I really bonded with Professor Bonden when I was trying to get my grade changed, I mean, trying to form a genuine bond. Regardless, Professor Bonden has always been really sweet"
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
            $bond_accept = True
            $success-=1
            m "Thank you so much Professor I really appreciate it"
            p "Any time"
    else:
        if prof_friendship>=0:
            show professor pleased
            p "Sure %(pname)s. I would love to. I really enjoyed having you in my class and I think you're certainly going places"
            m "Thank you so much Professor I really appreciate it"
            $bond_accept = True
            $success+=1
            $greed_check +=1
            p "Any time"
        else:
            show professor pleased
            p "Sure %(pname)s. I think I have a pretty good grasp on who you are. I think that I can provide valuable insight to your prospective employer. It would be my pleasure"
            m "Thank you so much Professor I really appreciate it"
            "I had never thought we had the greatest relationship but Professor Bonden as always is a really nice guy"
            $success-=1
            $bond_accept = True
            p "Any time"
    jump resume

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
                $greed_check +=1
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
                jump resume
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
            m "I was asking around for recommendation letters but to no avail"
            r "Sure! Roomies need to support each other after all!"
            r "Together we'll take the world by storm"
            m "Haha, thank you so much! You're the best Marie"
            "I quickly snap a picture of her recommendation letter"
            $greed_check +=1
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
            show marie v happy with moveoutright
            "The thought of asking to see Marie's letter in order to forge it briefly crossed my mind"
            "It'd be so easy to do and it wouldn't even hurt anyone, but I decided against it after seeing how Marie deserved her recommendation letter after all of her hard work"
            "After all, it was me that was rejected by Professor Breaken"
            "I guess, I'll just have to accept the L and write my own reccomendation letter or ask someone other than my Professors"
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
    jump resume

label breaken_draft(contact, message_title="Report Academic Violation"):
    menu:
        "Hi Professor, I wanted to report Marie for violating our school's academic integrity policies. Her final paper for the course was purchased through a third party":
            $ contact.draft_label = None # must include this line for each option
            $ add_message("Report Academic Violation:Re", "Professor Breaken", "Thank you for reporting this offense. This shall be dealt with immediately")
            play sound "audio/email_notif.mp3"
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
    jump resume
label resume:
    "Anyways yay, I've figured out my recommendation letter!"
    "Hmm, what's next on the list that Dream Job and Co. to include in my application again?"
    "Right! A resume. Let's head over to Buttler to properly focus"
    scene bg buthall with fade
    "Oh wow look at that, Marie is also here!"
    show marie happy
    r "Hey %(pname)s! What are you doing here?"
    m "Ah, I'm writing my resume"
    r "Nice, nice! I did that recently too. I'm just here finishing up an essay! Let me know if you need any help, I have a bunch of pointers"
    m "Thank youuuu"
    menu:
        "Write your resume by yourself":
            hide marie happy with dissolve
            "I think I've got things covered. How hard can writing a resume be anyways"
            "The hours pass by at Butler with many meme breaks and stretching but eventually my resume is complete"
            $sin+=1
            if success >=3:
                $greed_check +=1
                "It doesn't look too bad. Solid GPA. Fluffed up extracurricular activities"
                "I think if I took it to CCE there wouldn't be too much criticism"
                "I think I have a fair chance at being invited to an interview at least? Hopefully, Maybe"
                $success +=1
                #potentially show image of resume
            else:
                "It's a bit short.... Mediocre GPA. A bit intensely fluffed up extracurricular activities"
                "I think I have some? chance at being invited to an interview at least? Hopefully, Maybe"
                "It's not much but it's mine!"
                $success -=1
                #potentially show image of resume
        "Ask Marie for help":
            m "Hey Marie! Sorry to bother would you mind letting me take a look at your resume? I promise I won't copy or anything. My brain is just a bowl of jelly and I'm not quite sure where to start. This is really stressing me out"
            show marie ingenuine
            r "Yeah! Of course. I'd be happy to help. Here you go"
            m "Thanks a lot!!"
            #potentially show marie resume
            "Woah, this is brilliant. Super extensive"
            menu:
                "Copy Marie's Resume":
                    $greed_check +=1
                    $copy_res = True
                    show marie concerned
                    r "%(pname)s, wait! I forgot. I think that's an older version of my resume. Here's my newest one"
                    m "Aww, thanks Marie!"
                    "There's a tiny twinge of guilt. But I ignore it. With Marie's resume, I'll be able to land that internship!"
                    show marie happy
                    r "Any time! Happy to help"
                    hide marie happy with dissolve
                    "I quickly copy over Marie's resuem and tweak it just a bit so that it's plausibly my own"
                    "Perfect"
                    $success +=1
                    $sin -= 1
                    "I think I'll definitely be invited to an interview with this resume! All I need to do is submit it and watch the offers roll in"
                "Don't Copy and Write Resume by yourself":
                    "While the thought of copying Marie's resume crosses my mind, I resist the temptation. It's better for my resume to be made solely of my efforts anyways"
                    "So, I get to work. The hours pass by at Butler with many meme breaks and stretching but eventually my resume is complete"
                    $sin += 1
                    if success >=2:
                        $greed_check +=1
                        "It doesn't look too bad. Solid GPA. Fluffed up extracurricular activities"
                        "I think if I took it to CCE there wouldn't be too much criticism"
                        "I think I have a fair chance at being invited to an interview at least? Hopefully, Maybe"
                        $success +=1
                        #potentially show image of resume
                    else:
                        "It's a bit short.... Mediocre GPA. A bit intensely fluffed up extracurricular activities"
                        "I think I have some? chance at being invited to an interview at least? Hopefully, Maybe"
                        "It's not much but it's mine!"
                        $success -=1
                        #potentially show image of resume
            show marie distressed
            r "Hey %(pname)s. Do you mind if I just vent to you for a moment?"
            r "Recently, I've been feeling so lost in life. It feels like everyone here knows exactly what they plan on doing and they're working to make that happen."
            r "For me, I just feel like a poser that doesn't deserve to be here. Heck, I'm not even sure if I like what we're studying anymore"
            r "I couldn't even will myself to go the career fair because it felt so hopeless. There's no way those companies would hire someone like me anyways"
            menu:
                "They'd be lucky to have you!":
                    m "Please don't think that!"
                    m "From all the time that we've spent together. It's so obvious to me that you're going to achieve whatever it is you want"
                    show marie grateful
                    r "You're just saying that because you're my friend. But I appreciate you"
                    m "Nonono. Honestly, I feel jealous of you sometimes. But I totally relate to how you're feeling. It's hard not to with everyone here being so accomplished"
                    m "But we need to remember that everyone is different and we are all going to be just fine"
                    m "Things will get better! u_u"
                    r "Hehehe, Thanks %(pname)s. You're the best! I'm so glad that the random roommate assignment paired me with someone as great as you"
                    hide marie grateful
                    show marie happy at center, hop
                    r "I definitely feel cheered up now!"
                    $marie_friendship+=1
                "I didn't give you permission to spill your feelings to me":
                    m "Please kindly keep your thoughts to yourself."
                    m "Else, I'll be required to venmo you for emotional labor"
                    show marie aversem
                    hide marie aversem
                    r "Oh...I thought we could support each other. I shouldn't have assumed."
                    show marie cry
                    hide marie sad with moveoutright
                    "Yikes, what a wreck"
    jump intern_interview
label intern_interview:
    scene bg bedroom with fade
    "Man, it's been days since I've submitted my application to Dream Job and Co. I'm getting nervous. The lack of news is probably bad news"
    show screen mailbox_overlay
    "Omg, it's like the world is psychic or something"
    if greed_check >=2:
        $interview_offer = True
        #The Interviews
        #Todo: Message notification sound
        $ add_message("Offer to Your Dream Job:Re","HR @ Dream Job and Co","Hi, We are pleased to inform you that you are invited to the next stage of our interview process. Please come to SomeOffice at Number Lane at 5 pm on Friday. We're excited to learn more about you. With Dream Job and Co, all of our dreams will come true")
        play sound "audio/email_notif.mp3"
        "An email notification!"
        "Omg yes!! All of the studying and nights falling asleep in But. with questionable hygeine"
        "All of this preparation has paid off! I'm going to become top dog around here!"
        "I got to the interview!!!!"
        "Omg, what day is it. Wednesday? I should head over to CCE for a mock interview so I'm ready for Friday"
        "I'm so excited!!! AHHHHH"
    else:
        $ add_message("Offer to Your Dream Job:Re","HR @ Dream Job and Co","Hi, We regret to inform you that we will not be continuing with your application. Please note that this year's applicant pool was very competitive. While your skills and experience were very impressive, we sound someone better for the position. We look forward to your continued interest with Dream Job and Co. With Dream Job and Co, all of your dreams aren't coming true")
        play sound "audio/email_notif.mp3"
        "An email notification!"
        "Oh no"
        "It's exactly as I feared, it looks like my application wasn't good enough after all *sigh*"
        "I wonder what went wrong. Man, I couldn't even get to the interview stage"
        "Maybe my recommendation letter was bad. Or maybe it was my resume? Maybe it was both"
        "Well, at least I have those on hand for the next possible opportunity!"
        "And I may not have been invited to the interview, but I can still go to CCE and do a mock interview in preparation for a real one"
        "Hmm, I should do that! Let's go in for a walk in interview now!"
    hide screen mailbox_overlay
    scene bg CCE with fade
    "Hmm, that mock interview was mildly helpful. The best advice that they gave was be charming and confident. Easier said than done"
    "But whatever, I guess I'll have to keep doing research about Dream Job and Co. and doing more interview prep before Friday"
    show max neutral at right with dissolve
    "Oh woah, it's Maximillion! I wonder if he had an interview or something. Lucky dude must be raking it in with the internship interviews and getting offers left and right"
    m "Hey, Maximillion! How's it going? Did you just have an interview? How'd it go?"
    hide max neutral
    show max charm at right
    b "Hey %(pname)s the scrub. What are you doing here?"
    "Hmm, kind of odd that he didn't answer the question"
    if interview_offer == True:
        m "I made it to the interview stage for Dream Job and Co. I'm here for a mock interview to prep for it! What about you?"
    else:
        m "My application for Dream Job and Co was recently rejected before I reached the interview stage. I hate just waiting around for the next opportunity, so I came here to brush up my skills!  What about you?"
    b "Oh wow, you're chasing after Dream Job and Co? You peasants should really dream bigger. That's such a small insignificant ant of a company"
    m "If you say so! I'm hoping to work there some day!"
    hide max charm
    show max neutral at right
    b "And regarding your early question, child. I'm here to brush up the mock interviewer's schools by coming for a prep session"
    b "My most recent interviews have gone less than stellar. So, I'm thinking of new strategies to charm the swine"
    b "Not that I'm like you! I am really qualified and everyone is job hunting me. I don't need any one's help"
    menu:
        "I feel you. Recruiters surely are simpletons for not recognizing our great talents":
            $maximillion_friendship+=1
            "I could tell that Maximillion had probably been stressing out about internships like I and probably everyone else was"
            b"{p=2.0}{size=-8}yeah{/size}"
            b"But don't let this get to your head, we're for sure, NOT the same"
            m "Yeah, yeah, yeah"
            m "Man, it's been really rough though. And my parents are constantly lecturing me, as if I'm not just as stressed and worried about my future as they are"
            b "Wow, peasant families are like that too huh? My fellow royal asstard creators are constantly going on and on about how I haven't reached my maximum potential and should work harder"
            b "That my accomplishments are nothing compared to my brother's. HA As if he helped pave the way with him being the president of the {b}{i}T r i a n g l e{/i}{/b} his senior aka last year, his sickening charisma that charmed his and now my professors. As if"
            m "Totally, everyone knows that the younger siblings are better anyways"
            b "{p=1.0}... Silence peasant, my brother is still someone greater than you could ever be"
            if maximillion_friendship > 0:
                show max happy at right
                b "{p=2.0}...but it's not bad talking to you"
                hide max neutral with dissolve
        "Sure, of course":
            "With Maximillion, the best way to avoid his tangents on his greatness was to just quickly agree and get on with it"
            m "None of us can ever carry an ounce of the greatness of the Magnificent Maximillion"
            show max charm at right
            b "Man, what a fanatic follower you are"
            b "But, why of course. You really know your place compared to the likes of someone so above you like myself"
            m "Seeing my constant shortcomings compared to someone so great like yourself has trained me well"
            m "If it is alright with you, I beseech that I shall scurry my lowly self out of your presence"
            b "hAHAHA the peasants are finally learning. Fine, since you've implored so earnestly. I grant you permission to be dismissed"
            hide max charm with dissolve
        "...Haha you need help? Pathetic":
            $maximillion_friendship-=1
            show max mad at right
            b "{p=1.0}Excuse me? It might just be my imagination but I think an insect just spoke"
            m "Hahah keep it up with your false pretenses, you're so sad"
            b "Speaking so harshly to your future boss may just cause you to end up losing it all you know"
            m "You're so funny. Without a job offer and doing mock interviews, yet spitting such fire"
            b "It's like a speck of dust speaking to an emperor, so {p=1.0} unfathomable"
            b "Oh %(pname)s sad as always"
            if seduce_max == True:
                b "I so deeply regreat that night after Mel's"
            hide max mad with dissolve
    "Maximillion, always a whirlwind to handle as always"
    "Anyways, I've got my own stuff to do after all"
    if interview_offer == True:
        jump real_interview
    else:
        jump job_results

$ timer_range = 0
$ timer_jump = 0
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

label real_interview:
    $int_score =0
    scene bg bedroom with fade
    "Ah!! I'm so nervous about the interview today. This is it. Time to see if all that prep paid off"
    scene bg Interview with fade
    recruit "Hi %(pname)s, Thank you for taking the time to come in and of courrse your interst in Dream Jobs and Co. Our goal is always to have our employees be at their dream job."
    recruit "You must know that we service half of the nation's population with our unique services"
    """$ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'"""
    #show screen countdown
    $ pitch = renpy.input("Who are you and what makes you a qualified candidate?")
    if len(pitch) >=30 and pitch.isalpha():
        $int_score+=1
    #hide screen countdown
    "Hmm, very interesting"
    #show screen countdown
    menu: #ques2:
        "As a Columbia Alum, I have to ask: Which is the best dining hall"
        "JJs":
            recruit "Good ol' JJs. We love our guarantee of the Freshman (or any year) 15"
            #hide screen countdown
        "Ferris":
            recruit "Their cheesecakes were so good! "
            #hide screen countdown
        "Hewitt":
            $int_score+=1
            recruit "You've got very good taste"
            #hide screen countdown
    #show screen countdown
    menu: #ques3:
        "Please describe a time where you've shown initiative"
        "During the Crisis known as 2020, I attended the majority of my Zoom classes":
            recruit "That's great to hear!"
            #hide screen countdown
        "I was the team leader for a group project and decided to make a game!":
            $int_score+=1
            recruit "Oh, that's interesting! It's always great to hear about students interests outside of the classroom"
        #    hide screen countdown
        "Once, I called CAVA for my very wasted floormates":
            recruit "Haha that brings me back in the day. What a time"
        #    hide screen countdown
    #show screen countdown #ques4
    $ fight = int(renpy.input("How many words are in Columbia's Fight Song"))
    if int(39)-int(fight) <=5:
        $int_score+=1
        recruit "Very good, very good"
    else:
        recruit "How interesting"
    #hide screen countdown
    menu:
        "What do you view to be your greatest weakness?"
        "I'm scared that the goals I have are because that's what is expected from me rather than my own desire":
            recruit "Thank you for your honesty. I think that given more time in your field of interest you get to gauge your earnest interest for it"
            $int_score+=1
        "I'm too reliant on memes for daily function. It's quite the crutch":
            recruit "Thank you, that was very honest"
        "I've never climbed onto any rooftops like a scrub":
            recruit "Don't worry, I don't think I ever have either!"
            m "{size=-8}like a scrub{/size}"
    recruit "Alright! I think that's all the questions that I have for you"
    m "Thank you for this opportunity!"
    recruit "No, thank you for coming in!"
    recruit " Hmm{p=1.0} I probably shouldn't be offering but since I have a soft spot for any students of my alma mater. Want me to give you a heads up about your application?"
    m "Oh my. Here are the legendary aLuMnI connections coming in clutch. Yes please! Thank you so much"
    recruit "Haha, any time"
    if int_score >=3:
        $greed_check+=1
        $success+=1
    "Wow, that was certainly a whirlwind. I think that overall went decently? Oh well. All I can do now is wait anyways"

label job_results:
    scene bg bedroom with fade
    if greed_check == 3:
        "AHHHH the suspense for whether I got the job or not is killing me"
        if copy_res == True:
            call phone_start
            call message_start("Dream Job and Co", "Hey! This is your recruiter. I wanted to give you an insider tip and I would be saying you got the job")
            play sound "audio/phone_notif.mp3"
            "Omg. Omg. this is SO EXCITING"
            call message("Dream Job and Co", "But, unfortunately that's not what this message is going to end up being. I would have given you the job but it turns out that there was something suspicious in your resume so things didn't manage to work out in the end")
            play sound "audio/phone_notif.mp3"
            "Wait, what?"
            call phone_end
            "How could this be? My resume was perfect, especially considering I copied mine from Marie."
            "...I should go ask her about it"
            jump copied_marie
        else:
            call phone_start
            call message_start("Dream Job and Co", "Hey! This is your recruiter. I wanted to give you an insider tip and let you know that you got it!! I can't wait for your journey to continue with us here. Please feel free to reach out whenever")
            play sound "audio/phone_notif.mp3"
            call phone_end
            "OMG. THIS IS SO EXCITING"
            "YAYYYYY"
            "Man, this is wild. I should try and calm down a bit. Let's go on a walk. In fact, maybe I'll see someone and share the good news!"
            $success+=2
            if maximillion_friendship >= marie_friendship:
                jump sad_max
            else:
                jump sad_marie
        #interviewed and got the job
    elif greed_check == 2 and interview_offer == True:
        "AHHHH the suspense for whether I got the job or not is killing me"
        if copy_res == True:
            call phone_start
            call message_start("Dream Job and Co", "Hey! This is your recruiter. I wanted to give you an insider tip and let you know that ... you should probably send out more applications. You just weren't up to snuff for what we were looking for and I think there was also something wonky about your resume?")
            play sound "audio/phone_notif.mp3"
            "Wait, what?"
            call phone_end
            "How could this be? My resume was perfect, especially considering I copied mine from Marie."
            "...I should go ask her about it"
            jump copied_marie
        else:
            call phone_start
            call message_start("Dream Job and Co", "Hey! This is your recruiter. I wanted to give you an insider tip and let you know that ... you should probably send out more applications. You just weren't up to snuff for what we were looking for.")
            play sound "audio/phone_notif.mp3"
            call phone_end
            "Aww, that's unfortunate that things didn't work out"
            "Guess, it's back to the grind then"
            "First, I wanna go on a walk though. I want to clear my head"
            if maximillion_friendship >= marie_friendship:
                jump sad_max
            else:
                jump sad_marie
        #interviewed and didn't get job
    else:
        "Man, I should really go and send an application to some other companies. Just because it didn't work out with Dream Job and Co. doesn't mean that it wouldn't work ouut somewhere else"
        "Man, job hunting is so stressful. I need to go on a walk and clear my head first before I do anything"
        #didn't get job
        "Guess, it's back to the grind then"
        "First, I wanna go on a walk though. I want to clear my head"
        if copy_res == True:
            jump copied_marie
        else:
            if maximillion_friendship >= marie_friendship:
                jump sad_max
            else:
                jump sad_marie
label copied_marie:
    $ marieevil = True
    scene bg columbialawn with fade
    show marie happy at right with dissolve
    m "Oh hey Marie! How are you doing?"
    r "I'm doing really great! It's so nice and sunny outside. Everything is absolutely as perfect as it can be. "
    r "What's up with you?"
    m "I'm kind of bummed. I didn't manage to get an internship at Dream Jobs and Co after all"
    hide marie happy
    show marie ingenuine at right, hop
    r "Wow, that sucks. I can't believe you didn't get the job. I just got an offer from them today actually!"
    "What."
    "How could that be? I didn't even know Marie had applied"
    r "Why aren't you saying anything?"
    m "Oh, congratulations Marie! I'm so happy for you"
    r "Hehehe. That's funny"
    r "I'm really surprised you didn't get the job though. I mean, I even let you see my resume which was actually pretty similar to yours, wasn't it?"
    "Wait, does{p=1.0}.{p=1.0}.{p=1.0}Marie know? How?"
    show marie concerned at right
    r "Are you alright? You look a little red?"
    hide marie concerned
    show marie happy at right, hop
    r "Well, your resume looks pretty similar to my edited resume anyways"
    "Woah, wtf Marie completely strung me along"
    r "Hehe, I'll leave you to your thoughts"
    hide marie happy with moveoutright
    jump end_greed

label sad_marie:
    scene bg columbialawn with fade
    "Oh hey look it's Marie! "
    show marie distressed at topright with dissolve
    if greed_check == 3:     #dialogue for you getting job
        "I'm so excited to tell her the good news"
        m "Marie! Hey!!"
        hide marie distressed with dissolve
        show marie distressed at right, sright
        "Wait, oh no. Is Marie crying?"
        r "H...hey %(pname)s, how's it going?"
        m "Are you alright? You seem sad. I've got some news that should brightern your spirits!"
        r "I'm doing...okay. What's the good news?"
        m "I got the internship at Dream Job and Co!!!"
        r "{p=1}{size=-8}oh{/size}"
        r "{p=1}{size=-3}That's really great!{p=1} I'm r-really happy for you{/size}"
        r "You deserve it for all of your hard work"
        r "..."
        hide marie distressed
    else:
        "I'll share my sorrows with her. Chatting with Marie always cheers me up"
        m "Marie! Hey!!"
        hide marie distressed with dissolve
        show marie distressed at right, sright
        "Wait, oh no. Is Marie crying?"
        r "H...hey %(pname)s, How's it going?"
        m "Are you alright? You seem sad. Actually, I'm feeling a bit down too."
        r "I'm doing...{p=1}okay.{p=1} What's up with you?"
        m "I was rejected from Dream Job and Co"
        r "{p=1}{size=-8}Dream Job and Co?{/size}"
    show marie cry at right, shake
    r "I was rejected byt them"
    m "Oh no, Marie. Come here and let me give you a hug"
    r "I-{p=1}I always knew I was useless. I knew that it was pointless to even try applying"
    m "Nonono"
    m "Don't think like that Marie. You're one of the smartest people I know. I admire you so much and I hope that you recognize your talents too"
    r "{p=1}... Thanks %(pname)s. I don't agree with you but I really appreciate your support"
    m "Aww, do you want to go for a pick me up snack? We can spice up our life and get the spiciest level at the dry hot pot place?"
    hide marie cry
    show marie neutral
    r "Hehe, thanks for the offer. But, I think I want some time alone right now"
    m "Totally fine! I'm always here if you change your mind."
    hide marie neutral with moveoutleft
    jump end_greed

label sad_max:
    scene bg collegewalk with fade
    b "%(pname)s! I command you to wait up"
    show max charm at right, sright
    "Ah the Magnificent Maximillion"
    m "How's it going Maximillion?"
    b "Everything's going great as always! As per usual, I'm living a life that Lady Fortune has blessed after all"
    b "How did things work out with Dream Job and Co? It's a ruler's responsibility to look after the peasants of the land after all"
    if greed_check == 3:     #dialogue for you getting job
        m "Oh! Thanks for asking! I ended up getting the internship!! I'm super excited"
        hide max charm
        show max neutral at right, sright
        b "Pssh, you simpleton how can you be so happy to have landed such a mediocre internship"
        m "Ah, everything probably pales in comparison to whatever it is you're up to, Oh Great One"
        m "But, it doesn't change the fact that I'm still really excited about this opportunity!"
        b"Hmm, you're an interesting one %(pname)s"
        m "What about you though? Have you finalized your plans?"
    else:
        m "Oh! Thanks for asking! Things didn't work out in the end. I was formally rejected and everything"
        hide max charm
        show max neutral at right, sright
        b "Sorry to hear that peasant. Take comfort that it was a mediocre internship to be applying for anyways!"
        m "Ah, I didn't view it as a mediocre internship. But it's okay! I'm still going to apply again next year. It's my dream to work there after all"
        b "Hmm, you're oddly earnest %(pname)s"
        m "What about you though? Great one, have you finalized your plans?"
    b "{p=1}{size=-8}um{/size}"
    b "{size=-5}Well I now definitively know that I wasn't offered the Dream Job and Co internship{/size}"
    m "What? I thought you had rejected their offer"
    hide max neutral
    show max breaking at right, shake
    b "{p=1}Ha{p=1}ha{p=1}ha That's what I originally thought"
    "Oh no, Maximillion being emotionally vulnerable? The end of the world must be coming or something"
    b "You peasants wouldn't understand. I've rejected them before. So Dream Job and Co. was like my safety internship if nothing else panned out"
    b "{p=1}{size=-8}and nothing has really panned out yet{/size}{p=1}{size=-12}and then I didn't hear back from Dream Job and Co either{/size}"
    m "Things will work out! Don't be discouraged"
    b "Pipe down. You peasants wouldn't get it anyways"
    b "I can't even satisfy my parent's minimum expectations. Nonetheless make them proud of me. I keep failing my parents"
    b "Not even the Zook name can save me now"
    b "And then there's Mark who's leaps ahead of me in every league"
    m "Don't be like that. Isn't your brother older?"
    m "From the time that I've known you, I'm confident that you're destined for really big things"
    m "You're Maximillion the Magnificent after all"
    b "Ugh, how pathetic. For an underclassmen peasant to see me in such a dimmed light."
    hide max breaking
    show max grateful at right
    b "Don't worry peasant %(pname)s. I, your leader, will be shining brightly whenever you see me next"
    m "Thank you. I feel inspired already"
    hide max grateful with moveoutleft
    jump end_greed

label end_greed:
    "Sigh, the job hunt is so cruel"
    "Man, will the grind ever end?"
    jump pridebegin
