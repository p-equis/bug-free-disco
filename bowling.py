def score_cruncher(frames):
    scores_per_frame = frames.split(" ")
    frame_one_score = scores_per_frame[0]

    roll1 = frame_one_score[0]
    roll2 = frame_one_score[1]

    parse_roll(roll1) + parse_roll(roll2)

    return 0