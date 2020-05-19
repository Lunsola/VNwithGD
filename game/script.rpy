# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define r = Character("Marie")
define j = Character("Josh")
define b = Character("Maximillion")
define m = Character("Me")
define p = Character("Professor Bonden")
define op = Character("Professor Breaken")
define k = Character("Karen")
define a = Character("Marven")
define s = Character("Professor")
define w = Character("???") #for characters where name is thus far unknown
define c = Character("Crowd")

#character transforms
transform sleft:
    yalign 1.0
    xalign .25
transform sright:
    yalign 1.0
    xalign .75
transform hop: #makes character do small jump
    yalign 1.0
    linear .1 yalign .5
    linear .1 yalign 1.0
transform shake:
        yalign 1.0
        xalign .75
        ease .06 xoffset 8
        ease .06 xoffset -8
        ease .05 xoffset 2
        ease .05 xoffset -2
        ease .04 xoffset 4
        ease .04 xoffset -4
        ease .03 xoffset 6
        ease .03 xoffset -6
        ease .02 xoffset 4
        ease .02 xoffset -4
        ease .01 xoffset 2
        ease .01 xoffset -2
        ease .01 xoffset 0

#marie images
image marie neutral = "roomate_rabbit.png"
image marie happy = "roomate_smile_default.png"
image marie grateful = "roomate_natural_smile.png"
image marie surprised = "roomate_astonished.png"
image marie astonished = "roomate_very_astonished.png"
image marie confused = "roomate_extremely_astonished.png"
image marie ingenuine = "roomate_fake_smile.png"
image marie averse = "roomate_aversion.png"
image marie v happy = "roomate_big_smile.png"
image marie mad = "roomate_smiling_angry.png"
image marie nervous = "roomate_surprized.png"
image marie nervous2 = "roomate_sweating.png"
image marie distressed = "roomate_angry_sad.png"
image marie concerned = "roomate_concerned.png"
image marie urdumb = "roomate_speechless.png"
image marie angry = "roomate_angry.png"
image marie cry = "roomate_sad_2.png"

#max images
image max happy = "max happy.png"
image max neutral = "max neutral.png"
image max mad = "max mad.png"
image max breaking = "max breaking.png"
image max grateful = "max grateful.png"
image max skeptic = "max skeptic.png"
image max wink = "max wink.png"
image max vicious = "max vicious.png"
image max charm = "max charm.png"

#josh images
image josh grateful = "Neutral Grateful.png"
image josh v grateful = "Neutral v Grateful.png"
image josh sad = "Neutral Sad.png"
image josh shock = "Neutral Shock.png"
image josh stress = "Neutral Stress.png"
image josh wink = "Neutral Wink.png"
image josh happy = "Neutral Happy.png"
image josh wave = "wave happy.png"
image josh approve = "Thumbs up Happy.png"
image josh t grateful = "Thumbs up v grateful.png"
image josh support = "Thumbs up Wink.png"
image josh batterup = "Baseball Happy.png"
image josh v gratefulbat = "Baseball v Grateful.png"
image josh shockbat = "Baseball Shck.png"
image josh stressbat = "Baseball Stress.png"
image josh shockfg = "Finger Gun Shock.png"
image josh winkfg = "Finger Gun WInk.png"
image josh mad = "josh_anger.png"
image josh neutral = "josh_neutral.png"

#music boi images (added underscores bc music gets read as a fxn)
image music_neutral = "music_neutral.png"
image music_dark = "music_oho.png"
image music_unimpressed = "music_hmph.png"
image music_wink = "music_wink.png"
image music_moody = "music_moody.png"
image music_mad = "music_mad.png"
image music_talk = "music_openmouth.png"
image music_sad = "music_disappointment.png"
image music_smile = "music_heh.png"
image music_nervous = "music_nervous.png"
image music_bent = "music_maskbent.png"
image music_default = "music_maskdefault"
image music_cross = "music_maskcross.png"

#professor images
image professor happy = "Professor_happy.png"
image professor surprised = "Professor_Shocked.png"
image professor mad = "Professor_annoyed.png"
image professor neutral = "Professor_neutral.png"
image professor pleased = "Professor_pleased.png"

#other character images
image recruiter = "recruiter.png"
image triangler = "triangle.png"
image breaken = "breaken.png"
image Karen = "Karen.png"

#item images
image sandwich = "itsandwich.png"
image up:
    zoom 0.3
    "arrow_up.png"
