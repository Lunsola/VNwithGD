label lust_begin:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    $renpy.music.play("audio/LustMain.mp3", channel="Chan1", synchro_start=True)
    $renpy.music.play("audio/LustBonden.mp3", channel="Chan2", synchro_start=True)
    $renpy.music.play("audio/LustMaximillion.mp3", channel="Chan3", synchro_start=True)
    $renpy.music.play("audio/LustMarie.mp3", channel="Chan4", synchro_start=True)

    $prof_email = False
    $grade_change = False
    $twin = False
    $bizboss = False
    $dinoroar = False
    image bg but_entrance:
        zoom 0.50
        "But_Entrance.jpg"
    scene black
    with Pause(1)
    show text "{size=50}Semester 2: Still at School{/size}"
    with Pause(2)
    hide text
    scene bg bednight with fade

    "Ayyy. Bless. First round of testing season is over ... {p=1.5}and it's a Thursday night!! No immediate responsibilities that need to be taken care of and no need to stress about academics for a while...."
    "...{p=1.0}Maybe I should finally check my scores for Science of Everything class."
    "I've been avoiding checking grades to minimize stress but I'm free from everything now! {p=2.0}Nothing can hurt me now."
    call phone_start from _call_phone_start_6
    call message_start("OfCourseItWorks", "Science of Everything Midterm: 50") from _call_message_start_6
    play sound "audio/phone_notif.mp3"
    call message("OfCourseItWorks", "Science of Everything Midterm(Class Avg): 80, STD: 10") from _call_message_4
    play sound "audio/phone_notif.mp3"
    call phone_end from _call_phone_end_6
    "Oh"
    "My"
    "Gosh"
    "This can't be for real. I just missed the deadline for grade request inquiries too."
    menu:
        "SCREAM":
            r "Hmmmm?"
            jump roomie_talk
        "Social Media Time":
            "Time to check my feed for hot new memes, spicy takes and callout posts"
            jump social_media
        "Contact professor":
            "There must have been some mistake. There's no way that's my grade. I skipped classes and crammed for 12 hours straight. I need to speak with the professor."
            $prof_email = True
            jump prof_email

label roomie_talk:
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan4")
    show marie confused with moveinleft
    r "Hey is everything okay?"
    menu:
        "Not really":
            m "Kind of? Not really. I just got my train wreck of a grade back"
            hide marie confused
            show marie concerned
            r "I'm sorry. Remember, you're really smart no matter what any number says. It also might help to check if there were any grading mistakes."
            r "I am a self-proclaimed baking master so I flipped out when I apparently got a C- on my pie quality test"
            r "But after checking with my teacher, it turned out that she had just graded the wrong pie!"
            r "Ah sorry for getting off topic! Regardless, there are going to be more grades and I'm here for you if you ever want a study buddy!"
            menu:
                "Thank you. I really appreciate it":
                    hide marie concerned
                    show marie happy
                    m "Buttler gang for life after all! "
                    r "hehe you know that's right"
                    r "Ahh, look at the time! I need to grab a package from Weiner"
                    $marie_friendship +=1;
                    hide marie happy with moveoutright
                    jump thurs_end
                "I'll pass":
                    m "With your grades, I'd be the tutor"
                    hide marie concerned
                    show marie averse
                    r ".... Okay, I'll just be on my way then"
                    hide marie averse with moveoutright
                    "Finally, some peace and quiet. How annoying"
                    $marie_friendship -=1;
                    $sin -=1;
                    jump thurs_end
                "Say Nothing":
                    "I appreciate the sentiment, but no reply comes to mind"
                    r "Alright then! I'll leave you to your thoughts for now. I need to head out and grab a package from Weiner"
                    r "I'm here if you ever want to talk!"
                    hide marie concerned with moveoutright
                    jump thurs_end
        "Start tearing up":
            hide marie confused
            show marie concerned
            r "Oh no! Can I give you a hug?"
            menu:
                "Accepts Hug":
                    $marie_friendship +=1;
                    "We hug for a couple of seconds. It's nice and reassuring"
                    m "Thanks Marie, I needed that. Sometimes things can feel really overwhelming. You know?"
                    hide marie concerned
                    show marie grateful
                    r "Any time %(pname)s. I totally relate. Please let me now if there's anything I can do to help make life a little more manageable"
                    "I hug Marie again. I'm glad to have someone to have someone so supportive in my life"
                    m "Know that I'm here for you too, okay?"
                    r "Hehe thank you!"
                    r "Ahh! Look at the time, I need to grab a package from Weiner. I'll be back"
                    hide marie grateful with moveoutright
                    jump thurs_end
                "Screw off":
                    $marie_friendship -=1;
                    $sin -=1;
                    hide marie concerned
                    show marie distressed
                    m "I don't need your pity"
                    r "I'm not pitying you. I can tell you're upset so I'm going to give you some space. Let me know if you want to talk about it"
                    hide marie distressed with moveoutright
                    "In my rage, I feel a sliver of regret. I shouldn't have lashed out at Marie so harshly. It was definitely warranted though. Who does she thing she is anyways?"
                    jump thurs_end
                "I'd rather not":
                    r "Alright, I understand. I'm going to give you some space. Please let me know if you need anything!"
                    hide marie concerned with moveoutright
                    jump thurs_end
        "I'm fine. Don't worry about it":
            "I'm already feeling down. I don't really want to deal with people right now on top of that"
            r "I'm here for you if ever need anything!"
            hide marie concerned with moveoutright
            jump thurs_end

label social_media:
    call phone_start from _call_phone_start_7
    call message_img("Meme Central", "Here lies the spiciest of the spicy memes","meme1.jpg") from _call_message_img
    call message_img("Meme Central", "This is premium","meme2.jpg") from _call_message_img_1
    call message_img("Meme Central", "Quality","meme3.jpg") from _call_message_img_2
    call message_img("Meme Central", "Content","meme4.png") from _call_message_img_3
    call message_img("Meme Central", "Life when you have a smol bean of a roommate","meme5.jpg") from _call_message_img_4
    call phone_end from _call_phone_end_7
    "Your eyes burn from absorbing the memes and decide that's enough avoiding your pain today"
    "I'll just go and look for Professor Bonden tomorrow. Everything will be fine"
    jump thurs_end

label prof_email:
    $ prof = Contact("Professor Bonden", "bonden_draft")
    show screen mailbox_overlay
    "Let's draft this message! Check your message box at the upper right"
    "{p=3.0} Great message. Much professionalism"
    hide screen mailbox_overlay
    jump thurs_end

label bonden_draft(contact, message_title="Meeting Inquiry"):
    menu:
        "Hi Professor. I would really appreciate it if we could schedule a meeting for tomorrow":
            $ contact.draft_label = None # must include this line for each option
            $ add_message("Re: Meeting Inquiry", "Professor Bonden", "Yes! Of course. Come by my office tomorrow")
            play sound "audio/email_notif.mp3"
            $ prof_friendship +=1
        "Hi Professor. Any way I can help boost my grade? ;). Down for anything ;))))))":
            $ contact.draft_label = None
            $ prof_friendship -=1
            $ add_message("Re: Meeting Inquiry", "Professor Bonden", "Excuse me? Let's discuss in my office tomorrow")
            play sound "audio/email_notif.mp3"
        "Discard draft.":
            pass
    return


label thurs_end:
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan4")
    show marie neutral with moveinright
    r "I'm back! Hey %(pname)s! It's getting kind of late. I'm going to head to sleep now. Nighty night!"
    hide marie neutral with dissolve
    "Ahh how is it already 1 am?! What an emotional rollercoaster of a day. Time to conk out for today"


