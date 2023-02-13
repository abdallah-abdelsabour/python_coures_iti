# write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if is is divisible by both return "FizzBuzz"

def is_devidable_by_3(num):
    if num %3 ==0 and num %5 ==0 :
        return "fuzzBuzz"

    if num % 3 ==0  :
        return "fuzz"
    elif num % 5 ==0 :
        return "Buzz"


print(is_devidable_by_3(22))