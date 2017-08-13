def switch_sort(list=[]):
    if list is None:
        return
    for i in range(list.__len__()):
        min = list[i]
        k=0
        for j in range(i+1,list.__len__()):
            if list[j] < min:
                min = list[j]
                k = j
        if k == 0:
            pass
        else:
            list[i] = list[i] ^ list[k]
            list[k] = list[k] ^ list[i]
            list[i] = list[i] ^ list[k]
    print(list)
list = [1,9,1,2,3,4,5,10]
switch_sort(list)