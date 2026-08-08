Countries=["Kenya","Brazil","Uganda","London"]
print(Countries[3])
# adding and item in a list
Countries.append("Zanzibar")
print(Countries)
# changing an item in a list
Countries[2]="Dubai"
print(Countries)
# Removing/delting and item
Countries.remove("Kenya")
print(Countries)
del Countries[2]
print(Countries)
Countries.pop()
print(Countries)