def create_index(puzzles_nums, margin):
    index = puzzles_nums / margin if (puzzles_nums % margin) == 0\
        else (puzzles_nums / margin) + 1
    return [i+1 for i in range(int(index))]
