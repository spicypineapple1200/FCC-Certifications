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
    
    def transfer(self, amount, target):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {target.name}")
            target.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        num = int((30-int(len(self.name)))/2)
        output = ('*'*num)+(self.name)+('*'*num)
        
        for item in self.ledger:
            description = item['description'][:23]
            spacing = 30-len(description)-len(f"{item['amount']:.2f}")
            addition = description+(' '*spacing)+f"{item['amount']:.2f}"
            output+='\n'+addition
            pass
        # result_spacing = 
        output += f'\nTotal: {self.get_balance():.2f}'
        return output
    
def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    
    max_length = len(percentages)
    name_length = 0
    names = []
    for item in categories:
        if len(item.name) > name_length:
            name_length = len(item.name)
    max_length+=(1+name_length)
    
    for count in range(max_length):
        if count < len(percentages):
            output+=((" "*(4-len(str(percentages[count]))))+str(percentages[count])+'|\n')
        elif count == len(percentages):
            output+=('-'*3)+'\n'
        else:
            output+='space\n'
    return output

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print('\n\n')

print(create_spend_chart([food, clothing]))

# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96









