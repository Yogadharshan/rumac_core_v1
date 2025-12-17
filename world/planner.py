from world.env import ACTIONS
from world.predictor import predict_next_state
from world.world_model import WorldModel

def rollout(state, action, world_model, depth=3):
    pos = state["agent"]
    total_cost = 0.0

    for _ in range(depth):
        next_pos = predict_next_state({"agent": pos}, action)

        # base movement cost
        if next_pos == pos:
            total_cost += 2.0  # blocked or failed
        else:
            total_cost += 1.0

        # uncertainty cost (soft)
        if world_model:
            total_cost += world_model.failure_risk(action)

        pos = next_pos

    return pos, total_cost