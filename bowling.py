def score_cruncher(frames):
    scores_per_frame = frames.split(' ')

    total = 0


    for frame_count in range(10):
        frame = scores_per_frame[frame_count]

        # if frame[0] == 'x':
        #     strike_calculation(frame, scores_per_frame[frame_count + 1], scores_per_frame[frame_count + 2])
        # elif frame[1] == '/':
        #     spare_calculation(frame, scores_per_frame[frame_count + 1])

        # else:
        #     return parse_roll(frame[0]) + parse_roll(frame[1])

        if frame_count >= 9:
            total += frame_score(scores_per_frame[frame_count], None)
        else:
            total += frame_score(scores_per_frame[frame_count], scores_per_frame[frame_count + 1])

    return total


def parse_roll(roll):
    if roll == '-':
        return 0
    elif roll == 'x' or roll == '/':
        return 10
    else:
        return int(roll)
    
def spare_calculation(initial_frame, second_frame):
    if len(initial_frame) == 3:
        return 10 + (2 * parse_roll(initial_frame[2]))
    
    return 10 + parse_roll(second_frame[0])

    
def strike_calculation(initial_frame, second_frame, third_frame):
    if len(initial_frame) == 3:
        return parse_roll(initial_frame[0]) + parse_roll(initial_frame[1]) + parse_roll(initial_frame[2])
    elif second_frame[0] == 'x':
        return parse_roll(initial_frame[0]) + parse_roll(second_frame[0]) + parse_roll(third_frame[0])
    else:
        return parse_roll(initial_frame[0]) + parse_roll(second_frame[0]) + parse_roll(second_frame[1]) 
    
def frame_score(frame, next_frame):
    if list(frame)[0] == 'x':
        if next_frame[0] == 'x':
            return 10 + frame_score(next_frame, ["put something here, maybe recursion"])
        return 10 + parse_roll(next_frame[0]) + parse_roll(next_frame[1])
    
    elif list(frame)[1] == '/':
        if len(frame) == 3:
            return 10 + (2 * parse_roll(frame[2]))
        
        return 10 + parse_roll(next_frame[0])
    
    else:
        return parse_roll(frame[0]) + parse_roll(frame[1])