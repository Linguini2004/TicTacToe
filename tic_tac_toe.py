# tic tac toe
# this game will be player vs player and will be made up of a cycle where each player takes turns
import time
import random
grid = Actor("grid")
menu_back = Actor("menu_background")
button1 = Actor("1button", (150, 420))
button2 = Actor("2button", (350, 420))

crosses = []
noughts = []
check = []
check = ["","","","","","","","",""]
mode = "menu"

WIDTH = grid.width
HEIGHT = grid.height

turn = 0
counter = 0
num_cross = 5
num_nought = 4
cell_size = 166
size_across = 3
size_down = 3
grid_num = 0
counter1 = 0
cputurn = 1
first_play = "Player"
center_first = False
cpu_first = False
firstxox = True
firstxx = True
still_playing = True

def draw():
    global counter1
    screen.clear()
    if mode == "menu":
        menu_back.draw()
        button1.draw()
        button2.draw()
        screen.draw.textbox(
        "Tic Tac Toe\n select a game mode:",(50,20,400,100), background = None,
        color = "black", fontname = "dpcomic")

        screen.draw.textbox("Player vs Player",(100,445,100,50), background = None,
        fontname = "dpcomic")

        screen.draw.textbox("Player vs CPU",(300,445,100,50), background = None,
        fontname = "dpcomic")

    if mode == "playing_pvp":
        grid.draw()

        for cross in crosses:
            cross.draw()
        for nought in noughts:
            nought.draw()
    if mode == "playing_pvcpu":
        grid.draw()

        for cross in crosses:
            cross.draw()
        for nought in noughts:
            nought.draw()
        counter1 += 1

    if mode == "end":
        pass


def on_mouse_down(pos):
    global mode
    x, y = pos
    if mode == "playing_pvp":
        playing_pvp(pos)
    elif mode == "playing_pvcpu":
        playing_p(pos)
        clock.schedule(playing_cpu, 2.0)
    elif mode == "end":
        win_screen()


    if mode == "menu":
        if button1.left < x < button1.right and button1.top < y < button1.bottom:
            time.sleep(0.25)
            mode = "playing_pvp"
        if button2.left < x < button2.right and button2.top <   y < button2.bottom:
            time.sleep(0.25)
            mode = "playing_pvcpu"
            #print("sorry this feature is in development")



