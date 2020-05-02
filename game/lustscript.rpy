
label lust_start_dorm:

    $prof_email = False

    scene bg bednight #temp holder until bedroom upload

    "Ayyy. Bless. First round of testing season is over ... {p=3.0}and it's a Thursday night!! No immediate responsibilities that need to be taken care of and no need to stress about academics for a while...."
    "...{p=1.0}Maybe I should finally check my scores for Science of Everything class."
    "I've been avoiding checking grades to minimize stress but I'm free from everything! {p=2.0}Nothing can hurt me now."

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
            $ prof_friendship +=1
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
            $ prof_friendship +=1
            "Maybe if I ask more about him, he'll be more open to changing my exam grade"
            m "I read your most recent publication. It was really interesting. You're so knowledgeable. I was hoping that we could talk more about it?"
            p "Thank you %(pname)s! I'm so sorry to be doing this but I really do need to get going. Maybe we can chat more about this at a later time. I'm going to head out"
            "Damn. Maybe I should have given him a heads up earlier. I'll just need to find him again later to ask him about it"
            #hide prof
            "Guess, I'll head over to the Triangle's info session early"
            jump club_info
        "Complain about grade":
            $ prof_friendship -=1
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
            $ prof_friendship +=1
            "Flattery gets you everywhere right? Maybe asking him about his interests will make the Professor more willing to change my exam grade"
            m "I'm really curious about your most recent publication. Woud you mind speaking more about it?"
            p "Oh, yeah! Of course. So the ability to fold space within the reality envelope facilitates the ability to make use of hyperbolic sub-resonant variations, combined with total holistic resonant emanations manifesting astral holographic projection."
            "I blink blankly at Professor Bonden and nod in 'comprehension'. Wow, am I supposed to be understanding what he's saying based on the class materials?? Maybe there's nothing wrong with the test grading after all...."
            p "And that pretty much sums up that paper. Was there anything else you wanted to talk about?"
            menu:
                "Flattery":
                    $ prof_friendship +=1
                    m "That's really cool! You're so knowledgeable Professor! How did you get into doing research? I think it's something I might want to pursue in the future"
                    #show prof happy
                    p "Thank you %(pname)s. That's great to hear! We can always use more scientists in the world. I got started in research in high school by reaching out to a local college and fell in love with it from there. I'm really apreciative of the good fortune I've had that's led me to be here today and doing what I love"
                    "I'm not sure how to respond to that. It's really nice to hear someone so passionate about their job"
                    p "Ah, but enough about me. Is there something else I can help you with?"
                    menu:
                        "Flattery":
                            $ prof_friendship -=3
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
    $ prof_friendship -=1
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
                                    $grade_change = True
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
    w "Hi Guys! Thank you all for your interest in joining the {b}{i}T r i a n g l e{/i}{/b}! We’re a tight knit community from across the schools. We do X, Y and Z for the school, really great things. We have lots of funding for whatever projects that you come up with."
    "I over hear someone whispering to their friend. I've heard that getting into the Triangle pretty much sets you up for guaranteed work at any of the big companies. Their alumni connections are crazy."
    "Woah, I definitely want to get in if that's the case. It'll help me for whatever I want to do in the future"
    w "And that's the {b}{i}T r i a n g l e{/i}{/b}! Thank you all for coming. Please feel free to come up to any of the board members to fill out an application form and get to know us!"
    hide max charm
    show max wink
    w "Hope to learn more about all of you who manage to get into the best organization ever, the rest of you eh."
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
            m "Not really. Sounds like you've had a lot of personal experience with having no friends though"
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
                "That was a weak attempt at making things right. Man what was I doing? If that guy's a club member, he carries weight in whether I get into the club or not. I'll do better at trying to reconcile with him later tonight"
            "Maybe. Maybe not":
                hide max mad
                show max neutral
                m "Yeah, I guess we'll see!"
                b "Based on what I've seen. Let's hope not"
                "Ugh. Max seems like an ass. If he's there tonight, I'll just have to deal with it"
    "Ah ...I'm kinda tired from everything that's been going on today. Time to go to Beau's Coffee for a caffeine fix"
    jump caffeine
