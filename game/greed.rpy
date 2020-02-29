label career_fair_intro
    ##scene bg careerfair1

    "It's finally the day of the career fair! I will make something out of
    myself today just like Pres Beau wanted."

    "I guess I need to go talk to some recruiters though..."

    ##scene bg careerfair2

    "Ah! MicroHard! That's a really competitive company... Ugh... I should
    probably apply shouldn't I..."

    ##show recruiter

    define recruit = Character("Recruiter")

    "Ugh... I should introduce myself..."
    "Hello! Ugh...I'm " #$name
    "Um...I'm really interested in your company! What internship opportunities
    do you have for undergraduates?"

    recruit "Yes, well we have several hands-on opportunities for all years!
    If you are interesting in applying..."

    ##fade bg Burner

    "That was exhausting. I should..."

    menu:
        "Go back to my dorm.":
            "You return to your room."
            jump dorm1

        "Stay in Burner a while longer."
            "You loiter around the outside of Burner."
            jump Burner1

label dorm1

    ##scene bg room

    "Ah, finally it's time to nap."

    ##show roommate happy

    r "Hey, " #$name
    r "You just came back from the career fair right? How was it?"

##    menu:
##        "Ugh...It was awful. I hate networking.":
##            jump
