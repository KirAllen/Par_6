lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
num = int(input('Num: '))

def search(lst, num):
    a = 0
    if num == lst[len(lst)//2]:
        a = len(lst)//2
    elif num > lst[len(lst)//2]:
        for j in range(len(lst)//2):
            if num == lst[-j]:
                a = num
    elif num < lst[len(lst) // 2]:
        for g in range(len(lst)//2):
            if num == lst[g]:
                a = num
    if a != 0:
        return lst.index(a)
    else:
        return -1

print(f'Index: {search(lst, num)}')




