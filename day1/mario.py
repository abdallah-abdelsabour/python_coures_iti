
num=int(input("enter heigh of pyramid you wana build: "))

for i in range(1,num+1):
  star=i
  space=num-i
  print(" " * space,end="")
  print("*" * star)