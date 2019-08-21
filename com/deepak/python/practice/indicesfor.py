__author__ = 'deepak.k'
# counting no of adjacent pair of repeating character 
def adjacent_pair_count(s):
    '''(str)-> int
    return no of adjacent pair occuring '''
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count=count+1
    return count
# shift each element to left and first element to last index
''' left_shift([2,3,4,2,2]) '''
def left_shift(L):
    first=L[0]
    for i in range(1,len(L)):
        L[i-1]=L[i]

    L[-1]=first
    return L

if __name__ == '__main__':
    print(adjacent_pair_count('23422'))
    print(left_shift([2,3,4,2,2]))   
