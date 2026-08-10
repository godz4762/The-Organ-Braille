
# print game name


print("====================================")
print()
print("          The Organ Braille         ")
print()
print("====================================")

inventory = []

# ask for player username

name = input("What is your name, Traveler? ")

# welcome them


print(f"Welcome to the game, {name}, I wish you the best of luck!")


answer = input("Do you wish to proceed further? ")


if answer.lower() == "no":
	print("Well then, off you go!")
	exit()


print("Choose your class!")
print("1. Knight")
print("2. Rogue")
print("3. Mage")


valid_class = False


while valid_class == False:
	player_class = input("> ")

	if player_class == "1":
		print("A mighty knight you are! Move forward with pride!")
		valid_class = True
	elif player_class == "2":
		print("A stealthy rogue, sneak between shadows and cut from behind!")
		valid_class = True
	elif player_class == "3":
		print("A powerful mage, cast spells of fire and ice to batter your opponent!")
		valid_class = True
	else:
		print("That isn't a class!")

if player_class == "1":
	print("health - 150")
	player_health = 150
	max_player_health = 150
	print("damage - 80")
	player_damage = 80
elif player_class == "2":
    print("health - 80")
    player_health = 80
    max_player_health = 80
    print("damage - 120")
    player_damage = 120
elif player_class == "3":
    print("health - 130")
    player_health = 130
    max_player_health = 130
    print("damage - 90")
    player_damage = 90

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

def battle(enemy_name, enemy_health, enemy_damage):
    global player_health
    global inventory
    global max_player_health
    global player_damage
    import random
    print(f"You enter a battle with a {enemy_name}!")

    while player_health > 0 and enemy_health > 0:
        item_selected = False
        print("Select the number of the action you would like to do!")
        print("1. Fight")
        print("2. Item")
        print("3. Run")
        battle_selection = (input("> "))
        
    
        if battle_selection.lower() in ["1", "fight"]:
            print(f"You dealt {player_damage} to {enemy_name}")
            enemy_health = enemy_health - player_damage
            print(f"{enemy_name} has {enemy_health} HP remaining!")
        elif battle_selection.lower() in ["2", "item"]:
            if not inventory:
                print("Your inventory is empty!")
                continue
            else:    
                while item_selected == False:
                    print("Inventory")
                    for item in inventory:
                        print(f"- {item}")


                    itemselected = input("Use which item? Type exit to not use an item. ")
                    if itemselected.lower() == "potion":
                            if "Potion" in inventory:
                                inventory.remove("Potion")
                                player_health = player_health + 80
                                print("You drank the Alchemists potion. You regained 80 Health.")
                                item_selected = True
                                if player_health > max_player_health:
                                        player_health = max_player_health
                            else:
                                print("You do not have that!")          
                    elif itemselected.lower() == "bread":
                        if "Bread" in inventory:
                            inventory.remove("Bread")
                            player_health = player_health + 50
                            print("You ate the bread. You regained 50 Health.")
                            item_selected = True
                            if player_health > max_player_health:
                                    player_health = max_player_health
                    elif itemselected.lower() == "witch's brew":
                        if "Witch's Brew" in inventory:
                            inventory.remove("Witch's Brew")
                            brewkill = random.randint(1, 10000)
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
        elif battle_selection.lower() in ["3", "run"]:
            print("You can't run, idiot.")
            player_health = player_health - 15
            print("You tripped and took 15 damage.")
        else:
            print("Not an option!")


        if player_health <= 0:
            print("You Died!")
            exit()


        if enemy_health > 0: 
     
            
     
            enemy_damage = random.randint(
                enemy_damage - 5,
                enemy_damage + 5
            )
                                                

            player_health = player_health - enemy_damage
     
     
            print(f"{enemy_name} attacks!")
            print(f"You take {enemy_damage} damage")


        print(f"You have {player_health} HP Remaining!")


battle("Goblin", 125, 15)    


import random


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

road_shop = False


while road_shop == False:
    print(f"You have {player_gold} to spend!")
    item_bought = input("Potion 35 Gold, Bread 20 Gold, Witch's Brew 80 Gold. Type exit to leave without buying anything. ")


    if item_bought.lower() == "potion":
        print("You bought a Potion!")
        inventory.append("Potion")
        player_gold = player_gold - 35
        print(f"You have {player_gold} gold left!")    

    elif item_bought.lower() == "bread":
        print("You bought bread!")
        inventory.append("Bread")
        player_gold = player_gold - 20
        print(f"You have {player_gold} gold left!")

    elif item_bought.lower() == "witch's brew":
        print("You bought a bubbling Witch's brew!")
        inventory.append("Witch's Brew")
        player_gold = player_gold - 80
        print(f"You have {player_gold} gold left!")

    elif item_bought.lower() == "exit":
        print("You leave the shop after taking a look around.")
        road_shop = True

    else:
        print("Not an option!")


print("You stumble across a man along the path after you leave the shop.")
print("He asks if you want to know about the path ahead of you.")


manquestion = input("yes or no? ")


if manquestion.lower() == "yes":
    print("The man tells you about a powerful Ogre down the path a little while.")
    print("You feel as if you will cross paths with that monster.")


else:
    print("You feel an impending sense of doom of the path ahead of you.")
    print("You don't know how to feel about it.")


print("You come across a bridge. There's a seemingly evil presence under it. Will you investigate or not.")


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


battle("Strong Goblin", 300, 40)


print("The strong goblin falls beneath your strength. He gives you a permanent health upgrade.")


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


