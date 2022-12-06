programming_dictionary = {
    "Bug": "An Error that occurs in the program that prevents it from runnign as expected.", 
    "Function": "A piece of code that you can call over and over again with set paramaters",
    "Loop": "The action of doing something over and over again",
}

# print(programming_dictionary[1]) This does not work and causes and error.


## Retrieving items from Dictionary
print(programming_dictionary["Bug"]) # Gives you the value 

## Adding new items to Dictionary
programming_dictionary["Run"] = "A start of a script that begins the events that runs the program."

## Create an empty Dictionary
brand_new_dictionary = {}

## Wipe an Existing Dictionary
Name_A_Dictionary_That_Exists = {}

## Edit an Item
programming_dictionary["Bug"] = "Naughty Bug!!"

## Looping through a Dictionary
for key in programming_dictionary:
    print(key) ##Lists the Keys, not the values
    print(programming_dictionary[key]) ##Prints the Values