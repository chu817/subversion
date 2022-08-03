import time
import keyboard
import pygame
def printnew():
    print('\n')
def printcenter(x):
    var =175
    print(x.center(var))
def titlescreenselections():
    option=input("choose your option>>")
    if option.lower()==('play'):
        play()
    elif option.lower()==('help'):
        help_menu()
    elif option.lower()==('quit'):
        pass
    while option.lower() not in ['play','help','quit']:
        print('please enter your value')
        titlescreenselections()
def print_slow(s):
    for letter in s:
        print(letter,end='')
        time.sleep(0.01)
def titlescreen():
    c = '''             
                                                
                                                ░██████╗██╗░░░██╗██████╗░██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗
                                                ██╔════╝██║░░░██║██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║
                                                ╚█████╗░██║░░░██║██████╦╝╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║
                                                ░╚═══██╗██║░░░██║██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║
                                                ██████╔╝╚██████╔╝██████╦╝░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║
                                                ╚═════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝
                                                
                                                =============================================================================
                                                                                    ▄   ▄
                                                                                    █▀█▀█
                                                                                    █▄█▄█
                                                                                     ███  ▄▄
                                                                                     ████▐█ █
                                                                                     ████   █
                                                                                     ▀▀▀▀▀▀▀
                                                ==============================================================================

        '''
    printcenter(c)
    print('\n')
    printcenter("USE FULL SCREEN!!!")
    printcenter('-----------------------------------------')
    printcenter('''
                                                                        █   █ █▀▀ █   █▀▀ █▀▀█ █▀▄▀█ █▀▀ 
                                                                        █▄█▄█ █▀▀ █   █   █  █ █ ▀ █ █▀▀ 
                                                                         ▀ ▀  ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀   ▀ ▀▀▀
         ''')
    printcenter('-----------------------------------------')
    printcenter('       - Play -          ')
    printcenter('       - Help -          ')
    printcenter('       - Quit -          ')
    printcenter('-----------------------------------------')
    titlescreenselections()
def help_menu():
    print('\n')
    printcenter('-----------------------------------------')
    printcenter('##Welcome to SUBVERSION##')
    printcenter('-----------------------------------------')
    printcenter('-Use Up,Down,Left,Right  ')
    printcenter('-Type your command to do them')
    printcenter('-use "look" to inspect something')
    printcenter('#########################')
    titlescreenselections()
def showmap():
    floor1= '''
                                                                                  FLOOR 1
                                                            ##################################################
                                                            ##*###############################################    
                                                            ###_______\ /_______________________\ /_______ ###
                                                            ###            |                 |             ###
                                                            ###|Lower wing       Stage          Staff only|###
                                                            ###|________   |_________________|   _________|###
                                                            ###|        |  |                 |   |        |###
                                                            ###|        |  |                 |   |        |###
                                                            ###|Warehouse  |                 |     Waiting ###
                                                            ###            |                 |      Room   ###
                                                            ###|_ _ _  _|  |                 |   |   2    |###
                                                            ###|   |    |  |      Hall       |   |        |###
                                                            ###|washroom|  |                 |   |        |###
                                                            ###|___|____|  |                 |   |___  ___|###
                                                            ###|        |  |                 |   |        |###
                                                            ###| control|  |                 |   | Waiting|###
                                                            ###   room     |                 |      Room   ###
                                                            ###|        |  |                 |   |    1   |###
                                                            ###|___  ___|  |______     ______|   |__ _____|###
                                                            #######|  o |  |]]]]]]     [[[[[[|   |    |#######
                                                            #######   f           Stairs          wash #######
                                                            #######|  f |                        |____|#######
                                                            ###@###|  i |     Entrance Lobby     |    |####@##
                                                            #######   c                           wash #######
                                                            ####@##|__e_|_________     __________|____|#######
                                                            #######################    #######################
'''
    floor2='''          
                                                                                 FLOOR 2
                                                            ##################################################
                                                            ##*###############################################
                                                            ###___________________________________________ ###
                                                            ###|    |      |                 |       |    |###
                                                            ###     |                                |     ###
                                                            ###|    |      |                 |       |    |###
                                                            ###|    | Audio|                 |Light  |    |###
                                                            ###|    |  Room|                 |equipment   |###
                                                            ###     |      |                 | room  |     ###
                                                            ###|    |      |                 |       |    |###
                                                            ###|    |      |                 |       |    |###
                                                            ###|    |      |      Hall 2     |       |    |###
                                                            ###     |      |                 |       |     ###
                                                            ###|    |_   __|                 |__   __|    |###
                                                            ###|           |                 |            |###
                                                            ###|           |                 |            |###
                                                            ###|           |_________________|            |###
                                                            ###|                                          |###
                                                            ###|_____  __   __________________        ____|###
                                                            #######|     | |]]]]]]     [[[[[[||       |#######
                                                            #######      |       Stairs       |        #######
                                                            #######|store|                    |       |#######
                                                            ###@###| room|     Entrance Lobby |        ####@##
                                                            #######               Floor 2     |       |#######
                                                            ####@##|_____|________     _______|_______|#######
                                                            #######################    #######################
'''

    print(floor1,end='')
    printcenter(floor2)
positions='''             
                                                             _______________________________________________
                                                             |        Phoeb---Light Equipment Room         |
                                                             |        Yuri----Audio Equipment Room         |
                                                             |        Callisto-----------Warehouse         |
                                                             |        Dia-------------Control Room         |
                                                             |        Kale--------------Store Room         |   
                                                             -----------------------------------------------      '''
