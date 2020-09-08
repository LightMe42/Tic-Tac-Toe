field = "_________"
print(f"""---------
| {field[0]} {field[1]} {field[2]} |
| {field[3]} {field[4]} {field[5]} |
| {field[6]} {field[7]} {field[8]} |
---------""")
x_raw = 0
o_raw = 0
is_finished = False
field_list = [x for x in field]


def win_check(x):
    global x_raw, o_raw, is_finished
    if x == "X":
        x_raw += 1
    else:
        o_raw += 1

    if (x_raw == o_raw) and x_raw > 0:
        print("Draw")
        is_finished = True
    elif x_raw == 1 and o_raw == 0:
        print("X wins")
        is_finished = True
    elif o_raw == 1 and x_raw == 0:
        print("O wins")
        is_finished = True


def filled_cell():
    print("This cell is occupied! Choose another one!")


def cell_check(move, char):
    position = move[0] + move[1]

    if move[0] not in (1, 2, 3) or move[1] not in (1, 2, 3):
        print("Coordinates should be from 1 to 3!")
        return 0

    if position == 6:
        if field[2] == "_":
            field_list[2] = char
            return 1
        else:
            filled_cell()
            return 0
    elif position == 2:
        if field[6] == "_":
            field_list[6] = char
            return 1
        else:
            filled_cell()
            return 0
    elif position == 5:
        if move[0] == 2:
            if field[1] == "_":
                field_list[1] = char
                return 1
            else:
                filled_cell()
                return 0
        else:
            if field[5] == "_":
                field_list[5] = char
                return 1
            else:
                filled_cell()
                return 0
    elif position == 3:
        if move[0] == 1:
            if field[3] == "_":
                field_list[3] = char
                return 1
            else:
                filled_cell()
                return 0
        else:
            if field[7] == "_":
                field_list[7] = char
                return 1
            else:
                filled_cell()
                return 0
    else:
        if move[0] == 1:
            if field[0] == "_":
                field_list[0] = char
                return 1
            else:
                filled_cell()
                return 0
        elif move[0] == 2:
            if field[4] == "_":
                field_list[4] = char
                return 1
            else:
                filled_cell()
                return 0
        elif move[0] == 3:
            if field[8] == "_":
                field_list[8] = char
                return 1
            else:
                filled_cell()
                return 0


def field_print():
    print(f"""---------
| {field[0]} {field[1]} {field[2]} |
| {field[3]} {field[4]} {field[5]} |
| {field[6]} {field[7]} {field[8]} |
---------""")


def field_check():
    if field[0] == field[1] and field[1] == field[2] and field[0] != "_":
        win_check(field[2])
    if field[0] == field[3] and field[3] == field[6] and field[0] != "_":
        win_check(field[6])
    if field[1] == field[4] and field[4] == field[7] and field[1] != "_":
        win_check(field[7])
    if field[2] == field[5] and field[5] == field[8] and field[2] != "_":
        win_check(field[8])
    if field[0] == field[4] and field[4] == field[8] and field[0] != "_":
        win_check(field[8])
    if field[6] == field[4] and field[4] == field[2] and field[6] != "_":
        win_check(field[2])
    if is_finished:
        return True
    if "_" not in field:
        print("Draw")
        return True


while True:
    x_move = input().split()
    x_move = [int(x) for x in x_move]
    if cell_check(x_move, "X"):
        field = "".join(field_list)
        field_print()
        if field_check():
            break

    o_move = input().split()
    o_move = [int(o) for o in o_move]
    if cell_check(o_move, "O"):
        field = "".join(field_list)
        field_print()
        if field_check():
            break