label fri_morn:

    scene bg bedroom with fade
    "Ah!!! It's already 11 am. Time to get up"
    show screen mailbox_overlay
    "First things first, let's check message updates"
    if prof_email == True:
        $ add_message("Reminder!", "", "Meeting with Professor Today")
        play sound "audio/email_notif.mp3"
        $ add_message("Triangle Info Session", "{b}{i}T r i a n g l e{/i}{/b}", "Thank you for expressing interest into joining the Triangles! We will be hosting a meeting in Hamilton 702. Hope to see you there. Please wear business casual!")
        play sound "audio/email_notif.mp3"
    else:
        $ add_message("Triangle Info Session", "{b}{i}T r i a n g l e{/i}{/b}", "Thank you for expressing interest into joining the Triangles! We will be hosting a meeting in Hamilton 702. Hope to see you there. Please wear business casual!")
        play sound "audio/email_notif.mp3"
    menu: #TODO Figure out problem with loading images as menu options
        "Ah!! So much to get done. But let's see... time to figure out what to wear"
        "I 8 π T-shirt and Jeans": #"{image = ../images/itsandwich.png}":
            $twin = True
            pass
        "Dress-Shirt and Khakis": #"{image = ../images/itsandwich.png}":
            $bizboss = True
            pass
        "Dino Onesie": #"No pictures pls":
            $dinoroar = True
            pass
    hide screen mailbox_overlay
    "Now I'm ready to take on today's challenges! Time to go speak with Professor Bonden to learn more about what exactly happened with the exam"
    if prof_email == True:
        jump prof_meet
    else:
        jump short_meet

label short_meet:
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg hallway with fade
    show professor neutral with dissolve
    if persistent.ending == "unlock 2":
        $ persistent.ending="unlock 3"
    "Nice! Caught Professor Bonden before they leave for the day"
    if dinoroar == True:
        p "Oh wow, that's some interesting attire that you've chosen. Guess you could say you're looking {p=1.0} dino-mite"
        m "Haha, thanks Professor, I do think I'm looking pretty explosive"
    if twin == True:
        p "Oh wow, would you look at that! We're practically twinning!"
        menu:
            "Omg one of us needs to go change":
                $prof_friendship+=1
                p "Haha it should be you. I was on this planet first!"
                pass
            "If we were like chromosomes...you'd be my homologous pair":
                p "Ha{p=1.5}haha{p=1.5}ha{p=1.5} Good one"
                pass
            "Say Nothing":
                pass
    p "Hey %(pname)s, I'm actually on my way out. I'm going to buy planetarium viewing tickets before they run out. I'm really excited for their exhibit tomorrow."
    p "Is there something that I can do for you?"
    menu:
        "Your research is so interesting!":
            $ prof_friendship +=1
            "Maybe if I ask more about him, he'll be more open to changing my exam grade"
            m "I read your most recent publication. It was really interesting. You're so knowledgeable. I was hoping that we could talk more about it?"
            p "Thank you %(pname)s! I'm so sorry to be doing this but I really do need to get going. Maybe we can chat more about this later? I'm going to head out"
            "Damn. Maybe I should have given him a heads up earlier. I'll just need to find him again later to ask him about it"
            hide professor neutral with moveoutright
            "Guess, I'll head over to the Triangle's info session early"
            jump club_info
        "Complain about grade":
            $sin -=1;
            $ prof_friendship -=1
            m "I was really surprised about my grade. There must have been a grading error"
            hide professor neutral
            show professor mad
            p "Is that so? I put some higher-level concepts on the exam that I guess the class didn't quite understand as well as I had hoped. Whatever your grade is, do know that I adjust based on the median at the end"
            m "But my grade is much lower than even the median. Something must have gone wrong"
            p "I'm sorry %(pname)s but it's pass the regrade request deadline. I don't mean to be harsh but it's important to me and my TAs that we uphold that deadline."
            p "...So sorry to cut our conversation but I do need to get going now. Let's discuss this more later. Maybe we can work something else out? "
            hide professor mad with dissolve
            "Sigh. I guess I'll find the Professor again later, and maybe we can work something out."
            "Oh! Look at the time, I need to get the Triangle's info-session"
            jump club_info
        "Inquire about Exam":
            m "I was hoping to look over what I did incorrectly on my exam."
            p "Ah yes, I can give you your exam back! Remember that the regrade request deadline has passed already"
            m "Thanks Professor Bonden!"
            p "Sorry I can't stay and chat. But there you have your test back. If you need me for anything else, feel free to find me later!"
            hide professor neutral with dissolve
            "Man, he's disappeared already. I'll need to find the Professor again later, but it seems like he's pretty strict on grade request deadlines. Maybe we can work out something else though"
            "Oh! Look at the time, I need to get the Triangle's info-session"
            jump club_info


label prof_meet:
    scene bg office with fade
    if persistent.ending == "unlock 2":
        $ persistent.ending="unlock 3"
    show professor happy with dissolve
    "Oh boy, time to defend my GPA's honor"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    if dinoroar == True:
        p "Oh wow, that's some interesting attire that you've chosen. Guess you could say you're looking {p=1.0}dino-mite"
        m "Haha, thanks Professor, I do think I'm looking pretty explosive"
    if twin == True:
        p "Oh wow, would you look at that! We're practically twinning!"
        menu:
            "Omg one of us needs to go change":
                $prof_friendship+=1
                p "Haha it should be you. I was on this planet first!"
                pass
            "If we were like chromosomes...you'd be my homologous pair":
                p "Ha{p=1.5}haha{p=1.5}ha. Good one"
                pass
            "Say Nothing":
                pass
    p "Hey %(pname)s, thanks for sending the email! I managed to snag tickets to the Planetarium this morning. I was worried that they might have already sold out."
    "I highly doubt the tickets to a planetarium would have sold out so soon but as long as the professor's happy I guess!"
    p "What can I help you with today?"
    menu:
        "Your research is so interesting!":
            $ prof_friendship +=1
            "Flattery gets you everywhere right? Maybe asking him about his interests will make the Professor more willing to change my exam grade"
            m "I'm really curious about your most recent publication. Would you mind speaking more about it?"
            p "Oh, yeah! Of course. So, the ability to fold space within the reality envelope facilitates the ability to make use of hyperbolic sub-resonant variations, combined with total holistic resonant emanations manifesting astral holographic projection."
            "I blink blankly at Professor Bonden and nod in 'comprehension'. Wow, am I supposed to be understanding what he's saying based on the class materials?? Maybe there's nothing wrong with the test grading after all...."
            p "And that pretty much sums up that paper. Was there anything else you wanted to talk about?"
            menu:
                "I want to be like you":
                    $ prof_friendship +=1
                    m "That's really cool! You're so knowledgeable Professor! How did you get into doing research? I think it's something I might want to pursue in the future"
                    show professor happy
                    p "Thank you %(pname)s. That's great to hear! We can always use more scientists in the world. I got started in research in high school by reaching out to a local college and fell in love with it from there. I'm really appreciative of the good fortune I've had that's led me to be here today and doing what I love"
                    "I'm not sure how to respond to that. It's really nice to hear someone so passionate about their job"
                    p "Ah, but enough about me. Is there something else I can help you with?"
                    menu:
                        "Your class is my favorite":
                            $ prof_friendship -=2
                            $sin -=1;
                            hide professor happy
                            show professor neutral
                            m "I really liked your lecture last class!"
                            p "Thank you! It's always nice to hear feedback from students. Let me know if there's any complaints and ways I can improve too!"
                            p "Ah! I'm so sorry that we need to cut our conversation short, but I need to go to me next class now. Was there anything else you needed from me?"
                            "Oh crap where has the time gone"
                            m "Yeah! I was actually hoping to discuss the exam grade."
                            p "Ah, yes of course. If you want to go over any of the content, we can review it if you drop in at some later point. But remember, it's past the regrade request deadline"
                            m "I was actually hoping to ask for a regrade..."
                            jump end_prof
                        "Complain about grade":
                            jump complain_grade
                        "Inquire about exam":
                            jump exam_inquiry
                "Complain about grade":
                    jump complain_grade
                "Inquire about exam":
                    jump exam_inquiry
        "Complain about grade":
            jump complain_grade
        "Inquire about exam":
            jump exam_inquiry

label complain_grade:
    $sin -=1;
    $ prof_friendship -=1
    m "I was really surprised about my grade. There must have been a grading error"
    hide professor neutral
    show professor mad
    p "Is that so? I put some higher-level concepts on the exam that I guess the class didn't quite understand as well as I had hoped. Whatever your grade is, do know that I adjust based on the median at the end"
    m "But my grade is much lower than the median. Something must have gone wrong!"
    jump end_prof
