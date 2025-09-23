import random

# def table(m):
#     arr = [i for i in range(0,m)]
#     table_arr = []
#     for i in range(m):
#         table_arr.append(arr)
#     return table_arr
#

def in_a_row(m,number):
    if(number==0):
        return[1]
    elif(number==m):
        return[m-1]
    else:
        return[number-1,number+1]

# def main(table_arr):
#     table_arr_copy = table_arr
#     all_arr = []
#     m = len(table_arr)
#     for i in range(0,len(table_arr)):
#         game_arr = []
#         game_arr.append(i)
#         last_choice = i
#         j=0
#         while j!=m+1:
#
#             if table_arr[i][j] not in game_arr or table_arr[i][j] not in in_a_row(m,last_choice):
#                 game_arr.append(table_arr[i][j])
#                 last_choice = table_arr[i][j]
#                 j=0
#             j+=1
#             if(len(game_arr)!=m and j==9):
#                 break
#         if(len(game_arr)==m):
#             all_arr.append(game_arr)

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

game_arr = trying(9)
while(len(game_arr) !=9):
    game_arr = trying(9)
print(game_arr)
