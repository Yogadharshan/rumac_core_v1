from world.objects import WorldObject

def extract_objects(state):
    objects = []

    for w in state.get("walls", []):
        objects.append(WorldObject("wall", tuple(w)))

    objects.append(WorldObject("goal", tuple(state["goal"])))

    return objects
