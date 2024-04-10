# # Challenge

# def multiply(times):
#     for n in range (1, 11):
#         print(f"{times} x {n} = {n*times}")

# multiply(7)
#################################################
# Encrypted word
# import string
# alphabet = string.ascii_lowercase
# word = input("Please type a word: ").lower()
# Encrypted_word = ""

# for letter in word:
#     if letter in alphabet:
#        original_position = alphabet.index(letter)

#        new_position = (original_position + 2)%26
#        Encrypted_word += alphabet[new_position]
#     else:
#         Encrypted_word += letter
    
    # if original_position == alphabet.index("y"):
    #     new_position = alphabet.index("a")
    
    # elif original_position == alphabet.index("z"):
    #     new_position = alphabet.index("b")
    #     Encrypted_word += alphabet[new_position]
        
    
    # else:
    #    new_position = original_position + 2
    #    Encrypted_word += alphabet[new_position]
    
# print(Encrypted_word)

##################################################
# import string
# alphabet = string.ascii_lowercase

# message = input("Enter a message: ")
# shiftnumber =int (input("Enter a shift number: "))

# def encryptcode(sentence, shift):
#     encrypted_message = ""
#     for letter in sentence:
#         if letter.lower() in alphabet:
#            original_position = alphabet.index(letter.lower())
#            new_position = (original_position + shift)%26
#            encrypted_letter = alphabet[new_position]
#            if letter.isupper():
#                encrypted_letter = encrypted_letter.upper()
#            encrypted_message += encrypted_letter
#         else:
#             encrypted_message += letter
#     print(encrypted_message)

# encryptcode(message, shiftnumber)

###########################################
# decoding
# import string
# alphabet = string.ascii_lowercase

# message = input("Enter a message: ")
# shiftnumber =int (input("Enter a shift number: "))

# def encryptcode(sentence, shift):
#     original_message = ""
#     for letter in sentence:
#         if letter.lower() in alphabet:
#            encrypted_position = alphabet.index(letter.lower())
#            new_position = (encrypted_position - shift)%26
#            original_letter = alphabet[new_position]
#            if letter.isupper():
#                original_letter = original_letter.upper()
#            original_message += original_letter
#         else:
#             original_message += letter
#     print("Here is the original_message:", original_message)

# encryptcode(message, shiftnumber)

#####################################
# brothers= {
#     1: "Sameh",
#     2: "Sarah",
#     3: "Mahmoud", 
#     4: "Ibrahim", 

# }
# for n in brothers:
#     print(f"Brother: \n{n}\n{brothers[n] }.\n------------------------")
    
######################
# info = {}
# info["Name"] = input("What is your name? ")
# info["Age"] = int(input("How old are you? "))
# info["Country"] = input("Where do you come from? ")
# print(info)
#######################

# contact = {}
# while True:
#     print(""" 
# Contact Management
      

# 1- Add a contact
# 2- View contact
# 3- Edit contact
# 4- Exit""")
#     process = int(input("Please choose a number from 1 to 4:  "))
    
#     if process == 1:
#         ID = input("Please enter an ID number : ")
#         name = input("Please enter the name : ")
#         phone = input("Please enter a phone number : ")
#         contact[ID] = {"Name": name, "phone number": phone }
#         print(contact[ID]["phone number"])
#         while True:
#             if contact[ID]["phone number"].isdigit():
#                 print ("-------Great-------")
#                 break
#             else:
#                 print("The phone number is not digit, type a digit if you wanna continue")
#                 continue
        
#     elif process == 2:
#         print(contact)
        
        
#     elif process == 3:
#         id_to_edit = input("Enter the ID number to edit: ")
#         if id_to_edit in contact:  
#             new_name = input("Please enter a new name : ")
#             new_phone = input("Please enter a new phone number : ")
#             contact[id_to_edit] = {"Name": new_name, "Phone number": new_phone }  
#             while True:   
#                 if contact[ID]["phone number"].isdigit():
#                     print ("------Great------ ")
#                     break
                
#                 else:
#                     print("The phone number is not digit")
#                     continue
#         else:
#             print("\nThe typed ID number is not found\n ")    
        
#     elif process == 4:
#         print("Exit loading......")
#         break

#     else:
#         print("Wrong choice please enter right number from 1 to 4\n-----------------------------")
        
