fuellevel=90
if fuellevel>80:
    print("Fueltank is full, lets drive to the secret base")
elif fuellevel>20:
    print("fuel tank is low go to the nearest gas station")
else:
    print("grab ur running shoes")



zombiecount=100
if zombiecount==0:
    print("scanning all clear")
elif zombiecount<10:
    print("Target locked initilizing lazerbeem")
else:
    print("To many zombies deploying smoke bombs")



cratecolor="blue"
if cratecolor=="Gold":
 print("you found a legendary sword")
elif cratecolor== "Silver":
    print("you found a medkit")
else:
    print("its a box of stale pepperoni Yuck!")


players = ["Mario", "Luigi", "James", "Lilian"]

winner = players[0]

print(f"The Golden Mushroom goes to: {winner}")


Heroes = ["Batman", "Wonder Woman", "Spy", "Flash"]

Heroes[2] = "Super Dog"

print(Heroes)


Inventory = ["Sword", "Old Socks", "Shield"]

Inventory.remove("Old Socks")
Inventory.append("Cool Cape")

equipped_weapon = Inventory[0]

print(Inventory)
print(equipped_weapon)