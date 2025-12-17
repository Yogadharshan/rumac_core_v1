blocked_moves = set()
action_counts = {}

def update(prev_pos, action, predicted, actual):
    key = (prev_pos, action)

    action_counts[key] = action_counts.get(key, 0) + 1

    if predicted != actual:
        blocked_moves.add(key)

def can_move(pos, action):
    return (pos, action) not in blocked_moves

def experience_count(pos, action):
    return action_counts.get((pos, action), 0)