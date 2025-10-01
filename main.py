import random
from random import choice

game_size = 6
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



game_arr = trying(game_size)
while(len(game_arr) !=game_size):
    game_arr = trying(game_size)
print(game_arr)


for i in range(game_size):
    arr = [0]*game_size

    arr[game_arr[i]] = i+10
    table_arr.append(arr)


def side(a,b,game_size,side_arr):
    arr = [(a,b-1),(a,b+1),(a-1,b),(a+1,b)]
    if(a == b+1):
        arr.remove((a-1,b))
    elif(a+1 == b):
        arr.remove((a,b-1))

    try:
        k = []
        for i in arr:
            if(-1 in i or game_size in i or table_arr[i[0]][i[1]]>0 or i in side_arr):
                k.append(i)
        for i in k:
            arr.remove(i)
    except ValueError:
        pass
    return arr

# for i in range(game_size):
#     focus = game_arr[i]
#     for j in range(game_size):
#         if(j!= focus):
#             tuple = (table_arr[j-1][i],table_arr[j][i])
#             random_tab = random.randint(0,1)
#             choice = tuple[random_tab]
#
#             if(choice not in side(j,i,game_size)):
#                  choice = tuple[random_tab-1]
#
#             table_arr[j][i] = choice
#
#         elif(j == 0):
#             tuple = (table_arr[j+1][i],table_arr[j][i])
#             random_tab = random.choice(tuple)
#             choice = tuple[random_tab]
#
#             if (choice not in side(j, i, game_size)):
#                 choice= tuple[random_tab-1]
#
#             table_arr[j][i] = choice
#
# color_arr= random_color(game_size,0,color_arr,game_size*game_size)
#
# for i in range(game_size):
#     j = 0
#     while (True):
#         j += 1
#         if (j == color_arr[i]):
#             break
#         else:
#             rand = random.choice(side(i,game_arr[i],game_size))
side_arr =[]
c_arr = []
for i in range(game_size):
    side_arr.append(side(i,game_arr[i],game_size,[]))
    c_arr.append((i,game_arr[i]))
print(side_arr)

m = 0
for i in range(game_size):
    print(c_arr)
    for j in range(game_size):
        m+=1
        if(m==30):
            break
        choice = random.randint(0,game_size-1)

        for k in side_arr[choice]:
            if(k in c_arr):
                side_arr[choice].remove(k)

        while(len(side_arr[choice])==0):
            choice = random.randint(0,game_size-1)

        colored= random.choice(side_arr[choice])
        c_arr.append(colored)
        table_arr[colored[0]][colored[1]] = choice+10
        side_arr[choice].remove(colored)

        colored_arr = side(colored[0], colored[1], game_size,c_arr)
        for k in colored_arr:
            if (k in side_arr[choice]):
                pass
            else:
                side_arr[choice].append(k)



if(game_arr[0] != 0):
    side_first = [(0,1),(1,0)]
    rand = random.choice(side_first)
    table_arr[0][0] = table_arr[rand[0]][rand[1]]


print(table_arr)