label exam_inquiry:
    m "As mentioned in my email, I was hoping to look over what I did incorrectly on my exam"
    p "Ah yes, of course! Let me go grab yours. It's fine for you to look over the exam but remember that the regrade request deadline has passed already"
    m "Thanks Professor Bonden!"
    "Hmm the regrade deadline might have passed but maybe I can convince him to take another look if I find enough grading errors"
    p "Alright here you go! What do you have questions about?"
    "Let's look through my answers that were marked as incorrect and ask about them"
    #To make it harder, user must identify all the grading mistakes consecutively for Professor to consider a regrade
    menu:
        "Mitochondria is the powerhouse of the cell":
            hide professor neutral
            show professor surprised
            p "Oh my. Hmm, your rationale makes sense, guess the TA didn't include that as one of the possible answers. What else did you want to ask about?"
            hide professor surprised
            show professor neutral
            menu:
                "If you're not part of the solution, you're part of the precipitate":
                    hide professor surprised
                    show professor neutral
                    jump wrong_answer
                "Oxidation is Loss. Reduction is Gain ":
                    show professor surprised
                    p "Well you see, the reason why your answer is incorrect is {p=0.5}.{p=0.5}.{p=0.5} Hmm. This is arguably another answer that could work. Was there anything else?"
                    menu:
                        "I don't give a flux":
                            hide professor surprised
                            show professor neutral
                            jump wrong_answer
                        "F = ma":
                            p "Well your answer is factually correct but ... I guess the TA went in a different direction. Was there anything else?"
                            menu:
                                "Roses are Red, Violets are Blue. Unexpected \'{{\' on line 32":
                                    hide professor surprised
                                    show professor neutral
                                    jump wrong_answer
                                "!False is True":
                                    show professor surprised at center, hop
                                    p "Hmm. I would have given that credit as well"
                                    hide professor surprised
                                    show professor neutral
                                    $grade_change = True
                                    p "Actually for all of these questions that you pointed out, I think you could have earned some more points, why didn't you bring it up earlier?"
                                    m "I've been so stressed about my other classes that I didn't want to add the emotional backlash of a bad grade on top of this week. So, I only checked my score last night"
                                    m "Haha... I guess that wasn't the best move"
                                    p "That's alright,%(pname)s. When we look at things in hindsight, it's easy to find oversights and mistakes in our decisions."
                                    p "Unfortunately, it is past the regrade request deadline but let me look over your exam again and discuss with my TAs about anything we missed in our list of accepted answers. I will let you know what we decide"
                                    m "Thank you so much Professor Bonden! I really appreciate it."
                                    p "No problem that's what I'm here for after all"
                                    p "Oh my!! Look at the time, I'm late for the next class. Gotta run!"
                                    hide professor with moveoutright
                                    m "Well, I did all that I can do as of now. I can try to persuade Process Bonden to spare me some mercy at some other point"
                                    "Ahh! Look at the time, I need to hurry if I'm going to get to the Triangle's info session on time"
                                    jump club_info

                                "I rate this 10 out of 1010":
                                    hide professor surprised
                                    show professor neutral
                                    jump wrong_answer

                        "We're all Matter. Unless you multiply yourself times the speed of light squared. Then we're energy":
                            hide professor surprised
                            show professor neutral
                            jump wrong_answer
                "Orgo is difficult, I have alkynes of trouble":
                    hide professor surprised
                    show professor neutral
                    jump wrong_answer
        "Gregor Mendel says woopea!":
            jump wrong_answer
        "Biologists take cellfies":
            jump wrong_answer
label wrong_answer:
    p "That's not quite right. Great pun but not quite what we were looking for"
    m "But it's grounded in correct scientific principles"
    p "That's true but we didn't really ask for that either"
    m "Would it be possible to get some credit?"
    p "I don't mean to accuse but are you trying to inadvertently ask for a regrade?"
    m "Uh...A little bit"
    p "This time is meant for us to cover any concepts you don't understand. Not regrades"
    jump end_prof
label end_prof:
     p "I'm sorry %(pname)s but it's past the regrade request deadline. I don't mean to be harsh but it's important to me and my TAs that we uphold that deadline."
     p "...So sorry to cut our conversation but I do need to run to my next class now. Let's discuss this more later. Maybe we can work something else out? "
     "Sigh. I guess I'll find the Professor again later, and maybe we can work something out."
     "Oh! Look at the time, I need to get the Triangle's info-session"
     jump club_info

label club_info:
    scene bg classroom with fade
    "I get to the classroom and it's PACKED"
    "After carefully maneuvering myself around the people on the floor, I sign myself in and shuffle to an empty spot along the wall."
    "The room feel to a hush as some stranger starts their presentation"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    show max charm with dissolve
    play sound "audio/chimes.mp3"
    if persistent.ending == "unlock 3":
        $ persistent.ending="unlock 4"
    w "Hi Guys! Thank you all for your interest in joining the {b}{i}T r i a n g l e{/i}{/b}! We’re a tight knit community from across the schools. We do X, Y and Z for the school, really great things. We have lots of funding for whatever projects that you come up with."
    "I promptly zone out at the standard club pitch"
    "I overhear someone whispering: {i}I've heard that getting into the Triangle sets you up for guaranteed work at any of the big companies. Their alumni low key rule the world.{/i}"
    "Woah, I definitely want to get in if that's the case.{p=1} Actually, forget want. I NEED to get in"
    play sound "audio/chimes.mp3"
    w "And that's the {b}{i}T r i a n g l e{/i}{/b}! Thank you all for coming. Please feel free to come up to any of the board members to fill out an application form and get to know us!"
    hide max charm
    show max wink
    w "Hope to learn more about all of you who manage to get into the best organization ever, the rest of you eh."
    hide max wink
    show max neutral
    "Whoa arrogant much? Let's chat with him"
    if bizboss == True:
        $ maximillion_friendship +=1
        show max charm
        w "Ooh, hey stranger. I like your attire. Very appropriate"
        "Hmm, maybe he's not so bad.{p=1.0} maybe"
    if dinoroar == True:
        w "Uh, did you get the memo. What in the world are you wearing weirdo?"
        "Case in point"
    b "Hi, I'm Maximillion. My friends call me Max though. How can I assist a commoner like you today?"
    menu:
        "Commoner?"
        "Ignore the comment":
            "Commoner, the heck is wrong with this dude. Better to just fill out my club application and call it a day"
            m "Hi, I'm %(pname)s"
            jump club_app
        "Nice job up there. Maybe you're not a fellow commoner after all ":
            show max charm
            b "Wow. Sass back. I like. Be careful though, with someone as classy as myself. It'll be hard to keep up."
            m "Sounds to me like you're scared of some competition"
            b "You wish. Haha enough of this. And you are?"
            m "Maybe, I'm %(pname)s"
            b "Nice to meet you  %(pname)s, kinda!"
            m "I feel the same way"
            m "Haha anyways"
            $ maximillion_friendship +=1
            jump club_app
        "How can a pile of trash such as yourself help me?":
            show max mad
            $sin -=2;
            "This absolute ass"
            b "You must have no friends, so you don't understand the premise of helping others"
            m "Not really. Sounds like you've had a lot of personal experience with having no friends though"
            b "...What can I do for you trash?"
            $ maximillion_friendship -=1
            jump club_app
        "Great job up there!":
            $sin +=1;
            show max neutral
            "Let's just ignore the commoner comment. This dude clearly has a superiority complex better play into it. It might help my chances of getting in"
            m "Hi, I'm %(pname)s! Nice to meet you. Hopefully, I'll be able to be up there with you guys next year promoting the great {b}{i}T r i a n g l e{/i}{/b}"
            hide max neutral
            show max skeptic
            b "One can dream haha. What can I help you with?"
            hide max skeptic
            show max neutral
            jump club_app

label club_app:
    show max neutral
    m "I was hoping to fill out an application for the club"
    b "Alright. Here you go"
    $ app1 = renpy.input("Why do you want to join the Triangle?")
    $ app2 = renpy.input("What makes you worthy of being a Triangle?")
    $ app3 = renpy.input("We plan many events at school for the community. What event would you throw if you were in the Triangle?")
    "Hopefully, my answers are good enough"
    b "And now you're all set!"
    b "If you make it to the next stage, we'll reach out to you about setting up an interview this weekend"
    "Woah that's fast. I'm so nervous. Hopefully, I can get in"
    jump max_convo
