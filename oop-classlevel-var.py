import csv

class Item:
    payrate = 0.8   # class variable
    all_instances = []

    def __init__(self, name, qty, price):   #Magic method to initialise instance variables
        
        #Run validation of input arguments
        assert price > 0, f"Price {price} is not greater than 0."
        assert qty > 0, f"Quantity {qty} is not greater than 0"

        # Assign values
        self.name = name
        self.price = price
        self.qty = qty

        # keep adding all the instances created for this class
        Item.all_instances.append(self)

    def calculate_total_price(self):
        return self.qty * self.price
    
    def apply_discount(self):
        self.price = self.price * self.payrate

    def __repr__(self): #Magic method to represent instance, useful while printing the instance
        return f"Item('{self.name}', '{self.qty}', '{self.price}')";
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    qty=int(item.get('qty')),
                    price=float(item.get('price'))
                )


item1 = Item("phone", 100, 5)
print(item1.price)
item1.apply_discount()
print(item1.price)

item2 = Item("mobile", 10, 3)
item2.payrate=0.7   #explicit change of discount for specific instance(overrding class variable)
item2.apply_discount()  
print(item2.price)

print (item2) 

print("Printing all instances created:")
print (Item.all_instances)

print("\n Printing all instances created from reading csv:")
Item.instantiate_from_csv()
print(Item.all_instances)

