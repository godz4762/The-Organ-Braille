import json
# print game name

def intro():
    print("====================================")
    print()
    print("          The Organ Braille         ")
    print()
    print("====================================")


    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random

    inventory = []

    hpup1 = False
    townfirsttime = True

    # ask for player username

    name = input("What is your name, Traveler? ")

    # welcome them


    print(f"Welcome to the kingdom, {name}, I wish you the best of luck!")

    # troll

    answer = input("Do you wish to proceed further? ")


    if answer.lower() == "no":
    	print("Well then, off you go!")
    	exit()

    # classes

    print("Choose your class!")
    print("1. Knight")
    print("2. Rogue")
    print("3. Mage")


    valid_class = False


    while valid_class == False:
    	player_class_input = input("> ")

    	if player_class_input == "1":
    		print("A mighty knight you are! Move forward with pride!")
    		valid_class = True
    		player_class = 1
    		player_class_name = "Knight"
    	elif player_class_input == "2":
    		print("A stealthy rogue, sneak between shadows and cut from behind!")
    		valid_class = True
    		player_class = 2
    		player_class_name = "Rogue"
    	elif player_class_input == "3":
    		print("A powerful mage, cast spells of fire and ice to batter your opponent!")
    		valid_class = True
    		player_class = 3
    		player_class_name = "Mage"
    	else:
    		print("That isn't a class!")
    		
    # set stats

    if player_class == 1:
    	print("health - 150")
    	player_health = 150
    	max_player_health = 150
    	print("damage - 80")
    	player_damage = 80
    elif player_class == 2:
        print("health - 80")
        player_health = 80
        max_player_health = 80
        print("damage - 120")
        player_damage = 120
    elif player_class == 3:
        print("health - 130")
        player_health = 130
        max_player_health = 130
        print("damage - 90")
        player_damage = 90

    # small little thing to give player items

    alchemist_shop = False        


    print("You procede along a small path towards a giant cave far in the distance.")

    print("The cave was home to an evil dragon, the end goal of your quest is to slay him and save the kingdom!")

    print("Will you procede forward to fight a Goblin or detour at the Alchemy shop?")

    while alchemist_shop == False:
        potioninq = input("Goblin or Alchemist? ")


        if potioninq.lower() == "alchemist":
            print("You say hello to the Alchemist and he gives you a potion and a small piece of bread for the road.")
            inventory.append("Potion")
            inventory.append("Bread")
            alchemist_shop = True
        elif potioninq.lower() == "goblin":
            print("You procede forward to battle the goblin")
            alchemist_shop = True
        else:
            print("That isn't an option!")


intro()

# define battle function bc we're gonna need that maybe.

def battle(enemy_name, enemy_health, enemy_damage):
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random
    print(f"You enter a battle with a {enemy_name}!")

    while player_health > 0 and enemy_health > 0:
        itemselected = False
        print("Select the number of the action you would like to do!")
        print("1. Fight")
        print("2. Item")
        print("3. Run")
        battle_selection = (input("> "))
        
# fight
    
        if battle_selection.lower() in ["1", "fight"]:
            damage = random.randint(
                player_damage - 25,
                player_damage + 15
            )
            enemy_health = enemy_health - damage
            print(f"You dealt {damage} to {enemy_name}")
            print(f"{enemy_name} has {enemy_health} HP remaining!")

# items (my finest work)

        elif battle_selection.lower() in ["2", "item"]:
            if not inventory:
                print("Your inventory is empty!")
                continue
            else:    
                while itemselected == False:
                    print("Inventory")
                    for item in inventory:
                        print(f"- {item}")


                    itemselected = input("Use which item? Type exit to not use an item. ")
                    if itemselected.lower() == "potion":
                            if "Potion" in inventory:
                                inventory.remove("Potion")
                                if hpup1 == False:
                                    player_health = player_health + 80
                                    print("You drank the potion. You regained 80 Health.")
                                elif hpup1 == True:
                                    player_health = player_health + 130
                                    print("You drank the potion. You regained 130 Health.")
                                print(player_health)
                                itemselected = True
                                if player_health > max_player_health:
                                        player_health = max_player_health
                                print(player_health)
                            else:
                                print("You do not have that!")          
                    elif itemselected.lower() == "bread":
                        if "Bread" in inventory:
                            inventory.remove("Bread")
                            if hpup1 == False:
                                player_health = player_health + 50
                                print("You ate the bread. You regained 50 Health.")
                            elif hpup1 == True:
                                player_health = player_health + 90
                                print("You ate the bread. You regained 90 Health.")
                            itemselected = True
                            if player_health > max_player_health:
                                    player_health = max_player_health
                            print(player_health)
                    elif itemselected.lower() == "witch's brew":
                        if "Witch's Brew" in inventory:
                            inventory.remove("Witch's Brew")
                            brewkill = random.randint(1, 1000)
                            if brewkill >= 2:
                                player_health = max_player_health
                                print("You are healed fully by the Witch's Brew")
                                itemselected = True
                            elif brewkill <= 1:
                                print("The Witch's Brew eat and burns through your throat.")
                                print("You collapse slowly to the ground.")
                                print("Game over.")
                                exit()
                    elif itemselected.lower() == "exit":
                        itemselected = True
                        break
                continue
