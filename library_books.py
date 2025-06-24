library_books = {}

while True:
    print("\n LIBRARY BOOKS MENU")
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book_name = input("Enter book name: ")
        isbn_number = input("Enter isbn number: ")
        library_books[isbn_number]=book_name
        print(f" {book_name} added successfully.")

    elif choice == '2':
        if not library_books:
            print("📭 No books yet.")
        else:
            print(" All Books:")
            for isbn_number, book_name in library_books.items():
                print(f"{isbn_number}: {book_name}")

    elif choice == '3':
        search_name = input("Enter book name to search: ")
        if search_name in library_books:
            print(f" {search_name}: {library_books[search_name]}")
        else:
            print(" Book not found.")

    elif choice == '4':
        del_name = input("Enter book name to delete: ")
        if del_name in library_books:
            del library_books[del_name]
            print(f" {del_name} deleted.")
        else:
            print(" Book not found.")

    elif choice == '5':
        print(" Exiting Library Book. Goodbye!")
        break

    else:
        print(" Invalid choice. Please try again.")
