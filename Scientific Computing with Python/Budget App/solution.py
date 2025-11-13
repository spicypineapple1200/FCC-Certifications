class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total
    
    def transfer(self, amount, target_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer from {self.name}")
            target_category.deposit(amount, f"Transfer to {target_category.name}")
            return True
        else:
            target_category.ledger.append({"amount": 0, "description": f"Attempted transfer from {self.name}. No funds received."})
            return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        return f'{self.ledger}'
    
def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
clothing = Category('Clothing')
clothing.deposit(1000, 'deposit')

print(f'{food.get_balance()}\n{food}\n\n{clothing.get_balance()}\n{clothing}\n')

food.transfer(1999, clothing)

print(f'{food.get_balance()}\n{food}\n\n{clothing.get_balance()}\n{clothing}\n')

# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)


# item = '*************Food*************\ninitial deposit        1000.00\ngroceries               -10.15\nrestaurant and more foo -15.89\nTransfer to Clothing    -50.00\nTotal: 923.96'
# print(item)

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




