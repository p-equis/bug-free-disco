def score_cruncher(frames):
    scores_per_frame = frames.split(" ")
    frame_one_score = scores_per_frame[0]

    match(list(frame_one_score)):
        case ['x']: 
            return 10
        case [a, '/']:
            return 10
        case [a, b]:
            return parse_roll(a) + parse_roll(b)


def parse_roll(roll):
    if roll == "-":
        return 0
    else:
        return int(roll)