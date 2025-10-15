import random
import copy
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

# Find columns and rows are not same so, except color it is true for the game and it is an answer for the game.
def solution(m):
    # Here the first choice on the row is choosing randomly.
    arr = [i for i in range(0, m)]
    all_stages = []
    all_stages.append(arr)
    game_arr = []
    rand = random.choice(arr)
    last_choice = rand
    game_arr.append(rand)
    arr.remove(rand)

    # This part the rest of it choosing randomly and if it is not appropriate for the game it is trying again along the finding the solution.
    j=0
    while(len(arr)!=0):
        #

        rand = random.choice(arr)

        if rand not in in_a_row(m,last_choice) and rand not in game_arr:
            all_stages.append(arr)
            game_arr.append(rand)
            last_choice = rand
            arr.remove(rand)
            j=0

        elif(len(arr) < j+2):
            game_arr.remove(last_choice)
            if(len(game_arr)==0):
                break
            last_choice = game_arr[-1]
            arr = all_stages[-1]
            j=0
        j+=1
    return game_arr
############################################################################################

# Found the solution. game_arr include the solution which is obtained the all algorithm
game_arr = solution(game_size)
while(len(game_arr) !=game_size):
    game_arr = solution(game_size)
print(game_arr)
#############################################################################################

# There is a table_arr array which is included of right places of the game_arr's elements and I choose a color for them with numbers.
for i in range(game_size):
    arr = [0]*game_size
    arr[game_arr[i]] = i+10
    table_arr.append(arr)

#############################################################################################

# It is finding the left, right, up and down points of the given point.
def side(a,b,game_size,side_arr):
    arr = [(a,b-1),(a,b+1),(a-1,b),(a+1,b)]

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

side_arr =[]
c_arr = []
colors_loc = []

# colors_loc is needed for the store all colors rows and columns
# side_arr is storing the all sides of each color. When a color moving a different square it will append new sides.
# c_arr is store the history of chosen square for colors.

for i in range(game_size):
    colors_loc.append([])
    side_arr.append(side(i,game_arr[i],game_size,[]))
    c_arr.append((i,game_arr[i]))

m = 0
for i in range(game_size):
    for j in range(game_size):
        for k in range(len(side_arr)):
            for l in side_arr[k]:
                if (l in c_arr):
                    side_arr[k].remove(l)
        choice = random.randint(0,game_size-1)



        m = 0
        null = False
        while(len(side_arr[choice])==0):
            m+=1
            choice = random.randint(0,game_size-1)

            if(m==game_size+10):

                for k in range(len(side_arr)):
                    if(len(side_arr[k]) != 0):
                        choice=k

                        if(len(side_arr[choice])==0):
                            continue
                        else:
                            break

                    else:
                        null = True
                if(null):
                    break
        if(null):
            break


        colored= random.choice(side_arr[choice])
        c_arr.append(colored)
        table_arr[colored[0]][colored[1]] = choice+10
        colors_loc[choice].append((colored[0],colored[1]))

        side_arr[choice].remove(colored)

        colored_arr = side(colored[0], colored[1], game_size,c_arr)
        for k in colored_arr:
            if (k in side_arr[choice] or k in c_arr):
                pass
            else:
                side_arr[choice].append(k)

# A set to keep track of elements that have been seen



for i in range(len(table_arr)):
    print(table_arr[i])


player_game = []
player_hint_game= []
columns_empty = []
colors_empty = []
for i in range(game_size):
    arr = [0]*game_size
    columns_empty.append(game_size)
    player_hint_game.append(arr)
    player_game.append(arr)
    colors_empty.append(len(colors_loc[i]))
rows_empty = columns_empty
print(colors_empty)
print(player_game)
dup = player_game


def win_or_not(choice_x,choice_y,table_arr,player_game):
        if(player_game[choice_x][choice_y] != 0):
            return False
        # for i in range(game_size):
        #     if(player_game[i][choice_y]==-1):
        #         return False
        #     elif(player_game[choice_x][i]==-1):
        #         return False
        color = table_arr[choice_x][choice_y]-10
        for i in range(len(colors_loc[color])):
            print(colors_loc[color][i])
            x_loc = colors_loc[color][i][0]
            y_loc = colors_loc[color][i][1]

            if(player_game[x_loc][y_loc]==1001):
                return False
        return True

