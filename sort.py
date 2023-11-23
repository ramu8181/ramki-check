import big_o

list1 = [10,10,10,10]

def remove_item(i,list1):
    count = 0 
    for j in list1:
        if i == j:
            list1.remove(i)
            count = count + 1
    return list1,count
    
for i in list1:
    temp  = list1.count(i)
    #print ( str(i) + " In times in the list " + str(temp))
    list1,count = big_o.big_o(remove_item(i,list1))
    print ( str(i) + " In times in the list " + str(count))

    
