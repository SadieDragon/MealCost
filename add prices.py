

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

#read in the JSON of stuffz for each store
#add to the hash that corresponds with the store tag -> if a new store is detected, abort and ask them to add a new store and acronyms to the program

#if an item is already in the price list, prompt the user with the old price, and the price change

#do you have more to add to that store? 
#yes -> how many more items? -> repeat the above x times, minus the store tag -> no condition
#no -> do you have another store to add to? -> (yes -> repeat all of the above steps) (no -> next step)

#sort the hashes alphabetically. if a store doesn't have all the items the other store(s) have, insert a default value for N/A
#(N/A is bad for formatting reasons so find something to default to)

#update the JSON for the stores that were updated