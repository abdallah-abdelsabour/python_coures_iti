# Write a program that prints the locations of "i" character in any
# string you added.

string=input("enter string to count i: ")


for l in range(len(string)):
  if string[l]=="i":
    print(f'i occured  in  {l+1} place "{string}"')

# print(location)
