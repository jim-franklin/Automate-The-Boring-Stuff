def addToInventory(inventory, addedItems):
    
    for item in addedItems:
        inventory.setdefault(item, 0)   # set the value of a non-exitent key to 0
        inventory[item] += 1    # add 1 to the value of an item in the inventory if item
                                # can be found in `addedItems` list
    
    item_total = 0  # set total number of items to 0
    
    for k, v in inventory.items():
        print(str(v), k)
        item_total += v
        
    print(f'Total number of items: {item_total}')


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Call the function with `inv` and `dragonLoot` as arguments
addToInventory(inv, dragonLoot)
