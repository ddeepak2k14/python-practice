#parallel list and string
__author__ = 'deepak.k'
def sum_list(list1,list2):
    '''(list of number,list of number)->number
    return sum of two list
    sum_list([1,2,3,4],[1,2,3,4])
    [2,4,6,8]
    '''
    listsum=[]
    for i in range(len(list1)):
        listsum.append(list1[i]+list2[i])
     
    return listsum
def match_count(str1,str2):
    '''(str,str)->int
    return no of matching character at corresponding position
    match_count('abcd','abed')
    3 '''
    count=0
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            count=count+1
    return count
def avglistoflist(grade):
    '''(list of list of [str,number])->number'''
    total=0
    for i in grade:
        total=total+i[1]
    return total/2
