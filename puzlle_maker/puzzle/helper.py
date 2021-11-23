def more_than_specified_number(amount, specified_number=0):
    return specified_number \
        if specified_number <= amount else amount


def create_index(puzzles_nums, margin):
    index = 1
    if puzzles_nums / margin == 0:
        index = 1
    elif puzzles_nums % margin == 0:
        index = puzzles_nums / margin
    else:
        index = (puzzles_nums / margin) + 1

    return [i+1 for i in range(int(index))]
