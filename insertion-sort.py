'''升序排列'''
def insertion_sort(list=[]):
    if list is None:
        return
    for i in range(list.__len__()-1):
        key = list[i+1]
        while i >= 0 and list[i] > key:
            list[i+1] = list[i]
            i -= 1
        list[i+1] = key
    print(list)
    '''将序排列'''
    # list = [31,30,20,41,59,70,26,41,58]
    # for i in range(list.__len__()-1):
    #     key = list[i+1]
    #     while i >= 0 and list[i] < key:
    #         list[i+1] = list[i]
    #         i -= 1
    #     list[i+1] = key
    # print(list)
list = [1,0,4,3,2,1]
insertion_sort(list)
