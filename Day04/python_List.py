fruits = ["item1", "item2"]

junk = ["String", 23, True, "Can use Anything"]

United_Kingdom = ["England", "Scotland", "Wales", "Northern Ireland"]
print(United_Kingdom[1]) #Scotland
print(United_Kingdom[-1]) #Northern Ireland

# United_Kingdom[4] = ["Republic Ireland"]
# print(United_Kingdom[4]) #Errors as out of Range

United_Kingdom.extend(["Republic of Ireland"])
print(United_Kingdom) #Republic of Ireland is added