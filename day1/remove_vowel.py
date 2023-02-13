# Write a program that remove all vowels from the input word and
# generate a brief version of it

count=0
vowels="aeiou"
string =input("Enter string contain vowels: ")

for l in string :
  if l in vowels :
    string=string.replace(l,"")
    count +=1

print(f''' {count} vowel removed
string after remove vowel "{string or "no thing left" }"
 ''')    