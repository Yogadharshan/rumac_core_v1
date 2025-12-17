from collections import defaultdict
from collections import defaultdict
from world.regions import region_of

class WorldModel:
    def __init__(self):
        # action -> estimated failure probability
        self.failure_rate = defaultdict(lambda: 0.0)
        self.counts = defaultdict(int)

        self.region_failure = defaultdict(lambda: 0.0)
        self.region_counts = defaultdict(int)

        self.object_failure = {}
        self.object_counts = {}


    # ---- offline prior (from induced rules)
    def load_priors(self, rules):
        """
        rules: list of dicts from induced_rules.json
        """
        for r in rules:
            if r["type"] == "stochastic_action":
                self.failure_rate[r["action"]] = r["error_rate"]
                self.counts[r["action"]] = 1  # seed confidence

    # ---- online update (from live experience)
    def update(self, action, prediction_error, pos=None):
        # action-level update
        self.counts[action] += 1
        rate = self.failure_rate[action]
        n = self.counts[action]
        self.failure_rate[action] = rate + (prediction_error - rate) / n

        # region-level update
        if pos is not None:
            region = region_of(pos)
            self.region_counts[region] += 1
            rrate = self.region_failure[region]
            rn = self.region_counts[region]
            self.region_failure[region] = rrate + (prediction_error - rrate) / rn

    def failure_risk(self, action):
        return self.failure_rate[action]
    
    def region_risk(self, pos):
        return self.region_failure[region_of(pos)]
     
    def update_object_model(self, obj, prediction_error):
        key = obj.kind

        self.object_counts[key] = self.object_counts.get(key, 0) + 1
        rate = self.object_failure.get(key, 0.0)
        n = self.object_counts[key]

        self.object_failure[key] = rate + (prediction_error - rate) / n

    def object_risk(self, kind):
        return self.object_failure.get(kind, 0.0)