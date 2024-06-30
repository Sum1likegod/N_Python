class Library:
    def __init__(self, no_of_books, books):
        self.books = books
        self.no_of_books = no_of_books

    def if_no_of_books_equals_books(self):
        if self.no_of_books == len(self.books):
            print("No. of books and books are equal.")
        else:
            print("No. of books and books are not equal.")

    def add_book(self):
        flag = input('Do you want to add a book? (y/n): ')
        if flag == "y":
            book = input("Enter the name of the book: ")
            self.books.append(book.title())
            self.no_of_books += 1
        else:
            print("No book added.")

    def show_details(self):
        for i in range(len(self.books)):
            print(f"The book {i+1} in the Library is {self.books[i]}.")


library_1 = Library(3, ['Harry Potter', 'Hunger Games', 'Lord of the Rings'])
while True:
    print("\t\tCHOOSE WHAT YOU WANT TO DO:")
    print("""1. Show Details            2. Add Book
3. Checking the Library    4. Quit
   Items                                """)
    user_choice = int(input("\t\tEnter your choice: "))
    if not 0 < user_choice < 5:
        raise ValueError("Valid Options are 1, 2, 3, 4.")

    match user_choice:
        case 1:
            library_1.show_details()
        case 2:
            library_1.add_book()
        case 3:
            library_1.if_no_of_books_equals_books()
        case 4:
            break
