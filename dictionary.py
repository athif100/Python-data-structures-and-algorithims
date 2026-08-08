Hero={
"name":"Spiderman",
"CT":"New york",
"Health":100,
"named_after":"Spider"
}
print(Hero)
#getting one item from the dict
print(Hero["name"])
print(Hero.keys())
print(Hero.values())
#add an item
Hero["nemesis"]="Sandman"
print(Hero)
#cnage an item
Hero["CT"]="Tokiyo"
print (Hero)
#deleting an item
del Hero["Health"]
print(Hero)