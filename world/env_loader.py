import importlib

def load_env(world_name):
    """
    world_name: 'world' or 'world2'
    """
    env = importlib.import_module(f"{world_name}.env")
    grid = importlib.import_module(f"{world_name}.grid")

    return {
        "initial_state": grid.initial_state,
        "step": env.step,
        "render": getattr(env, "render", None),
        "ACTIONS": env.ACTIONS
    }
