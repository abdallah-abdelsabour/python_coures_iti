
def longet_sub(string):
    current=[]
    longest=[]
    for i in range(len(string)):
        if i==0:
            current=[string[i]]
        else:
            if string[i] > string[i-1]:
                current+=string[i]
            else:
                current=string[i]
        if len(current) > len(longest)   :
            longest = current
    return longest



print(longet_sub("abcdedflklmnop"))