move_up = 2
move_down = -1


# a no work
# b work

while not (move_up >= 100):
    move_up = move_up - move_down
    move_down = -(move_up - move_down)
    print(move_down, move_up)
print("The cate made it to the top!")
