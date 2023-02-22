
import os
import json

def get_new_item(message):
  #ask the user to input [(the store), (the item), (the package size (ie 12 oz)), and (the cost of the item)]
  item = input(message)
  #break that input into an array based on commas (as shown above in the comment)
  item_array = item.split(", ")

  #make sure that both the store and item are capatalized
  item_array[0] = item_array[0].title()
  item_array[1] = item_array[1].title()

  #return the list
  return item_array

#Fancy multiline string, thank you python, I don't have to call every print to greet the new user.
print("""Welcome, user. The format for your input should be as follows, ignoring the parantheses:
(store name), (item you're adding), (package size- ie, 12 oz), (cost of item)
And... Please, put in the full name. (Food Lion) instead of FL, (Dollar General) instead of DG. Please?""")

first_item = get_new_item("Please input your first item: ")
#make sure that the stores modified are stored in an array
modified_stores = first_item[0]

#The path that the files are in may change, so get the working directory and plonk on the folder for prices
path = os.getcwd() + "\prices"
#You need this list of jsons in the directory for reasons (below)
stores_available = os.listdir(path) #TODO: bulletproof this to only give a care about JSON files
#This happy little variable? This makes adding new stores not a problem.
store_map = {}
#Get the JSON stuffz for every store available
for store in stores_available:
    #open the json file (val)
    store_path = path + "\\" + store
    f = open(store_path)

    #take off that .json tag from the store, and upper case it (key)
    store = store.split('.')[0].title()

    #read in the json file as a new val in the store map at modified store key
    store_map[store] = json.load(f)

    #close thejson file
    f.close()

print(store_map)
  
#add to the hash that corresponds with the store tag -> if a new store is detected, add that to the store map

#if an item is already in the price list, prompt the user with the old price, and the price change

#do you have more to add to that store? 
#yes -> how many more items? -> repeat the above x times, minus the store tag -> no condition
#no -> do you have another store to add to? -> (yes -> repeat all of the above steps) (no -> next step)

#sort the hashes alphabetically. if a store doesn't have all the items the other store(s) have, insert a default value for N/A
#(N/A is bad for formatting reasons so find something to default to)

#update the JSON for the stores that were updated