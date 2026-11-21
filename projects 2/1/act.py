
import random
import time

name = input("Enter your player name: ")

health = 100
coins = 0
damage = 10
level = 1
potions = 3
inventory = []

print("\nWELCOME", name)
print("YOU ARE ENTERING THE MYSTERY DUNGEON")

while health > 0:

    print("\n======================")
    print("       DUNGEON")
    print("======================")
    print("Player:", name)
    print("Health:", health)
    print("Coins:", coins)
    print("Level:", level)
    print("Potions:", potions)

    print("\n1 Explore")
    print("2 Shop")
    print("3 Inventory")
    print("4 Rest")
    print("5 Quit")

    choice = input("\nWhat do you want to do: ")

    if choice == "1":

        print("\nYou are exploring...")
        time.sleep(1)

        event = random.randint(1, 5)

        if event == 1:
            monster = random.choice(["Zombie", "Dragon", "Goblin", "Skeleton"])
            monster_health = random.randint(20, 60)

            print("\nA", monster, "appeared!")

            while monster_health > 0 and health > 0:

                print("\nYour health:", health)
                print("Monster health:", monster_health)
                print("1 Attack")
                print("2 Use potion")
                print("3 Run")

                action = input("Choose: ")

                if action == "1":
                    hit = random.randint(damage - 3, damage + 10)
                    monster_health -= hit
                    print("You dealt", hit, "damage!")

                    if monster_health > 0:
                        enemy_hit = random.randint(5, 15)
                        health -= enemy_hit
                        print("Monster attacked you for", enemy_hit)

                elif action == "2":
                    if potions > 0:
                        health += 30
                        potions -= 1
                        print("You recovered 30 health!")
                    else:
                        print("No potions left!")

                elif action == "3":
                    print("You escaped!")
                    break

                else:
                    print("Invalid choice")

            if monster_health <= 0:
                reward = random.randint(10, 50)
                coins += reward
                level += 1
                print("\nYOU WON!")
                print("You earned", reward, "coins!")

        elif event == 2:
            reward = random.randint(10, 40)
            coins += reward
            print("\nYou found a treasure chest!")
            print("You got", reward, "coins!")

        elif event == 3:
            print("\nYou found a secret room!")
            print("You discovered a magic sword!")
            damage += 5
            inventory.append("Magic Sword")

        elif event == 4:
            loss = random.randint(5, 20)
            health -= loss
            print("\nYou stepped into a trap!")
            print("You lost", loss, "health!")

        else:
            print("\nYou found a healing fountain!")
            health = min(100, health + 25)

    elif choice == "2":

        print("\n====== SHOP ======")
        print("Coins:", coins)
        print("1 Buy potion - 20 coins")
        print("2 Upgrade sword - 50 coins")
        print("3 Leave shop")

        buy = input("Choose: ")

        if buy == "1" and coins >= 20:
            coins -= 20
            potions += 1
            print("Potion purchased!")

        elif buy == "2" and coins >= 50:
            coins -= 50
            damage += 10
            print("Your sword is stronger!")

        elif buy == "3":
            print("You left the shop")

        else:
            print("Not enough coins or invalid choice!")

    elif choice == "3":
        print("\n====== INVENTORY ======")
        print(inventory)
        print("Potions:", potions)

    elif choice == "4":
        health = min(100, health + 20)
        print("You rested and recovered health!")

    elif choice == "5":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice!")

    if health <= 0:
        print("\nGAME OVER")
        print("You reached level", level)
        print("You collected", coins, "coins")
        print("Thanks for playing", name)

print("\nGAME ENDED")
