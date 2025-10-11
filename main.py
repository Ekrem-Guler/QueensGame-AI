import random
from itertools import product
import copy
game_size = 9
table_arr = []
color_arr = []
all = []

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
            if(len(game_arr)==0):
                break
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

side_arr =[]
c_arr = []
colors_loc = []

for i in range(game_size):
    colors_loc.append([])
    side_arr.append(side(i,game_arr[i],game_size,[]))
    c_arr.append((i,game_arr[i]))

m = 0
for i in range(game_size):
    for j in range(game_size):

        choice = random.randint(0,game_size-1)

        for k in side_arr[choice]:
            if(k in c_arr):
                side_arr[choice].remove(k)
        m = 0
        null = False
        while(len(side_arr[choice])==0):
            m+=1
            choice = random.randint(0,game_size-1)
            if(m==game_size+10):

                for k in range(len(side_arr)):
                    if(len(side_arr[k]) != 0):
                        choice=k
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





for i in range(len(table_arr)):
    all.append([])
    for j in range(len(table_arr[i])):
        if(table_arr[i][j] == 0):
            try:
                table_arr[i][j] = table_arr[i][j-1]
            except IndexError:
                table_arr[i][j] = table_arr[i][j+1]
        all[i].append([i,j,table_arr[i][j]-10])
print(table_arr)


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

def heuristic(heuristic_value,a,b,columns_empty,rows_empty):
    color = table_arr[a][b]-10
    color_value = 0
    for i in range(len(colors_loc[color])):
        if(colors_loc[color][i][0] != a and colors_loc[color][i][1] != b):
            color_value += 1
    heuristic_value -= columns_empty[b]+rows_empty[a]+color_value-1
    columns_empty[b] = 0
    rows_empty[a] = 0
    for i in range(game_size):
        columns_empty[i]-=1
        rows_empty[i] -= 1

