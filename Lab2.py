import random

# Define Variables
numLives = 10           # Player ki lives
mNumLives = 12          # Monster ki lives

# Weapon list with increasing strength
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
weaponStrength = [1, 2, 3, 4, 5, 6]

# Get combat strengths with error handling
try:
    combatStrength = int(input("Enter your combat Strength: "))
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

# Dice options
diceOptions = [1, 2, 3, 4, 5, 6]

# Roll dice for health points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Weapon roll to determine which weapon is chosen
input("Roll the dice to determine your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)
combatStrength += weaponStrength[weaponRoll - 1]  # Weapon ki strength ko combat strength mein add karo
chosenWeapon = weapons[weaponRoll - 1]  # Selected weapon

print(f"You rolled {weaponRoll} and chose the {chosenWeapon}.")

# Conditionals for weapon strength
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if chosenWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Health aur combat ka logic
input("Analyze the roll (Press enter)")

if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

# Combat ka logic
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print(f"Your sword ({combatStrength}) ---> Monster ({mHealthPoints})")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print(f"Monster's Claw ({mCombatStrength}) ---> You ({healthPoints})")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))