def playing_p(pos):
    global grid_num
    global turn
    global check
    turn += 1
    x, y = pos

    valx = (x // cell_size) + 1
    valy = (y // cell_size) + 1

    grid_num = ((valy - 1) * 3) + valx
    grid_num = grid_num - 1

    #Player
    #NB: x and y co-ordinates as tuple
    if check[grid_num] == "":
        destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
        cross = Actor("ximage1", (0, 0))
        animate(cross, pos=destination_pos)
        crosses.append(cross)
        check[grid_num] = "x"
        turn += 1
    else:
        print("sorry, cell occupied")
        turn -= 1

    if check_vict(check) == "xyes":
            print("player wins")
            mode = "end"

def playing_cpu():
    #CPU
    global cputurn
    global grid_num
    global check
    global center_first
    global firstxox
    global firstxx
    global still_playing
    random_num1 = 0
    random_num2 = 0
    num_list1 = [1, 3, 5, 7]
    num_list2 = [0, 2, 6, 8]
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    counter1 = 1
    counter2 = 0
    cpu_winning = False
    test = False

    if still_playing == True:

        if cputurn == 1:
            if check[4] == "":
                grid_num = 4
                center_first = True
            else:
                center_first = False
                while True:
                    random_num1 = random.randint(0, 8)
                    if random_num1 == 0 or random_num1 == 2 or random_num1 == 6 or random_num1 == 8:
                        if check[random_num1] == "":
                            grid_num = random_num1
                            break
            print(firstxx)
        if cputurn == 2:
            if cpu_first == True:
                while True:
                    random_num2 = random.randint(0, 8)
                    if random_num2 == 0 or random_num2 == 2 or random_num2 == 6 or random_num2 == 8:
                        if check[random_num2] == "":
                            grid_num = random_num2
                            break

            if cpu_first == False:
                if center_first == True:
                    for i in num_list1:
                        for j in num_list2:
                            if check[i] + check[j] == "xx":
                                if j > i:
                                    grid_num = i - (j - i)
                                if i > j:
                                    grid_num = (i - j) + i

                    for i in num_list2:
                        if counter1 == 1:
                            if check[i] == "x":
                                num1 = i
                                test = True
                        if counter1 == 2:
                            if check[i] == "x":
                                num2 = i
                                counter1 = 3
                                test = False
                        if test == True:
                            counter1 = 2
                    if counter1 == 3:
                        if (num2 - num1) == 6:
                            grid_num = num2 - 3
                        if (num2 - num1) == 2:
                            grid_num = num2 - 1
                        firstxox = False

                if center_first ==  False:
                    if firstxx == 1:
                        for i in range(0, 9):
                            if i != 4:
                                if check[i] + check[4] == "xx":
                                    if check[(4 - i) + 4] == "":
                                        grid_num = (4 - i) + 4
                                        num4 = i
                                        firstxx += 1
                                        #print("hi")
            print(firstxx)
        if cputurn == 3:
            for i in num_list1:
                for j in num_list2:
                    if check[i] + check[j] == "oo":
                        if j > i:
                            if j - i < 3 and j + i != 5 and j + i != 11:
                                grid_num = i - (j - i)
                                cpu_winning = True
                        if i > j:
                            if i - j < 3 and j + i != 5 and j + i != 11:
                                grid_num = (i - j) + i
                                cpu_winning = True

            for i in range(0, 9):
                if i != 4:
                    if check[i] + check[4] == "oo":
                        grid_num = (4 - i) + 4

            print(cpu_winning)
            if cpu_winning == False:

                if firstxx == 2:
                    for i in range(0, 9):
                        if i != 4 and i != num4:
                            if check[i] + check[4] == "xx":
                                if check[(4 - i) + 4] == "":
                                    grid_num = (4 - i) + 4
                                    num4 = i
                                    firstxx += 1
                                    #print("hi2")

                if firstxx == 1:
                    for i in range(0, 9):
                        if i != 4:
                            if check[i] + check[4] == "xx":
                                if check[(4 - i) + 4] == "":
                                    grid_num = (4 - i) + 4
                                    num5 = i
                                    firstxx += 1

                if check[1] + check[4] + check[7] == "oox":
                    num3 = random.randint(1, 2)
                    if num3 == 2:
                        grid_num = 8
                    elif num3 == 1:
                        grid_num = 6

                if check[1] + check[4] + check[7] == "xoo":
                    num3 = random.randint(1, 2)
                    if num3 == 2:
                        grid_num = 0
                    elif num3 == 1:
                        grid_num = 2

                if check[3] + check[4] + check[5] == "oox":
                    num3 = random.randint(1, 2)
                    if num3 == 2:
                        grid_num = 8
                    elif num3 == 1:
                        grid_num = 2

                if check[3] + check[4] + check[5] == "xoo":
                    num3 = random.randint(1, 2)
                    if num3 == 2:
                        grid_num = 0
                    elif num3 == 1:
                        grid_num = 6

                if firstxox == True:
                    for i in num_list2:
                        if counter1 == 1:
                            if check[i] == "x":
                                num1 = i
                                test = True
                        if counter1 == 2:
                            if check[i] == "x":
                                num2 = i
                                counter1 = 3
                                test = False
                        if test == True:
                            counter1 = 2
                    if counter1 == 3:
                        if (num2 - num1) == 6:
                            grid_num = num2 - 3
                        if (num2 - num1) == 2:
                            grid_num = num2 - 1
                        firstxox = False

        if cputurn == 4:
            print("turn4", firstxx)
            for i in num_list1:
                for j in num_list2:
                    if check[i] + check[j] == "oo":
                        if j > i:
                            if j - i < 3 and j + i != 5 and j + i != 11:
                                var4 = i - (j - 1)
                                if check[var4] == "":
                                    grid_num = var4
                                    cpu_winning = True
                                    var4 = 0

                        if i > j:
                            if i - j < 3 and j + i != 5 and j + i != 11:
                                var4 = (i - j) + i
                                if check[var4] == "":
                                    grid_num = var4
                                    cpu_winning = True
                                    var4 = 0

            for i in range(0, 9):
                if i != 4:
                    if check[i] + check[4] == "oo":
                        var4 = (4 - i) + 4
                        if check[var4] == "":
                            grid_num = (4 - i) + 4

            if firstxx == 3:
                for i in range(0, 9):
                    if i != 4 and i != num4 and i != num5:
                        if check[i] + check[4] == "xx":
                            if check[(4 - i) + 4] == "":
                                grid_num = (4 - i) + 4
                                firstxx += 1

            if firstxx == 2:
                for i in range(0, 9):
                    if i != 4 and i != num5:
                        if check[i] + check[4] == "xx":
                            if check[(4 - i) + 4] == "":
                                grid_num = (4 - i) + 4
                                firstxx += 1

            if firstxx == 1:
                for i in range(0, 9):
                    if i != 4:
                        if check[i] + check[4] == "xx":
                            if check[(4 - i) + 4] == "":
                                grid_num = (4 - i) + 4
                                firstxx += 1



            for i in range(0, 9):
                if check[i] == "":
                    if counter2 == 0:
                        var1 = i
                        counter2 += 1
                    if counter2 == 1:
                        var2 = i
                        counter2 += 1

            if counter2 == 2:
                var3 = random.randint(1, 2)
                if var3 == 1:
                    grid_num = var1
                    print(grid_num)
                if var3 == 2:
                    grid_num = var2
                    print(grid_num)
            print(firstxx)
        if cputurn == 5:
            if first_play == "player":
                for i in range(0, 9):
                    if check[i] == "":
                        grid_num = i

    cpuy = ((grid_num) // 3) + 1
    cpux = ((grid_num + 1) - ((cpuy - 1) * 3))

    destination_pos = ((cpux * cell_size) - 80, (cpuy * cell_size) - 82)
    nought = Actor("oimage1", (0, 0))
    animate(nought, pos=destination_pos)
    noughts.append(nought)
    check[grid_num] = "o"

    counter2 = 0
    for i in range(0, 9):
        if check[i] == "":
            counter2 += 1
    if counter2 == 0:
        mode = "end"
        print("it's a draw")
        still_playing = False

    if check_vict(check) == "oyes":
        print("CPU wins")
        mode = "end"

    cputurn += 1

def playing_pvp(pos):
    global grid_num
    global turn
    turn += 1
    x, y = pos

    valx = (x // cell_size) + 1
    valy = (y // cell_size) + 1

    #gets the the single number that corresponds with that cell
    grid_num = ((valy - 1) * 3) + valx
    grid_num = grid_num - 1

    print(grid_num)


    #PLAYER1
    if turn % 2 != 0:
        #NB: x and y co-ordinates as tuple
        if check[grid_num] == "":
            destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
            cross = Actor("ximage1", (0, 0))
            animate(cross, pos=destination_pos)
            crosses.append(cross)
            check[grid_num] = "x"
        else:
            print("sorry, cell occupied")
            turn -= 1

        if check_vict(check) == "xyes":
            print("player 1 wins")
            mode = "end"


    #PLAYER2
    if turn % 2 == 0:
        if check[grid_num] == "":
            destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
            nought = Actor("oimage1", (0, 0))
            animate(nought, pos=destination_pos)
            noughts.append(nought)
            check[grid_num] = "o"
        else:
            print("sorry, cell occupied")
            turn -= 1

        if check_vict(check) == "oyes":
            print("player 2 wins")
            mode = "end"

def win_screen():
    pass
#NB: checks if anyone has won
def check_vict(list):
    if list[0] + list[4] + list[8] == "xxx":
        return "xyes"
    if list[2] + list[4] + list[6] == "xxx":
        return "xyes"
    if list[0] + list[4] + list[8] == "ooo":
        return "oyes"
    if list[2] + list[4] + list[6] == "ooo":
        return "oyes"

    for i in range(3):
        i = i * 3
        if list[0 + i] + list[1 + i] + list[2 + i] == "xxx" :
            return "xyes"
        if list[0 + i] + list[1 + i] + list[2 + i] == "ooo" :
            return "oyes"

    for i in range(3):
        if list[0 + i] + list[3 + i] + list[6 + i] == "xxx" :
            return "xyes"
        if list[0 + i] + list[3 + i] + list[6 + i] == "ooo" :
            return "oyes"




