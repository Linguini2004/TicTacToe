# tic tac toe
# this game will be player vs player and will be made up of a cycle where each playyer takes turns
grid = Actor("grid")

crosses = []
noughts = []
check = []
check = [0,0,0,0,0,0,0,0,0]
#print(check[0])

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


def draw():
    screen.clear()
    grid.draw()

    for cross in crosses:
        cross.draw()
    for nought in noughts:
        nought.draw()


def on_mouse_down(pos):
    global turn
    turn += 1
    x, y = pos
    #NB: identifying what cell was selected
    for i in range(1, size_across + 1):
        i1 = i - 1
        i2 = i + 1
        x1 = i1 * cell_size
        x2 = i * cell_size
        x3 = i2 * cell_size
        if x > x1 and x < x2:
            valx = i
        y1 = i1 * cell_size
        y2 = i * cell_size
        y3 = i2 * cell_size
        if y > y1 and y < y2:
            valy = i

    #get's the the single number that corresponds with that cell
    grid_num = ((valy - 1) * 3) + valx
    print(grid_num)


    if turn % 2 != 0:
        #NB: x and y co-ordinates as tuple
        cross = Actor("ximage", ((valx * cell_size) - 80, (valy * cell_size) - 82))
        crosses.append(cross)

        check[grid_num - 1] = "x"

        if check_vict(check) == "xyes":
            print("player 1 wins")

    if turn % 2 == 0:
        nought = Actor("oimage", ((valx * cell_size) - 80, (valy * cell_size) - 82))
        noughts.append(nought)

        check[grid_num - 1] = "o"

        if check_vict(check) == "oyes":
            print("player 2 wins")


#NB: checks if anyone has won
def check_vict(list):
    if str(list[0]) + str(list[4]) + str(list[8]) == "xxx":
        return "xyes"
    if str(list[2]) + str(list[4]) + str(list[6]) == "xxx":
        return "xyes"
    if str(list[0]) + str(list[4]) + str(list[8]) == "ooo":
        return "oyes"
    if str(list[2]) + str(list[4]) + str(list[6]) == "ooo":
        return "oyes"

    for i in range(3):
        i = i * 3
        if str(list[0 + i]) + str(list[1 + i]) + str(list[2 + i]) == "xxx" :
            return "xyes"
        if str(list[0 + i]) + str(list[1 + i]) + str(list[2 + i]) == "ooo" :
            return "oyes"

    for i in range(3):
        if str(list[0 + i]) + str(list[3 + i]) + str(list[6 + i]) == "xxx" :
            return "xyes"
        if str(list[0 + i]) + str(list[3 + i]) + str(list[6 + i]) == "ooo" :
            return "oyes"