rope = '''   
                                                                                 \\//
                                                                                  //
                                                                                 //\\ 
                                                                                 \\//
                                                                                  //
                                                                                 //\\
                                                                                 \\//
                                                                                  //
                                                                                 //\\
                                                                                 \\//
                                                                                  //
                                                                                 //\\ 
                                                                                 \\//
                                                                                  //
                                                                                 //\\
                                                                                 \\//
                                                                                  //
                                                                                 //\\'''
bloodyhand=('''
                                    ..                                                                              .,***,,*,,*,*******/
                                     ...                                                                    **//(//*(///**////((((((((((
                                      ..                                                             ./((///,//#####%%&&&%%((((#%(#((((#
                                     . ...                                                        ,(/////(#&&%%%&&&&&&&@&&%#############
                                     ......                                                    .(((///((&&@@@@&&&&&&&&&@@&@@&%#####%%%%%
                                    .......                                                ..//(##/(/(&@@@&&%&&&&&&@@@@@@@@@@%%%%%######
                                    ........                                             ./(/(#(*/(##%&@@@@@@&&@@@@@@@@@@&#*............
                                    .........                                         */###((#///(#%&&&@@@@@&&%..  .....................
                                    ........ .    .                              ./(#(((#((#///(%%&&&&&@@      . .......................
                                    ............                              (%%%%%%%&%(#///#%&&&@&%@@@      ..........................
                                    ...............                        *%%%%&&&&%#&#//%&&&&@@&%@@@&       ..........................
                                    ....................                 #%%%&&&&@@@@&#//%&&&%&@@@@@@ ..................................
                                    ................ ....             *##%%&&@@@@&&&%#(%&&&@@@@@@@&. ................................,,,
                                    ...........................     .((%&&&@@@@@@@%%&&&&&@@@@@@@.... ..............................,.,,,
                                    .............................. %%&&&&% .@&&&%%&&&%&&&@@@@@,.................................,,,,,,,,
                                    .............................,%&&&@,. .&&%%%((%&&&@/.,@&&&&&&/%..........................,,,,,,,,,,,
                                    ............................#&&&&#....&#((&&&&&&&&%...(%#&&%%&@........................,,,,,,,,,,,,,
                                    ........................../&&@@&.......&%(%&. .%&%&#/.............................,,,,,,,,,,,,,,,,,,
                                    ...........................(&..........%&#%&*....#&&&%&.......................,,,,,,,,,,,,,,,,,,,***
                                    ............................%...........%&%&&.......*&@/..................,,,,,,,,,,,,,,,,,,,*******
                                    ............................&.............&&&&.......................,,,.,,,,,,,,,,,,,,,,,**********
                                    .,...............................................................,,,,,,,,,,,,,,,,,,,,,,*************
                                    ,,,,,.......................................................,,,,,,,,,,,,,,,,,,,,,,,*****************
                                    ,,,,,,,,,,,...........................................,..,,,,,,,,,,,,,,,,,,,,,,,,,******************
                                    ,,,,,,,,,,,,,,,,.,,,.,,...................,..,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,*******************
                                    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**********************///
                                    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**********************///////''')
ahaha=('list',positions)
inventory=[ahaha,]
def addtoinventory(x):
    global inventory
    inventory+=[x]
def viewinventory():
    printcenter('INVENTORY')
    for i in range(len(inventory)):
        y=str(i+1)+'.'+inventory[i][0]
        printcenter(y)
    print('\n')
def viewobj(x):
    print('\n')
    inflag=0
    printcenter("INVENTORY")
    for i in inventory:
        if i[0]==x.lower():
            printcenter(i[0])
            printcenter(i[1])
            inflag=1
    if inflag==0:
        print("No such object found")
cflag=0
dflag=0
pflag=0
kflag=0
flagg=0
a = 'Choice 1: Is it Callisto?'
b = 'Choice 2: Do you think it’s Dia?'
c = 'Choice 3: Are you saying it’s Phoeb?'
d = 'Choice 4: Kale is the culprit?'
def kale_choices(x):
    global kflag
    if x==1:
        if kflag==0:
            print_slow("""Kale:Yeah, him. 
     Well, from the looks of it, you're pretty clueless about this stuff.""")
            kflag+=1
        elif kflag==1:
            print_slow("""Kale: It could be her, but she's a scaredy-cat.
     I doubt she had the guts to do that.
     But it would be ignorant to rule out that possibility. 
     That's a stupid thing to do.""")
    if x==2:
        if kflag==0:
            print_slow("""Kale: ...no. It's by Knox. 
     Quite the clueless lad you are.""")
            kflag+=1
        elif kflag==1:
            print_slow("""Kale: Could be, but it could've been Phoeb as well, or maybe both of them. 
     We can't tell for sure without solid proof. 
     Accusing someone of murder without proof is the most idiotic thing you can do.""")
def phoeb_choices(x):
    global pflag
    if x==1:
        if pflag==0:
            print_slow("""
Phoeb: The killer? I'm not sure...
       All I know is that whoever did that, must be really, really dangerous...
       I hope I don't have to encounter them...""")
            pflag+=1
    elif x==2:
        if pflag==0:
            print_slow("""
Phoeb: Is there anyone you find suspicious in this house?
Phoeb: Suspicious? I don't think so...
       Are you suggesting it was one of us...?
       I personally don't think so...we're all friends. Why would anyone here do that.""")
