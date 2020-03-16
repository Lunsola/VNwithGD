#will either automatically show a certain image if a stat changes
#or provide a function that is called deliberately to pull up an image

label indicator:
    #initalize with default values
    #def __init__(self,initial):
    $def_moral = 100
    $cur_moral =0
    $def_quest = 0
    $cur_quest =0
    #friendship points
    $fr_jock = 0
    $cur_jock =0
    $fr_biz = 0
    $cur_biz =0
    $fr_room = 0
    $cur_room =0
    if($def_moral != $cur_moral):
        python:
            moralChange(cur_moral-def_moral)
    if($def_quest != $cur_quest):
        python:
            questChange(cur_quest-def_quest)
    if($fr_jock != $cur_jock):
        python:
            frJockChange(cur_jock-fr_jock)
    if($fr_biz != $cur_biz):
        python:
            frBizChange(cur_biz-fr_biz)
    if($fr_room != $cur_room):
        python:
            frRoomChange(cur_room-fr_room)
python:
    def moralChange(num):
        #need graphic change
        #if(num>0):
            #show positive indicator
        def_moral = cur_moral
    def questChange(num):
        #need graphic change
        def_quest = cur_quest
    def frJockChange(num):
        #need graphic change
        fr_jock = cur_jock
    def frBizChange(num):
        fr_biz = cur_biz
    def frRoomChange(num):
        fr_room = cur_room
