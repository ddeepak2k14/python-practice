__author__ = 'deepak.k'
def no_of_vowels(str):
    '''(str)->int
    return number of vowels in str
    no_of_vowels('abcde')
    2 '''
    count=0
    for i in str:
        if i in 'aeiouAEIOU':
            count=count+1
    return count
def print_vowels(str):
    ''' (str)->str
    return vowels in str
    print_vowels('deepakalok')
    eeaao
    '''
    vowels=''
    for i in str:
        if i in 'aeiouAEIOU':
            vowels=vowels+i

    return vowels

if __name__ == '__main__':
    print((no_of_vowels('deepakkumar')))
    print((print_vowels('deepakkumar')))
    