def dia_choices(x):
    global dflag
    if x==1:
        if dflag==0:
            print_slow("""
Dia: silent
     Thinking about a potential murderer in the same roof as me...
     I'm getting goosebumps.
     I don't like this.""")
            dflag+=1
    elif x==2:
        if dflag==0:
            print_slow("""
Dia: What if the killer is in this very house...
     This doesn't feel right.""")
            dflag+=1
def callisto_choices(x):
    global cflag
    if x==1:
        if cflag==0:
            print_slow("""
Callisto: Oh, I see. Maybe you're not fazed that much.Maybe we shouldn't have come here.
          Maybe, we shouldn't have met up in the first place.
          I wouldn't have shown up if I knew this was gonna happen.""")
            cflag+=1
        elif cflag==1:
            print_slow("""
Callisto: Oh, that could make sense.
          In a LOCKED ROOM, there isn't much choice of escape routes for the culprit. The only openings were the window and the door.
          The door was locked when we entered, so that couldn't have been it...
          So...as you said.
          The window.
MC: nods""")
            cflag+=1
    elif x==2:
        if cflag==0:
            print_slow("Callisto: Yeah, me too. I guess that's an expected response. It would be pretty weird if someone didn't find this scary.")
            cflag+=1
        elif cflag==1:
            print_slow("""
Callisto: Got no clues?
          Well, I do have a theory.
          I think it must've been through the window.
          In a “LOCKED ROOM”, there isn't much choice for escape routes for the culprit.
          The only openings were the window and the door.
          The door was locked when we entered, so that couldn't have been it...
          So, it must be...
MC: The window. 
Callisto: Yes. The window.""")
            cflag+=1
def yuri_choices(x):
    global flagg
    global a
    global b
    global c
    global d
    if x==1:
        a=''
        print_slow('''
Yuri: No, it’s not him. 
      He headed to the left corridor and never had the chance to meet up with the victim. 
      There’s no chance he could’ve turned his heels back that quick and killed Sam. 
      You would’ve caught him red-handed.
Yuri: Hallway…
Yuri: …!
MC: ?
Yuri: Right…!
Yuri: And there’s also Dia to consider. 
      She’s his alibi because she headed down the same direction as him.
      Couldn’t have slipped past her that easily.
''')
        flagg+=1
    elif x==2:
        b=''
        print_slow('''
Yuri: Dia, you say? Now that’s quite the answer. 
      She sometimes comes off as rude and petty, but I don’t think it’s her.
      You would’ve caught her following Sam.
Yuri: And…!
      She’s got Callisto as her alibi as they both went down the left corridor. 
      She possibly couldn’t have snuck past him without getting caught.
''')
        flagg+=1
    elif x==3:
        c=''
        print_slow('''
Yuri: Haha! Creative. 
      The poor girl can barely keep it together in front of a crowd, but to murder someone? Wow, that’s peak thinking right there. 
      Okay,but in all seriousness, it’s not her.
      She headed up to the first floor towards the audio room. The left corridor. So that rules out the possibility of her coming back down. You would’ve seen her if she climbed down the stairs.
Yuri: Stairs…
Yuri: …!
MC: ?'''
)
        flagg+=1
    elif x==4:
        d=''
        print_slow('''
Yuri: Kale, huh. Wasn’t he on the first floor during the time of murder? 
      It’s highly unlikely that he would’ve jumped out the window, it’s a pretty steep fall. 
      The only other option is back down the stairs. 
      Even if he did come back, you would’ve seen him....
MC:...?
Yuri: Right! So um, like I said, it’s not him, would’ve been too obvious because he would’ve been seen in the lobby.
''')
        flagg+=1
def kale_dialogue():
    global places
    global location
    print()
    dialogue1='''Kale: Hi there!
MC: Hello.
Kale: Man, this was quite the turn of events, huh.
      A dead person in an abandoned mansion in the middle of a dense forest.
      If you think about, it's the perfect setup for a murder scene- it doesn't grab attention, and the plan goes by smoothly.
MC: ...
Kale: Ahem. Sorry about that. This isn't something I should be looking forward to.
      You see, I'm just an avid Sherlock fan.
      I can't help but relate everything I see with mystery.
      By chance, are you familiar with “The 20 Rules”?
MC: No...
Kale: “Chandler's Laws”?
MC: Nope...
Kale: At least “The 10 Commandments”?
MC:'''
    
    print_slow(dialogue1)
    printcenter('Choice 1: By Knox...?')
    printcenter('Choice 2: By Mose...?')
    choice=input("Enter your choice (1/2): ")
    if choice not in['1','2']:
        print_slow(dialogue1)
        printcenter('Choice 1: By Knox...?')
        printcenter('Choice 2: By Mose...?')
        choice=input("Enter your choice (1/2): ")
    choice=int(choice)
    kale_choices(choice)
    dialogue2="""
Kale: Whatever, I don't want to waste my time on this, we're not getting anywhere.
MC: At least I can agree with you on that one...
Kale: You know bud, if you ask me, I think it was either Phoeb or Yuri. 
      The door was locked from the inside, and cannot be opened unless you have access to the key. 
      Forget about the window, because it's busted by the looks of it. 
      God knows how old this building is. And I doubt the killer entered in through the window undetected, without causing any ruckus. 
      It would be pretty stupid of the victim to just stand there and watch the killer break in.
MC: So, what do you think happened?
Kale: I'm glad you asked. Of course you wouldn't know, silly me.
MC: ...
You see, the only way in and out was through the door.
And who went to bring the masterkey which could open the door?
MC: ...
MC:
"""
    print_slow(dialogue2)
    printcenter('Choice 1: Phoeb...?')
    printcenter('Choice 2: Yuri...?')
    choice=input("Enter your choice (1/2): ")
    if choice not in['1','2']:
        print_slow(dialogue2)
        printcenter('Choice 1: Phoeb...?')
        printcenter('Choice 2: Yuri...?')
        choice=input("Enter your choice (1/2): ")
    choice=int(choice)
    kale_choices(choice)
    dialogue3="""
MC: Do you have anything useful, like clues?
Kale: Now buddy, sorry to break it to you. If I had clues and knew who the actual killer was, I'd rat them out by now. 
MC: Shouldn't have talked to him in the first place. 
    This conversation was pointless...
Kale: If you're trying to find out the real culprit, all I can say is be smart about it.
      You'll never know what's hiding in plain sight.
MC: Thanks...?"""
    places[location]['SOLVED'] = True
