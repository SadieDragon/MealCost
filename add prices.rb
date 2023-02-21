
def full_string_cap(item)
  item.gsub(/\S+/, &:capitalize)
end

def get_item(message)
  #ask the user to input [(the store), (the item), (the package size (ie 12 oz)), and (the cost of the item)]
  puts message
  @item = gets.chomp()

  #break that input into an array based on commas (as shown above in the comment)
  @item_array = @item.split(", ")
  @item_array[0] = full_string_cap(@item_array[0]) #make sure the store is capitalized
  @item_array[1] = full_string_cap(@item_array[1]) #make sure the item is also capitalized
  
  return @item_array
end

puts "Welcome, user. The format for your input should be as follows, ignoring the parentheses:"
puts "(store name), (the item you are adding), (package size- ie, 12 oz), (cost of item)"
puts "And... Please put in the full name. (Food Lion) instead of FL, (Dollar General) instead of DG. Please?"

first_item = get_item("First item, please?")

#make sure that the stores modified are stored in an array
stores_modified = [first_item[0]]

#read in the JSON of stuffz for each store
#add to the hash that corresponds with the store tag -> if a new store is detected, abort and ask them to add a new store and acronyms to the program

#if an item is already in the price list, prompt the user with the old price, and the price change

#do you have more to add to that store? 
#yes -> how many more items? -> repeat the above x times, minus the store tag -> no condition
#no -> do you have another store to add to? -> (yes -> repeat all of the above steps) (no -> next step)

#update the JSON for the stores that were updated