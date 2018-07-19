def Orderedlist(list):
    for i in range(0,len(list)-1):
        if list[i] > list[i+1]:
            return False
    return  True        


lst=[0,1,2,3,4,5]
println=Orderedlist(lst)
print(println)