label max_convo:
    if maximillion_friendship > 0:
        show max charm
        b "You seem like someone that's worthwhile of being more than just an acquaintance. Dare I even say it, a friend?"
        m "Wow. Who would have thought? The Mighty Maximillion deigning himself to fraternize with a commoner like me"
        b "Hey that's the Mighty Max to you"
        m "*shook Pikachu face* o_O WOAH"
        b "What are you up to tonight, %(pname)s?"
        m "Just getting a jump start on assignments at the library"
        b "Nice! That's what I'm doing too. Guess I'll see there!"
        menu:
            "Hopefully not":
                hide max charm
                show max neutral
                $ maximillion_friendship -=1
                b "Or maybe not then."
                "Why did I say that? We were getting along so well. Whatever, Maximillion was starting to act way too friendly anyways"
            "Totally":
                m "Yeah, see you there later tonight!"
                b "See ya!"
                $ maximillion_friendship +=1
                "That went pretty well! Maximillion's a good guy"
            "Maybe. Maybe not":
                m "Yeah, I guess we'll see!"
                b "Alright see ya!"
                "That went pretty well! Maximillion seems alright"
    elif maximillion_friendship ==0:
        show max neutral
        b "Thanks for coming! Please feel free to contact me if you ever have any more questions about the Triangle"
        m "Thanks for that offer! I'll take you up on that. Nice to meet you! I'm going to head out. Gonna get some caffeine in me before heading to the library tonight"
        b "I'm heading to the library tonight as well! Maybe I'll see you there!"
        menu:
            "Hopefully not":
                hide max neutral
                show max mad
                b "Alright. Jerk. Hopefully not indeed"
                $ maximillion_friendship -=1
                "Why did I say that? We were getting along so well. Whatever, Maximillion was starting to act way too friendly anyways"
            "Totally":
                hide max neutral
                show max charm
                m "Yeah, see you there later tonight!"
                $ maximillion_friendship +=1
                b "See ya!"
                "That went pretty well! Maximillion's a good guy"
            "Maybe. Maybe not":
                m "Yeah, I guess we'll see!"
                b "Alright see ya!"
                "That went pretty well! Maximillion seems alright"
    else: #case where friendship is negative number
        show max mad
        b "What are you still doing here?"
        m "Just seeing if an ass such as yourself has any plans on a Friday night"
        b "I'll be at the library studying. Not that your small brain would be able to relate to mental stimulus"
        m "I'm actually on heading there later too"
        b "Ugh. Unfortunately, I'll see you later then"
        menu:
            "Hopefully not":
                hide max neutral
                show max mad
                b "Yeah. I wouldn't want to be seen fraternizing with filth after all"
                hide max mad with moveoutright
                $ maximillion_friendship -=1
                "That guy's such an ass. What type of club member is rude to prospective members? Once I get into the club, I'll kick him out..."
                "I guess I was being a bit if a jerk too...{p=.0}No. My reactions were warranted."
                "Ugh. Hopefully, I don't see him at the library tonight"
            "Totally":
                hide max mad
                m "Yeah, see you there later tonight!"
                show max skeptic
                $ maximillion_friendship +=1
                b "Uh ...{p=1.0}sure"
                hide max skeptic with moveoutright
                "That was a weak attempt at making things right. Man, what was I doing? If that guy's a club member, he carries weight in whether I get into the club or not."
                "I'll do better at trying to reconcile with him later tonight"
            "Maybe. Maybe not":
                hide max mad
                show max neutral
                m "Yeah, I guess we'll see!"
                b "Based on what I've seen. Let's hope not"
                hide max neutral with moveoutright
                "Ugh. Max seems like an ass. If he's there tonight, I'll just have to deal with it"
    "Ah ...I'm kind of tired from everything that's been going on today. Time to go to Joe's Coffee for a caffeine fix"
    jump caffeine
label caffeine:
    scene bg coffeeshop with fade
    "Nothing beats a cup of coffee"
    "Oh look! It's Professor Bonden"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    show professor happy with dissolve
    m "Hey Professor"
    p "Hey %(pname)s, nice to see you again. How are you doing?"
    menu:
        "I'm doing pretty well! Thanks for asking. How are you doing?":
            $ prof_friendship +=1
            p "I am doing amazingly! I have my Planetarium tickets that I'm super excited for. They're doing an exclusive show about a recent breakthrough on {b}Dark Energy{/b}."
            p "It should be really exciting! If you get a chance, you should check it out!"
            m "Maybe! Sounds interesting"
            p "Right and before I forget about our earlier discussion, I think we can work out some extra credit assignment to help boost your grade"
            "Hmm that's kind of vague, what kind of assignment?"
            p "We can work out the details later! But for now, I gotta run!"
            hide professor happy with moveoutright
            "I'm so glad to have Professor Bonden. His passion for astronomy is adorable. Nerdy. {p=1.5} But adorable. Hmm I wonder what the extra credit assignment is going to be exactly?"
        "I'm doing eh. Could be better. Especially if my exam score was better":
            $ prof_friendship -=1
            hide professor happy
            show professor neutral
            p "I'm sorry %(pname)s. Rules are rules. There can't be any exceptions regarding regrades"
            m "Please professor. Isn't there anything I can do? My test wasn't even wrong, just graded incorrectly"
            p "Maybe we can work out some extra credit assignment to help boost your grade. I'm not so sure"
            m "Thank you. Thank you! I'll definitely do it"
            p "No promises though. I need to run, see you"
            hide professor neutral with moveoutright
            "I don't think Professor Bonden appreciated the attitude. Or maybe he did. He's considering giving me more points for extra credit after all! Now what kind of extra credit assignment would be grand enough to convince him of giving me extra points?"
        "I'm doing well, thanks for asking! I was wondering if you would mind if we continued our discussion from earlier?":
            hide professor happy
            show professor neutral
            p "Yeah, sure. I can spare a few minutes."
            if  grade_change == True:
                p "I'm still discussing with the TAs about our decision regarding the regrade of your answers. But we'll let you know!"
                m "Thank you so much Professor! I really appreciate it"
                p "But aside from that, I think that we can potentially work out some extra credit assignment to help boost your grade."
                m "Really? Thank you so much! I would really appreciate that."
                p "Yeah! Let's speak more about this later. I need to go. Remind me!"
                hide professor neutral with moveoutright
                "Thank goodness. Based on our earlier conversation, I will probably be able to get my test regraded after all. But I guess you never really know."
                "I wonder what the extra credit assignment would be"
            else:
                m "I understand that I missed the regrade request deadline and that's my fault. But I'm really worried about my performance in this class"
                p "Thank you for reaching out to me about this. I think we can work out some extra credit assignment to help boost your grade."
                m "...Really? {p=1.5} THANK YOU SO MUCH PROFESSOR YOU WON'T REGRET THIS"
                p "Hahahaha I'm glad to be of service."
                p "I need to run now, but let's hash out the specifics later!"
                hide professor neutral with moveoutright
                "Professor Bonden is so nice. I wonder what the extra credit assignment is going to be?"
    "Ah, well anyways. Now with my life saving bean juice, I shall head over to Buttler"
    jump max_library