def phoeb_dialogue():
    global places,location
    print()
    dialogue1="""
MC: Hey.
Phoeb: EEK!
       Oh, it's you.
       Wow you scared me for a second there.
       I've been on edge ever since that happened...
       He doesn't deserve a death like that, it's way too brutal.
       ...
       So, is there anything you want to ask me? 
MC:
"""
    print_slow(dialogue1)
    printcenter('Choice 1: Who do you think is the killer?')
    printcenter('Choice 2: Is there anyone you find suspicious in this house?')
    choice=input("Enter your choice (1/2): ")
    if choice not in ['1','2']:
        print_slow(dialogue1)
        printcenter('Choice 1: Who do you think is the killer?')
        printcenter('Choice 2: Is there anyone you find suspicious in this house?')
        choice=input("Enter your choice (1/2): ")
    choice=int(choice)
    phoeb_choices(choice)
    dialogue2="""
Phoeb: Well, since you're asking for my input, I'd say it must've been someone else. 
A mysterious entity.
MC: Like?
Phoeb: Like maybe, a ghost.
       A ghost! Yes, definitely a ghost.
       A ghost with a revenge plan.
       Maybe it thinks we're invading its house, so it's set on a mission to kill all of us. 
       That must be it, I'm sure.
MC: ...
    I'll, uh, take my leave now.
Phoeb: Okay! I get that you're busy. 
       But be careful out there, you might expect the unexpected."""
    print_slow(dialogue2)
    places[location]['SOLVED'] = True
def dia_dialogue():
    global places
    global location
    print()
    dialogue1="""
Dia: Oh.
     It's you.
     ...
MC: ...
Dia: I thought we would have fun today, but we ended up with a dead body instead.
     ...
     Who do you think did this?
MC:
"""
    print_slow(dialogue1)
    printcenter( 'Choice 1: Someone in this house.')
    printcenter('Choice 2: No clue.')
    choice=input("Enter your choice (1/2): ")
    if choice not in ['1','2']:
        printcenter( 'Choice 1: Someone in this house.')
        printcenter('Choice 2: No clue.')
        choice=input("Enter your choice (1/2): ")
    dia_choices(choice)
    dialogue2="""
Dia: If I had to pin-point a name among us.
     I'd bet it was Yuri.
     She always gave off icky-vibes.
     And she's always quiet, like she's up to something. Something really bad.
MC: ...
MC: How do you think she did it?
Dia: See, if you think about it.
     When we entered the room, it was locked.
     So no one could have entered through that way.
     What if she climbed down a rope from the room above. 
     Seems like a perfect plan in my books.
     She would've sensed the perfect opportunity and striked at the right time.
     Then there's nothing much left after that.
     She climbed back up, closing the window on the way out, back to her room.
     Like nothing happened in the first place.
MC: ...
Dia: What, do you think I'm lying?
     She is a rock climbing professional, she definitely could've done this! I saw a rope in her backpack!
MC: How did she find that out, now...I'm not even gonna bother...
MC: Why don't I find this “rope” you're talking about since you're persistent about this certain person being a murderer.
Dia: Go look for it! 
     And come right back to me after you find it, with an apology as well. 
     For doubting me.
MC: ...
MC: Okay...if you say so."""
    print_slow(dialogue2)
    places[location]['SOLVED'] = True
