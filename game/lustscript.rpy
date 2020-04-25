
label lust_start_dorm:

    $prof_email = False
    scene bg bednight #temp holder until bedroom upload

    "Ayyy. Bless. First round of testing season is over ... and it's a Thursday night!! No immediate responsibilities that need to be taken care of and no need to stress about academics for a while...."
    "...Maybe I should finally check my scores for Science of Everything class. I've been avoiding checking grades to minimize stress this week but I'm free rom everything! Nothing can hurt me now."


    #Need to figure out how to program a dramatic scroll and frame with grades
    #otherwise show image of grades would suffice
    "Oh"
    "My"
    "Gosh"
    "This can't be for real. I just missed the deadline for grade request inquiries too."
    menu:
        "SCREAM":
            "Your screaming prompts a confused inquiry from your roommate."
            jump roomie_talk
        "Social Media Time":
            "Time to check my feed for hot new memes, spicy takes and call out posts"
            jump social_media
        "Contact professor":
            "There must have been some mistake. There's no way that's my grade. I skipped classes and crammed for 12 hours straight. I need to speak with the professor."
            $prof_email = True
            jump prof_email

label roomie_talk:
    show marie confused
    r "Hey is everything okay?"
    menu:
        "Not really":
            m "Kinda? Not really. I just got my trainwreck of a grade back"
            hide marie confused
            show marie concerned
            r "I'm sorry. Remember, you're really smart no matter what any number says.It also might help to check if there were any grading mistakes."
            r "In my Home Ec class, I almost got a failing grade. I checked with my teacher and apparently she had graded the wrong pie."
            r "Ah sorry for getting off topic! Regardless, there are going to be more grades and I'm here for you if you ever want a study budy!"
            menu:
                "Thank you. I really appreciate it":
                    hide marie concerned
                    show marie happy
                    m "Butler gang for life after all! "
                    r "hehe you know that's right"
                    $marie_friendship +=1;
                    hide marie happy
                    jump thurs_end
                "I'll pass":
                    m "With your grades, I'd be the tutor"
                    hide marie concerned
                    show marie averse
                    r ".... Okay, I'll just be on my way then"
                    hide marie averse
                    "Finally some peace and quiet. How annoying"
                    $marie_friendship -=1;
                    jump thurs_end
                "Say Nothing":
                    "I appreciate the sentiment but no reply comes to mind"
                    r "Alright, good night then! I'm here if you want to talk."
                    hide marie concerned
                    jump thurs_end
        "Start tearing up":
            hide marie confused
            show marie concerned
            r "Oh no! Can I give you a hug?"
            menu:
                "Accepts Hug":
                    "We hug for a couple of seconds. It's nice and reassurring"
                    m "Thanks Marie, I needed that. Sometimes things can feel really overwhelming. You know?"
                    hide marie concerned
                    show marie grateful
                    r "Any time %(pname)s. I totally relate. Please let me now if there's anything I can do to help make life a little more manageable"
                    "I hug Marie again. I'm glad to have someone to have someone so supportive in my life"
                    m "Know that I'm here for you too, okay?"
                    r "Hehe Thank you"
                    hide marie concerned
                    jump thurs_end
                "Screw off":
                    hide marie concerned
                    show marie distressed
                    m "I don't need your pity"
                    r "I'm not pitying you. I can tell you're upset so I'm going to give you some space. Let me know if you want to talk about it"
                    hide marie distressed
                    "In my rage, I feel a sliver of regret. I shouldn't have lashed out at Marie so harshly. It was definitely warranted though. Who does she thing she is anyways?"
                    jump thurs_end
                "I'd rather not":
                    r "Alright, I understand. I'm going to give you some space. Please let me know if you need anything!"
                    hide marie concerned
                    jump thurs_end
        "I'm fine. Don't worry about it":
            "I'm already feeling down. I don't really want to deal with people right now on top of that"
            r "I'm here for you if ever need anything!"
            hide marie concerned
            jump thurs_end



label social_media:
    "Here lies the spiciest of the spicy memes"
    "This is premium"
    "Quality"
    "Content"
    jump thurs_end


label prof_email:
    #TODO: figure out how to do screen
    $ email = renpy.input("Email to Proffesor Bonden")
    jump thurs_end
    #$ x = renpy.call_screen("input", prompt="Whatcha gonna do?", someText = "Something")
