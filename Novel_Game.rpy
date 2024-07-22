# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Narrator")
define mc = Character("You")
define wind = True
define run = True
define light = False
define injured = False
define weapon_choice = None
define camp = True
define fight = False
define chest = False
define head = False
# The game starts here.

label start:
   
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.

    "This game is a work of fiction."

    "Any relationships to a real person, alive or dead, will be entirely coincidental."
   
    "Do you agree to this contract?"
    menu:
        "Yes":
            jump choice1_yes
    
        "No":
            jump choice1_no

    label choice1_yes:
            $ menu_flag=True
            "Good..lets go forward"  
    jump choice1_done

    label choice1_no:
            $ menu_flag = False
            "Too scared?"
            $ renpy.quit()
    jump choice1_done
    label choice1_done:   
      
  
    label scene1:
        scene black
        show darkroad
        with Dissolve(.5)
        "You woke up confused on the side of the road"
        "with your limited options, you decided to go down the road to find help"

    label scene2:
        scene black
        show treeclaw
        with Dissolve(.5)
        "You noticed very unusual clawmarks on a nearby tree as you were walking "

    
    menu:
        "check to see if anyone's nearby":
            jump choice2_hello

        "Probably just a bear":
            jump choice2_walk
    label choice2_hello:
        $ menu_flag=True
        mc "Hello? Is anyone there?!"
        "Deafening silence greets your ears."
        "You called out to the wood, but alas, there was a lack of answer."
        jump choice2_done
    label choice2_walk:
        $ menu_flag = False
        "You choose to ignore the claw marks and keep walking"
        jump choice2_done
        label choice2_done:
    


    label scene3:
        scene black
        show cross_road
        with Dissolve(.5)
        "You approached the fork in the road and had to make a critical decision"
    
    menu:
        "windmill ->":
            jump choice3_windmill

        "<- log cabin":
            jump choice3_cabin

    label choice3_cabin:
        define wind = False 
        scene black
        show logcabin
        with Dissolve(.15)
        "you have come across an abandoned log cabin and decide to enter"
        show insidelog
        with Dissolve(.5)
        "you've entered the cabin to see it ramsacked with broken glass all over the floor"
        "It looks as if a fight occured inside, perhaps a wild animal attacked"
        menu:
            "Search through the remains":
                jump choice3a_search
            "Leave the cabin":
                jump choice3a_leave
        label choice3a_search:
            $ light = True
            show insidelog
            with Dissolve(.5)
            show light at center with moveintop
            "You have found a flashlight"
        
            jump choice3a_done
        label choice3a_leave:
            "Fearing whatever caused the mess might return, you leave the cabin anxiously"
            jump choice3a_done
            label choice3a_done:



    if wind:
        label choice3_windmill:
            scene black
            show windmill
            with Dissolve(.15)
            "You have come across an adandoned windmill"
            "The seemingly ancient strucure seems to have decayed over time"
            "You decide to go inside to search for supplies"
            show windinside
            menu:
                "Take rusty ladder to second floor":
                    jump choice3b_ladder
                "Search the current floor":
                    jump choice3b_search
            label choice3b_ladder:
                show fall 
                with Dissolve(.15)
                    #Insert ladder audio here
                "The rusty ladder gives up, casuing you to fall and sustain minor injuries to the leg"
                scene black
                "You decide to leave the building with a minor leg injury"
                $ injured = True
                jump choice3b_done
            label choice3b_search:
                $ light = True
                show light at center with moveintop
                "You've found a flashlight after a few minutes of searching"
                jump choice3b_done
                label choice3b_done:


    jump choice3_done
    label choice3_done:
    show outside
    with Dissolve(1)
    "Your back outside outside now but something isn't right..."
    "You feel uneasy as if you're being watched"
    "Like prey being hunted"
    "...."
    "It's no longer a feeling..."
    "You KNOW something is watching you"
    show bush
    with Dissolve(0.1)
    #Bush rustling audio
    "You notice bizzare snarling noises coming from the bushes"
    "Perhaps a deer?"
    
    
    
menu:
    "Search the bushes":
        jump choice4_bushes
    "Run":
        jump choice4_run

label choice4_bushes:
    if light == True:
        show bush
        "A creature jumps out and you flashed it, then start to run"
        # You can add more here if needed
    else:
        $ light = False  # Set light to False if the user didn't search the cabin or windmill
        show monster_jump
        "A nightmarish creature launches itself at you and shreds you apart"
        show death
        "You bleed out..."
        $ renpy.quit()

label choice4_run:
    if injured == False:
        show monster_jump
        "You chose to run and the creature comes out the bush and chases you"
    else:
        $ injured = True
        show death
        "Since your leg is injured, the creature catches and kills you"
        $ renpy.quit()
    # This is the "Run" choice label
    # You can add the relevant code for running here

