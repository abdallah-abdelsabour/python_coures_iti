

def multiblicationTable(num):
    arr=[]
    for i in range(1,num+1):
        subarr=[]
        for l in range(1,i+1):
            subarr.append(l*i)
        arr.append(subarr)


    return arr


print(multiblicationTable(5))

