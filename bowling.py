def score_cruncher(frames):
    scores_per_frame = frames.split(' ')

    total = 0

    for frame_count in range(10):
        total += frame_score(frame_count, scores_per_frame)

    return total

def frame_score(frame_count, scores_per_frame):
    frame = scores_per_frame[frame_count]
        
    if frame[0] == 'x':
        second_frame = scores_per_frame[frame_count + 1]
        third_frame = scores_per_frame[frame_count + 2]

        return strike_calculation(frame, second_frame, third_frame)
    elif frame[1] == '/':
        second_frame = scores_per_frame[frame_count + 1] if frame_count < 9 else "--"
        return spare_calculation(frame, second_frame)
    else:
        return parse_roll(frame[0]) + parse_roll(frame[1])

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
    if second_frame[0] == 'x':
        return 10 + parse_roll(second_frame[0]) + parse_roll(third_frame[0])
    else:
        return 10 + parse_roll(second_frame[0]) + parse_roll(second_frame[1]) 
    


class Frame:

    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score