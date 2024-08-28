import sys

# Game setup
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious land, and your adventure begins now.")
    character_name = input("Enter your character's name: ")
    print(f"Hello, {character_name}! Let's begin your journey.")
    main_story(character_name)

# Main story function
def main_story(character_name):
    inventory = []
    while True:
        print("\nYou are standing at a crossroads. Where do you want to go?")
        print("1. Enter the forest")
        print("2. Go to the village")
        print("3. Check inventory")
        print("4. Quit game")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            enter_forest(inventory)
        elif choice == "2":
            go_to_village(inventory)
        elif choice == "3":
            check_inventory(inventory)
        elif choice == "4":
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Forest path function
def enter_forest(inventory):
    print("\nYou enter the dark, dense forest.")
    print("Suddenly, you encounter a wild wolf!")
    action = input("Do you want to (a) fight the wolf or (b) run away? ")

    if action == "a":
        if "Sword" in inventory:
            print("You use your Sword to fight off the wolf and win!")
        else:
            print("You have no weapon to defend yourself. The wolf overpowers you.")
            print("Game Over.")
            sys.exit()
    elif action == "b":
        print("You successfully run away from the wolf and return to the crossroads.")
    else:
        print("Invalid action. Returning to the crossroads.")

# Village path function
def go_to_village(inventory):
    print("\nYou arrive at a peaceful village.")
    print("An old man approaches you and offers you a Sword.")
    take_sword = input("Do you want to take the Sword? (yes/no) ")

    if take_sword.lower() == "yes":
        if "Sword" not in inventory:
            inventory.append("Sword")
            print("Sword has been added to your inventory.")
        else:
            print("You already have a Sword.")
    else:
        print("You decline the offer and return to the crossroads.")

# Inventory check function
def check_inventory(inventory):
    if inventory:
        print(f"Your inventory: {', '.join(inventory)}")
    else:
        print("Your inventory is empty.")

# Start the game
if __name__ == "__main__":
    start_game()
