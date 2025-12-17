import json
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "experience.jsonl"

def log_experience(
    episode,
    step,
    state_before,
    action,
    predicted_state,
    actual_state,
    reward
):
    record = {
        "episode": episode,
        "step": step,
        "state_before": state_before,
        "action": action,
        "predicted_state": predicted_state,
        "actual_state": actual_state,
        "reward": reward,
        "prediction_error": predicted_state != actual_state
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
