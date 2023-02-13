# Write a program that counts up the number of vowels [a, e, i, o,
# u] contained in the string.

string = input("Please enter string contain vowels: ")
count=0
vowels="aeiou"
for l in string:
  if l in vowels :
    count +=1
print(f'your input is {string} contain {count} vowle')    