#####################################
# import os
# import random
# rand_number = random.randint(1, 11)
# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")
# while True:
#     clear_screen()
#     guessed_number = int(input("Guess the number between 1 and 10: "))
#     if guessed_number == rand_number:
#         print("Congratulations! You guessed the correct number.")
#         break
#     else:
        
#         print("Wrong guess. Try again")
#         print(input("Press any key to continue...."))

#############################
# import os
# def clear_screen():
#     os.system("cls" if os.name=="nt" else "clear")
# Liberary = {}
# while True:
#     print("""
#       Menu
#           1. Add Book
#           2. Check Out Book
#           3. Check In Book
#           4. List Books
#           5. Exit
#           """)
#     choice = int(input("Enter your choice (1- 5): "))
#     print(choice)
#     if choice == 1:
#         while True:
#             clear_screen()
#             isbn = input("Enter ISBN: ")
#             title = input("Enter title: ")
#             author = input("Enter Author: ")
#             Liberary[isbn] = {"Title": title, "Author": author, "Available": True}
#             print(Liberary)

#             print(f"Book'{title}' by {author} added to the catalog with ISBN {isbn}")
#             another_book = input("Do you wannna add another book? (Y/N): ").lower()
#             if another_book == "y" :
#                 continue
#             elif another_book == "n":
#                 break
#             else:
#                 again = (input(" Please type 'Y' or 'N'")).lower()
#                 if again == "y":
#                     continue
#                 else:
    
#                     break 
         
#     elif choice == 2:
         
#          while True:
#             clear_screen()
#             isbn = input("Enter ISBN to check out ")
#             title = Liberary[isbn]["Title"]
#             author = Liberary[isbn]["Author"]
#             Liberary[isbn]["Available"] = False
            
            
            
            
#             if  isbn in Liberary:
#                 print(f"Book '{title}' checked out successfully")
#                 checkedout_book = input("Do you wannna check out another book? (Y/N): ").lower()
#                 if checkedout_book == "y"  :        
#                     continue
#                 elif checkedout_book == "n" :
#                     break
#                 else:
#                     again = (input(" Please type 'Y' or 'N'")).lower()
#                     if again == "y":
#                         continue
#                     else:
#                         break
#             else:
#                 print("This book is not found")
#                 continue
#     elif choice == 3:
#          while True:
#             clear_screen()
#             isbn = input("Enter ISBN to check in ")
#             title = Liberary[isbn]["Title"]
#             author = Liberary[isbn]["Author"]
#             Liberary[isbn]["Available"] = True
            
            
#             if  isbn in Liberary:
#                 print(f"Book '{title}' checked in successfully")
#                 checkedin_book = input("Do you wannna check in another book? (Y/N): ").lower()
#                 if checkedin_book == "y"  :
#                     continue
#                 elif checkedin_book == "n" :
#                     break
#                 else:
#                     again = (input(" Please type 'Y' or 'N'")).lower()
#                     if again == "y":
#                         continue
#                     else:
#                         break
#             else:
#                 print("This book is already available in the liberary")
#                 continue

#     elif choice == 4:
        
#         print("Liberary Catalog:")
#         for isbn in Liberary:
#             print(f"""

# ISBN: {isbn}, Title: {Liberary[isbn]["Title"]}, Author: {Liberary[isbn]["Author"]}, Available: {Liberary[isbn]["Available"]}
#         """)
#         back_menu = input("Do you wanna back to the main menu? (Y/N)").lower()
#         if back_menu == "y" :
#                 continue
#         elif back_menu == "n":
#                 break
#         else:
#             again = (input(" Please type 'Y' or 'N'")).lower()
#             if again == "y":
#                 continue
#             else:
#                 break
#     elif choice == 5:
#          clear_screen()
#          break
#     else:
#          print("Wrong choice. Write the correct choice between ( 1-5 )")
#          continue 

############################################################################
# import os
# def clear_screen():
#     os.system("cls" if os.name=="nt" else "clear")

# def budget(number_items, price_per_item ):
#     """
#     you have to input two variables (number of items = any, price of item = any)
#     """
#     return number_items*price_per_item

# while True:
#     clear_screen()
#     spending_budget = float(input("Enter your spending budget: "))

#     wanted_item = input("Enter the item you want to buy: ")
#     number_items = int(input(f"How many {wanted_item}s do you want to buy "))

