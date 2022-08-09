class Item:
    pay_rate = 0.8
    all_items = []

    def __init__(self, name, price, quantity=0):
        #give limitations to the recieved arguments
        assert price >= 0
        assert quantity >= 0

        #assign variables/attributes to the self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #save all the items to a list (could be useful when many items are required)
        Item.all_items.append(self)


    def total_value(self):
        #do not need any further arguements as the price and quantity variables are already
        #created and linked to the self object
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

#all of our items
item_1 = Item("phone", 100,2)
item_2 = Item("laptop", 100,2)
item_3 = Item("keyboard", 30, 4)


total_phone = item_1.total_value()
total_laptop = item_2.total_value()

if total_phone == 0:
   print(f"{item_1.name}s are out of stock")
else:
    print(f"Total value from phones in inventory: {total_phone}")


#magic method that can be used to find all the attributes for the insance level
print(item_1.__dict__ )
print("")

#since we do not specify a payrate, the function above takes the payrate from the class level
item_1.apply_discount()
print(item_1.price)

#since we specify the pay rate, it uses the variable from the instance level!
item_2.pay_rate = 0.7
item_2.apply_discount()
print(item_2.price)
print("")

print(f"These are all the items (objects) that are stored in a list {Item.all_items}")
print("")
print("Below are all the items that cost more than 60 units")
for item in Item.all_items:
    if item.price > 60:
        print(item.name)