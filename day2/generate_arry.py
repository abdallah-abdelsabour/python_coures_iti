# Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# increased by one from start.
def generate_arry(start, length):
   new_arr=[]

   while length > 0:
       new_arr.append(start)
       start+=1
       length-=1

   return  new_arr
print(generate_arry(10,6))