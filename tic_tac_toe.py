# tic tac toe
# this game will be player vs player and will be made up of a cycle where each player takes turns
grid = Actor("grid")

crosses = []
noughts = []
check = []
check = ["","","","","","","","",""]

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

ok = tone.create("A3", 0.5)
fail = tone.create("C1", 0.5)

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
            cross = Actor("ximage", (0, 0))
            animate(cross, pos=destination_pos)
            crosses.append(cross)
            check[grid_num] = "x"
            print("correct")
            ok.play()
        else:
            print("sorry, cell occupied")
            turn -= 1
            fail.play()

        if check_vict(check) == "xyes":
            print("player 1 wins")

    #PLAYER2
    if turn % 2 == 0:
        if check[grid_num] == "":
            destination_pos = ((valx * cell_size) - 80, (valy * cell_size) - 82)
            nought = Actor("oimage", (0, 0))
            animate(nought, pos=destination_pos)
            noughts.append(nought)
            check[grid_num] = "o"
            ok.play()
        else:
            print("sorry, cell occupied")
            turn -= 1
            fail.play()

        if check_vict(check) == "oyes":
            print("player 2 wins")



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



