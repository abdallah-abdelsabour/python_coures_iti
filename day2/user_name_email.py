# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email
# or not

def is_name_correct():

    while True:
       user_name= input("enter your name :")
       if not user_name:
           print("username cant be empty please try again ")
           continue
       elif user_name.isnumeric():
            print("username cant be number please try again ")
            continue
       else:
            print(f"welcome {user_name}")
            user_email= is_email_coorect(user_name)
            print(f"welcome {user_name} you email correct and it {user_email}")
            break


def is_email_coorect(user_name):

    while True:
      email = input(f"enter your Email  {user_name}: ")
      if email and "@" in email and "." in email :
         return email
      else:
        print("wrong email formate please try again")





is_name_correct()