label max_library:
    scene bg but_entrance with  Pause(1.5) #fade,
    "Good Ol' Buttler"
    scene bg themil with slideup
    show max neutral with dissolve
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    if maximillion_friendship >= 2:
        hide max neutral
        show max charm
        b "Well, well, well. Look who finally decided to join us. Peasant %(pname)s has arrived"
        m "Milord, why of course. Here to provide my duties to the king himself"
        b "All is right in the world then"
        m "You're a weirdo, man."
        b "Speak for yourself. Anyways let's get working!"
        m "Actually, before we do that, can we just talk for a bit"
        hide max charm
        show max wink
        show max charm
        b "Sure, I'll depart my wisdom upon today's uncouth youth"
        menu:
            "What do I want to talk about?"
            "Professor Bonden":
                m "Do you know about Professor Bonden?"
                b "Yep! He's one of the science professors, yeah? I think I've heard mixed things about him"
                m "Yeah, he's my Science of Everything Professor. I'm worried about my grade for the class especially after my last test"
                hide max charm
                show max neutral
                b "Huh, can't say I relate to that problem, but have you tried discussing your concerns with him?"
                m "Not everyone can be blessed with your talents."
                m "Actually, I missed the regrade request deadline. But when I spoke with him today, he vaguely mentioned an extra credit opportunity"
                b "Huh, that was kind of irresponsible of you"
                b "Wait, you said Professor Bonden right? I have heard about his extra credit assignments!"
                m "Really? Please do tell"
                hide max neutral
                show max wink
                b "I've heard that he has quite the reputation in letting people plead their case back in his bedroom"
                menu:
                    "Confused":
                        m "Huh? Is that where his students go to present their side report? Why not just do it in his office or the classroom?"
                        b "Hahahahahahahahahahahaha that's funny. {p=1.5}  Wait {p=1}Are you serious? How oblivious can you be"
                        hide max wink
                        show max neutral
                        b "Simpleton much?"
                        $maximillion_friendship -=1
                        m "Dude, chill. Elaborate please?"
                        "Man, this dude has a hell of a superiority complex"
                        b "You know, the devil's tango? Do the nasty? A bit of crumpet?"
                        b "Baking the potato? Funny business? Snibbing? Testing the humidity? Violating the prime directive? Monkey business"
                        b "Making the beast with two backs?"
                        m "Alright!!! I get it. Stop it. People are looking at us weirdly"
                        b "Well, now you know."
                        m "I don't know, Bonden doesn't seem like the type."
                        play sound "audio/chimes.mp3"
                        b "Why not? Sometimes that's just how it is. Actually, something similar happens with the {b}{i}T r i a n g l e{/i}{/b} actually"
                        m "So, if I were to get closer with you, I'd be a future Triangle huh?"
                        hide max neutral
                        show max wink
                        b "Now you're getting it"
                        m "Huh, I see"
                        hide max wink with dissolve
                    "Accept":
                        m "Woah, really?? I never imagined Bonden to be so saucy. Good on him for using his position in his favor lol"
                        b "Right, what a guy. Kind of sus but you know both parties are benefitting"
                        m "Righttttt, no need to delve into the ethics of this situation"
                        b "Wow, how refreshing to hear that's how you feel. Actually, speaking about all of this."
                        show max wink
                        $ maximillion_friendship +=1
                        $sin -=1;
                        play sound "audio/chimes.mp3"
                        b "Just to give you an insider tip, there's a supplement you can attach for your {b}{i}T r i a n g l e{/i}{/b} application too."
                        b "Involving us {p=1.5}....attaching ourselves together"
                        hide max wink
                        show max charm
                        m "Well, I guess we'll have to see about that huh?"
                        b "I think I know what's going to happen, not everyone gets such privileges %(pname)s,  you know?"
                        b "Oh, just so you know. You've got an interview Sunday morning. Let me know if you want me to put in a good word before it. I'll be at Hel's tomorrow night maybe I'll see you then"
                        m "Guess we'll have to see how lucky you get then huh?"
                        b "Ha, I guess so"
                        hide max charm with dissolve
                    #"Rage":
                        #Is it worth having this option or just leaving it
                        #pass
            #"{b}{i}T r i a n g l e{/i}{/b}":
            #    pass

    elif maximillion_friendship < 0 :
        hide max neutral
        show max mad
        b "I'm surprised they let such trash as yourself in here"
        m "Wow, you stole the words right from my mouth. Did you think that up all by yourself?"
        b "Thought more than your parents ever did about their life decisions. Ugh, anyway I'm going to get out of here. Else, your stupidity will spread"
        "What.{p=1.0} the. {p=1.0} "
        "This guy is the Asshole Supreme Overlord or something"
        m "Before I hurt you and make the world a slightly better place. Can I ask you something?"
        "Might as well get some intel from this unpleasant conversation"
        hide max mad
        show max skeptic
        b "I guess...I'll do some charity work and depart my wisdom upon today's uncouth youth"
        menu:
            "What do I want to talk about?"
            "Professor Bonden":
                hide max skeptic
                show max neutral
                m "Do you know anything about Professor Bonden and his extra credit policy?"
                b "Ha! Of course {b}YOU {/b} would be asking about extra credit policies. What, are you failing classes already?"
                m "No. Just curious"
                b "Right, sure. Yeah, I do know about Professor Bonden and his ways. He's got quite the interesting extra credit policies"
                m "Right, spit it out already"
                b "Hah, now what would I get out of just telling you"
                b "What are you willing to do for this info"
                menu:
                    "Anything":
                        m "I need to know. Out with it"
                        b "Aw,%(pname)s what a sad desperate fellow you are."
                        "I roll my eyes"
                        b "Bonden has quite the reputation in letting people plead their case back in his bedroom"
                        menu:
                            "Disgust":
                                m "You've got to be kidding me. There's no way Professor Bonden is the type"
                                b "Take it or leave it. That's what I know"
                                m "Ugh of course you'd be the type to be so nonchalant about this"
                                b "What's wrong? It's A mutualistic relationship. The professor and the student both benefit from the transaction"
                                b "With a whole lot of debauchery"
                                show max wink
                                b "Since you're so desperate for information. Let me give you some extra intel. Consider it a gift for the unfortunate"
                                play sound "audio/chimes.mp3"
                                b "We actually do something similar at the {b}{i}T r i a n g l e{/i}{/b} too"
                                m "What."
                                b "You didn't hear it from me. But maybe you want to consider doing something supplemental with your interview on Sunday morning and everything."
                                b "Let me know what you decide at Hel's tomorrow night"
                                m "WHAT"
                                $ maximillion_friendship -=1
                                hide max wink with dissolve
                            "Accept":
                                m "Huh, I'm surprised to hear that Professor Bonden would be the type. But I guess with every system, there's bound to be some form of corruption"
                                b "Even a desperate idiot like you gets it. How refreshing"
                                show max vicious
                                $sin -=1;
                                play sound "audio/chimes.mp3"
                                b "I'll let you in on some even more information. That's a supplement that can benefit your {b}{i}T r i a n g l e{/i}{/b} application too."
                                m "Ugh. The thing that you're implying sickens me greatly"
                                b "You sicken me. Well...you wouldn't want to hurt your chances especially since you've made it to the interview stage and everything"
                                m "....What?"
                                b "Being on the exec board and everything, it'd be so easy to sway the decision of your application"
                                m "Now what would you have me do about this?"
                                b "Let me know, I'll be at Hel's tomorrow night"
                                b "See ya, wouldn't want to be ya"
                                m "Lol, true that. Even you wouldn't want to do the nasties with yourself huh?"
                                hide max vicious with dissolve
                    "Nothing":
                        m "Haha, for you? Nothing really, your information is probably useless anyways"
                        b "Just as I expected from you %(pname)s"
                        b "There's nothing that you have worth anything of value to me anyways"
                        m "Whatever, knowing you. This was expected. Nothing comes from nothing after all"
                        b "Ignoring that zinger. I'm going to bless your desperate self with some information"
                        b "Bonden has quite the reputation in letting people plead their case back in his bedroom"
                        menu:
                            "Disgust":
                                m "You've got to be kidding me. There's no way Professor Bonden is the type"
                                b "Take it or leave it. That's what I know"
                                m "Ugh of course you'd be the type to be so nonchalant about this"
                                b "What's wrong? It's a mutualistic relationship. Both the professor and student benefit"
                                b "With a whole lot of debauchery"
                                $ maximillion_friendship -=1
                                show max wink
                                play sound "audio/chimes.mp3"
                                b "We actually do something similar at the {b}{i}T r i a n g l e{/i}{/b} too"
                                m "What."
                                b "You didn't hear it from me. But maybe you want to consider doing something supplemental with your interview on Sunday Morning and everything."
                                b "Let me know what you decide at Hel's tomorrow night"
                                m "WHAT"
                                hide max wink with dissolve
                            "Accept":
                                m "Huh, I'm surprised to hear that Professor Bonden would be the type. But I guess with every system there's some form of corruption"
                                b "Even an idiot like you gets it. How refreshing"
                                show max vicious
                                $sin -=1;
                                play sound "audio/chimes.mp3"
                                b "I'll let you in on some even more information. That's a supplement that can benefit your {b}{i}T r i a n g l e{/i}{/b} application too."
                                m "Ugh. The thing that you're implying sickens me greatly"
                                b "You sicken me. Well...you wouldn't want to hurt your chances especially since you've made it to the interview stage and everything"
                                m "....What?"
                                b "Being on the exec board and everything, it'd be so easy to sway the decision of your application"
                                m "Now what would you have me do about this?"
                                b "Let me know, I'll be at Hel's tomorrow night"
                                b "See ya, wouldn't want to be ya"
                                m "Lol, true that. Even you wouldn't want to do the nasties with yourself huh?"
                                hide max vicious with dissolve
    else:
        show max neutral
        b "Hey, %(pname)s right? Surprised to see you here on a Friday night"
        "Right, the guy from the {b}{i}T r i a n g l e{/i}{/b} earlier"
        m "Hey Maximillion. Yeah, the grind really doesn't stop"
        m "Actually, would you mind if I asked you about something?"
        b  "Sure, I'll depart my wisdom upon today's uncouth youth"
        "My gosh. Uncouth? Youth? What type of eccentric boomer is this"
        menu:
            "What do I want to talk about?"
            "Professor Bonden":
                m "Do you know about Professor Bonden?"
                b "Yep! He's one of the science professors, yeah? I think I've heard mixed things about him"
                m "Yeah, he's my Science of Everything Professor. I'm worried about my grade for the class especially after my last test"
                hide max charm
                show max neutral
                b "Huh, can't say I relate to that problem, but have you tried discussing your concerns with him?"
                m "I spoke about it with him today."
                m "Actually, I missed the regrade request deadline. But when I spoke with him today, he vaguely mentioned an extra credit opportunity"
                b "Huh, sounds kind of irresponsible"
                b "Wait, you said Professor Bonden right? I have heard about his extra credit assignments!"
                m "Really? Please do tell"
                hide max neutral
                show max wink
                b "I've heard that he has quite the reputation in letting people plead their case back in his bedroom"
                menu:
                    "Confused":
                        m "Huh? Is that where his students go to present their side report? Why not just do it in his office or the classroom?"
                        b "Hahahahahahahahahahahaha that's funny. {p=1.5}Wait{p=0.5}Are you serious? How oblivious can you be"
                        hide max wink
                        show max neutral
                        b "Simpleton much?"
                        $ maximillion_friendship -=1
                        m "Dude, chill. Elaborate please?"
                        "Man, this dude is judgmental to the max"
                        b "You know, the devil's tango? Do the nasty? A bit of crumpet?"
                        b "Baking the potato? Funny business? Snibbing? Testing the humidity? Violating the prime directive? Monkey business"
                        b "Making the beast with two backs?"
                        m "Alright!!! I get it. Stop it. People are looking at us weirdly"
                        b "Well, now you know."
                        m "I don't know, Bonden doesn't seem like the type."
                        play sound "audio/chimes.mp3"
                        b "Why not? Sometimes that's just how it is. Actually, something similar happens with the {b}{i}T r i a n g l e{/i}{/b} actually"
                        m "So, if I were to get closer with you, I'd be a future Triangle huh?"
                        hide max neutral
                        show max wink
                        b "Now you're getting it"
                        m "Huh, I see"
                        hide max wink with dissolve
                    "Accept":
                        m "Woah, really?? I never imagined Bonden to be so saucy. Good on him for using his position in his favor lol"
                        b "Right, what a guy. Kind of sus but you know both parties are benefitting"
                        m "Righttttt, no need to delve into the ethics of this situation"
                        b "Wow, how refreshing to hear that's how you feel. Actually, speaking about all of this."
                        show max wink
                        $maximillion_friendship +=1
                        $sin -=1;
                        play sound "audio/chimes.mp3"
                        b "Just to give you an insider tip, there's a supplement you can attach for your {b}{i}T r i a n g l e{/i}{/b} application too."
                        b "Involving us {p=1.5}....attaching ourselves together"
                        hide max wink
                        show max charm
                        m "Well, I guess we'll have to see about that huh?"
                        b "I think I know what's going to happen, not everyone gets such privileges %(pname)s,  you know?"
                        b "Oh, just so you know. You've got an interview Sunday morning. Let me know if you want me to put in a good word before it. I'll be at Hel's tomorrow night maybe I'll see you then"
                        m "Guess we'll have to see how lucky you get then huh?"
                        b "Ha, I guess so"
                        hide max charm with dissolve

    "As our conversation comes to a stop, I try to focus on my work with no avail...Was Maximillion right about Professor Bonden?"
    "If he is, was I willing to go through with it just to get the grade boost?"
    "And what the heck. The way to get into the Triangle is the same way?"
    "After failing to get any work done in the hours I spend at the library. I call it a night and trudge back to my dorm"

