# # file =open("vvv.txt","r")
# # content=file.read()
# # print(content)

# ########################################
# # with open("varun.txt","r") as file:
# #     content=file.read()
# #     print(content)

# #########################################

# # with open("varun.txt","r") as file :
# #     for line in file:
# #         print(line.strip())

# ########################################

# # with open("varun.txt","r") as file:
# #     file.readline(23)
# #     content=file.read(15)
# #     print(content)

# ##########################################

# # with open("varun.txt","w") as file:
# #     file.write("hello,my name is varun")

# ###########################################

# # with open("varun.txt","a") as file:
# #     file.write("\n this is another new line.")

# #############################################

# # with open("varun.txt","r") as file:
# #     # file.read(10)
# #     # file.read(5)
# #     file.seek(5)
# #     print(file.read())
# #     print(file.tell())

# #############################################

# # try:
# #     with open("varun.txt","r") as file:\
# #     print(file.read())
# # except FileNotFoundError:
# #     print("file is not available")
# # finally:
# #     print("code executed")

# ##################################################

# import os
# if os.path.exists("vvv.txt"):
#     os.remove("vvv.txt")
#     print("file is deleted")
# else:
#     print("file not found")


# import os

# def menu():
#     print("nsti book store")
#     print("1. add a book:")
#     print("2. view book:")
#     print("search for book :")
#     print("exit")

# #add a new book 

# def add_new_book(filename):
#     try:
#         with open(filename,"a") as file:
#             title=input("enter the book title: ")
#             author=input("enter the author: ")
#             price=input("enter the price: ")
#             book=f'{title},{author},{price}\n'
#             file.write(book)
#             print("book added succesfully,")
#     except Exception as e:
#         print(f'an error occured:',{e})

# def view_inventory(filename):
#     try:
#         if os.path.exists(filename):
#             with open(filename,"r") as file:
#                 books=file.readlines()
#                 if books:
#                     print("inventory:")
#                     for book in books:
#                         try:
#                             title,author,price=book.strip().split(',')
#                             print(f'Title:{title},Author: {author},price:{price}')
#                         except ValueError as ve:
#                             print(f'An error occured',{ve})
#             if not books:
#                 print("no record found...")
#         else:
#              print("no record found...")
#     except Exception as e:
#         print(f'an error occured:', {e})

# def search_book(filename):
#     try:
#         if os.path.exists(filename):
#             search=input("enter the book name:")
#             with open(filename,"r") as file:
#                 books=file.readlines()
#                 found=False
#                 for book in book:
#                     title,author,price=book.strip().split(',')
#                     if title==search:
#                         print("book found below:")
#                         print(f'found-Title:{title}')
#                         print(f'Author:{author}')
#                         print(f'Price:{price}')
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

# def main():
#     filename="123.txt"
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

#             print("exiting the code:")
#             break
#         else:
#             print("invalid choice .")

# if __name__=="__main__":
#     main()


    

    