#     price_per_item = float(input(f"Enter the price per {wanted_item}: "))   

#     if budget(number_items, price_per_item) >= spending_budget:
#         print("Warning: Your purchase exceeds your daily budget!")
        
#     else:
#         print("Purchase successful! Enjoy your new item.")
#     repeat = input("Do you want to continue? y/n ").lower()
#     if repeat != "y":
#         break

#####################################################################
# import time
# def tax_calculator(total_salary):
#     return 0.15*(total_salary)

# def net_salary(salary, bonus):
#     time.sleep(3)
#     print("Calculating your total salary .... please wait")
#     time.sleep(2)
#     print("Finding the tax amount in Egypt .... please wait")
#     time.sleep(3)
#     print("Calculating your final salary .... please wait")
#     return print(f"final salaryafter tax: {((salary+bonus) - tax_calculator(total_salary=bonus+salary))}")

# net_salary(float(input("enter your base salary: ")), float(input("How much bonus did you get? ")))

################################################################
# import time
# def add_email(name, email):
#     time.sleep(2)
#     print("Checking user name .... ")
#     time.sleep(3)
#     print("Validating email address .......")
#     time.sleep(5)
#     if checking_email(email):
        
#         return print(f"User'{name}' with email '{email} successfully added'")
#     else:
#         return print("Email is not Valid. Registeration failed")


# def checking_email(email):
#     if "." and "@" in email:
#         return True
        
#     else:
#         return False

# add_email(input("Enter a user name: "), input("Enter your Email: "))

########################################################################  
# import os
# import time
# exchange_rate = {
#         "USD" : 1,
#         "EURO" : 0.85,
#         "EGP" : 30.9,
#         "RMB" : 6.5
#         }
# def exchange_loop():
#      print("""
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠤⠶⠚⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣴⠖⠚⠋⠉⠀⠀⠀⠀⣀⣀⣤⡽⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠉⠛⠲⣶⠶⢲⣞⢻⡯⢉⠕⢋⣴⣾⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠇⠀⠀⠀⣿⣴⣟⣵⣿⡼⠵⠶⠿⠾⠟⠧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⣠⡴⠞⠛⠉⠁⠀⠀⠀⠀⠙⢿⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠤⣄⡀⠀⠀⠀⠀
# ⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⡀⠀
# ⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⣿⠂
# ⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⣀⣤⣴⢶⡟⣻⠍⣩⠟⠉⢻⡇
# ⢸⡇⠀⠀⠀⠀⠀⣠⠖⢺⡆⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣯⢎⣴⢏⣴⡵⠋⢁⡴⠋⣸⣧
# ⠸⣷⠀⠀⠀⠀⢰⡟⠀⢸⡇⠀⠀⠀⣿⠛⠷⣦⣄⠀⠀⠀⠀⢸⣧⡞⣱⡿⠋⢀⡴⠋⣠⠞⢉⣿
# ⠀⢿⡄⠀⠀⠀⢸⣧⠀⢸⡇⠀⠀⠀⣿⣛⣧⠞⢛⣳⣄⠀⠀⢸⣿⡾⠋⢀⡴⠋⣠⠞⠁⡰⢋⣿
# ⠀⠘⣷⡀⠀⠀⠀⠻⣦⣸⡇⠀⠀⠀⣿⣁⣤⠾⢛⣡⠙⣷⣄⢸⡟⣁⠔⠁⣠⠞⣁⣠⣮⡤⠞⠁
# ⠀⠀⠘⣷⡀⠀⠀⠀⠈⠻⠇⠀⠀⠀⣿⣭⣴⢾⣻⠽⣒⣭⣿⣿⣯⣥⣶⠚⠋⠉⠉⠁⠀⠀⠀⠀
# ⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣗⣚⣭⢶⣿⡿⠟⢋⣹⡿⠟⢉⢷⣄⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣯⡶⠛⠉⣠⡴⠟⠁⣀⠔⣡⠟⢉⣳⣄⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡚⠉⢀⡤⠊⣡⠞⣡⡴⠟⠁⠈⣳⣄⠀⠀⠀
# ⠀⠀⠀⠀⢀⣀⣤⡾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣾⣁⣠⠞⣡⡾⠋⠀⢀⣠⠞⠁⠈⢳⡀⠀
# ⠀⣠⣶⣿⣿⠿⣋⣴⣿⡽⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡅⢶⠋⠀⢀⡴⠟⣁⡤⠖⠚⢉⣷⠀
# ⢠⣿⠘⣿⣵⣾⡿⠟⣩⡾⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣠⠞⢋⠴⠊⠁⣀⡴⠞⠉⢸⡇
# ⠸⣿⠀⠸⣿⣉⡴⠟⣁⠴⠚⣿⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠹⣧⠞⠁⣀⡴⠞⠁⠀⢀⣠⡼⡇
# ⠀⣿⡀⠀⠹⣯⡴⢊⣥⠶⢛⣿⠆⠀⢸⡟⢷⣄⠀⠀⠀⠀⠀⠀⢻⣷⠞⠉⠀⣀⣤⠶⠛⠉⢠⡇
# ⠀⢹⣇⠀⠀⠈⠻⣯⣠⡾⢛⡿⠀⠀⢸⣷⠀⢿⣆⠀⠀⠀⠀⠀⠈⣿⡶⠶⠛⢉⣀⡤⠖⠚⢹⡇
# ⠀⠀⠻⣆⠀⠀⠀⠈⠙⠛⠋⠀⠀⠀⠘⣿⢀⣼⣿⠆⠀⠀⠀⠀⠀⣿⡤⠖⠚⠉⢀⣀⣤⢀⡿⠀
# ⠀⠀⠀⠉⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠿⠋⠀⠀⠀⠀⠀⠀⣿⠤⠶⠚⣋⣉⣤⣄⣾⠃⠀
# ⠀⠀⠀⠀⠀⠈⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡷⠶⠛⣛⣉⣭⣠⡾⠁⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠛⠛⠋⣉⣭⡿⠋⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⣴⣿⡴⠶⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⢰⣿⢿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣼⡯⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        
       
