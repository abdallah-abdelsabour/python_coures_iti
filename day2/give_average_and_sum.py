# Write a program which repeatedly reads numbers until the user
# enters “done”.
# ○
# ○
# Once “done” is entered, print out the total, count, and
# average of the numbers.
# If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.
numbers = []

# get numbers from user
while True:
    num = input("Enter numper please :")
    if num =="done" :
        print("thank you ")
        break
    elif not num.isnumeric() :
     print("ERROR: please enter valid number ")
     continue
    else:
        numbers.append(num)

# count =
total=0
for i in numbers:
    total+=int(i)
# average
average =total /len(numbers)
count =len(numbers)

print(f'you numbers is {numbers}\n and the count {count}\nthe average={average} \ntotal ={total}')


