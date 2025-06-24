national_flag= (
    ("Saffron", ("courage", "sacrifice", "strength")),
    ("white", ("peace", "truth", "Dharma Chakra",("law of dharma","movement of time"))),
    ("green", ("fertility", "growth", "land's auspiciousness"))
)

while True:
    print("\n NATIONAL FLAG MENU")
    print("1. View all symbols")
    print("2. View a specific symbol's characteristics")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print("👥 Symbols:")
        for symbol in national_flag:
            print(f"- {symbol[0]}")

    elif choice == '2':
        name = input("Enter the symbol's name: ")
        found = False
        for symbol in national_flag:
            if symbol[0].lower() == name.lower():
                print(f" Characteristics for {symbol[0]}: {symbol[1]}")
                print(f" Characteristics for {symbol[0]}: {symbol[1][2]}:{symbol[1][3]}")
                found = True
                break
        if not found:
            print("symbol not found.")

    elif choice == '3':
        print(" Exiting. Goodbye!")
        break

    else:
        print(" Invalid choice. Try again.")
