scores_per_frame

def score_cruncher(frames):
    scores_per_frame = frames.split(" ")

    total = 0


    for frame in range(10):
        if frame >= 9:
            total += frame_score(scores_per_frame[frame], None)
        else:
            total += frame_score(scores_per_frame[frame], scores_per_frame[frame + 1])

    return total


def parse_roll(roll):
    if roll == "-":
        return 0
    else:
        return int(roll)
    
def frame_score(frame, index_of_frame):
    if list(frame) == ['x']:
        return 10
    elif list(frame)[-1] == '/':
        return 10 + parse_roll(scores_per_frame[index_of_frame+1][0])
    else:
        return parse_roll(frame[0]) + parse_roll(frame[1])