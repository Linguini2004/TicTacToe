# tic tac toe
# this game will be player vs player and will be made up of a cycle where each player takes turns
import time
import random
grid = Actor("grid")
menu_back = Actor("menu_background")
end_back = Actor("end_background")
button1 = Actor("1button", (150, 420))
button2 = Actor("2button", (350, 420))
reboot = Actor("reboot_button", (75, 375))

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
counter3 = 0
draw_counter = 0
cputurn = 1
end_text = ""
first_play = "Player"
player_done = False
animating = False
center_first = False
cpu_first = False
firstxox = True
firstxx = True
still_playing = True

def finished_waiting_animating():
    global animating
    animating = False

def finished_animating():
    clock.schedule(finished_waiting_animating, 0.5)

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
        if animating:
            grid.draw()

            for cross in crosses:
                cross.draw()
            for nought in noughts:
                nought.draw()
        else:
            end_back.draw()
            reboot.draw()
            screen.draw.textbox(
            end_text,(20,0,300,80), background = None,
            color = "white", fontname = "dpcomic", align="left")
            screen.draw.textbox(
            "Created by:\nDavide Masini",(10,450,100,40), background = None,
            color = "white", fontname = "dpcomic", align="left")


def on_key_down(key):
    global mode
    if key == keys.LEFT:
        mode = "end"

def on_mouse_down(pos):
    global mode
    global counter3
    global player_done
    global grid_num

    x, y = pos
    if mode == "playing_pvp":
        playing_pvp(pos)
    elif mode == "playing_pvcpu":
        playing_p(pos)
        if player_done == True:
            counter3 += 1
            player_done = False
            clock.schedule(playing_cpu, 2.0)
    elif mode == "end":
        if reboot.left < x < reboot.right and reboot.top < y < reboot.bottom:
            reset()


    if mode == "menu":
        if button1.left < x < button1.right and button1.top < y < button1.bottom:
            time.sleep(0.25)
            mode = "playing_pvp"
        if button2.left < x < button2.right and button2.top <   y < button2.bottom:
            time.sleep(0.25)
            mode = "playing_pvcpu"

def reset():
    global check
    global crosses
    global mode
    global noughts
    global counter3
    global cputurn
    global firstxox
    global firstxx
    global still_playing
    global turn
    global draw_counter

    draw_counter = 0
    turn = 0
    firstxox = True
    firstxx = True
    still_playing = True
    cputurn = 1
    check = ["","","","","","","","",""]
    counter3 = 0
    mode = "menu"
    crosses.clear()
    noughts.clear()

