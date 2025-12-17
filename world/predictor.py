from world.learner import can_move

def predict_next_state(state, action):
    x, y = state["agent"]
    if action == "up":
        return (x, y - 1)
    if action == "down":
        return (x, y + 1)
    if action == "left":
        return (x - 1, y)
    if action == "right":
        return (x + 1, y)
    return (x, y)