def yuri_dialogue():
    global places
    global location
    global inventory
    dialogue1='''Yuri: Hi
MC: …
MC: Hello
Yuri: Is something bothering you?
MC: Actually, I was sent here to find this “rope”.
    …
    And it might be yours.
Yuri: A rope? Mine?
MC: …that’s what I was told.
Yuri: Well I do have one, but I don’t see how this can be of help right now.
'''
    print_slow(dialogue1)
    printcenter('Hands you a jute rope, which is about 5 metres long')
    dialogue2='''
MC: Certainly not long enough to climb down with. And definitely not sturdy enough to uphold a human.
MC: Is this it?
Yuri: Huh? Are you asking if I have more ropes with me? Because I don’t.
MC: …
Yuri: Are you curious as to why I’m carrying this rope with me?
MC: …yes.
Yuri: You see, it was part of the supplies for the tent we were gonna set up. And I figured this rope might come in handy.
MC: Oh.
Yuri: …
MC: Actually, the real reason I’m here is that I wanted to ask you something.
Yuri: Oh? A question?
MC: Yes.
Yuri: Okay. Shoot.
MC: Who do you think is the killer?
Yuri: Hmm. I don’t want to say anything quite yet, because I still have my own doubts, but I think I have a certain idea as to who the killer might be.
MC: …!
'''
    print_slow(dialogue2)
    while flagg<4:
        printcenter(a)
        printcenter(b)
        printcenter(c)
        printcenter(d)
        choice=int(input("enter your choice"))
        yuri_choices(choice)
    if flagg==4:
        print_slow('''
MC: So you’re saying it’s not Kale…
Yuri: Yup.
MC: Not Dia…
Yuri: Mhm.
MC: It’s not Phoeb.
Yuri: Hmm.
MC: And not Callisto.
Yuri: Exactly.
MC: …
MC: Is it…
Yuri: ?
MC: Are you the killer?
Yuri: …
Yuri: I get why you came to that conclusion, but there was no way I could’ve climbed down the window from the first floor. 
MC: But…
Yuri: But?
MC: Phoeb…she said you’re a rock climber.
Yuri: ?
Yuri: I don’t have my climbing rope with me.
The only rope I brought to this trip was the rope I gave you.
And it’s shorter than me.
Quite the predicament you came up with if you think I used that to somehow climb down, kill Sam, and climb back up the same way.
MC: …
MC: But Phoeb said…
Yuri: …
Yuri: Didn’t think you would actually believe her. We all know she exaggerates and overreacts just for the attention.
MC: …
MC: …!
MC: Wait…
Then…
Who is-
Yuri: !
''')
        places[location]['SOLVED'] = True
        tata = ('jute rope', rope)
        addtoinventory(tata)
def callisto_dialogue():
    print()
    dialogue="""Callisto to MC: Ah, hey there.
               This sure is quite a turn of events, huh.
               To think one of us would end up dead on a reunion.
               Man, I still can't wrap my mind around this.
               Sam out of everyone...
               Um, anyways I'm going on a tangent here.
               How are you feeling?

MC:
"""
    print_slow(dialogue)
    printcenter('Choice 1: I\'m fine')
    printcenter(' Choice 2: Still Shocked')
    choice=int(input("Enter your choice(1/2)"))
    callisto_choices(choice)
    dialogue2="""\nCallisto: But, now that I think about it, there really couldn't be a murderer who happened to be wandering around this area on a summer afternoon, right...?
MC: The killer couldn't have gotten far.
Callisto: silent
          As much as I don't want to admit it, you're right.
          ...
          So...
          Do you know who it might be...?
          I'm not trying to point fingers but...I think...
          It's someone in this mansion...
          One of us.
          Is a killer.
          What do you think?
MC:
"""
    print_slow(dialogue2)
    printcenter('Choice 1: Window')
    printcenter('Choice 2: Let me think...')
    choice = int(input("Enter your choice (1/2)"))
    callisto_choices(choice)
    dialogue3="""
Callisto: Well, now that we found out the escape route, why don't you go tell the others about this discovery you made, huh?
          And might as well ask for their opinions and thoughts as well, maybe they came up with something too."""
    print_slow(dialogue3)
    places[location]['SOLVED']=True


places={'Lower Wing':{'DESCRIPTION':'a long hallway','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':None,'DOWN':'Warehouse','LEFT':None,'RIGHT':'Stage'},
        'Stage':{'DESCRIPTION':'a wooden stage','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':None,'DOWN':'Hall','LEFT':'Lower Wing','RIGHT':'Staff Only'},
        'Staff Only':{'DESCRIPTION':'access restricted','PERSON':'Sam','EXAMINATION':'examine','SOLVED':None,'UP':None,'DOWN':'Waiting Room 2','LEFT':'Stage','RIGHT':None},
        'Control Room':{'DESCRIPTION':'room for control equipment','PERSON':'Dia','EXAMINATION':'examine','SOLVED':False,'UP':'Washroom','DOWN':'Office','LEFT':None,'RIGHT':'Entrance Lobby'},
        'Warehouse':{'DESCRIPTION':'storage room filled with junk','PERSON':'Callisto','EXAMINATION':'examine','SOLVED':False,'UP':None,'DOWN':'Washroom','LEFT':None,'RIGHT':'Entrance Lobby'},
        'Washroom':{'DESCRIPTION':'a washroom, with a toilet and bathtub','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Warehouse','DOWN':None,'LEFT':None,'RIGHT':None},
        'Hall':{'DESCRIPTION':'a hall, quite empty in here','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':None,'DOWN':'Entrance Lobby','LEFT':None,'RIGHT':None},
        'Entrance Lobby':{'DESCRIPTION':'the lobby,filled with cobwebs','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Hall','DOWN':'Stairs','LEFT':'Office','RIGHT':'Wash'},
        'Office':{'DESCRIPTION':'office room, where the keys belong to','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Control Room','DOWN':None,'LEFT':None,'RIGHT':'Entrance Lobby'},
        'Waiting Room 1':{'DESCRIPTION':'a waiting room with broken furniture','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Waiting Room 2','DOWN':None,'LEFT':'Entrance Lobby','RIGHT':None},
        'Wash':{'DESCRIPTION':'toilet','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Waiting Room 1','DOWN':None,'LEFT':'Entrance Lobby','RIGHT':None},
        'Waiting Room 2':{'DESCRIPTION':'another waiting room, with more broken furniture','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':None,'DOWN':None,'LEFT':'Entrance Lobby','RIGHT':None},
        'Audio Room':{'DESCRIPTION':'audio room, filled with old audio equipment','PERSON':'Yuri','EXAMINATION':'examine','SOLVED':False,'UP':None,'DOWN':'Entrance Lobby Floor 2','LEFT':None,'RIGHT':'Hall 2'},
        'Light Equipment Room':{'DESCRIPTION':'light equipment room, filled with old and broken light equipment','PERSON':'Phoeb','EXAMINATION':'examine','SOLVED':False,'UP':None,'DOWN':'Entrance Lobby Floor 2','LEFT':'Hall 2','RIGHT':None},
        'Hall 2':{'DESCRIPTION':'a hall on the top floor, quite empty in here','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':None,'DOWN':None,'LEFT':'Audio Room','RIGHT':'Light Equipment Room'},
        'store room':{'DESCRIPTION':'a store room, nothing useful to be found in here','PERSON':'Kale','EXAMINATION':'examine','SOLVED':False,'UP':'Entrance Lobby Floor 2','DOWN':None,'LEFT':None,'RIGHT':'Entrance Lobby Floor 2'},
        'Entrance Lobby Floor 2':{'DESCRIPTION':'a lobby filled with cobwebs','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Stairs','DOWN':'Entrance Lobby','LEFT':'store room','RIGHT':'Light Equipment Room'},
        'Stairs':{'DESCRIPTION':'an old creaky stairway','PERSON':None,'EXAMINATION':'examine','SOLVED':None,'UP':'Entrance Lobby Floor 2','DOWN':'Entrance Lobby','LEFT':None,'RIGHT':None}}