label caffeine:
    scene bg coffeeshop
    "Nothing beats a cup of coffee"
    "Oh wow look at that! It's Professor Bonden"
    show professor happy
    m "Hey Professor"
    p "Hey %(pname)s?, nice to see you again. How are you doing?"
    menu:
        "Ask about Well Being":
            $ prof_friendship +=1
            m "I'm doing pretty well! Thanks for asking. How are you doing?"
            p "I am doing amazingly! I have my Planetarium tickets that I'm super excited for. They're doing an exclusive show about a recent breakthrough on {b}Dark Energy{\b}."
            p "It should be really exciting! If you get a chance, you should check it out!"
            m "Maybe! Sounds interesting"
            p "Right and before I forget about our earlier discussion, I think we can work out some extra credit assignment to help boost your grade"
            "Hmm that's kind of vague, what kind of assignment?"
            p "We can work out the details later! But for now, I gotta run!"
            hide professor happy
            "I'm so glad to have Professor Bonden. His passion for astronomy is adorable. Nerdy. {p=1.5} But adorable. Hmm I wonder what the extra credit assignment is going to be exactly?"
        "Snarkily Mention Grade":
            $ prof_friendship -=1
            $grade_change = False
            m "I'm doing eh. Could be better. Especially if my exam score was better"
            #hide professor happy
            #show professor neutral
            p "I'm sorry %(pname)s. Rules are rules. There can't be any exceptions regarding regrades"
            m "Please professor. Isn't there anything I can do? My test wasn't even wrong, just graded incorrectly"
            p "Maybe we can work out some extra credit assignment to help boost your grade. I'm not so sure"
            m "Thank you. Thank you! I'll definitely do it"
            p "No promises though. I need to run, see you"
            "I don't think Professor Bonden appreciated the attitude. Or maybe he did. He's considering giving me more points for extra credit after all! Now what kind of extra credit assignment would be grand enough to convince him of giving me extra points?"
        "Polite Grade Inquiry":
            m "I'm doing well, thanks for asking! I was wondering if you would mind if we continued our discussion from earlier?"
            #hide professor happy
            #show professor neutral
            p "Yeah, sure. I can spare a few minutes."
            if  grade_change == True:
                p "I'm still discussing with the TAs about our decision regarding the regrade of your answers. But we'll let you know!"
                m "Thank you so much Professor! I really appreciate it"
                p "But aside from that, I think that if you want we can potentially work out some extra credit assignment to help boost your grade."
                m "Really? Thank you so much! I would really appreciate that."
                p "Yeah! Let's speak more about this later. I need to go. Remind me!"
                "Thank goodness. I think based on our earlier conversation, I should be set regarding my test regrade. But, I guess you never really know. I wonder what the extra credit assignment would be exactly?"
            else:
                m "I understand that I missed the regrade request deadline and that's my fault. But I'm really worried about my performance in this class"
                p "Thank you for reaching out to me about this. I think we can work out some extra credit assignment to help boost your grade."
                m "...Really? {p=2.0} THANK YOU SO MUCH PROFESSOR YOU WON'T REGRET THIS"
                p "Hahahaha I'm glad to be of service."
                p "I actually need to run now, but let's hash out the specifics later!"
                "Professor Bonden is so nice. I wonder what the extra credit assignment is going to be exactly?"
    jump max_library

