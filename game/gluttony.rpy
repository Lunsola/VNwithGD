#this is the gluttony chapter

#format for writing dialogue is:
#e "dialogue goes here" (where e is the variable associated with the character)
#"this is a narrative with no actual speaker"

label roommateintro:
    r "I’m so excited for us to get to know each other!"
    menu:
        "Me too!": #friendship +1
            pass
            #roommate response
        "I guess. We‘ll sure be spending a lot of time together.":
            pass
            #roommate response
        "Don't say anything":
            pass
            #dialogue box goes away and cricket sound effect
    r "By the way, do you want to have lunch together today? I invited someone I met in class and I’d love for you to join."
    menu:
        "Yeah! Sounds fun, I love meeting new people.": #friendship +1
            pass
            #roommate response
        "No thanks.":
            pass
            #roommate response
        "Don't feel like it, no":
            pass
            #roommate response


##label gluttonyscene_1:
    ##"just start writing text"
    ##if conditionupon:
        ##jump conditionupon
    ##else:
        ##jump secondoption

##label conditionupon:
