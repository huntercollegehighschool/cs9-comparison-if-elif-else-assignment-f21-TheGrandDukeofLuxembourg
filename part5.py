'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below
month=str(input("Enter a month: "))
list31=["January", "March", "May", "July", "August", "October", "December"]
list30=["September","April","June","November"]
if (month in list31):
  print("31")
elif(month in list30):
  print("30")
elif(month=="February"):
  print("28 or 29")
else:
  print("Not a month.")
#nJanuary, March, May, July, August, October, and December.