# troll more (run)
        elif battle_selection.lower() in ["3", "run"]:
            print("You can't run, idiot.")
            player_health = player_health - 15
            print("You tripped and took 15 damage.")
        else:
            print("Not an option!")
            continue

# enemy attacks
        if enemy_health > 0: 
     
            
     
            enemy_attack = random.randint(
                enemy_damage - 5,
                enemy_damage + 5
            )
                                                

            player_health = player_health - enemy_attack

# check if you died like a pleb
        if player_health <= 0:
            print("You died!")
            exit()    
     
     
            print(f"{enemy_name} attacks!")
            print(f"You take {enemy_damage} damage")


        print(f"You have {player_health} HP Remaining!")

# actually run the battle fnct
def story1():
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random
    battle("Goblin", 125, 15)    


    import random

    # money
    player_gold = random.randint(150, 250)


    print("You won! The goblin falls to the ground defeated.")
    print()
    print()
    print("He points you down the path. Ahead was a small shop.")               
    print(f"The goblin gives you {player_gold} gold.")
    print()
    print()
    print()
    print("Down the path was a little shop. You stop inside.")
    print("Spend your gold here!")
    print("What would you like to buy?")


story1()

# add shop func
def road_shop():
    global player_gold
    road_shop = False


    while road_shop == False:
        print(f"You have {player_gold} to spend!")
        item_bought = input("Potion 35 Gold, Bread 20 Gold, Witch's Brew 80 Gold. Type exit to leave without buying anything. ")


        if item_bought.lower() == "potion":
            if player_gold >= 35:
                print("You bought a Potion!")
                inventory.append("Potion")
                player_gold = player_gold - 35
                print(f"You have {player_gold} gold left!")    
            elif player_gold < 35:
                print("You don't have enough gold...")

        elif item_bought.lower() == "bread":
            if player_gold >= 20:
                print("You bought bread!")
                inventory.append("Bread")
                player_gold = player_gold - 20
                print(f"You have {player_gold} gold left!")
            elif player_gold < 20:
                print("You don't have enough gold...")

        elif item_bought.lower() == "witch's brew":
            if player_gold >= 80:
                print("You bought a bubbling Witch's brew!")
                inventory.append("Witch's Brew")
                player_gold = player_gold - 80
                print(f"You have {player_gold} gold left!")
            elif player_gold < 80:
                print("You don't have enough gold...")

        elif item_bought.lower() == "exit":
            print("You leave the shop after taking a look around.")
            road_shop = True

        else:
            print("Not an option!")

# let the player get items
def story2():
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random
    road_shop()


    print("You stumble across a man along the path after you leave the shop.")
    print("He asks if you want to know about the path ahead of you.")


    manquestion = input("yes or no? ")

    # story stuff
    if manquestion.lower() == "yes":
        print("The man tells you about a powerful Ogre down the path a little while.")
        print("You feel as if you will cross paths with that monster.")


    else:
        print("You feel an impending sense of doom of the path ahead of you.")
        print("You don't know how to feel about it.")


    print("You come across a bridge. There's a seemingly evil presence under it. Will you investigate or not.")

    # prompt for more money
    bridgelook = input("yes or no ")

    if bridgelook.lower() == "yes":
        print("You find a horrifying looking monster. He tells you to not worry.")
        print()
        print("He tells you that he wasn't anything to worry about.")
        print("The creature asks if you wanted to be friends, and introduces himself as Golem.")
        print()
        print("You tell him you will be his friend, and he gives you 200 Gold.")
        player_gold = player_gold + 200


    else:
        print("You cross the bridge carefully. Nothing happens as you cross, and you continue down the path.")


    print("You felt a sense of unease rise onto your back. You turn and a goblin ambushes you!")

    # more battle
    battle("Strong Goblin", 300, 40)


    print("The strong goblin falls beneath your strength. He gives you a permanent health upgrade.")

    # give player more hp for later things
    if player_class == 1:
        print("Your max HP increased to 350")
        max_player_health = 350
        player_health = max_player_health
        print("Your HP was also fully restored!")
    elif player_class == 2:
        print("Your max HP increased to 180")
        max_player_health = 180
        player_health = max_player_health
        print("Your HP was also fully restored!")
    elif player_class == 3:
        print("Your max HP increased to 230")
        max_player_health = 230
        player_health = max_player_health
        print("Your HP was also fully restored!")

    # make it so that the hpup affects items
    hpup1 = True


story2()

