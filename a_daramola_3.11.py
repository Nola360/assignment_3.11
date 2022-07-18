#Akinola Daramola Jr
#Programming Exercise 3.11
#06/22/2022



"""

Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:
If a customer purchases 0 books, he or she earns 0 points.
If a customer purchases 2 books, he or she earns 5 points.
If a customer purchases 4 books, he or she earns 15 points.
If a customer purchases 6 books, he or she earns 30 points.
If a customer purchases 8 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.

"""

#Initializing variable
books_purchased = 0

#Declaring variable
books_purchased = int(input("Enter number of books purchased: "))

#Conditional Statement
if books_purchased >= 8:
    print(f"You've earned 60 points!")
elif books_purchased >= 6 and books_purchased <= 7:
    print(f"You've earned 30 points!")
elif books_purchased >= 4 and books_purchased <= 5:
    print(f"You've earned 15 points!")
elif books_purchased >= 2 and books_purchased <= 3:
    print(f"You've earned 5 points!")
elif books_purchased == 0:
    print(f"You've earned 0 points.")
else:
    print(f"You've purchased {books_purchased} book. Purchase more books to earn points.")
    
