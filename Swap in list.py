def swaplist(list1,pos1,pos2):
    temp=list1[pos1]
    list1[pos1]=list1[pos2]
    list1[pos2]=temp
    return list1
list2=[18,27,16,20,32,9]
print(list2)
pos1,pos2=1,4
print(swaplist(list2,pos1-1,pos2-1))
