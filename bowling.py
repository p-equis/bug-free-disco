def score_cruncher(frames):
    scores_per_frame = frames.split(" ")

    total = 0
    
    for frame in scores_per_frame:
        total += frame_score(frame)

    return total


def parse_roll(roll):
    if roll == "-":
        return 0
    else:
        return int(roll)
    
def frame_score(frame):
    if list(frame) == ['x']:
        return 10
    elif list(frame)[-1] == '/':
        return 10
    else:
        return parse_roll(frame[0]) + parse_roll(frame[1])