def ai_try(player_game,rows_empty,columns_empty,colors_empty,all,colors_loc):
    last = []
    last_columns = []
    last_rows = []
    last_colors=[]
    tried = []
    last_tried = []
    i=-1
    c=0
    while(True):
        stop = False
        i+=1
        last.append(player_game)
        c +=1
        print(f"{c}  {last}")
        last_columns.append(columns_empty)
        last_rows.append(rows_empty)
        last_colors.append(colors_empty)
        rand = random.randint(0,game_size-1)

        while(player_game[i][rand] == -1 and rand in tried):
            rand = random.randint(0,game_size-1)
        color = table_arr[i][rand]-10
        player_game[i][rand] = 800
        for j in range(len(colors_loc[color])):
            if(colors_loc[color][j] != (i,rand)):
                player_game[colors_loc[color][j][0]][colors_loc[color][j][1]] = -1
            all[colors_loc[color][j][0]][colors_loc[color][j][1]] = -1
            columns_empty[colors_loc[color][j][1]] -= 1
            rows_empty[colors_loc[color][j][0]] -= 1
        colors_loc[color] = []
        for j in range(game_size):
            if (all[i][j] != -1):
                if(rand!= j):
                    player_game[i][j] = -1
                    all[i][j] = -1
                    columns_empty[j] -= 1
                    rows_empty[i] -=1
                if(i!=j):
                    player_game[j][rand] = -1
                    all[j][rand] = -1
                    rows_empty[rand] -= 1
                    columns_empty[i] -= 1
        sides = [(i-1,rand-1),(i-1,rand+1),(i+1,rand-1),(i+1,rand+1)]
        if(i==0 and rand == 0):
            sides = [(i+1,rand+1)]
        if(i==0 and rand == game_size-1):
            sides = [(i-1,rand+1)]
        if(i==game_size-1 and rand == 0):
            sides = [(i+1,rand-1)]
        if(i==game_size-1 and rand == game_size-1):
            sides = [(i-1,rand-1)]
        if(i==0 and rand != 0):
            sides.remove(sides[0])
            sides.remove(sides[1])
        if(i==game_size-1 and rand != 0):
            sides.remove(sides[2])
            sides.remove(sides[3])
        if(i!= 0 and rand == 0):
            sides.remove(sides[0])
            sides.remove(sides[2])
        if(i!= 0 and rand == game_size-1):
            sides.remove(sides[1])
            sides.remove(sides[3])
        for k in range(len(sides)):

            if(all[sides[k][0]][sides[k][1]] != -1 and all[sides[k][1]][sides[k][0]] != 800):
                player_game[sides[k][0]][sides[k][1]] = -1
                rows_empty[sides[k][0]] -=1
                columns_empty[sides[k][1]] -= 1

        for k in range(game_size):
            if((columns_empty[k] == 0 and k!= rand) or (rows_empty[k] == 0 and k!= i) or (colors_loc[k] == [] and k != color)):
                last_tried.append(tried)
                tried.append(rand)
                player_game = last[i]
                print("hi")
                columns_empty = last_columns[i]
                rows_empty = last_rows[i]
                colors_empty = last_colors[i]
                last.remove(last[i])
                last_columns.remove(last_columns[i])
                last_rows.remove(last_rows[i])
                last_colors.remove(last_colors[i])
                i-=1
                count = 0
                for k in range(game_size):
                    if(player_game[i+1][k] == 0):
                        count +=1
                if(count<len(tried)):
                    if(i==1):
                        pass
                    tried = last_tried[i]
                    last_tried.remove(last_tried[i])
                    player_game = last[i]
                    columns_empty = last_columns[i]
                    rows_empty = last_rows[i]
                    colors_empty = last_colors[i]
                    last.remove(last[i])
                    last_columns.remove(last_columns[i])
                    last_rows.remove(last_rows[i])
                    last_colors.remove(last_colors[i])
                    i-=1

                break

        if(i==game_size - 1):
            break
    return player_game
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
    i=-1
    count = 1
    passed=0
    while(True):
        i+=1
        print(player_game)
        all.append(copy.deepcopy(all_number))
        game.append(copy.deepcopy(player_game))
        rand = random.choice(all_number)
        tried = []
        tried.append(rand)
        we_stop = False
        print(all_number)
        print(rand)
        print(f"i: {i}")
        while not win_or_not(i, rand,table_arr,player_game):
            if rand not in tried:
                tried.append(rand)
            rand = random.choice(all_number)
            if len(tried) == len(all_number):
                we_stop = True
                break
        if(we_stop == False):
            passed+=1
            if(passed>=2):
                count = 1
            for k in sidess(i,rand):
                player_game[k[0]][k[1]] = -1
            for k in range(game_size):
                player_game[k][rand] = -1
                player_game[i][k] = -1

            player_game[i][rand] = 1001
            all_number.remove(rand)

        else:
            passed=0
            print(f"COUNT:> {count}")
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
                i-=count-1
            all_number = all[-1]
            player_game = game[-1]
            all.pop()
            game.pop()
            count += 1
        if(len(all_number) == 0):
            break
    print(player_game)

def ai_try3(player_game):
    all_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    all = []
    game = []
    i = 0
    count = 1
    while True:
        i += 1
        game.append(copy.deepcopy(player_game))
        all.append(copy.deepcopy(all_number))

        tried = []
        we_stop = False
        rand = random.choice(all_number)

        while not win_or_not(i, rand,table_arr):
            if rand not in tried:
                tried.append(rand)
            if len(tried) == len(all_number):
                we_stop = True
                break
            rand = random.choice(all_number)

        if not we_stop:
            for x, y in sidess(i, rand):
                player_game[x][y] = -1
            for k in range(game_size):
                player_game[k][rand] = -1
                player_game[i][k] = -1

            player_game[i][rand] = 1001
            all_number.remove(rand)

        else:
            if i > 1:
                i -= 1
                player_game = copy.deepcopy(game[i - 1])
                all_number = copy.deepcopy(all[i - 1])
                del game[i:]
                del all[i:]
            if len(all_number) < 3:
                if i > 1:
                    i -= 1
                    player_game = copy.deepcopy(game[i - 1])
                    all_number = copy.deepcopy(all[i - 1])
                    del game[i:]
                    del all[i:]

        if not all_number:
            break

print(player_game)

ai_try2(player_game)
def cost_function(value):
    return value+1
print("Game Over")