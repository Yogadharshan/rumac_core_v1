current_subgoal = None
current_plan = []

def get_subgoal():
    return current_subgoal

def set_subgoal(pos):
    global current_subgoal, current_plan
    current_subgoal = pos
    current_plan = []

def clear_subgoal():
    global current_subgoal, current_plan
    current_subgoal = None
    current_plan = []

def has_subgoal():
    return current_subgoal is not None
