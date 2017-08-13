def insertion_sort(list=[]):
    if list is None:
        return
    for i in range(list.__len__()-1):
        key = list[i+1]
        while i >= 0 and list[i] > key:
            list[i+1] = list[i]
            i -= 1
        list[i+1] = key

def merge(list=[],start=0,middle=0,end=0):
    if list is None:
        return
    list1=[]
    list2=[]
    if len(list) % 2 == 0:
        for i in range(start,middle):
            list1.append(list[i])
    else:
        for i in range(start,middle+1):
            list1.append(list[i])
    insertion_sort(list1)
    # list1.append(65535)
    print(list1)
    # list1.sort()
    if len(list) %2 ==0 :
        for j in range(middle,end):
            list2.append(list[j])
    else:
        for j in range(middle+1,end):
            list2.append(list[j])
    insertion_sort(list2)
    # list2.append(65535)
    print(list2)
    # list2.sort()
    # i=0
    # j=0
    for k in range(start,end):
        if list1.__len__() == 0:
            for i in range(len(list2)):
                list[k] = list2.pop()
        if list2.__len__() == 0:
            for i in range(len(list1)):
                list[k] = list1.pop()
        if list1.__len__() != 0 and list2.__len__() != 0:
            if list1[0] <= list2[0]:
                list[k]=list1.pop(0)
                # i += 1
            else:
                list[k]=list2.pop(0)
'''归并排序算法'''
def merge_sort(list,start=0,end=0):
    # for i in range(start,end):
    #     print(list[i])
    if start < end:
        middle = (start + end) //2
        merge_sort(list,start,middle)
        merge_sort(list,middle+1,end)
        merge(list,start,middle,end)
list=[15,10,15,1,1,2,4,45,3,4,54,12,1,23,3,4,13]
merge_sort(list,0,len(list))
# merge(list,0,len(list)//2,len(list))
print(list)
