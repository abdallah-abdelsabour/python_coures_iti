# Write a function which has an input of a string from user then it
# will return the s
#
# a

def reverse_string(string):
        l= list(string)
        l.reverse()
        return "".join(l)


print(reverse_string("Abdallah"))