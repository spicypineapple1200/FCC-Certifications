class Category:
    def __init__(self, ledger):
        self.ledger = []
    
    def deposit(self):
        pass
    
    def withdraw(self):
        pass
    
    def get_balance(self):
        pass
    
    def transfer(self):
        pass
    
    def bark(self):
        pass
    

def create_spend_chart(categories):
    myList = []
    for item in categories:
        item = Category(item)
        myList.append(item)
    print(myList)

item = '*************Food*************\ninitial deposit        1000.00\ngroceries               -10.15\nrestaurant and more foo -15.89\nTransfer to Clothing    -50.00\nTotal: 923.96'
print(item)

# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96



# class MyClass:
#     def __init__(self, health, mana, stamina):
#         self.health = health
#         self.mana = mana
#         self.stamina = stamina

# warrior = MyClass(100, 10, 50)
# mage = MyClass(25, 100, 40)
# archer = MyClass(50, 30, 100)

# print(archer.health)




