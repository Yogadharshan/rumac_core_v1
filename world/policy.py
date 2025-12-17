from world.env import ACTIONS
from world.planner import rollout
from world.regions import region_of
from world.object_extractor import extract_objects

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def choose_action(state, last_pos, world_model):
    agent = state["agent"]
    goal = state["goal"]

    best_score = float("inf")
    best_action = None

    for action in ACTIONS:
        # initialize score first
        score = 0.0

        future_pos, cost = rollout(state, action, world_model, depth=3)
        score += cost
        score += manhattan(future_pos, goal)

        # loop avoidance
        if future_pos == last_pos:
            score += 5.0

        # action-level risk
        score += 3.0 * world_model.failure_risk(action)

        # region-level risk
        score += 4.0 * world_model.region_risk(future_pos)

        # object-level risk
        for obj in extract_objects(state):
            if obj.pos == future_pos:
                score += 6.0 * world_model.object_risk(obj.kind)

        if score < best_score:
            best_score = score
            best_action = action

    return best_action