# story
def story3():
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random
    print("You press on going forawrd.")
    print()
    print()
    print()
    print("You enter a forest. You heard a twig break behind you and you look to see a young girl.")


    print("Be a monster?")
    print("1. Yes.")
    print("2. No.")

    # ask if the player wants to fight and impossible fight
    brutality = input("> ")


    if brutality.lower() == "yes":
        print("You feel stronger. You leave the splatter of blood on the ground.")
        print("Your fate is sealed.")
        print()
        print()
        print()
        print("You encounter a dreadful Ogre. Be prepared.")
        print("He judges you a distasteful stain of this world. Good luck.")
        battle("Enraged Ogre", 9999999999, 100)


    elif brutality.lower() == "no":
        print("You give the girl a little flower.")
        print("She runs off into the wilderness.")


    if manquestion.lower() == "yes":
        print("You come across the Ogre that the strange man told you about.")
        print("He thanks you for gifting his friend a flower.")
        print()
    elif manquestion.lower() == "no":
        print("You come across an Ogre")
        print("He thanks you for gifting his friend a flower.")

    # hard fight?

    print("Attack the Ogre in fear?")
    print("Yes.")
    print("No.")
    ogrefight = input("> ")

    # good luckkk

    if ogrefight.lower() in ["1", "yes"]:
        print("You swing at the Ogre. He initates a fight.")
        battle("Ogre", 850, 60)
        player_gold = player_gold + random.randint(500, 700)
    # boring
    elif ogrefight.lower() in ["2", "no"]:
        print("You carry on down the path.")
        print("Good choice.")

# atp the player wants or needs more items depending on their choices, so let em have it.
road_shop()


def town_shop():
    global player_gold
    road_shop = False


    if townfirsttime == True:
        print("The shopkeep welcomes you. He says you look new around here. You exchange names and then begin browsing.")
    elif townfirsttime == False:
        print(f'The shopkeep welcomes you to his shop. "Welcome back {name}."')
    
    
    while road_shop == False:
        print(f"You have {player_gold} to spend!")
        item_bought = input("Potion 35 Gold, Bread 20 Gold, Witch's Brew 80 Gold. Type exit to leave without buying anything. ")
    
    
        if item_bought.lower() == "potion":
            if player_gold >= 35:
                print("You bought a Potion!")
                inventory.append("Potion")
                player_gold = player_gold - 35
                print(f"You have {player_gold} gold left!")    
            elif player_gold < 35:
                print("You don't have enough gold...")
    
        elif item_bought.lower() == "bread":
            if player_gold >= 20:
                print("You bought bread!")
                inventory.append("Bread")
                player_gold = player_gold - 20
                print(f"You have {player_gold} gold left!")
            elif player_gold < 20:
                print("You don't have enough gold...")
    
        elif item_bought.lower() == "witch's brew":
            if player_gold >= 80:
                print("You bought a bubbling Witch's brew!")
                inventory.append("Witch's Brew")
                player_gold = player_gold - 80
                print(f"You have {player_gold} gold left!")
            elif player_gold < 80:
                print("You don't have enough gold...")
    
        elif item_bought.lower() == "exit":
            print("You leave the shop after taking a look around.")
            road_shop = True
    
        else:
            print("Not an option!")


def town_tavern():
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random


    if townfirsttime == True:
        print("You enter the tavern down the small main street. the barkeep welcomes you.")
        print("He lets you know that the Tavern also has an Inn attached, most people aren't used to that.")
        print()
        print()
        print(f'He asks your name. You say with a charming confidence. "{name}." The barkeep nods.')
        print("You take a seat at the bar.")
    elif townfirsttime == False:
        print(f'The Barkeep welcomes you. "Sup {name}." he says. You walk in as normal and sit at the bar.')


    print("What would you like to do? (type the letters in ' ' to purchase)")
    print("Purchase 'HP' Upgrade, (3x in stock 175 Gold). Purchase 'DMG' Upgrade, (2x in stock, 150 Gold). Stay in a room in the Inn. (80 Gold)")    
    tavernbought = input("> ")


    if tavernbought.lower == hp:
        print("The barkeep hands you a red liquid. You drink it and feel blissful. Your HP was permanently upgraded.")
                
        
# FINALLY DEFINE SAVING!
def save_game():
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    global name
    import random
    save_data = {
        "player_health" : player_health,
        "max_player_health" : max_player_health,
        "player_damage" : player_damage,
        "player_class" : player_class,
        "player_class_name" : player_class_name,
        "inventory" : inventory,
        "hpup1" : hpup1,
        "player_gold" : player_gold,
        "townfirsttime" : townfirsttime
    }

    with open("save.json", "w") as file:
        json.dump(save_data, file, indent=4)


    print("Game saved!")
#new global hub area.
def town():
    global player_health
    global inventory
    global max_player_health
    global player_damage
    global hpup1
    global townfirsttime
    global player_gold
    global player_class
    global player_class_name
    import random
    towncomplete = False
    while towncomplete == False:
        if townfirsttime == True:
            print("You continue down the path and emerge from the forest. You end up at a large town.")
        else:
            print("You head back to the town.")
        
        
        print()
        print()
        print()
        print("What would you like to do?")
        print("1, Shop")
        print("2. Tavern/Inn.")
        print("3. Save Game.")
        print("4. Leave the town. WARNING, this will proceed your game and you may not be able to come back for a long time.")


        townoption = input("> ")


        if townoption.lower() in ["1", "shop"]:
            town_shop()
