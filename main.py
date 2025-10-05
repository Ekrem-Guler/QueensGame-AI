import random


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
    for j in range(len(table_arr[i])):
        if(table_arr[i][j] == 0):
            try:
                table_arr[i][j] = table_arr[i][j-1]
            except IndexError:
                table_arr[i][j] = table_arr[i][j+1]
print(table_arr)


player_game = []
for i in range(game_size):
    arr = [0]*game_size
    player_game.append(arr)
print(player_game)


def win_or_not(choice_x,choice_y):
        if(player_game[choice_x][choice_y] != 0):
            return False
        for i in range(game_size):
            if(player_game[i][choice_y]>9):
                return False
            elif(player_game[choice_x][i]>9):
                return False
        color = table_arr[choice_x][choice_y]-10
        for i in range(len(colors_loc[color])):
            x_loc = colors_loc[color][i][0]
            y_loc = colors_loc[color][i][1]
            if(player_game[x_loc][y_loc]>9):
                return False
        sides = [(choice_x + 1, choice_y + 1), (choice_x + 1, choice_y - 1), (choice_x - 1, choice_y + 1),
                 (choice_x - 1, choice_y - 1)]
        sides = [choice_x+1, choice_y+1, choice_x-1, choice_y-1]

        if(choice_x == game_size-1):
            sides.remove(sides[0])
        if(choice_y == game_size-1):
            sides.remove(sides[1])
        if(choice_x == 0):
            sides.remove(sides[2])
        if(choice_y == 0):
            sides.remove(sides[3])
        crosses = []
        for i in range(len(sides)):
            for j in range(i,len(sides)//2):
                if(player_game[sides[i]][sides[j]] > 9):
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
            game_over+=1
            if(game_over==9):
                break
        else:
            player_game[x_coordinate][y_coordinate] = -1

        print(player_game)


game()
print("Game Over")