#      for n in exchange_rate:
#          print(f"{n} = {exchange_rate[n]}")

# def clearscreen(): 
#     os.system("cls" if os.name=="nt" else "clear")


        
# while True:
#       exchange_loop()
#       currency_from = input("Choose a currency to convert from: ").upper()
#       amount= int(input("Enter the amount: "))
#       to_confirm = input(f"You entered {amount} {currency_from}. Confirm? (Y,N)").lower()
#       if to_confirm == "n":
#             continue
#       else:
#             clearscreen()
#             exchange_loop()
#             currency_to = input("Choose a currency to convert to: ").upper()
#             time.sleep(3)
#             print("Analyzing your request... Please wait")
#             time.sleep(2)
#             print("Checking for the USD's best rates available... Please wait")
#             time.sleep(2)
#             print(f"Getting a discount price for {currency_from} ... Please wait")
#             clearscreen()
#             print(f"Preparing the deal from {currency_from} to {currency_to}..... Please wait")
#             if (currency_from or currency_to) in exchange_rate:
#                   print(f"Exchange rate: {currency_from} = {exchange_rate[currency_to]/exchange_rate[currency_from]} {currency_to}")
#                   print(f"{amount} {currency_from} is equal to {round(amount*exchange_rate[currency_to]/exchange_rate[currency_from])} {currency_to}")
#                   to_accept = input("Do you accept this transaction (Y/N)").lower()
#                   if to_accept == "n":
#                         print("Transaction cancelled")
#                         another_ = input("Do you wanna perform another conversion? (Y/N) ")
#                         if another_ == "y":
#                               clearscreen()
#                               print("Thanks for coming")
#                         else:
#                               break
#                   else: 
#                         print("Thanks for coming")
#             else:
#                   print("Invalid currency. Conversion cancelled")
#                   another_ = input("Do you wanna perform another conversion? (Y/N) ")
#                   if another_ == "y":
#                      clearscreen()
#################################################################
import time
import random
from ascii import logo # type: ignore
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
# define a function to return card 
def dealing_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card
# return it's a black jack
def calculate_score(cards ):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    return sum(cards)
# function to compare scores
def comprare(computer_score, user_score):
    if user_score > 21 and computer_score > 21:
        return "You lose"
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You win"
    elif computer_score == 0:
        return "You lose"
    elif computer_score >21:
        return "You lose"
    elif computer_score >21:
        return "You win"
    elif user_score > computer_score:
        return "You lose"
    else:
        return "You lose"
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range (2):
        user_cards.append(dealing_cards())
        computer_cards.append(dealing_cards())
        


    

