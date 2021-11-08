def create_index(puzzles_nums):
    index = puzzles_nums / 30 if (puzzles_nums % 30) == 0\
        else puzzles_nums / 30 + 1
    return [i+1 for i in range(int(index))]
