contacts={}
while True:
    print("Contact Book Details")
    print("1.Add New Contact")
    print("2.view all contacts")
    print("3.Search a contact")
    print("4.Delete a contact")
    print("5.Exit")
    
    ch=input("Enter your choice(1-5):")
    
    if ch == '1':
        name=input("please enter a name:")
        number=int(input("please enter your number:"))
        contacts[name]=number
        print(f"{name} added to your contacts successfully.")
        
    elif ch =='2':
        if not contacts:
            print("No contacts exist in your contacts book")
        else:
         print("All contacts:")   
         for name,number in contacts.items():
            print(f"{name}: {number}")
            
    elif ch =='3':
        search_name= input("Enter a name to search in your contact:")
        if search_name in contacts:
            print(f"{search_name}: {contacts[name]}")
        else:
            print("searched name is not in your contact book")
            
    elif ch=='4':
        del_name=input("Enter a name to delete:")
        if del_name in contacts:
            del contacts[del_name]
            print(f"{del_name} deleted successfully.")
            
    elif ch =='5':
        print("exited successfully")
        break
    else:
       print("invalid choice.")
            