python:
    """
    TODO
    test and figure out how this works for code
    screen email_input():
        window:
            has vbox

            text "Email to Professor Bonden"
            input default ""

    screen email(prompt, someText = ""):

        window style "input_window":
            has vbox

            text prompt style "input_prompt"
            input id "input" style "input_text" default someText
    """
label thurs_end:
    show marie neutral
    r "It's geeting late. I'm going to sleep now. Nighty night!"
    "Ahh how is it already 1 am?! What an emotional rollercoaster of a day. Time to conk out for today"


label fri_morn:

    scene bg bedroom #temp holder until bedroom upload
    "Ah!!! It's already 11 am. Time to get up"
    "First things first, let's check phone updates"

    if prof_email == True:
        "1. Reminder meeting with professor 2. Triangle Info Session 3. Friend: Let's Hang out 4. Email from Triangle: Make sure to be in business casual for club meeting today"
    else:
        "1. Triangle Info Session 2. Friend: Let's Hang out 3. Email from Triangle: Make sure to be in business casual for club meeting today"

    #TODO: either requestt art or look into code if there's a way to create screen for this
        #first notification- meeting with professor
        #else-club fair today
         #friend text:"Hey let's go out"
         #email notification subject line: dress business casual for club meeting today!
    "Ah!! So much to get done. But let's see... time to figure out what to wear"
    menu: #TODO Figure out problem with loading images as menu options
        "I Sigma Pie T-shirt": #"{image = ../images/itsandwich.png}":
            pass
        "Dress-Shirt and Khakis": #"{image = ../images/itsandwich.png}":
            pass
        "Denim Jacket": #"No pictures pls":
            pass
    "Now all ready to take on today's challenges! We should go speak with Professor Bonden to learn more about what exactly happened with the exam"
    if prof_email == True:
        jump prof_meet
    else:
        jump short_meet

label short_meet:
    scene bg hallway
    show professor happy
    "Nice! Caught Professor Bonden before they leave for the day"
    p "Hey %(pname)s, I'm actully on my way out. I'm going to buy planetarium viewing tickets before they run out. I'm really excited for their exhibit tomorrow."
    p "Is there something that I can do for you?"
    menu:
        "Flattery":
            "Maybe if I ask more about him, he'll be more open to changing my exam grade"
            m "I read your most recent publication. It was really interesting. You're so knowledgeable. I was hoping that we could talk more about it?"
            p "Thank you %(pname)s! I'm so sorry to be doing this but I really do need to get going. Maybe we can chat more about this at a later time. I'm going to head out"
            "Damn. Maybe I should have given him a heads up earlier. I'll just need to find him again later to ask him about it"
            #hide prof
            "Guess, I'll head over to the Triangle's info session early"
            jump club_info
        "Complain about grade":
            m "I was really surprised about my grade. There must have been a grading error"
            #hide prof neutral
            #show prof annoyed/some facial change
            p "Is that so? I put some higher level concepts on the exam that I guess the class didn't quite understand as well as I had hoped. Whatever your grade is, do know that I adjust based on the median at the end"
            m "But my grade is much much worse than even the median. Something must have gone wrong"
            p "I'm sorry %(pname)s but it's pass the deadline for regrades. I don't mean to be harsh but it's important to me and my TAs that we uphold the deadline."
            p "...So sorry to cut our conversation but I do need to get going now. Let's discuss this more later. Maybe we can work something else out? "
            #hide prof
            "Sigh. I guess I'll find the professor again later and maybe we can work something out."
            "Oh! Look at the time, I need to get the Triangle's info-session"
            jump club_info
        "Inquire about Exam":
            m "I was hoping to look over what I did incorrectly on my exam."
            p "Ah yes, I can give you your exam back! Let me go grab yours. Remember that any question regrades should have been requested already"
            m "Thanks Professor Bonden!"
            p "Sorry to cut our meeting short but I do need to run. If you need me for anything, feel free to find me later!"
            #hide prof
            "Man, he's disappeared already. I'll need to find the Professor again later but it seems like he's pretty strict on grade request deadlines. Maybe we can work out something else though"
            "Oh! Look at the time, I need to get the Triangle's info-session"
            jump club_info


