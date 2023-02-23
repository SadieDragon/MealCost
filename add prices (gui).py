
from tkinter import *
import os
import json

root = Tk()
root.title('Testing Layouts')
root.geometry("500x500")

#=================================================================================================================
#frame declaring this is a store selection box
storeFrame = LabelFrame(root, text="Store Selection", padx=5, pady=5)
storeFrame.pack(padx=10, pady=10)

#a dropdown box with all the stores currently in the database-----------------------------------------------------
#The path that the files are in may change, so get the working directory and plonk on the folder for prices
path = os.getcwd() + "\prices"
#create new Direcotry if it doesn't exist
if not os.path.exists(path):
  os.mkdir(path)

# keep only the json stuffz (I only used this bit)
# https://stackoverflow.com/questions/48715569/load-and-read-all-files-json-in-a-folder-with-python
stores_available = [ x for x in os.listdir(path) if x.endswith("json") ]

#go ahead and make the happy lil map for later use
store_map = {}
for store in stores_available:
  #open the json file (value)
  store_path = path + "\\" + store 
  f = open(store_path)

  #take off that .json, make sure caps are proper (key)
  store = store.split('.')[0].title()

  #read in the json as a new value in the store map, with the store as the key
  store_map[store] = json.load(f)

  #close the file
  f.close()

chosenStore = StringVar()
stores = ["[Add New Above]"].append(list(store_map.keys()))
storeList = OptionMenu(storeFrame, chosenStore, stores)
storeList.pack()

#-----------------------------------------------------------------------------------------------------------------

#a textbox marked for "if you can't find the store you are looking for, add it here" 
newStoreField = Entry(storeFrame, width=15)
newStoreField.pack(padx=5, pady=5)

# with a button to confirm the addition of a new store ------------------------------------------------------------
def newStoreCommand():
  newStore = newStoreField.get()

  #TODO: GLOBALS, DAMNIT. (there's probs not a better way)
  #The dropbox should already set this value and I need to modify it
  global chosenStore
  #also also, need this to get modified if we add a new store (or things break)
  global store_map
  
  #Put the new store in the map if one was added, and set chosen store
  if not (newStore == ""):
    chosenStore = newStore
    store_map[newStore] = {}
  
confirmNewStore = Button(storeFrame, text="Add Store", command=newStoreCommand)
confirmNewStore.pack()
#-----------------------------------------------------------------------------------------------------------------

#=================================================================================================================

root.mainloop()

print(chosenStore)
print(store_map)