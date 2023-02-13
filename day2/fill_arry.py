# Fill an array of 5 elements from the user, Sort it in descending
# and ascending orders then display the output

def fill_arry():
    arry=[]
    num=0
    while num < 5:
        arry.append(int(input(f"please Enter Number {num+1} :")))
        num+=1
    ascending = sorted(arry)
    desinding = sorted(arry , reverse=True)

    return (ascending , desinding)



print(fill_arry())