label sat_room:
    scene bg bedroom with fade
    "I get a restless sleep. Thinking about what Maximillion had said the other today. What kind of extra credit did Professor Bonden mean?"
    "I was originally thinking about doing a presentation or report about the planetarium or something academic related. Who would have thought that getting a good grade would be this complicated?"
    "Not to mention, what Maximillion said about the {b}{i}T r i a n g l e{/i}{/b} application. Things like this actually happen?"
    show screen mailbox_overlay
    $ add_message("Congratulations", "{b}{i}T r i a n g l e{/i}{/b}", "Hi, We would like to cordially offer you the opportunity to join our ranks. Please come to Hamilton 705 at 11 am tomorrow for your interview with one of our executive board members")
    play sound "audio/email_notif.mp3"
    "Oh, speaking about the Triangle, there's a new email notification!"
    "Ahh, it's just like Max said. I landed the interview tomorrow. Then I guess if I really want to get in the Triangle...{p=.10}I need to sleep with Max"
    "Trying to refocus on my work, nothing really gets done for the entire day as I deliberate the best course of action"
    hide screen mailbox_overlay
    "Come on, %(pname)s! What to do, what to do"
    "After a lot of deliberation, and the day pretty much gone to waste. The one thing I'm set on is that I need to go to Hel's and talk to Maximillion some more."

