import random

def check(list,check_arr,rand):
    for i in range(len(check_arr)):
        if list[rand][check_arr[i]] != 0:
            return True
    return False
def table(m):
    big_arr = []
    arr = []
    r = [0]*m
    rand=-1
    for i in range(m):
        if(rand>0 and rand<m):
            check_arr = [rand-1,rand,rand+1]
        elif(rand == 0):
            check_arr = [rand,rand+1]
        else:
            check_arr = [rand-1,rand]
        rand = random.randint(0,m-1)
        if(i!=0 and i!=m-2):

            while r[rand] != 0 or check(big_arr,check_arr,i-1):
                rand = random.randint(0,m-1)
        elif(i==m-2):
            check_arr = []
            for i in range(m):
                if(r[i] == 1):
                    check_arr.append(i)
            if(check_arr[1]-1 != check_arr[0] and check_arr[1]+1 != check_arr[2]):
                continue
            else:
                rand = check_arr[1]

        r[rand] +=1
        for j in range(m):

            if(j == rand):
                arr.append(1)
            else:
                arr.append(0)

        big_arr.append(arr)
        arr = []
    return big_arr

print(table(9))