label prof_meet:
    scene bg office #office better, classroom works
    show professor happy
    "Oh boy, time to defend my GPA's honor"
    p "Hey %(pname)s, thanks for sending an email to let me know that you were planning on coming in! I managed to snag tickets to the Planetarium this morning. I was worried that they might sell out before I got mine."
    "I highly doubt the tickets to a planetarium would have sold out so soon but as long as the professor's happy I guess!"
    p "What can I do to help you today?"
    menu:
        "Flatery/Ask about Research":
            "Flattery gets you everywhere right? Maybe asking him about his interests will make the Professor more willing to change my exam grade"
            m "I'm really curious about your most recent publication. Woud you mind speaking more about it?"
            p "Oh, yeah! Of course. So the ability to fold space within the reality envelope facilitates the ability to make use of hyperbolic sub-resonant variations, combined with total holistic resonant emanations manifesting astral holographic projection."
            "I blink blankly at Professor Bonden and nod in 'comprehension'. Wow, am I supposed to be understanding what he's saying based on the class materials?? Maybe there's nothing wrong with the test grading after all...."
            p "And that pretty much sums up that paper. Was there anything else you wanted to talk about?"
            menu:
                "Flattery":
                    m "That's really cool! You're so knowledgeable Professor! How did you get into doing research? I think it's something I might want to pursue in the future"
                    #show prof happy
                    p "Thank you %(pname)s. That's great to hear! We can always use more scientists in the world. I got started in research in high school by reaching out to a local college and fell in love with it from there. I'm really apreciative of the good fortune I've had that's led me to be here today and doing what I love"
                    "I'm not sure how to respond to that. It's really nice to hear someone so passionate about their job"
                    p "Ah, but enough about me. Is there something else I can help you with?"
                    menu:
                        "Flattery":
                            #hide prof happy
                            #show prof neutral
                            m "I really liked your lecture last class!"
                            p "Thank you! It's always nice to hear feedback from students. Let me know if there's any complaints and ways I can improve too!"
                            p "Ah! I'm so sorry that we need to cut our conversation short but I actually need to run for a class now. Was there anything else you needed from me?"
                            "Oh crap where had the time gone"
                            m "Yeah! I was actually hoping to discuss the exam grade."
                            p "Ah, yes of course. If you want to go over any of the content, we can review if you drop in at some later point. But remember it's past the deadline to ask for any regrades"
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
    m "I was really surprised about my grade. There must have been a grading error"
    #hide prof neutral
    #show prof annoyed/some facial change
    p "Is that so? I put some higher level concepts on the exam that I guess the class didn't quite understand as well as I had hoped. Whatever your grade is, do know that I adjust based on the median at the end"
    m "But my grade is much much worse than even the median. Something must have gone wrong"
    jump end_prof
label exam_inquiry:
    m "As mentioned in my email, I was hoping to look over what I did incorrectly on my exam"
    p "Ah yes, of course! Let me go grab yours. It's fine for you to look over the exam but remember any regrades should have been requested already"
    m "Thanks Professor Bonden!"
    "Hmm grades might have passed but perhaps if I find enough grading errors the Professor will naturally feel like my exam was graded incorrectly"
    p "Alright here you go! What do you have questions about?"
    "Let's look through my answers that were marked as incorrect and ask about them"
    #To make it harder, user must identify all the grading mistakes consecutively for Professor to consider a regrade
    menu:
        "Mitochondria is the powerhouse of the cell":
            #hide prof neutral
            #show prof shocked
            p "Oh my. Hmm, your rationale makes sense, guess the TA didn't include that as one of the possible answers. What else did you want to ask about?"
            menu:
                "Wrong Answer":
                    #hide prof shocked
                    #show prof neutral
                    jump wrong_answer
                "Right Answer":
                    p "Hmm. I wonder why the TA didn't give you some credit for that response. Was there anything else?"
                    menu:
                        "Wrong Answer":
                            #hide prof shocked
                            #show prof neutral
                            jump wrong_answer
                        "Right Answer":
                            p "Well your answer is factually correct but ... I guess the TA went in a different direction?Was there anything else?"
                            menu:
                                "Wrong Answer":
                                    #hide prof shocked
                                    #show prof neutral
                                    jump wrong_answer
                                "Right Answer":
                                    #show prof shocked
                                    p "Hmm. I would have given that credit as well"
                                    #hide prof schocked
                                    #show prof neutral
                                    p "Actually for all of these questions that you pointed out, I think you could have earned some more points, why didn't you bring it up earlier?"
                                    m "I've been so stressed about my other classes that I didn't want to add the emotional backlash of a bad grade on top of this week. So I only checked my score last night"
                                    m "Haha... I guess that wasn't the best move"
                                    p "That's totally understandable, %(pname)s. We all do our best to handle all of our responsibilities but sometimes it just gets too much and you need to avoid certain stressors."
                                    p "It is past the time that we usually allow for regrades but let me look over your exam again and discuss with my TAs about anything we missed in our accepted answers"
                                    m "Thank you so much Professor Bonden! I really appreciate it."
                                    p "No problem that's what I'm here for after all"
                                    p "Oh my!! Look at the time, I'm late for the next class that I'm scheduled to teach. Gotta run!"
                                    m "Well, I did all that I can do. Oh my! Look at the time, I need to hurry in order to get the Triangle's info session on time"
                                    jump club_info

                                "Wrong Answer":
                                    #hide prof shocked
                                    #show prof neutral
                                    jump wrong_answer

                        "Wrong Answer":
                            #hide prof shocked
                            #show prof neutral
                            jump wrong_answer
                "Wrong Answer":
                    jump wrong_answer
        "Wrong Answer":
            jump wrong_answer
        "Wrong Answer":
            jump wrong_answer
