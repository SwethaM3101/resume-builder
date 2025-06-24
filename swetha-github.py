def fruitss():
    fruit_item=[]
    fruit=input("Enter a fruit name to add:")
    fruit_item.append(fruit)
    fruit_item.append("apple")
    fruit_item.append("mango")
    fruit_item.append("green apple")
    fruit_item.append("pine apple")
    print("All Fruits Are:",fruit_item)
    print("Total fruits are:",len(fruit_item))
    print(f"Price of {fruit_item[0]} is Rs.300")
    print(f"I want to buy {fruit_item[3]} instead of {fruit_item[0]}")
    print("Fruits in orderwise")
    for i, fruit in enumerate(fruit_item, 1):
                print(f"{i}. {fruit}")
            
    
def products():
    pdt_item=("111M","milk",25,300)
    print("All product details are:",pdt_item)
    print(f"Total no of products are:{pdt_item[3]}")
    print(f"Price of {pdt_item[1]} is Rs.{pdt_item[2]}")
    print(f"I want to buy {pdt_item[1]}")
    

bakery_and_bread = {
    "Bread": {"price": 2.99, "quantity": 100},
    "Pastries": {"price": 1.99, "quantity": 50},
    "Cakes": {"price": 19.99, "quantity": 20},
    "Cookies": {"price": 4.99, "quantity": 30}
}

def bakery():
    for item, details in bakery_and_bread.items():
        print(f"Item: {item}, Price: ${details['price']:.2f}, Quantity: {details['quantity']}")

def access_bakery_item():
    print("gggg")
    keys = list(bakery_and_bread.keys())
    print(f"I like {keys[0]} and its price is ${bakery_and_bread[keys[0]]['price']:.2f}")
    
def update_bakery_item(item, price=None, quantity=None):
    if item in bakery_and_bread:
        if price:
            bakery_and_bread[item]["price"] = price
        if quantity:
            bakery_and_bread[item]["quantity"] = quantity
    else:
        print("Item not found.")


def add_bakery_item(item, price, quantity):
    bakery_and_bread[item] = {"price": price, "quantity": quantity}

def remove_bakery_item(item):
    if item in bakery_and_bread:
        del bakery_and_bread[item]
    else:
        print("Item not found.")
#Display initial bakery items
print("Initial Bakery Items:")
bakery()

#access bakery item
access_bakery_item()



# Display bakery items
#bakery()

# Update bakery item
update_bakery_item("Bread", price=3.99)
access_bakery_item()
# Add new bakery item
add_bakery_item("Muffins", 2.49, 40)

# Remove bakery item
remove_bakery_item("Cookies")

# keys=list(bakery_and_bread.keys())
# print(f"I like {keys[0]} and its price is",bakery_and_bread[keys[3]]["price"])
# # Display updated bakery items
# print(f"I like Cookies") 
#access_bakery_item()
bakery()
    
def sample():
    while True:
        print("\n SUPERMARKET")
        print("1.Fruits")
        print("2.Products")
        print("3.Bakery")
        print("4.Exit")
        ch=input("Enter your choice:")
        if ch == '1':
            print("Fruit details:")
            fruitss()
            
        elif ch == '2':
           print("Product details:")
           products()
           
        elif ch == '3':
           print("Bakery details:")
           bakery()
           
        elif ch =='4':
            print("Exittingg...Good Bye!!!!!!")        
            break
        else:
            print("Invalid Choice.Please enter a valid choice.")
        
sample()    