def game():
    while(True):
        player_choice = 0
        game_over = 0
        says_empty =  int(input(f"if you mark cross write 0 if you mark a queen write 1: "))
        while(says_empty!=0 and says_empty!=1):
            says_empty = int(input("Please choose valid number. if you mark cross write 0 if you mark a queen write 1: "))

        x_coordinate = int(input(f"Choose a x coordinate 0-{game_size-1}: "))
        y_coordinate = int(input(f"Choose a y coordinate 0-{game_size-1}: "))

        while (says_empty == 1 and win_or_not(x_coordinate, y_coordinate) == False):
            says_empty = int(input(f"if you mark cross write 0 if you mark a queen write 1: "))
            x_coordinate = int(input(f"Please choose valid number. Choose a x coordinate 0-{game_size - 1}: "))
            y_coordinate = int(input(f"Please choose valid number. Please choose a y coordinate 0-{game_size - 1}: "))

        if(says_empty==1):
            player_choice = int(input(f"Color 0-{game_size-1}: "))

            while(player_choice >game_size-1 or player_choice <0):
                player_choice = int(input(f"Please choose valid number. Color 0-{game_size-1}: "))
        while(x_coordinate >game_size-1 or y_coordinate >game_size-1 or x_coordinate <0 or y_coordinate <0):
            x_coordinate = int(input(f"Please choose valid number. Choose a x coordinate 0-{game_size-1}: "))
            y_coordinate = int(input(f"Please choose valid number. Please choose a y coordinate 0-{game_size-1}: "))


        if(says_empty==1):
            player_game[x_coordinate][y_coordinate] = player_choice+10
            # player_hint_game[x_coordinate][y_coordinate] = player_choice+10
            game_over+=1
            # color = table_arr[x_coordinate][y_coordinate]-10
            # sum_of_crosses = 0
            # for j in range(len(colors_loc[color])):
            #     if(colors_loc[color][j][0] != x_coordinate and colors_loc[color][j][1] != y_coordinate):
            #         player_hint_game[colors_loc[color][j][0]][colors_loc[color][j][1]] = -1
            #         sum_of_crosses += 1
            # for j in range(game_size):
            #     if (j != y_coordinate):
            #         player_hint_game[x_coordinate][j] = -1
            #         sum_of_crosses += 1
            #     if(j != x_coordinate):
            #         player_hint_game[j][y_coordinate] = -1
            #         sum_of_crosses += 1
            #
            if(game_over==9):
                break
        else:
            player_game[x_coordinate][y_coordinate] = -1
        # print(player_hint_game)
        print(player_game)


def sidess(i,rand):
    sides = [[i - 1, rand - 1], [i - 1, rand + 1], [i + 1, rand - 1], [i + 1, rand + 1]]
    sides_all=[]
    for k in sides:
        if((k[0]!=-1 and k[0]!=game_size)):
            if(k[1]!=-1 and k[1]!=game_size):
                sides_all.append(k)
    return sides_all

def ai_try2(player_game):
    all_number = list(range(game_size))
    all =[]
    game = []
    tried_rand = []
    tried_rand.append([])
    answer = []
    i=-1
    count = 1
    passed=0
    back = 0
    tried_rand = -1
    while(True):
        i+=1
        print(player_game)
        all.append(copy.deepcopy(all_number))
        game.append(copy.deepcopy(player_game))
        random.shuffle(all_number)
        randomm = random.randint(0,len(all_number)-1)
        rand = all_number[randomm]
        tried = []
        tried.append(rand)

        we_stop = False
        print(all_number)
        print(rand)
        print(f"i: {i}")
        while  win_or_not(i, rand,table_arr,player_game) == False:
            if rand not in tried:
                tried.append(rand)
            random.shuffle(all_number)
            randomm = random.randint(0,len(all_number)-1)
            rand = all_number[randomm]
            if len(tried) == len(all_number):
                we_stop = True
                break

        if(we_stop == False):
            passed+=1
            if(passed>=max(back,2)):
                count = 1
            for k in sidess(i,rand):
                if(player_game[k[0]][k[1]] != -1 and player_game[k[0]][k[1]] != 1001):
                    player_game[k[0]][k[1]] = -1
            for k in range(game_size):
                if((player_game[k][rand] != -1 and player_game[k][rand] != 1001)):
                    player_game[k][rand] = -1
                if(player_game[i][k] != -1 and player_game[i][k] != 1001):
                    player_game[i][k] = -1
            color = table_arr[i][rand]-10
            for k in range(len(colors_loc[color])):
                if((colors_loc[color][k][0],colors_loc[color][k][1])  != (i,rand) and (player_game[colors_loc[color][k][0]][colors_loc[color][k][1]] != 1001)):
                    player_game[colors_loc[color][k][0]][colors_loc[color][k][1]] = -1

            player_game[i][rand] = 1001
            answer.append((i,rand))
            all_number.remove(rand)

        else:
            passed=0
            print(f"COUNT:> {count}")
            if(count+len(all_number)>=game_size):
                count = game_size - len(all_number)
            for k in range(count):
                all.pop()
                all= all
                game.pop()
                game = game
                print(len(all))
                i-=1
                print(f"i_change: {i}")
                if(count == 1):
                    i-=1
            if(count>=2):
                i-=1

            all_number = all[-1]
            player_game = game[-1]
            all.pop()
            game.pop()
            count += 1
            back = count
        if(len(all_number) == 0):
            break
    print(player_game)
    return player_game


answer = []
players_game = ai_try2(player_game)
for i in range(len(players_game)):
    for j in range(len(players_game[i])):
        if(players_game[i][j] == 1001):

            answer.append(table_arr[i][j])
            print(table_arr[i][j])

seen = set()
# A list to store duplicates found in the input list
duplicates = []

# Iterate over each element in the list
for i in answer:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)
print("Game Over")