label mel_night:
    scene bg hels with fade
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    show max charm with moveinleft
    b "Oh, hey %(pname)s! Nice of you to finally join us. Did you think about what I said?"
    "Wait, it can't be. Is that... Professor Bonden?"
    m "Wait, sorry. Let me get back to you. "
    b "Aurevoir"
    hide max charm with moveoutleft
    $renpy.music.set_volume(0.33, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.33, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    show professor happy with dissolve
    p "Hey %(pname)s! It's not weird at all to be seeing you at such an establishment"
    "O .o can't say I relate to that"
    m "Hey ....Professor! It's nice seeing you here"
    p "Yeah! The Planetarium was mind boggling. There's so many interesting things you can learn in there"
    p "Sorry for cutting our conversation short yesterday. About the extra credit?"
    menu:
        "What will your extra credit be?"
        "Science Report":
            m "Right! So, after looking into your research, I was thinking about doing a report or giving a presentation on Dark Matter or something astronomy related?"
            "I hold my breath. This is it.{p=1.5}What is he going to say?"
            hide professor happy
            show professor neutral
            p "{p=1.5}....."
            m "Professor?"
            p "That's not what I was thinking at all"
            m "Would you rather me do something else?"
            p "{p=1.5}....."
            "Why isn't he saying anything???"
            hide professor neutral
            show professor pleased
            p "THAT'S FANTASTIC! At the planetarium yesterday, I encountered so many interesting topics that I can recommend to you! Have you considered..."
            "I'm stunned. It looks like things are going to work out after all! But there was one question that still weighed on my mind"
            "Was Maximillion right?"
            m "Ah Professor, that sounds great! I would love this to discuss this more with you, maybe at your office hours on Monday? But I'm curious, what were you originally thinking for my extra credit assignment?"
            p "Brilliant, brilliant. I wouldn't want to talk shop about grades and extra work on a Saturday night after all! Let's talk more on Monday."
            "Was he avoiding the question? Is he embarrassed about his shady actions?"
            p "Oh, I like your idea better! I was thinking you could help me set up some demos for my classes to illustrate your understanding of the course"
            "Huh, it seems like Maximillion was completely wrong then...Or did he try to deliberately sabotage me?"
            p "That's still an option of course, if you'd rather do that instead?"
            m "Oh no, that's fine. I'm excited to write this report!"
            p "Splendid! Alright, I must run now. Have a good one, %(pname)s"
            $ prof_friendship +=1
            $sin +=1;
            hide professor pleased with moveoutright
            "Oh wow, that went better than I could have hoped for"
        "Seduction Time":
            $seduce_prof = True
            $grade_change = False
            m "Don't worry Professor I know exactly what kind of activities will get me in your good graces"
            "Maximillion told me all about it after all"
            p "It doesn't quite work like that %(pname)s, I need to agree on what the assignment will actually be. I was actually thinking of"
            m "Shh. Don't worry, I know."
            m "Professor Bonden, what's your electronegativity levels? Because I feel us {b}bonden{/b} tonight"
            show professor neutral
            "The professor doesn't say anything. But I assume that this is working?"
            m "What say you? Let's go back to your place and test our co-efficient of friction"
            m "If I were a protein, I'd be a DNA helicase so I could unzip your genes"
            m "You've got my rapt attention on me orbiting around that ass"
            m "Care to explain what thrust is back at your place?"
            m "How about you let me take you to the Planetarium? We can learn about astronomy then afterward maybe I can explore Uranus"
            hide professor neutral
            show professor surprised
            p "Excuse me, %(pname)s! As much as I appreciate you illustrating your....{p=1.5} understanding of the sciences?"
            p "{p=1.0}What. {p=1.0}Are. {p=1.0}You. {p=1.0}Doing?"
            p "I'm sorry if I confused you regarding the nature of our relationship but I would like to keep things strictly professional"
            #here: can offer a menu option where you maybe feign romantic interest in professor (better ending in terms of your relationship with the professor)
            #menu:
            "Hmm, someone's being shy about their shady dealings. I start to wonder...had Maximillion's intel been wrong?"
            m "Come on Professor. Everyone knows about your reputation"
            m "I help you out below Orion's belt and you help me out in the grade department"
            hide professor surprised
            show professor mad
            p "What reputation? Excuse me?"
            p "Is that really what you think of me? Who do you think I am to do such debauched things with a student"
            p "When I was talking about extra credit, I was thinking about you helping me set up some science demos for my classes or something else"
            m "...."
            "Oh no. This all unraveled so quickly"
            "I have no words to say. I want to vaporize away. I had the completely wrong understanding"
            p "I see now that we are not on the same page. So, I'll get back to you about looking at your exam for a regrade. I must get going. Good night,%(pname)s. I guess I'll see you on Monday."
            hide professor mad with moveoutright
            $ prof_friendship -=3
            $sin -=2;
            "Oh my gosh. That went HORRIBLY"
            "WTF. Maximillion completely screwed me over"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    show max charm with moveinleft
    b "Hey, so how'd the big confrontation go?"
    menu:
        "Confront Him":
            if seduce_prof == True:
                m "You were so wrong about Professor Bonden. Like COMPLETELY, the biggest margin of error, I've seen in{p=1.0}my{p=1.0}LIFE"
                hide max charm
                show max neutral
                m "What is wrong with you?"
                b "Hey, plebian. Chill. I told you what I thought was true. You were the one that took action based on that information"
                m "Yeah, based on YOUR information"
                m "You ruined my relationship with Professor Bonden"
                b "Actually, it kind of sounds like {b}YOU{/b} ruined your relationship"
            else:
                m "Luckily, no confrontation happened. Because I didn't listen to your stupid false information"
                hide max charm
                show max neutral
                m "What is wrong with you? Did you try and set me up? What did I do to you to deserve this??"
                b "Hey, plebian. Chill. I told you what I thought was true. You were the one that took action based on that information"
                m "Yeah, based on YOUR information"
                m "You could have ruined my relationship with Professor Bonden"
                b "But I didn't!"
            "I gawk at him. Speechless"
            $maximillion_friendship -= 1
        "Say Nothing":
            m "...."
            b "Err. I guess that means things went well huh?"
            b "Or I guess things went really badly?"
            "I have nothing to say to Maximillion. He was so grossly mistaken about Professor Bonden."
            "Now the question is, was it intentional? Maximillion wouldn't confess to that"
            "Guess, I'll have to wait and see"
            b "Looks like you're broken huh? Hello? Space Center to %(pname)s. Come in"
        "Great":
            "Despite, how wrong Maximillion was. There's no need to ruin the night over it"
            "Maybe, he just had the wrong information"
            "There's also my Triangle application to consider after all"
            m "Yeah, thanks for the advice. Our meeting went swimmingly well"
            m "It's all smooth sailing for %(pname)s in the Science of Everything class now"
            b "Well, yeah. Of course. Who do you think I am? I give the best and greatest intel around"
            m "Righttttt"
    show max charm
    b "Now moving on from that, did you have time to think over my offer from last night? Will you be joining me for some fun night activities tonight?"
    menu:
        "What are you going to do?"
        "Join Maximillion":
            $sin -=1
            $seduce_max = True
            if maximillion_friendship >= 2:
                m "Looks like you're getting lucky tonight"
                b "Pshh let's be real, this must be beyond your wildest imagination"
                m "Eh, I've had better"
                b "Of course %(pname)s, you're not delusional or anything"
            elif maximillion_friendship >= 0:
                m "I guess, I can grant you some of my time tonight"
                b "Can't say that I'm surprised about your decision"
                b "%(pname)s, you're getting so lucky tonight"
            else:
                m "Ugh, as much as it pains me, let's get this over with"
                hide max charm
                show max skeptic
                b "I'm nauseated by you, hopefully you can exceed my low expectations"
                m "Says the most desperate man of all the land"
                b "Eh, I like to think about it as community service"
            jump morning_aftermax
        "Go to Room":
            $sin +=1;
            if maximillion_friendship >= 2:
                m "As pleasant as your company always is, I need to get going"
                m "I think I've got things covered with my {b}{i}T r i a n g l e{/i}{/b} application."
                b "Suit yourself %(pname)s, you're missing out on a magical mystery ride though"
                hide max charm
                show max wink
                m "Bahahahahahahahahaha"
                m "oh yeah, of course. Maybe I'll be honored with another opportunity like this some other time"
                hide max wink
                show max charm
                b "Aww, you poor confused peasant. This was a once in a lifetime opportunity. Maybe your dreams will be blessed with my presence"
                m "Maybe. Hopefully, I miss out on seeing you in my nightmares"
                b "Ugh, get out of here. You need to make your interview tomorrow morning"
                m "See ya your highness!"
                hide max charm
            elif maximillion_friendship >= 0:
                m "I'm afraid I've got some work I need to get done so I must decline."
                b  "Oooh, scared of having the best night of your life eh?"
                "Man, this guy's completely bonkers"
                m "Uh...{p=1.0}sure. Maybe some other time I guess?"
                b "Eh...guess we'll see if you're lucky"
                m "...Okay, see you around I guess"
                b "Yes, you're dismissed. I bid thee adieu"
                hide max charm
            else:
                m "I'd rather bite my tongue, you nasty"
                $maximillion_friendship -= 1
                hide max charm
                show max mad
                b "Oh please do, save me from hearing the blathering of an idiot"
                m "I think only you can save yourself from the nonsense spewing from your mouth"
                b "How you've made it this far in the application process astounds me"
                m "Of course. You wouldn't understand what talent and intelligent looks like"
                b "I know that it's not you"
                m "Guess we'll see, once I kick your ass out of the {b}{i}T r i a n g l e{/i}{/b}"
                b "Eh, we'll be all talking about what a nitwit you are tomorrow "
                m "Ugh, I'm getting out of here. Save my brain cells from talking to you"
                hide max mad
                show max vicious
                b "I'd say good luck for tomorrow. But let's be real, you're going to crash and burn"
                hide max vicious
            $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
            $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
            jump morning_afterhome
label morning_aftermax:
    $renpy.music.set_volume(0.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg maxs with fade
    "Crap."
    "Double Crap."
    "Triple Crap"
    "What time is it?"
    "{p=1.5} I'M LATE FOR MY INTERVIEW"
    "There's only like 5 minutes left, damn it"
    "Ahhhhh, what was the point of last night then, ugh"
    $renpy.music.set_volume(0.5, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    show max charm with moveinright
    b "Oh hey %(pname)s, you're up."
    menu:
        "Why didn't you wake me up?":
            if maximillion_friendship >= 2:
                hide max charm
                show max skeptic
                b "Huh? That's not my responsibility"
                m "But couldn't you have helped me out by waking me up? You knew that I had an interview today."
                hide max skeptic
                show max wink
                b "What am I, your butler? Shouldn't you be used to keeping track of your own schedule being an underling and all"
                "I glare at him angrily for making light of the situation"
                m "You're SO right. If you don't mind as an 'underling', I'm going to excuse myself now"
                hide max wink
                show max charm
                b "Uh... okay, you're dismissed. See you later!"
                m "Yeah, maybe"
                $ maximillion_friendship -=1;
                "AHH How frustrating. I thought Maximillion was a nice guy but sometimes he can be pretty inconsiderate"
                jump lust_ending
            elif maximillion_friendship >= 0:
                b "I thought you took care of your own matters by setting an alarm?"
                "My annoyance grows. He has a point, but the lack of remorse is quite irritating"
                m "Yeah, it seems like I forgot to set one up since yesterday took an unexpected turn"
                b "What can I say, I bring spice to the normies' lives"
                "Who does this guy think he is?!"
                m "Right, yeah. I'm just going to head out now"
                b "Alright! Maybe I'll see you later."
                m "Yeah ... {size=-8}hopefully not{/size}"
                "AHH I'm so annoyed. Last night was pointless in the end and Maximillion is a pretty aggravating guy"
                $ maximillion_friendship -=1;
            else:
                show max skeptic
                b "Do tell %(pname)s, how in the world was that my responsibility?"
                m "You're right. My apologies for expecting you to have a shred of human decency and empathy"
                hide max skeptic
                show max mad
                b "Excuse me, I gave a commoner like you, an opportunity of a lifetime"
                m "HA more like I've been punished with no rewards"
                b "You're so simple. Sometimes that's just how it is. Remember, you're at fault here"
                m "Ugh, I'm getting out of this toxicity"
                b "Hopefully see you never"
                m "Yeah, hopefully that's the case"
                "AHHH That pompous arse. At least without being in the Triangles this should mean that I get to see his ugly mug less."
                $ maximillion_friendship -=2;
        "Hey! Good Morning":
            "I missed my interview but might as well still be amiable. It's not Maximillion's fault after all "
            $maximillion_friendship += 1;
            if maximillion_friendship >= 2:
                b "Aren't you quite the sleepyhead? It's practically noon already. You missed your interview I believe?"
                m "Oh well, at least I've been able to bask longer in your presence"
                b "Wow, you know how to properly flatter a lord"
                m "Oh yikes, looks like your non-existent power is getting to your head then"
                b "Ugh, what are you still doing here? Begone commoner %(pname)s"
                m "Alright, alright. With your banishment, I shall get out of here"
            elif maximillion_friendship >= 0:
                b "Weren't you supposed to be somewhere this morning?"
                m "Yeah, I missed my interview unfortunately. But that's on me after all"
                b "Oh dear, maybe I can speak with the board and we can work something out"
                m "Really? That'd be super awesome!"
                b "No promises though!"
                m "Thank you! I really appreciate it. I'll get out of your hair now. See you!"
            else:
                "Maximillion pauses for a second, surprised about the lack of outright hostility like usual"
                b "Is it really a good morning? You've missed your chance of joining the Triangle and all"
                m "Yeah, that's alright! I still have three years to end up as president or do even bigger things"
                b "What a cute fantasy. I guess we'll have to see"
                m "Yeah, you better watch your back. Plebian"
                "Before Maximillion can respond, I turn and walk out"
                "Wow Maximillion and I {size =10}CAN{/size} have a semi-civil conversation after all."
    jump lust_ending

label morning_afterhome:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg bednight with fade
    "Ah!! I'm so nervous. This is it. Let's get to the interview!"
    scene bg classroom with fade
    show triangler with dissolve
    play sound "audio/chimes.mp3"
    w "Hey %(pname)s! Thanks for coming in. The {b}{i}T r i a n g l e{/i}{/b} is always excited to welcome new applicants"
    m "Thanks for having me"
    w "Now, let's get started. Why do you want to join the {b}{i}T r i a n g l e{/i}{/b}?"
    m "Well as a Freshman, I've always"
    w "Wait pardon, freshman? Did you not see on the application form we're only recruiting sophomores and up"
    "W{p=0.5}h{p=0.5}a{p=0.5}t{p=0.5}"
    w "...Well{p=1.5}...This is awkward. We appreciate the interest but maybe come back next year?"
    w "Huh, I heard from Max that you guys have met. I thought he would have mentioned something"
    m "Oh dear, looks like I'm mistaken then, my bad!"
    "Ahhhh, why didn't I pay attention during the info session properly"
    jump lust_ending
if professor_friendship <=-3:
    $grade_change = False
label lust_ending:
    $renpy.music.set_volume(1.0, delay=0.5, channel="Chan1")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan2")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan3")
    $renpy.music.set_volume(volume=0.0, delay=0.5, channel="Chan4")
    scene bg collegewalk with fade
    "Aww man. I can't believe after all those steps I couldn't get into the {b}{i}T r i a n g l e{/i}{/b} in the end"
    "No need to be too upset over it though. There are other clubs! Also there's always next year!"
    "Man, what a wacky weekend though. Meeting Maximillion has certainly been...interesting to say the least"
    if maximillion_friendship >= 3:
        "The guy is pretty eccentric and lowkey has quite the superiority complex, but I think he's a decent guy!"
    elif maximillion_friendship >= 0:
        "The guy is relatively friendly and useful. His mannerisms can be a bit much but they're not malicious... I think? I'll have to see"
    else:
        "Ugh, I can't stand him. He's so arrogant and condescending. The less of him I see the better"
    "Not to mention my Science of Everything exam. Please will the spirit of Pres Beau depart some good fortune"
    show screen mailbox_overlay
    if grade_change ==True:
        $ success +=1
        $ add_message("Regarding Exam and Extra Credit", "Professor Bonden", "Hey, Congrats! I've spoken with the TAs and they agreed that even though it's past the regrade period. There were some oversights in our grading rubric, so we'll be extending the option to all students to submit another regrade request. So your grade will go up!  Regarding the extra credit we've spoken about, it's still an option open to you if you're interested. Just let me know!")
        play sound "audio/email_notif.mp3"
        "Oh, dear. Speaking about the Science of Everything class, new email notification!"
        "YESSSSSSSSSSSSSSSSSSS. I've boosted my grade and I can do extra credit"
    else:
        if prof_friendship >=0:
            $ success +=1
            $ add_message("Regarding Exam and Extra Credit", "Professor Bonden", "Hey, I've spoken with the TAs and I'm sorry to inform you that your exam grade can not be changed. But as we've spoken earlier, extra credit is certainly an option!")
            play sound "audio/email_notif.mp3"
            "Oh, dear. Speaking about the Science of Everything class, new email notification!"
            "Aww, my grade's gonna stay as is"
            "Bless Professor Bonden has spared me a little bit and graced me with some extra credit though"
        else:
            $ add_message("Regarding Exam and Extra Credit", "Professor Bonden", "Hey, I've spoken with the TAs and I'm sorry to inform you that your exam grade can not be changed and we can not offer extra credit at this time")
            play sound "audio/email_notif.mp3"
            "Oh dear. Speaking about the Science of Everything class, new email notification!"
            "NOOOOOOOOOOOOOOOOOOOOOO. I'm so screwed for this class"
            "I thought Professor Bonden was going to at least offer extra credit. What did I do wrong?"
    hide screen mailbox_overlay
    "Everything is going to be fine! There's always next semester after all. Time to get this bread!"
    $ prof.delete()
jump greed_begin
