# tic tac toe
# this game will be player vs player and will be made up of a cycle where each player takes turns
import time
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
        print(counter1)

    if mode == "end":
        pass


def on_mouse_down(pos):
    global mode
    x, y = pos
    if mode == "playing_pvp":
        playing_pvp(pos)
    elif mode == "playing_pvcpu":
        playing_pvcpu(pos)
    elif mode == "end":
        win_screen()


    if mode == "menu":
        if button1.left < x < button1.right and button1.top < y < button1.bottom:
            time.sleep(0.25)
            mode = "playing_pvp"
        if button2.left < x < button2.right and button2.top < y < button2.bottom:
            time.sleep(0.25)
            mode = "playing_pvcpu"
            #print("sorry this feature is in development")



def playing_pvcpu(pos):
    global grid_num
    global turn
    turn += 1
    x, y = pos

    valx = (x // cell_size) + 1
    valy = (y // cell_size) + 1

    grid_num = ((valy - 1) * 3) + valx
    grid_num = grid_num - 1

    #Player
    #NB: x and y co-ordinates as tuple
    if check[grid_num] == "":
        #destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
        cross = Actor("ximage1", (valx * cell_size - 80, valy * cell_size - 82))
        #animate(cross, pos=destination_pos)
        crosses.append(cross)
        check[grid_num] = "x"
        turn += 1
    else:
        print("sorry, cell occupied")
        turn -= 1

    if check_vict(check) == "xyes":
            print("player 1 wins")
            mode = "end"

    #CPU
    #if check[4] == "":
    grid_num = 4
    #actual position is grid_num + 1
    cpuy = ((grid_num) // 3) + 1
    cpux = ((grid_num + 1) - ((cpuy - 1) * 3))

    #destination_pos = ((cpux * cell_size) - 80, (cpuy * cell_size) - 82)
    nought = Actor("oimage1", ((cpux * cell_size) - 80, (cpuy * cell_size) - 82))
    #animate(nought, pos=destination_pos)
    noughts.append(nought)
    check[grid_num] = "o"

    if check_vict(check) == "oyes":
        print("player 2 wins")
        mode = "end"

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