label wrong_answer:
    p "That's not quite right. You need to be a bit more specific in your answer as well as the information that you did provide is factually incorrect"
    m "I don't get why I didn't get any credit for this question. It can be interpreted that way"
    p "This quesiton isn't really one for interpretation. It's an all or nothing kind of question"
    m "I think I could have still gotten some credit though"
    p "I don't mean to accuse but are you trying to inadvertently ask for a regrade?"
    m "Uh...A little bit"
    p "This time is meant for us to cover any concepts you don't understand. Not regrades"
    jump end_prof
label end_prof:
     p "I'm sorry %(pname)s but it's past the deadline for regrades. I don't mean to be harsh but it's important to me and my TAs that we uphold the deadline."
     p "...So sorry to cut our conversation but I do need to run to my next class now. Let's discuss this more later. Maybe we can work something else out? "
     "Sigh. I guess I'll find the professor again later and maybe we can work something out."
     "Oh! Look at the time, I need to get the Triangle's info-session"
     jump club_info

label club_info:
    scene bg classroom
    "Walking in the club room, the first thing I notice is that it’s packed. All the classroom seats were filled with people spilling out sitting on the floor and standing at the back. I spot a sign in sheet and awkwardly maneuver myself through the crowd."
    "Muttering “I’m sorrys” for disrupting the people on the floor, I signed myself in and shuffled to an empty spot along the wall."
    "The room feel to a hush as some stranger started their presentation"
    show max charm
    b "Hi Guys! Thank you all for your interest in joining the {b}{i}T r i a n g l e{/i}{/b}! We’re a tight knit community from across the schools. We do X, Y and Z for the school, really great things. We have lots of funding for whatever projects that you come up with."
    "I over hear someone whispering to their friend. I've heard that getting into the Triangle pretty much sets you up for guaranteed work at any of the big companies. Their alumni connections are crazy."
    "Woah, I definitely want to get in if that's the case. It'll help me for whatever I want to do in the future"
    b "And that's the {b}{i}T r i a n g l e{/i}{/b}! Thank you all for coming. Please feel free to come up to any of the board members to fill out an application form and get to know us!"
    hide max charm
    show max wink
    b "Hope to learn more about all of you who manage to get into the best organization ever, the rest of you eh."
    hide max wink
    show max neutral
    "Whoa arrogant much? Let's chat with him"
    b "Hi, I'm Maximillion. My friends call me Max though. How can I assist a commoner like you today?"
    "Commoner?"
    menu:
        "Ignore ":
            "Commoner, the heck is wrong with this dude. Better to just fill out my club application and call it a day"
            m "Hi,I'm %(pname)s"
            jump club_app
        "Snarkily Compliment":
            m "Nice job up there. Maybe you're not a fellow commoner after all "
            show max charm
            b "Wow. Sass back. I like. Be careful though, with someone as classy as myself. It'll be hard to keep up."
            m "Sounds to me like you're scared of some competition"
            b "You wish. Haha enough of this. And you are?"
            m "Maybe, I'm %(pname)s"
            b "Nice to meet you  %(pname)s, kinda!"
            m "I feel the same way"
            m"Haha anyways"
            $ maximillion_friendship +=1
            jump club_app
        "Insult":
            "This absolute ass"
            m "How can a pile of trash such as yourself help me?"
            show max mad
            b "You must have no friends so you don't understand the premise of helping others"
            m "Not really, sounds like you've had experience though"
            b "...What can I do for you trash?"
            $ maximillion_friendship -=1
            jump club_app
        "Compliment":
            show max neutral
            "Let's just ignore the commoner comment. This dude clearly has a superiority complex better play into it. It might help my chances of getting in"
            m "Hi, great job up there! I'm %(pname)s Hopefully, I'll be able to be up there with you guys next year presenting about the great Triangle club"
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
    $ app2 = renpy.input("What past experiences do you have that makes you qualified to be a Triangle")
    $ app3 = renpy.input("We plan many events at school for the community. What event would you throw if you were in the Triangle")
    "Hopefully my answers are good enough"
    b "And now you're all set!"
    b "If you make it to the next stage, we'll reach out to you about setting up an interview this weekend"
    "Woah that's fast. I'm so nervous. Hopefully this all works out"
    jump max_convo
