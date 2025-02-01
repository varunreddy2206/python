# import os

# def menu():
#     print("Nsti book store")
#     print("1. Add a book:")
#     print("2. view book:")
#     print("3. search for the book:")
#     print("4. delete book:")
#     print("5.borrow book")

# def add_new_book(filename):
#         try:
#             with open(filename,"a") as file:
#                  title=input("enter the book title:")
#                  author=input("enter the author:")
#                  publication_year=input("enter publication year:")
#                  book=f'{title},{author},{publication_year}\n'
#                  file.write(book)
#                  print('book added successfully,')
#         except Exception as e:
#              print(f'an error occured:',{e})

# def view_inventory(filename):
#      try:
#           if os.path.exists(filename):
#                with open(filename,"r") as file:
#                     books=file.readlines()
#                     if books:
#                          print("inventory:")
#                          for book in books:
#                               try:
#                                    title,author,publication_year=book.strip().split(',')
#                                    print(f'Title:{title},Author:{author},Publication_year:{publication_year}')
#                               except ValueError as ve:
#                                    print(f'An error occured',{ve})
#                     if not books:
#                          print(" record found...")
#           else:
#                print("no record found...")
#      except Exception as e:
#           print(f'an error occured:',{e})

# def search_book(filename):
#     try:
#         if os.path.exists(filename):
#             search=input("enter the book name:")
#             with open(filename,"r") as file:
#                 books=file.readlines()
#                 found=False
#                 for book in book:
#                     title,author,publication_year=book.strip().split(',')
#                     if title==search:
#                         print("book found below:")
#                         print(f'found-Title:{title}')
#                         print(f'Author:{author}')
#                         print(f'Publication_year:{publication_year}')
#                         found=True
#                         break
#                 if not found:
#                     print("book not found")
#         else:
#             print("inventory file does not exists.")
#     except Exception as e:
#         print(f"an error occured: {e}")
        
# def del_book(filename):
#     try:
#         if os.path.exists(filename):
#             title1=input("enter the title of book: ")
#             with open (filename,"r") as file:
#                 books=file.readlines()
#                 found=False
#                 with open(filename,"w") as file:
#                     for book in books:
#                         title,author,price=book.strip().split(',')
                        
#                         if title==title1:
#                             print(f"deleted -{title},{author},{price}")
#                             found=True
#                         else:
#                             file.write(book)
#                         if not found:
#                             print("book not found.")
#                         else:
#                             print("inventory file does not exist.")
#     except Exception as e:
#         print(f"an error occured {e}")

# def borrow_book(filename):
#      try:
#           if os.path.exists(filename):
#                title1=input('enter thew book name: ')
#                with open(filename,"r") as file:
#                     books=file.readlines()
#                with open(filename,'w') as file:
#                     found=False
#                     # if books:
#                     #      print("inventory:")
#                     for book in books:
#                               try:
#                                    title,author,publication_year=book.strip().split(',')
#                                    if title==title:
#                                         print(f"borrow-{title},{author},{publication_year}")
#                                         found==True
#                                    else:
#                                         file.write(book)
#                                    print(f'Title:{title},Author:{author},Publication_year:{publication_year}')
#                               except ValueError as ve:
#                                    print(f'An error occured',{ve})
#                     if not books:
#                          print("no record found...")
#           else:
#                print("no record found...")
#      except Exception as e:
#           print(f'an error occured:',{e})

        

# def main():
#     filename="xyz.txt"
#     while True:
#         menu()
#         choice=input("enter you choice : ")
#         if choice == "1":
#             add_new_book(filename)
#         elif choice== "2":
#             view_inventory(filename)
#             print("existing the code: ")
#         elif choice== "3":
#             search_book(filename)
#         elif choice=="4":
#             del_book(filename)
#         elif choice=="5":
#             borrow_book(filename)
#             print("exiting the code:")
#             break
#         else:
#             print("invalid choice .")

# if __name__=="__main__":
#      main()

                    
       

