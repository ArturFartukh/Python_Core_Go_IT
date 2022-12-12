def solve_riddle(riddle, word_length, start_letter, reverse=False):
    try:
        index = riddle.index(start_letter)
        print(index)
        if reverse:
            return riddle[index: index - word_length: -1]
        else:
            return riddle[index: index + word_length]
    except:
        return ""



# print(solve_riddle('mi1rewopret', 5, 'x', True))