show run
with Dissolve(.2)

menu:
    "Run into a nearby campsite -> ":
        jump choice5_camp
    " <- Continue deeper into the forest":
        jump choice5_forest

        label choice5_camp:
            show campsite
            with Dissolve(1)
            "As you run into the campsite the creature loses track of you"
            "You quickly search for a wapon to defend yourself with"
            menu:
                "search tent":
                    jump choice5a_tent
                "search log":
                    jump choice5b_log
                "search truck":
                    jump choice5c_truck

                    label choice5a_tent:

                        $ weapon_choice = "search tent" 
                        scene campsite
                        if  weapon_choice == "search tent":
                            show key at center with moveintop
                            "You've acquired boat keys from the tent"
                            "You hear the monster nearby, so you make a run for it"
                            jump choice5_done

                    label choice5b_log:
                        $ weapon_choice = "search log"
                        scene campsite
                        if weapon_choice == "search log":
                            show axe at center with moveintop
                            "You've acquired an axe from the log"
                            "You hear the monster nearby, so you make a run for it"
                            jump choice5_done

                    label choice5c_truck:
                            $ weapon_choice = "search truck"
                            scene campsite
                            if weapon_choice == "search truck":
                                show glock at center with moveintop
                                "You've acquired a gun from the truck"
                                "You hear the monster nearby, so you make a run for it"
                                jump choice5_done
                    label choice5_done:


        if camp:
            show afteritem
            "The monster's snarls seem to be closing in"
            "It's getting closer"
            "CLOSER"
            show encounter
            "You freeze in place as you come face to face with the creature"
            "In the corner of your eye, you notice a dock in the distance"
            menu:
                "fight monster":
                    jump choice6_fight
                "Dodge the monster and run towards the dock":
                    jump choice6_dodge
                    label choice6_fight:
                        if weapon_choice == "search truck":
                            show gunfight
                            $ key_flag = False
                            $ axe_flag = False
                            menu:
                                "Shoot chest":
                                    jump choice6_chest
                                "Shoot head":
                                    jump choice6_head
                                    label choice6_chest:
                                        show jumpscare
                                        with Dissolve(1)
                                        "The chest shot was not enough for the creature and it charges and drags you off"
                                        show death
                                        with Dissolve(.6)
                                        "Bad ending"
                                        $ renpy.quit()
                                    label choice6_head:
                                        "The monster falls to the ground and dies from the shot to the head"
                                        "Then the monster bleeds out on the floor"
                                        scene black
                                        with Dissolve(1)
                                        "You check to see if the monster is dead"
                                        "It is indeed dead"
                                        "You need to figure out a way to leave the forest but at least you can rest easy"
                                        $ renpy.quit()
                        elif weapon_choice == "search tent":
                            $ gun_flag = False
                            $ axe_flag = False
                            show jumpscare
                            with Dissolve(.4)
                            "With nothing to defend yourself against the monster, it lunges toward you and shreds you to pieces"
                            show death
                            with Dissolve(2)
                            "Bad ending"
                            $ renpy.quit()
                        elif weapon_choice == "search log":
                            $ key_flag = False
                            $ gun_flag = False
                            show axefight
                            with Dissolve(.3)
                            "You attempt to defend yourself with an axe"
                            show jumpscare
                            with Dissolve(.3)
                            "The creature then rushes you and tears you apart"
                            show death
                            with Dissolve(2)
                            "Bad ending"
                            $ renpy.quit()        
                    label choice6_dodge:
                        "You dodge the creature and make a run for the docks"
                        show boatend
                        with Dissolve(.6)
                        "you find the boat"
                        if weapon_choice == "search truck":
                            show jumpscare
                            "Your cornered at the boat by the docks and is about to maul you"  
                            scene black
                            with Dissolve(.4)
                            "You've shot the creature three times and it collapses"
                            "You need to find a way out, but at least you're able to rest easy"
                            $ renpy.quit()
                        elif weapon_choice == "search log":
                            show jumpscare
                            "Your cornered at the boat by the docks"
                            scene black
                            with Dissolve(1)
                            "The creature gabs you and tears you in half"
                            show death
                            with Dissolve(2)
                            $ renpy.quit()
                        elif weapon_choice == "search tent":
                            "You've gotten in the boat and escaped"
                            "Good ending"
                            $ renpy.quit()


                       
        label choice5_forest:
            "You're running out of stamina"
            "You hear the creature closing in"
            show jumpscare
            "The creature mauls you to death"
            show death
            with Dissolve(2)
            "Bad ending"
            $ renpy.quit()
                                    
                                    
                                  




# End of the game
return

