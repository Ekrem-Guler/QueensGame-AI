import random

game_size = 9
table_arr = []
color_arr = []

def in_a_row(m,number):
    if(number==0):
        return[1]
    elif(number==m):
        return[m-1]
    else:
        return[number-1,number+1]

def trying(m):
    arr = [i for i in range(0, m)]
    all_stages = []
    all_stages.append(arr)
    game_arr = []
    rand = random.choice(arr)
    last_choice = rand
    game_arr.append(rand)
    arr.remove(rand)
    j=0
    while(len(arr)!=0):
        rand = random.choice(arr)
        if rand not in in_a_row(m,last_choice) and rand not in game_arr:
            all_stages.append(arr)
            game_arr.append(rand)
            last_choice = rand
            arr.remove(rand)
            j=0

        elif(len(arr) < j+2):
            game_arr.remove(last_choice)
            last_choice = game_arr[-1]
            arr = all_stages[-1]
            j=0
        j+=1
    return game_arr




def random_color(m,i,color_arr,k):
    a = random.randint(1,k//2)
    color_arr.append(a)

    if i!=m-2:
        i+=1

        random_color(m,i,color_arr,k-a)
    else:
        color_arr.append(k-a)
    return color_arr

def side_to_side(a,b,arr):

    arr.append((a,b+1))
    arr.append((a,b-1))
    arr.append((a+1,b))
    arr.append((a-1,b))
    return arr

game_arr = trying(game_size)
while(len(game_arr) !=game_size):
    game_arr = trying(game_size)
print(game_arr)


for i in range(0,game_size):
    arr = [0]*9
    arr[game_arr[i]] = 1
    table_arr.append(arr)


color_arr= random_color(9,0,color_arr,81)


for i in range(0,game_size):
    table_arr[game_arr[i]] = i+1
    arr = []
    arr = side_to_side(i, game_arr[i], arr)
    for j in range(color_arr[i]-1):
        choice = random.choice(arr)
        table_arr[choice[0]][choice[1]] = i+1



print(color_arr)
print(table_arr)