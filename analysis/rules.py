import json
from collections import defaultdict

def load_experience(path="../logs/experience.jsonl"):
    with open(path) as f:
        for line in f:
            yield json.loads(line)

def find_blocked_patterns(experiences):
    counts = defaultdict(int)
    failures = defaultdict(int)

    for e in experiences:
        key = (tuple(e["state_before"]["agent"]), e["action"])
        counts[key] += 1
        if e["prediction_error"]:
            failures[key] += 1

    rules = []
    for key in counts:
        if failures[key] / counts[key] > 0.7:
            rules.append({
                "pattern": key,
                "type": "blocked_move"
            })

    return rules

def abstract_blocked(rules, experiences):
    abstractions = []

    for rule in rules:
        pos, action = rule["pattern"]

        abstractions.append({
            "type": "constraint",
            "rule": f"action {action} sometimes leads to no movement"
        })

    return abstractions

def detect_stochastic_actions(experiences):
    stats = defaultdict(list)

    for e in experiences:
        key = e["action"]
        stats[key].append(e["prediction_error"])

    stochastic = []
    for action, errors in stats.items():
        rate = sum(errors) / len(errors)
        if 0.1 < rate < 0.9:
            stochastic.append({
                "type": "stochastic_action",
                "action": action,
                "error_rate": rate
            })

    return stochastic

def export_rules(stochastic_rules, path="../logs/induced_rules.json"):
    import json
    with open(path, "w") as f:
        json.dump(stochastic_rules, f, indent=2)


if __name__ == "__main__":
    exps = list(load_experience())

    blocked = find_blocked_patterns(exps)
    abstracted = abstract_blocked(blocked, exps)
    stochastic = detect_stochastic_actions(exps)

    print("constraints:")
    for r in abstracted:
        print("-", r["rule"])

    print("\nstochastic actions:")
    for r in stochastic:
        print("-", r)
    
    export_rules(stochastic)
    print("\nrules exported to logs/induced_rules.json")