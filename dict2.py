#stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def displayInventory(inventory):
    print('Inventory')
    count = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        count = count + v
    print('Total number of items:' + str(count))

def addToInventory(inventory,addItems):
    for item in addItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory

#inv = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)