label max_convo:
    if maximillion_friendship > 0:
        show max charm
        b "You seem like someone that's worthwhile of being more than just an acquintance. Dare I even say it, a friend?"
        m "Wow. Who would have thought. The Mighty Maximillion deigning himself to fraternize with a commoner like me"
        b "Hey that's the Mighty Max to you"
        m "*shook pikachu face* o_O WOAH"
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
                "That went prety well! Maximillion's a good guy"
            "Maybe. Maybe not":
                m "Yeah, I guess we'll see!"
                b "Alright see ya!"
                "That went prety well! Maximillion seems alright"
    elif maximillion_friendship ==0:
        show max neutral
        b "Thanks for coming to attend! Please feel free to contact me if you ever have any more questions about the Triangle"
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
                "That went prety well! Maximillion's a good guy"
            "Maybe. Maybe not":
                m "Yeah, I guess we'll see!"
                b "Alright see ya!"
                "That went prety well! Maximillion seems alright"
    else: #case where friendship is negative number
        show max mad
        b "What are you still doing here?"
        m "Just seeing if an ass such as yourself has any plans on a Friday night"
        b "I'll be at the library studying. Not that your small brain would be able to relate to mental stimulus"
        m "I'm actually on heading there later too"
        b "Oh,ugh. Unfortunately, I'll see you later then"
        menu:
            "Hopefully not":
                hide max neutral
                show max mad
                b "Yeah. I wouldn't want to be seen fraternizing with filth after all"
                $ maximillion_friendship -=1
                "That guy's such an ass. What type of club member is unable to even be polite to prospective members. Once I get into the club, I'll kick him out... I guess I was being a jerk too. No. My reactions were warranted. Ugh. Hopefully, I don't see him at the library tonight"
            "Totally":
                hide max mad
                show max skeptic
                m "Yeah, see you there later tonight!"
                $ maximillion_friendship +=1
                b "Oh, yeah. I guess, maybe"
                "That was a weak attempt at making things right. Man what was I doing? If that guy's a club member, he carries weight in whether I get into the club or not. I'll do better at trying to reconcile with him"
            "Maybe. Maybe not":
                hide max mad
                show max neutral
                m "Yeah, I guess we'll see!"
                b "Based on what I've seen. Let's hope not"
                "Ugh. Max seems like an ass. If he's there tonight, I'll just have to deal with it"
    "Ah ...I'm kinda tired from everything that's been going on today. Time to go to Boz for a caffeine fix"
    jump caffeine
label caffeine:
    scene bg coffeeshop
    "Nothing beats a cup of boz"
    "Oh wow look at that! It's Professor Bonden"
    show professor happy
    m "Hey Professor"

python:
    """"label friend_party:
        menu:
            "Challenge Friend to SMASH ULTIMATE DEATH MATCH":
                pass
            "Talk to mysterious stranger in the sweater vest":
                pass
            "Speak with friend":
                pass"""
