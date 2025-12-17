GRID_SIZE = 5

def initial_state():
    return {
        "agent": (0, 0),
        "goal": (4, 4),
        "walls": [(2, 2)],
        "step": 0,
        "goal_reached": False
    }
