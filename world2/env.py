import random
from world2.grid import GRID_SIZE

def render(state):
    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for wx, wy in state["walls"]:
        grid[wy][wx] = "#"

    gx, gy = state["goal"]
    grid[gy][gx] = "g"

    ax, ay = state["agent"]
    grid[ay][ax] = "a"

    for row in grid:
        print(" ".join(row))
    print()


ACTIONS = ["up", "down", "left", "right"]

def step(state, action):
    x, y = state["agent"]

    # stochastic failure
    if random.random() < 0.2:
        new = (x, y)
    else:
        if action == "up":
            new = (x, y - 1)
        elif action == "down":
            new = (x, y + 1)
        elif action == "left":
            new = (x - 1, y)
        elif action == "right":
            new = (x + 1, y)
        else:
            new = (x, y)

    # boundary
    if new[0] < 0 or new[0] >= GRID_SIZE or new[1] < 0 or new[1] >= GRID_SIZE:
        new = (x, y)

    # soft wall toggles every 5 steps
    if state["step"] % 5 != 0 and new in state["walls"]:
        new = (x, y)

    state["agent"] = new
    state["step"] += 1

    reward = 0
    done = False

    if state["goal_reached"]:
        reward = 10
        done = True

    if new == state["goal"]:
        state["goal_reached"] = True

    return state, reward, done