def endcredits():
    print('''  
                                                      ██████  █    ██  ▄▄▄▄   ██▒   █▓▓█████  ██▀███    ██████  ██▓ ▒█████   ███▄    █ 
                                                    ▒██    ▒  ██  ▓██▒▓█████▄▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
                                                    ░ ▓██▄   ▓██  ▒██░▒██▒ ▄██▓██  █▒░▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒██▒▒██░  ██▒▓██  ▀█ ██▒
                                                      ▒   ██▒▓▓█  ░██░▒██░█▀   ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒░██░▒██   ██░▓██▒  ▐▌██▒
                                                    ▒██████▒▒▒▒█████▓ ░▓█  ▀█▓  ▒▀█░  ░▒████▒░██▓ ▒██▒▒██████▒▒░██░░ ████▓▒░▒██░   ▓██░
                                                    ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
                                                    ░ ░▒  ░ ░░░▒░ ░ ░ ▒░▒   ░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
                                                    ░  ░  ░   ░░░ ░ ░  ░    ░     ░░     ░     ░░   ░ ░  ░  ░   ▒ ░░ ░ ░ ▒     ░   ░ ░ 
                                                          ░     ░      ░           ░     ░  ░   ░           ░   ░      ░ ░           ░ 
                                                                            ░     ░                                                                                                                                                                         
              ''')
    time.sleep(0.7)
    print('''
                                                    
                                                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
                                                                 ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗
                                                                ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
                                                                ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗
                                                                ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║
                                                                ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║
                                                                 ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝
                                                                                                                    
                                                                
                                                                ####################################################
                  ''')
    time.sleep(0.7)
    printcenter('𝐒𝐭𝐨𝐫𝐲𝐛𝐨𝐚𝐫𝐝 𝐛𝐲.....................................Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printcenter('𝐒𝐜𝐫𝐢𝐩𝐭 𝐛𝐲........................................Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printcenter('𝐋𝐞𝐚𝐝 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐦𝐞𝐫..................................Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐋𝐞𝐚𝐝 𝐬𝐭𝐨𝐫𝐲 𝐝𝐞𝐬𝐢𝐠𝐧..................................Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printcenter('𝐋𝐞𝐚𝐝 𝐝𝐢𝐜𝐭𝐢𝐨𝐧𝐚𝐫𝐲 𝐜𝐫𝐞𝐚𝐭𝐨𝐫..............................Ｔｈａｒｕｎ')
    time.sleep(0.7)
    printcenter('𝐋𝐞𝐚𝐝 𝐬𝐨𝐮𝐧𝐝 𝐝𝐞𝐬𝐢𝐠𝐧.................................Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐀𝐝𝐝𝐢𝐭𝐢𝐨𝐧𝐚𝐥 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐦𝐞𝐫𝐬.......................Ｓｒｉｎｉｊａ, Ｔｈａｒｕｎ')
    time.sleep(0.7)
    printcenter('𝐄𝐝𝐢𝐭𝐨𝐫𝐬...........................Ｔｈａｒｕｎ, Ｓｒｉｎｉｊａ, Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐂𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫 𝐃𝐞𝐬𝐢𝐠𝐧...................................Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printcenter('𝐌𝐨𝐝𝐮𝐥𝐞 𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫...........................Ｔｈａｒｕｎ, Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐆𝐚𝐦𝐞 𝐂𝐨𝐧𝐭𝐫𝐨𝐥𝐬....................................Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐀𝐫𝐜𝐡𝐢𝐯𝐞...................................Ｔｈａｒｕｎ')
    time.sleep(0.7)
    printcenter('𝐆𝐚𝐦𝐞 𝐃𝐞𝐬𝐢𝐠𝐧.....................................Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐆𝐚𝐦𝐞 𝐃𝐞𝐬𝐢𝐠𝐧.......................Ｔｈａｒｕｎ, Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printcenter('𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭 𝐀𝐫𝐭𝐢𝐬𝐭𝐬.........................Ｈｉｍａｎｉ, Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printcenter('𝐕𝐢𝐬𝐮𝐚𝐥 𝐄𝐟𝐟𝐞𝐜𝐭𝐬....................................Ｈｉｍａｎｉ')
    time.sleep(0.7)
    printcenter('𝐃𝐢𝐚𝐥𝐨𝐠 𝐒𝐮𝐩𝐞𝐫𝐯𝐢𝐬𝐨𝐫..................................Ｓｒｉｎｉｊａ')
    time.sleep(0.7)
    printnew()
    printnew()
    printcenter('𝕊𝕡𝕖𝕔𝕚𝕒𝕝 𝕋𝕙𝕒𝕟𝕜𝕤 𝕥𝕠 𝕠𝕦𝕣 𝔽𝕣𝕚𝕖𝕟𝕕𝕤')
    printnew()
    time.sleep(0.7)
    printcenter('𝖤𝗑𝗍𝗋𝖺 𝖲𝗉𝖾𝖼𝗂𝖺𝗅 𝖳𝗁𝖺𝗇𝗄𝗌 𝗍𝗈 𝗈𝗎𝗋 𝖳𝖾𝖺𝗆')
    time.sleep(0.7)
    printnew()
    print('''
                                                                                   𝖺𝗇𝖽
                                                                    
                                                                              
                                                    
                                                                        ██╗░░░██╗░█████╗░██╗░░░██╗
                                                                        ╚██╗░██╔╝██╔══██╗██║░░░██║
                                                                        ░╚████╔╝░██║░░██║██║░░░██║
                                                                        ░░╚██╔╝░░██║░░██║██║░░░██║
                                                                        ░░░██║░░░╚█████╔╝╚██████╔╝
                                                                        ░░░╚═╝░░░░╚════╝░░╚═════╝░
                                                                        
                                                                        
                                                                        
                                                                        :)
                                                                        
                                                                        
                                                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
def play():
    global location
    dummyflag=0
    done=0
    floor='1'
    location='Staff Only'
    f=open('subversion.txt','a+')
    f.seek(0)
    c=f.readlines()
    d={'Phoeb':[],'Dia':[],'Callisto':[],'MC':[],'Yuri':[],'Kale':[],'Sam':[],'Narrator':[]}
    t=0
    for i in c:
        t+=1
        x=i.split()
        if x[0]=='Phoeb:':
            l=d['Phoeb']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='Yuri:':
            l=d['Yuri']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='Dia:':
            l=d['Dia']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='Callisto:':
            l=d['Callisto']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='Sam:':
            l=d['Sam']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='Kale:':
            l=d['Kale']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='MC:':
            l=d['MC']
            tupl=[i,t]
            l.append(tupl)
        elif x[0]=='Scene':
            continue
        else:
            l=d['Narrator']
            tupl=[i,t]
            l.append(tupl)
    f.close()
    print("Press enter for the dialogue\nPress m for map")
    c=-1
    while True:
        if keyboard.is_pressed('m'):
            keyboard.press('backspace')
            time.sleep(0.1)
            showmap()
        if keyboard.is_pressed('enter'):
            keyboard.press('backspace')
            time.sleep(0.2)
            if c<=109:
                c+=1
                for i in d:
                    for j in d[i]:
                        if j[1]==c:
                            print()
                            if len(j[0])<175:
                                print_slow(j[0])
                            else:
                                k=len(j[0])
                                lenn=len(j[0])%175
                                for i in range(lenn):
                                    pos1=175*(i-1)
                                    pos2=175*(i)
                                    if pos2>=k:
                                        print_slow(j[0][pos1:k])
                                        break
                                    else:
                                        print_slow(j[0][pos1:pos2])
            if c==109:
                break
            
    print("ACT TWO")
    print("Press i for instructions\nYou have a new item in your inventory!")
    flagger=0
    pressed=0
    act2=True
    while act2==True:
        if keyboard.is_pressed('6'):
            keyboard.press('backspace')
            print('\n')
            time.sleep(0.5)
            zee='y'
            viewinventory()
            while zee=='y':
                choiceee=input("enter the object to view")
                keyboard.press('backspace')
                viewobj(choiceee)
                zee=input('view another object?(y/n)')
        if keyboard.is_pressed('m'):
            keyboard.press('backspace')
            #ch=int(input("Which floor do you want to view?"))
            time.sleep(0.5)
            showmap()
        if keyboard.is_pressed('i'):
            keyboard.press('backspace')
            time.sleep(0.5)
            print('\n1.Press 1 to see current location\n2.Press 2 to see current floor\n3.Press m to see map\n4.Press 3 to examine\n5.press 4 to see directions you can move\n6.Press 5 to see if someone is in the room\n7.Press 6 to see inventory')
            continue
        if keyboard.is_pressed('1'):
            keyboard.press('backspace')
            time.sleep(0.5)
            print('\nCurrent location:',location)
            continue
        if keyboard.is_pressed('2'):
            keyboard.press('backspace')
            if location in ['Lower wing','Stage','Staff Only','Warehouse','Washroom','Waiting Room 2','Waiting Room 1','Hall','Wash','Office','Entrance Lobby']:
                floor=1
            elif location=='Stairs':
                floor=1.5
            else:
                floor=2
            time.sleep(0.5)
            print('\nCurrent floor:',floor)
            continue
        if keyboard.is_pressed('3'):
            keyboard.press('backspace')
            time.sleep(0.5)
            print()
            pa='Description:'+places[location]['DESCRIPTION']
            printcenter(pa)
        if keyboard.is_pressed('4'):
            keyboard.press('backspace')
            time.sleep(0.5)
            if places[location]['UP']!=None:
                time.sleep(0.5)
                up=places[location]['UP']
                print('Press U to go to',up)
            else:
                print("You cannot move up")
            if places[location]['DOWN']!=None:
                time.sleep(0.5)
                down=places[location]['DOWN']
                print('Press D to go to',down)
            else:
                print("You cannot move down")
            if places[location]['LEFT']!=None:
                time.sleep(0.5)
                left=places[location]['LEFT']
                print('Press L to go to',left)
            else:
                print("You cannot move left")
            if places[location]['RIGHT']!=None:
                time.sleep(0.5)
                right=places[location]['RIGHT']
                print('Press R to go to',right)
            else:
                print("You cannot move right")
        if keyboard.is_pressed('5'):
            keyboard.press('backspace')
            time.sleep(0.5)
            if places[location]['PERSON']!=None:
                print(places[location]['PERSON'],'is in the room with you!')
                print('press j to interact')
            else:
                print('No one is in the room')
        if keyboard.is_pressed('u'):
            up = places[location]['UP']
            keyboard.press('backspace')
            time.sleep(0.5)
            location=up
            printnew()
            print('you are now in',location)
            if places[location]['PERSON']!=None:
                print(places[location]['PERSON'],'is in the room with you!')
        if keyboard.is_pressed('d'):
            down = places[location]['DOWN']
            keyboard.press('backspace')
            time.sleep(0.5)
            location=down
            printnew()
            print('you are now in',location)
            if places[location]['PERSON']!=None:
                print(places[location]['PERSON'],'is in the room with you!')
        if keyboard.is_pressed('l'):
            left = places[location]['LEFT']
            keyboard.press('backspace')
            time.sleep(0.5)
            location=left
            printnew()
            print('you are now in',location)
            if places[location]['PERSON']!=None:
                print(places[location]['PERSON'],'is in the room with you!')
        if keyboard.is_pressed('r'):
            right = places[location]['RIGHT']
            keyboard.press('backspace')
            time.sleep(0.5)
            location=right
            printnew()
            print('you are now in',location)
            if places[location]['PERSON']!=None:
                print(places[location]['PERSON'],'is in the room with you!')
        if keyboard.is_pressed('j'):
            keyboard.press('backspace')
            time.sleep(0.5)
            if places[location]['PERSON']=='Callisto':
                callisto_dialogue()
            elif places[location]['PERSON']=='Phoeb':
                phoeb_dialogue()
            elif places[location]['PERSON']=='Kale':
                kale_dialogue()
            elif places[location]['PERSON']=='Sam':
                print("Sam is lying in the middle of the floor, surrounded by a pool of blood...")
            elif places[location]['PERSON']=='Dia':
                dia_dialogue()
            elif places[location]['PERSON']=='Yuri':
                yuri_dialogue()
        for i in places:
            if places[i]['SOLVED']==True:
                places[i]['SOLVED'] = None
                flagger+=1
                print('\nYou solved room',flagger)
            if flagger==5:
                print('''Callisto: Hey guys! We need you to come back down to the main lobby.Everyone’s meeting up.
                    MC: …
                    Yuri: We’ll be right there.
                    Callisto: Alright then!''')
                flagger=0
                act2=False
    print('ACT 3')
    act3=True
    while act3==True:
        global inventory
        printcenter('The atmosphere is tense, and everyone is weary. Everyone is glancing around each other, like something bad’s about to happen.')
        printcenter('The lingering gazes thrown at MC is subtle, but definitely noticeable.')
        printcenter('Yuri is standing there with the others, and looks like she knows something, something very important. ')
        printcenter('She looks like she has something to say, but she decides against it for now.')
        print_slow('''
Dia: Yuri, you look like you wanna say something. 
Spit it out because you look like you’re gonna puke.
Yuri: …
Yuri: You’re not wrong.
Yuri: silent
Phoeb: What’s the problem?
Kale: This doesn’t seem good…
Callisto: What is it-
Yuri: The killer.''')
        time.sleep(3)
        print_slow('''
MC: …!
Everyone: silent
Yuri: The staff room had two entry points-the window, and the door.
When Callisto opened the window, it seemed like the window was budged, so pushing it up took quite the effort. The killer couldn’t have entered through the window without Sam noticing, he would’ve ran out for help by then.
So we can rule out the possibility that the culprit came and went through the window.
MC: What about the door?
Yuri: Yes, the door.
No one had the key to the door other than Sam.
The only other spare key in this house is the masterkey.
And if I recall correctly, the masterkey was hanging on the wall in the office room.
Unless…someone used it.
MC: …!
Yuri: The only possible explanation would be the masterkey. The culprit killed Sam, locked him back in the room, and came out, replacing the masterkey to where it belonged, like nothing happened.
Just like that, the deed was done. An easy in-and-out.
MC: But, who’s the culprit.
Yuri: Oh that’s simple.
The culprit of this crime is…
''')
        time.sleep(5)
        print_slow("""
                                                                                  New object in inventory!!!
             """)
        final=('bloodyhand',bloodyhand)
        addtoinventory(final)
        time.sleep(3)
        viewobj('bloodyhand')
        time.sleep(10)
        endcredits()
        act3=False
pygame.mixer.init()
pygame.mixer.music.load('soundtrack.wav')
pygame.mixer.music.play()
titlescreen()
