from world.grid import initial_state
from world.env import step, render
from world.predictor import predict_next_state
from world.learner import update
from world.policy import choose_action
import time
from world.intent import clear_subgoal, has_subgoal, current_subgoal
from world.experience import log_experience
from world.metrics import Metrics
from world.env_loader import load_env
from world.world_model import WorldModel
import json
from world.object_extractor import extract_objects

world_model = WorldModel()

try:
    with open("./logs/induced_rules.json") as f:
        rules = json.load(f)
        world_model.load_priors(rules)
except FileNotFoundError:
    pass


ENV_NAME = "world"  # change to "world2" to switch

env = load_env(ENV_NAME)

initial_state = env["initial_state"]
step = env["step"]
render = env["render"]
ACTIONS = env["ACTIONS"]


metrics = Metrics()

state = initial_state()
last_pos = None

episode = 1
step_count = 0

TOTAL_EPISODES = 30

all_metrics = []

for episode in range(1, TOTAL_EPISODES + 1):
    state = initial_state()
    last_pos = None
    metrics = Metrics()
    step_count = 0

    while True:
        action = choose_action(state, last_pos, world_model)

        prev_pos = state["agent"]
        predicted = predict_next_state(state, action)

        state, reward, done = step(state, action)
        actual = state["agent"]

        update(prev_pos, action, predicted, actual)
        world_model.update(action, predicted != actual, pos=prev_pos)
        metrics.update(predicted, actual)

        last_pos = prev_pos
        step_count += 1
        objects = extract_objects(state)
        for obj in objects:
            if obj.pos == actual:
                world_model.update_object_model(obj, predicted != actual)
        

        if done or step_count > 200:
            all_metrics.append({
                "episode": episode,
                "steps": metrics.steps,
                "error_rate": metrics.error_rate(),
                "invalid_rate": metrics.invalid_rate(),
                "oscillations": metrics.oscillations
            })
            break


with open("./logs/episode_metrics.json", "w") as f:
    import json
    json.dump(all_metrics, f, indent=2)