label max_library:
    scene bg themil
    show max neutral
    if maximillion_friendship == 2:
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
        "What do I want to talk about?"
        menu:
            "Professor Bonden":
                m "Do you know about Professor Bonden?"
                b "Yep! He's one of the science professors, yeah? I think I've heard mixed things about him"
                m "Yeah, he's my Science of Everything Professor. I'm worried about my grade for the class especially after my last test"
                hide max charm
                show max neutral
                b "Huh, can't say I relate to that problem but have you tried discussing your concerns with him?"
                m "Not everyone can be blessed with your talents."
                m"Actually, I missed the deadline for regrades but when I spoke with him today he did vaguely mention the opportunity for extra credit"
                b "Huh, sounds kind of irresponsible"
                b "Wait, you said Professor Bonden right? I have heard about his extra credit assignments!"
                m "Really? Please do tell"
                hide max neutral
                show max wink
                b "I've heard that he has quite the reputation in letting people plead their case back in his bedroom"
                menu:
                    "Confused":
                        m "Huh? Is that where his students go to present their side report? Why not just do it in his office or the classroom?"
                        b "Hahahahahahahahahahahaha that's funny. {p=3.0}  Wait are you forreal? How oblivious can you be"
                        hide max wink
                        show max neutral
                        b "Simpleton much?"
                        #maximillion_friendship -=1 (Should I? D:)
                        m "Dude, chill. Elaborate please?"
                        "Man this dude has a hell of a superiority complex"
                        b "You know, the devil's tango? Do the nasty? A bit of crumpet?"
                        b "Baking the potato? Funny business?Snibbing? Testing the humidity? Violating the prime directive? Monkey business"
                        b "Making the beast with two backs?"
                        m "Alright!!! I get it. Stop it. People are looking at us weirdly"
                        b "Well, now you know."
                        m "I don't know, Bonden doesn't seem like the type."
                        b "Why not? Sometimes that's just how it is. Actually, something similar happens with the {b}{i}T r i a n g l e{/i}{/b} actually"
                        m "So, if I were to get closer with you, I'd be a future Traingle huh?"
                        hide max neutral
                        show max wink
                        b "Now you're getting it"
                        m "Huh, I see"
                        hide max wink
                    "Accept":
                        m "Woah, really?? I never imagined Bonden to be so saucy. Good on him for using his position in his favor lol"
                        b "Right, what a guy. Kind of sus but you know both parties are benefitting"
                        m "Righttttt, no need to delve into the ethics of this situation"
                        b "Wow, how refreshing to hear that's how you feel. Actually, speaking about all of this."
                        show max wink
                        $ maximillion_friendship +=1
                        b "Just to give you an insider tip, there's a supplement you can attach for your {b}{i}T r i a n g l e{/i}{/b} application too."
                        b "Involving us {p=2.0}....attaching ourselves together"
                        hide max wink
                        show max charm
                        m "Well, I guess we'll have to see about that huh?"
                        b "I think I know what's going to happen, not everyone gets such priviledges %(pname)s,  you know?"
                        b "Oh, just so you know. You've got an interview Sunday morning. Let me know if you want me to put in a good word before it. I'll be at Hel's tomorrow night maybe I'll see you then"
                        m "Guess we'll have to see how lucky you get then huh?"
                        b "Ha, I guess so"
                        hide max charm
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
        "What.{p=2.0} the. {p=2.0} "
        "This guy is the Asshole Supreme Overlord or something"
        m "Before I hurt you and make the world a slightly better place. Can I ask you something?"
        "Might as well get some intel from this unpleasant conversation"
        hide max mad
        show max skeptic
        b "I guess...I'll do some charity work and depart my wisdom upon today's uncouth youth"
        "What do I want to talk about?"
        menu:
            "Professor Bonden":
                hide max skeptic
                show max neutral
                m "Do you know anything about Professor Bonden and his extra credit policy?"
                b "Ha! Of course you'd be asking about extra credit policies. What, flunkinng classes already?"
                m "No. Just curious"
                b "Right, sure. Yeah, I do know about Professor Bonden and his ways. He's got quite the interesting extra credit policies"
                m "Right, spit it out already"
                b "Hah, now what would I get out of just tellilng you"
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
                                b "What's wrong? A mutualistic relationship, the professor gets something and the student gets something"
                                b "With a whole lot of debauchery"
                                show max wink
                                b "Since you're so desperate for information. Let me give you some extra intel. Consider it a gift for the unfortunate"
                                b "We actually do something similar at the {b}{i}T r i a n g l e{/i}{/b} too"
                                m "What."
                                b "You didn't hear it from me. But maybe you want to consider doing something supplemental with your interview on Sunday morning and everything."
                                b "Let me know what you decide at Mel's tomorrow night"
                                m "WHAT"
                                hide max wink
                            "Accept":
                                m "Huh, I'm surprised to hear that Professor Bonden would be the type. But I guess with every system there's some form of corruption"
                                b "Even a desperate idiot like you gets it. How refreshing"
                                show max vicious
                                b "I'll let you in on some even more infomation. That's actulally something that could benefit your {b}{i}T r i a n g l e{/i}{/b} application too."
                                m "Ugh. The thing that you're implying sickens me greatly"
                                b "You sicken me. Well...you wouldn't want to hurt your chances especially since you've made it to the interview stage and everything"
                                m "....What?"
                                b "Being on the exec board and everything, it'd be so easy to sway the decision of your application"
                                m "Now what would you have me do about this?"
                                b "Let me know, I'll be at Hel's tomorrow night"
                                b "See ya, wouldn't want to be ya"
                                m "Lol, true that. Even you wouldn't want to do the nasties with yourself huh?"
                                hide max vicious
                    "Nothing":
                        m "Haha, for you? Nothing really, your information is probably useless anyways"
                        b "Just as I expected from you %(pname)s"
                        b "There's nothing that you have worth anything of value to me anyways"
                        m "Whatever, knowing you, this was expected. Nothing comes from nothing after all"
                        b "Ignoring that zinger. I'm going to bless your desperate self with some information"
                        b "Bonden has quite the reputation in letting people plead their case back in his bedroom"
                        menu:
                            "Disgust":
                                m "You've got to be kidding me. There's no way Professor Bonden is the type"
                                b "Take it or leave it. That's what I know"
                                m "Ugh of course you'd be the type to be so nonchalant about this"
                                b "What's wrong? A mutualistic relationship, the professor gets something and the student gets something"
                                b "With a whole lot of debauchery"
                                show max wink
                                b "We actually do something similar at the {b}{i}T r i a n g l e{/i}{/b} too"
                                m "What."
                                b "You didn't hear it from me. But maybe you want to consider doing something supplemental with your interview on Sunday Morning and everything."
                                b "Let me know what you decide at Mel's tomorrow night"
                                m "WHAT"
                                hide max wink
                            "Accept":
                                m "Huh, I'm surprised to hear that Professor Bonden would be the type. But I guess with every system there's some form of corruption"
                                b "Even an idiot like you gets it. How refreshing"
                                show max vicious
                                b "I'll let you in on some even more infomation. That's actulally something that could benefit your {b}{i}T r i a n g l e{/i}{/b} application too."
                                m "Ugh. The thing that you're implying sickens me greatly"
                                b "You sicken me. Well...you wouldn't want to hurt your chances especially since you've made it to the interview stage and everything"
                                m "....What?"
                                b "Being on the exec board and everything, it'd be so easy to sway the decision of your application"
                                m "Now what would you have me do about this?"
                                b "Let me know, I'll be at Hel's tomorrow night"
                                b "See ya, wouldn't want to be ya"
                                m "Lol, true that. Even you wouldn't want to do the nasties with yourself huh?"
                                hide max vicious
    else:
        show max neutral
        b "Hey, %(pname)s right? Surprised to see you here on a Friday night"
        "Right, the guy from the {b}{i}T r i a n g l e{/i}{/b} earlier"
        m "Hey Maximillion. Yeah, the grind really doesn't stop"
        m "Actually, would you mind if I asked you about something?"
        b  "Sure, I'll depart my wisdom upon today's uncouth youth"
        "My gosh. Uncouth? Youth? What type of eccentric boomer is this"
        "What do I want to talk about?"
        menu:
            "Professor Bonden":
                m "Do you know about Professor Bonden?"
                b "Yep! He's one of the science professors, yeah? I think I've heard mixed things about him"
                m "Yeah, he's my Science of Everything Professor. I'm worried about my grade for the class especially after my last test"
                hide max charm
                show max neutral
                b "Huh, can't say I relate to that problem but have you tried discussing your concerns with him?"
                m "I spoke about it with him today."
                m"Actually, I missed the deadline for regrades but when I spoke with him today he did vaguely mention the opportunity for extra credit"
                b "Huh, sounds kind of irresponsible"
                b "Wait, you said Professor Bonden right? I have heard about his extra credit assignments!"
                m "Really? Please do tell"
                hide max neutral
                show max wink
                b "I've heard that he has quite the reputation in letting people plead their case back in his bedroom"
                menu:
                    "Confused":
                        m "Huh? Is that where his students go to present their side report? Why not just do it in his office or the classroom?"
                        b "Hahahahahahahahahahahaha that's funny. {p=3.0}  Wait are you forreal? How oblivious can you be"
                        hide max wink
                        show max neutral
                        b "Simpleton much?"
                        $ maximillion_friendship -=1
                        m "Dude, chill. Elaborate please?"
                        "Man this dude is judgemental to the max"
                        b "You know, the devil's tango? Do the nasty? A bit of crumpet?"
                        b "Baking the potato? Funny business?Snibbing? Testing the humidity? Violating the prime directive? Monkey business"
                        b "Making the beast with two backs?"
                        m "Alright!!! I get it. Stop it. People are looking at us weirdly"
                        b "Well, now you know."
                        m "I don't know, Bonden doesn't seem like the type."
                        b "Why not? Sometimes that's just how it is. Actually, something similar happens with the {b}{i}T r i a n g l e{/i}{/b} actually"
                        m "So, if I were to get closer with you, I'd be a future Traingle huh?"
                        hide max neutral
                        show max wink
                        b "Now you're getting it"
                        m "Huh, I see"
                        hide max wink
                    "Accept":
                        m "Woah, really?? I never imagined Bonden to be so saucy. Good on him for using his position in his favor lol"
                        b "Right, what a guy. Kind of sus but you know both parties are benefitting"
                        m "Righttttt, no need to delve into the ethics of this situation"
                        b "Wow, how refreshing to hear that's how you feel. Actually, speaking about all of this."
                        show max wink
                        $maximillion_friendship +=1
                        b "Just to give you an insider tip, there's a supplement you can attach for your {b}{i}T r i a n g l e{/i}{/b} application too."
                        b "Involving us {p=2.0}....attaching ourselves together"
                        hide max wink
                        show max charm
                        m "Well, I guess we'll have to see about that huh?"
                        b "I think I know what's going to happen, not everyone gets such priviledges %(pname)s,  you know?"
                        b "Oh, just so you know. You've got an interview Sunday morning. Let me know if you want me to put in a good word before it. I'll be at Hel's tomorrow night maybe I'll see you then"
                        m "Guess we'll have to see how lucky you get then huh?"
                        b "Ha, I guess so"
                        hide max charm

    "As our conversation comes to a stop, I try to focus on my work with no avail...Was Maximillion right about Professor Bonden?"
    "If he is, was I willing to go through with it just to get the grade boost?"
    "And what the heck. The way to get into the Triangle is the same way?"
    "After failing to get any work done in the hours I spend at the library. I call it a night and trudge back to my dorm"