def playing_p(pos):
    global turn
    global check
    global player_done
    global grid_num
    x, y = pos

    valx = (x // cell_size) + 1
    valy = (y // cell_size) + 1

    grid_num = ((valy - 1) * 3) + valx
    grid_num = grid_num - 1

    #Player
    #NB: x and y co-ordinates as tuple

    if check[grid_num] == "":
        player_done = True
        if player_done == True:
            destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
            cross = Actor("ximage1", (0, 0))
            animating = True
            animate(cross, pos=destination_pos, on_finished = finished_animating)
            crosses.append(cross)
            check[grid_num] = "x"
            turn += 1


    if check_vict(check) == "xyes":
        end_text = "You Win/nso much for AI"
        counter3 = 9
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
    global counter3
    global mode
    global animating
    global end_text
    random_num1 = 0
    random_num2 = 0
    last_resort_num = 0
    num_list1 = [1, 3, 5, 7]
    num_list2 = [0, 2, 6, 8]
    numl1_it2 = [7, 5, 3, 1]
    numl2_it2 = [8, 6, 2, 0]
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    iteration = 1
    counter1 = 1
    counter2 = 0
    counter4 = 0
    already_done = False
    cpu_winning = False
    test = False

    if counter3 == 9:
        still_playing = False

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
                                if j > i and i - (j - i) < 9:
                                    if check[i - (j - i)] == "":
                                        grid_num = i - (j - i)
                                        already_done = True
                                if i > j and (i -j) + i < 9:
                                    if check[(i - j) + i] == "":
                                        grid_num = (i - j) + i
                                        already_done = True


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
                            if check[num2 - 3] == "":
                                grid_num = num2 - 3
                                already_done = True
                                firstxox = False
                        if (num2 - num1) == 2:
                            if check[num2 - 1] == "":
                                grid_num = num2 - 1
                                already_done = True
                                firstxox = False

                if center_first ==  False:
                    if firstxx == 1:
                        for i in range(0, 9):
                            if i != 4:
                                if check[i] + check[4] == "xx":
                                    if check[(4 - i) + 4] == "":
                                        grid_num = (4 - i) + 4
                                        already_done = True
                                        num4 = i
                                        firstxx += 1

                if already_done == False:
                    counter4 = 1
                    for i in num_list1:
                        if check[i] == "x":
                            if counter4 == 1:
                                var5 = i
                                counter4 = 2
                            if counter4 == 2:
                                if i != var5:
                                    var6 = i
                                    counter4 = 3
                    if counter4 == 3:
                        if (var5, var6) == (1, 3):
                            grid_num = 0
                            already_done = True
                        if (var5, var6) == (1, 5):
                            grid_num = 2
                            already_done = True
                        if (var5, var6) == (3, 7):
                            grid_num = 6
                            already_done = True
                        if (var5, var6) == (5, 7):
                            grid_num = 8
                            already_done = True

                if already_done == False:
                    for i in range(0, 9):
                        last_resort_num = random.randint(0, 8)
                        if last_resort_num != 4 and check[last_resort_num] == "":
                            grid_num = last_resort_num

        if cputurn == 3:
            for i in num_list1:
                for j in num_list2:
                    if check[i] + check[j] == "oo":
                        if j > i:
                            if j - i < 3 and j + i != 5 and j + i != 11:
                                if check[i - (j - i)] == "":
                                    grid_num = i - (j - i)
                                    cpu_winning = True
                                    already_done = True
                        if i > j:
                            if i - j < 3 and j + i != 5 and j + i != 11:
                                if check[i - (j - i)] == "":
                                    grid_num = (i - j) + i
                                    cpu_winning = True
                                    already_done = True

            if already_done == False:
                for i in range(0, 9):
                    if i != 4:
                        if check[i] + check[4] == "oo":
                            if check[(4 - i) + 4] == "":
                                grid_num = (4 - i) + 4
                                already_done = True

            if cpu_winning == False:

                if already_done == False:
                    if firstxx == 2:
                        for i in range(0, 9):
                            if i != 4 and i != num4:
                                if check[i] + check[4] == "xx":
                                    if check[(4 - i) + 4] == "":
                                        grid_num = (4 - i) + 4
                                        already_done = True
                                        num4 = i
                                        firstxx += 1

                if already_done == False:
                    if firstxx == 1:
                        for i in range(0, 9):
                            if i != 4:
                                if check[i] + check[4] == "xx":
                                    if check[(4 - i) + 4] == "":
                                        grid_num = (4 - i) + 4
                                        already_done = True
                                        num5 = i
                                        firstxx += 1

                if already_done == False:
                    for i in num_list1:
                        for j in num_list2:
                            if check[i] + check[j] == "xx":
                                if j > i:
                                    if j - i < 4 and j + i != 5 and j + i != 11:
                                        if check[i - (j - i)] == "":
                                            grid_num = i - (j - i)
                                            already_done = True
                                if i > j:
                                    if i - j < 4 and j + i != 5 and j + i != 11:
                                        if check[(i - j) + i] == "":
                                            grid_num = (i - j) + i
                                            already_done = True

                if already_done == False:
                    if check[1] + check[4] + check[7] == "oox":
                        already_done = True
                        num3 = random.randint(1, 2)
                        if num3 == 2:
                            grid_num = 8
                        elif num3 == 1:
                            grid_num = 6

                    if check[1] + check[4] + check[7] == "xoo":
                        already_done = True
                        num3 = random.randint(1, 2)
                        if num3 == 2:
                            grid_num = 0
                        elif num3 == 1:
                            grid_num = 2

                    if check[3] + check[4] + check[5] == "oox":
                        already_done = True
                        num3 = random.randint(1, 2)
                        if num3 == 2:
                            grid_num = 8
                        elif num3 == 1:
                            grid_num = 2

                    if check[3] + check[4] + check[5] == "xoo":
                        already_done = True
                        num3 = random.randint(1, 2)
                        if num3 == 2:
                            grid_num = 0
                        elif num3 == 1:
                            grid_num = 6

                if already_done == False:
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
                                already_done = True
                                firstxox = False
                            if (num2 - num1) == 2:
                                grid_num = num2 - 1
                                already_done = True
                                firstxox = False

                if already_done == False:
                    for i in range(0, 9):
                        last_resort_num = random.randint(0, 8)
                        if last_resort_num != 4 and check[last_resort_num] == "":
                            grid_num = last_resort_num

        if cputurn == 4:
            for i in num_list1:
                for j in num_list2:
                    if check[i] + check[j] == "oo":
                        if j > i:
                            if j - i < 4 and j + i != 5 and j + i != 11:
                                var4 = i - (j - 1)
                                if check[var4] == "":
                                    grid_num = var4
                                    cpu_winning = True
                                    var4 = 0
                        if i > j:
                            if i - j < 4 and j + i != 5 and j + i != 11:
                                var4 = (i - j) + i
                                if check[var4] == "":
                                    grid_num = var4
                                    cpu_winning = True
                                    var4 = 0

            if already_done == False:
                for i in num_list2:
                    if counter1 == 1:
                        if check[i] == "o":
                            num1 = i
                            test = True
                    if counter1 == 2:
                        if check[i] == "o":
                            num2 = i
                            counter1 = 3
                            test = False
                    if test == True:
                        counter1 = 2
                if counter1 == 3:
                    if (num2 - num1) == 6 and check[num2 - 3] == "":
                        grid_num = num2 - 3
                        already_done = True
                    if (num2 - num1) == 2 and check[num2 - 1] == "":
                        grid_num = num2 - 1
                        already_done = True

            if already_done == False:
                for i in range(0, 9):
                    if i != 4:
                        if check[i] + check[4] == "oo":
                            var4 = (4 - i) + 4
                            if check[var4] == "":
                                grid_num = (4 - i) + 4
                                already_done = True

            if already_done == False:
                for i in num_list1:
                    for j in num_list2:
                        if check[i] + check[j] == "xx":
                            if j > i:
                                if j - i < 4 and j + i != 5 and j + i != 11:
                                    if check[i - (j - i)] == "":
                                        grid_num = i - (j - i)
                                        already_done = True
                            if i > j:
                                if i - j < 4 and j + i != 5 and j + i != 11:
                                    if check[(i - j) + i] == "":
                                        grid_num = (i - j) + i
                                        already_done = True
            numl1_it2 = [7, 5, 3, 1]
            numl2_it2 = [8, 6, 2, 0]
            if already_done == False:
                for i in range(2):
                    if iteration == 1:
                        list2_in_use = num_list2
                    elif iteration == 2:
                        list2_in_use = numl2_it2
                    for i in list2_in_use:
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
                            if check[num2 - 3] == "":
                                grid_num = num2 - 3
                                already_done = True
                        elif (num2 - num1) == 2:
                            if check[num2 - 1] == "":
                                grid_num = num2 - 1
                                already_done = True
                        else:
                            iteration = 2

            if already_done == False:
                if firstxx == 3:
                    for i in range(0, 9):
                        if i != 4 and i != num4 and i != num5:
                            if check[i] + check[4] == "xx":
                                if check[(4 - i) + 4] == "":
                                    grid_num = (4 - i) + 4
                                    already_done = True
                                    firstxx += 1

            if already_done == False:
                if firstxx == 2:
                    for i in range(0, 9):
                        if i != 4 and i != num5:
                            if check[i] + check[4] == "xx":
                                if check[(4 - i) + 4] == "":
                                    grid_num = (4 - i) + 4
                                    already_done = True
                                    firstxx += 1

            if already_done == False:
                if firstxx == 1:
                    for i in range(0, 9):
                        if i != 4:
                            if check[i] + check[4] == "xx":
                                if check[(4 - i) + 4] == "":
                                    grid_num = (4 - i) + 4
                                    already_done = True
                                    firstxx += 1


            if already_done == False:
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
                        already_done = True
                    if var3 == 2:
                        grid_num = var2
                        already_done = True

        if cputurn == 5:
            if first_play == "player":
                for i in range(0, 9):
                    if check[i] == "":
                        grid_num = i

        cpuy = ((grid_num) // 3) + 1
        cpux = ((grid_num + 1) - ((cpuy - 1) * 3))

        destination_pos = ((cpux * cell_size) - 80, (cpuy * cell_size) - 82)
        nought = Actor("oimage1", (0, 0))
        animating = True
        animate(nought, pos=destination_pos, on_finished = finished_animating)
        noughts.append(nought)
        check[grid_num] = "o"
        counter2 = 0

    for i in range(0, 9):
        if check[i] == "":
            counter2 += 1
    if counter3 >= 9:
        mode = "end"
        end_text = "It's a draw"

    if check_vict(check) == "oyes":
        end_text = "You Lose\nAI will rule the world"
        counter3 = 9
        mode = "end"

    counter3 += 1
    cputurn += 1

def playing_pvp(pos):
    global grid_num
    global turn
    global mode
    global animating
    global end_text
    global draw_counter
    already_won = False
    turn += 1
    draw_counter += 1
    x, y = pos

    valx = (x // cell_size) + 1
    valy = (y // cell_size) + 1

    #gets the the single number that corresponds with that cell
    grid_num = ((valy - 1) * 3) + valx
    grid_num = grid_num - 1


    #PLAYER1
    if turn % 2 != 0:
        #NB: x and y co-ordinates as tuple
        if check[grid_num] == "":
            destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
            cross = Actor("ximage1", (0, 0))
            animating = True
            animate(cross, pos=destination_pos, on_finished = finished_animating)
            crosses.append(cross)
            check[grid_num] = "x"
        else:
            print("sorry, cell occupied")
            turn -= 1

        if check_vict(check) == "xyes":
            end_text = "Player1 Wins"
            already_won = True
            mode = "end"


    #PLAYER2
    if turn % 2 == 0:
        if check[grid_num] == "":
            destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
            nought = Actor("oimage1", (0, 0))
            animating = True
            animate(nought, pos=destination_pos, on_finished = finished_animating)
            noughts.append(nought)
            check[grid_num] = "o"
        else:
            print("sorry, cell occupied")
            turn -= 1

        if check_vict(check) == "oyes":
            end_text = "Player2 Wins"
            already_won = True
            mode = "end"

    if draw_counter >= 9 and not already_won:
        mode = "end"
        end_text = "It's a draw"


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




