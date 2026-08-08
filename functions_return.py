import datetime
def add(num1,num2):
    return(num1/num2)
    print("hello")
#any code you have put after the return as long as it is in the function will be ignored
ans=add (12,90)
print(ans)





def multiply(num1,num2,num3):
    return(num1*num2*num3)
newans=multiply (69,90,49)
print(newans)

current_time=datetime.datetime.now()
print(current_time)

#mission 1
def calculate_gold(bag1,bag2):
    return(bag1+bag2)
total_gold=calculate_gold(100,190)
print(f"Total tresure collected:{total_gold}coins!")


#misson 2
def apply_torbo(base_speed,torbo_boost):
    return(base_speed+torbo_boost)
final_speed=apply_torbo(600,900)
print(f"Robot speed increased to{final_speed} km/h")

#misson 3
def mix_potion(jar_one_energy,jar_two_energy):
    return(jar_one_energy+jar_two_energy)
total_energy=mix_potion(30,90)
print(f"The potion is ready with:{total_energy} units of magic")


#misson 4
def vending_machine(money):
    if(money>10):
        return ("choclatebar")
    elif(money>=5):
        return ("bag of chips")
    elif(money<=5):
        return("piece of gum")
my_snack=vending_machine(3)
print(f"I inserted my coins and recived a:{my_snack} tasty!")




#mission 5
def craft_item(raw_material):
    if(raw_material=="wood"):
        return( "crafting_table")
    elif(raw_material=="Iron"):
        return("Iron_sword")
    elif(raw_material=="Diamond"):
        return("Diamond pickaxe")
    else:
        return("stick")
my_item=craft_item("wood")
print(f"Succes you placed a material on rhe bench and got a:{my_item} cool!")





def Bypass_level(security_level):
    if(security_level>90):
        return(" admin access_granted")
    elif(security_level>50 and security_level<90):
        return("user access granted")
    else:
        return("Access denied firewall locked")
status=Bypass_level(999)
print(f"The terminal flashes:{status}")