# import json
# import os

# def menu():
#     print("librar data")
#     print("1.add a book to library")
#     print("2.view books")
#     print("3.borrow book")
#     print("4.return book")

# library_file='library_data.json'

# def load_library():
#     if not os.path.exists(library_file):
#         return{}
#     try:
#         with open(library_file,'r') as file:
#             return json.load(file)
#     except Exception as e:
#         print(f"error loading library data: {e}")
#         return{}

# def save_library(library):
#     try:
#         with open(library_file, 'w') as file:
#             json.dump(library, file)
#     except Exception as e:
#         print(f"Error saving library data: {e}")

# def add_book (library, title, author, quantity):

#     if title in library:
#        print("Book already exists. updating the quantity.")
#        library [title][quantity] += quantity
#     else:
#        library[title] = {'author': author, "quantity": quantity, 'borrowed_by': None}
#        save_library(library)
#        print(f"Book '{title}' added successfully!")

# def view_books(library):
#     if not library:
#         print("the library is empty.")
#         return
#     for title,details in library.items():
#         status=f"Available({details['quantity']})" if not ['borrowed_by'] else f"Borrowed by{details['borrowed_by']}"
#         print(f"Title:{title},Author:{details['autor'],status:(status)}")

# def borrow_book(library,title,borrower_name):
#     if title not in library:
#         print("book not found in the library.")
#         return
#     if library[title]['quality']==0:
#         print(f"All copies of '{title}' are currently borrowed.")
#         return
#     if library[title]['borrowed_by']:
#         print(f"the book '{title}'is currently borrowed by {library[title]["borrowed_by"]},")
#         return
#     if library[title]["borrowed_by"]:
#         print(f"the book'{title}' is currently borrowed by {library[title]["borrowed_by"]}.")
#         return
#     library[title]['quality']-=1
#     library[title]['borrowed_by']=borrower_name
#     save_library(library)
#     print(f"'{title}' has been borrowed by {borrower_name}.")

# def return_book(library, title):
#   if title not in library:
#    print("Book not found in the library.")
#    return
#   if not library [title] ['borrowed_by']:
#    print(f"The book '{title} was not borrowed.")
#    return

#   library [title]['quantity'] += 1
#   borrower_name = library [title] ['borrowed_by']
#   library [title]['borrowed_by'] = None
#   save_library(library)
#   print(f" (title) has been returned by {borrower_name}.")

# def main():
#       library=load_library()
#       while True:
#           choice=input("enter your choice: ")
#           if choice == '1':
#             title= input("Enter the book title: ")
#             author= input("Enter the book author: ")
#             try:
#               quantity=int(input("Enter the quantity of the book: "))
#               add_book(library, title, author, quantity)
#               print("Invalid input for quantity. Please enter an integer.")
#             except ValueError:
#                 print("invalid input for quantity.please enter an interger")
#           elif choice=='2':
#              view_books (library)
#           elif choice == '3':
#              title = input("Enter the book title: ")
#              borrower_name = input("Enter your name:")
#              borrow_book (library, title, borrower_name)

#           elif choice=='4':
#               title= input("Enter the book title:")
#               return_book(library, title)

#           elif choice==5:
#              print("Exiting the system Goodbye!")
#              break

#           else:
#              print("Invalid choice. Please enter a number between 1 and 5.")
# if __name__=="__main__":
#    main()

    







