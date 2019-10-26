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
winner = ""
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

    if winner:
        screen.draw.textbox(
            "%s wins" % winner,
            (0, HEIGHT / 3, WIDTH, HEIGHT / 3),
            background="blue",
            color="yellow"
        )

def on_mouse_down(pos):
    global turn, winner
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
            cross = Actor("ximage", ((valx * cell_size) - 80, (valy * cell_size) - 82))
            crosses.append(cross)
            check[grid_num] = "x"
            print("correct")
        else:
            print("sorry, cell occupied")
            turn -= 1

        if check_vict(check) == "xyes":
            winner = "Player 1"

    #PLAYER2
    if turn % 2 == 0:
        if check[grid_num] == "":
            nought = Actor("oimage", ((valx * cell_size) - 80, (valy * cell_size) - 82))
            noughts.append(nought)
            check[grid_num] = "o"
        else:
            print("sorry, cell occupied")
            turn -= 1

        if check_vict(check) == "oyes":
            winner = "Player 2"



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