label sat_room:
    scene bg bedroom
    "I get a restless sleep. Thinking about what Maximillion had said the other today. What kind of extra credit did Professor Bonden mean?"
    "I was originally thinking about doing a presentation or report about the planetarium or something academic related. Who would have thought that getting a good grade would be this complicated"
    "Not to mention, what Maximillion said about the {b}{i}T r i a n g l e{/i}{/b} application. Things like this actually happen?"
    "Trying to focus on my work, nothing really gets done for the entire day as I deliberate the best course of action"
    "Come on, %(pname)s! What to do, what to do"
    "After a lot of deliberation, and the day pretty much gone to waste. The one thing I'm set on is that I need to go to Hel's and talk to Maximillion some more."




label mel_night:
    scene hel
    show max charm
    b "Oh, hey %(pname)s! Nice of you to finally join us. Did you think about what I said?"
    "Wait, it can't be. Is that... Professor Bonden?"
    m "Wait, sorry. Let me get back to you. "
    b "Aurevoir"
    hide max charm
    show professor happy
    p "Hey %(pname)s! It's not weird at all to be seeing your at such an establishment"
    "O .o can't say I relate to that"
    m "Hey ....Professor! It's nice seeing your here"



python:
    """"label friend_party:
        menu:
            "Challenge Friend to SMASH ULTIMATE DEATH MATCH":
                pass
            "Talk to mysterious stranger in the sweater vest":
                pass
            "Speak with friend":
                pass"""
