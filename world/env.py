from world.grid import GRID_SIZE

ACTIONS = ["up", "down", "left", "right"]

def step(state, action):
    x, y = state["agent"]

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

    # boundary check
    if new[0] < 0 or new[0] >= GRID_SIZE or new[1] < 0 or new[1] >= GRID_SIZE:
        new = (x, y)

    # wall check
    if new in state["walls"]:
        new = (x, y)

    state["agent"] = new
    state["step"] += 1

    done = new == state["goal"]
    reward = 10 if done else -1

    return state, reward, done

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
