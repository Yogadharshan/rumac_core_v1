class Metrics:
    def __init__(self):
        self.steps = 0
        self.prediction_errors = 0
        self.invalid_moves = 0
        self.oscillations = 0
        self.last_pos = None

    def update(self, predicted, actual):
        self.steps += 1

        if predicted != actual:
            self.prediction_errors += 1
            self.invalid_moves += 1

        if self.last_pos == actual:
            self.oscillations += 1

        self.last_pos = actual

    def error_rate(self):
        return self.prediction_errors / max(1, self.steps)

    def invalid_rate(self):
        return self.invalid_moves / max(1, self.steps)
