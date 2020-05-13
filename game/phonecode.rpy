############ phone code screens here########
# if you dont use  1920 x 1080 youre going to have to play with these numbers to get it to work and make the phone image be smaller somehow
# just keep changing stuff and refreshing the game until it works, sorry lol

#by nadia nova: https://nadianova.itch.io/phone-message-system-for-renpy


init 5:
    style phone_message_vbox:
        xalign 0.54
        yalign 0
        ypos 215
        xsize 360
        xoffset -40

    style phone_message_frame:
        background Solid("#d9398c")
        ypadding 10
        xpadding 10

    style phone_message_frame2:
        background Solid("#78E8A0")
        ypadding 10
        xpadding 10

    style phone_message_contents:
        spacing 10

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message2 is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0


    style phone_message_who is phone_message:
        color "#ecf0f1"
        size 25

    style phone_message_what is phone_message:
        color "#ffffff"
        size 24
    style phone_reply is default:
        size 18
        xalign 0.56
        xsize 475
        background Solid("#666")
        hover_background Solid("#78E8A0")
        ypadding 10
        xpadding 10


screen phone_message(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message2(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -300
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("#78E8A0")
            xsize 200

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message3(what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -300
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("#78E8A0")
            xsize 200

            vbox:
                style "phone_message_contents"
                ##text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_reply(reply1, label1, reply2, label2):
    modal True
    vbox:
        xalign 0.50
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"

# here is a new menu that has more options than two
# basically i just added one more textbutton here, and the additional labels needed in the call
# if you wish to make a menu with one or four just copy the code below and modify it a bit
screen phone_reply3(reply1, label1, reply2, label2, reply3, label3,):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"
        textbutton "[reply3]" action Jump(label3) style "phone_reply"


style phone_reply_text:
    xalign 0.56

screen phone_message_image(who, what, img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"
                add img



############# phone code ends ############



################# phone code options start ###################

image phone:
    zoom .75
    "images/phone.png"


# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.3 yoffset 100

transform phone_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300


transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1

transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message


#### labels to shortcut stuff so you dont need to copypaste stuff repeatedly! #####

label phone_start:
    window hide
    show phone at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return

label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return

label phone_msgi:
    $ renpy.pause()
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return


label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return

label phone_end:
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    show phone at phone_hide
    $ renpy.pause(0.2)
    return

label message(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return

label reply_message(what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    return

label message_img(who, what,img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    return


label message_start(who, what):
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return





######### phone code ends here ##########
