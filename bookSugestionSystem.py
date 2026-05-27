import random

def main():
    
    books = ["1984", "The Hobbit", "Dracula"]

    while True:
        print("""
            ================================================>
                    1. Suggest
                    2. Add
                    3. Remove
                    4. Update
                    5. Exit.
          <===================================================
                    """)
        choice = input("Enter your choice of action: ")

        if choice == "1":
            if len(books) == 0:
                print("No books!")
                continue
            
            while True:
                print(get_suggestion(books))
                answer = input("(Yes/No): ").lower()
 
                break
        
        elif choice == "2":
            title = input("Title to add: ")
            original_size = len(books)
            books = add_book(books, title)
            print("Book has been added!" if len(books) > original_size else "Already exists!")
            
        elif choice == "3":
            title = input("Title to remove: ")
            original_size = len(books)
            books = remove_book(books, title)
            print("Removed" if len(books) < original_size else "Book Not found!")
            
        elif choice == "4":
            old_title = input("Old title: ").strip()
            new_title = input("New title: ").strip()
            
            updated_books = update_book(books, old_title, new_title)
            
            if updated_books == books:
                print("Not found!")
            else:
                books = updated_books
                print("Updated!")
                
        elif choice == "5":
            print("Exit!")
            break

def get_suggestion(books):
    
    random_book = random.choice(books)
    random_page = random.randint(1, 100)
    return f'Book: "{random_book}" at Page {random_page}'

def add_book(books, title):
    
    for name in books:
        if name.lower() == title.lower():
            return books 
            
    
    new_books = books.copy()
    new_books.append(title)
    return new_books

def remove_book(books, title):
    
    found = False
    for name in books:
        if name.lower() == title.lower():
            found = True
            break
    if not found:
        return books

    
    new_books = []
    for name in books:
        if name.lower() == title.lower():
            continue
        new_books.append(name)
    return new_books

def update_book(books, old_title, new_title):
    
    updated_books = books.copy()
    for count in range(len(updated_books)):
        if updated_books[count].lower() == old_title.lower():
            updated_books[count] = new_title
            return updated_books
    return books


if __name__ == "__main__":
    main()

