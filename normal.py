import random


def text_adventure():
    player_health = 100
    player_gold = 0
    locations = ["forest", "cave", "mountain", "village", "dungeon"]
    enemies = ["goblin", "wolf", "bandit", "skeleton", "troll"]

    print("Welcome to the Mini Adventure!")
    player_name = input("Enter your name: ")

    while player_health > 0:
        current_location = random.choice(locations)
        print(f"\n{player_name}, you are in the {current_location}.")

        action = input("Do you want to [e]xplore, [r]est, or [q]uit? ").lower()

        if action == 'e':
            if random.random() < 0.7:
                enemy = random.choice(enemies)
                damage = random.randint(5, 25)
                gold_found = random.randint(5, 20)
                print(f"You encountered a {enemy} and took {damage} damage, but found {gold_found} gold!")
                player_health -= damage
                player_gold += gold_found
            else:
                print("You explored safely and found nothing of interest.")
        elif action == 'r':
            heal_amount = random.randint(10, 30)
            player_health = min(100, player_health + heal_amount)
            print(f"You rested and recovered {heal_amount} health. Current health: {player_health}")
        elif action == 'q':
            break

    print(f"Game over! You collected {player_gold} gold in your adventure.")


text_adventure()