image down:
    zoom 0.8
    "down_arrow.png"
image PosterP = "partyposter.png"
image gift = "gift.jpg"
image meme1 = "meme1.jpg"
image meme2 = "meme2.jpg"
image goodend = "goodend.png"
image badend = "badend.png"
image dinhallfood = "dinhallfood.png"
image dinhallfood2 = "dinhallfood2.png"
image pizza = "pizza.png"

#backgrounds
image bg classroom:
    zoom 1.3
    "classroom.jpg"
image bg john jay = "jonathanjay.jpg"
image bg EC = "EC.jpg"
image bg themil = "library.jpg"
image bg bednight:
    zoom 1.2
    "bedroom_night.jpg"
image bg bedroom:
    zoom 1.2
    "bedroom.jpg"
image bg office:
    zoom 0.5
    "office.jpg"
image bg coffeeshop:
    zoom 1.40
    "Coffee Shop.jpg"
image bg hallway = "Hallway.jpg"
image bg hels:
    zoom 3.0
    "mels.jpg"
image bg maxs:
    zoom 1.5
    "max_room.jpg"
image bg lecture hall:
    zoom 0.35
    "havemeyer.jpeg"
image bg mil = "milstein.jpg"
image bg buthall:
    zoom 0.6
    "buthall.jpg"
image bg collegewalk:
    zoom 0.5
    "CollegeWalk.jpg"
image bg lernerramps:
    zoom 1.5
    "lernerramps.jpg"
image bg black = "#000000"
image bg partyline:
    zoom 1.2
    "partyline.png"
image bg partylinefront:
    zoom 1.2
    "partylinefront.png"
image bg columbialawn:
    zoom .5
    "columbialawn.jpg"
image bg milfloor = "milfloor.jpg"
image bg entrance = "entrance.jpg"
image bg convention = "convention.jpg"
image bg careerfair1 = "careerfair1.jpg"
image bg careerfair2:
    zoom 2.5
    "careerfair2.jpg"
image bg CCE:
    zoom 1.5
    "CCE.jpg"
image bg Interview:
    zoom 1.75
    "Interview.jpg"
image bg low:
    zoom .45
    "lowsteps.jpg"
image bg lowonfire = "fire2.png"
image bg singleroom:
    zoom .95
    "singleurs.jpg"
image bg singleroomd:
    zoom .95
    "singleursd.jpg"
image bg singlemarie:
    zoom .95
    "single.jpg"
image bg singlemaried:
    zoom .95
    "singledark.jpg"
image bg singleonfire:
    zoom .95
    "singleburn.jpg"
image bg columbiagates:
    zoom 1.5
    "columbiagates.jpg"
image bg shakeshack = "shakeshack.jpeg"
image bg john jay inside:
    zoom 2
    "johnjayinside.jpg"
image bg john jay outside:
    zoom 1.1
    "johnjayoutside.jpg"
image bg ferris = "ferrisbooth.jpg"
image bg ferris inside = "ferrisinside.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    ########################

    #these are all sprite tests between the hashes. Just ignore them

    #bg test scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #item test show sandwich

    #character tests show marie neutral at left
    #show max neutral at right
    #show josh happy

    #######################

    # init all variables here. Add in character relationship stats and flags as needed
    $ sin = 0 #positive is good morality, negative is bad?
    $ success = 0 #amount of quest points
    $ josh_friendship = 0 #josh friendship points
    $ maximillion_friendship = 0 #maximillion friendship points
    $ marie_friendship = 0 #marie friendship points
    $ prof_friendship = 0 #professor friendship points
    $ music_friendship = 0 #marvien friendship points
    $ josh_hasnumber = False #does player have josh's number?
    # Message System Variables
    #Todo: Make some dialogue edits in script so it's less tell more show
    $ mail = []
    $ mail_queue = []
    $ contacts = []

    #important flags
    $ fightwithjosh = False #were you so mean to Josh he called you out?
    $ marieevil = False #did you steal Marie's resume?
    $ committedArson = False #did you set fire to Marie's room???
    $seduce_prof = False
    $seduce_max = False
    $Marvensenpai = False #Marven is your senpai
    $Marvenperfectrun = False #Perfect grade and Marven is your senpai!
    $failedPride = False
    $ignoranceisbliss = False


    # These display lines of dialogue.

    # Name your character: (moved to limbo. "Oh hi, I'm %(pname)s")

    jump limbobegin

    # This ends the game.

    return
