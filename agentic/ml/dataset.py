"""
Dataset extraction for Task-Planning Autonomous Agent.

Transforms agent state into supervised learning samples.
"""

from typing import List, Dict


def extract_dataset(state: Dict) -> List[Dict]:
    """
    Returns a list of training samples.
    Each sample is a dict: {features..., label}
    """

    samples = []

    tasks = state.get("tasks", [])
    feedback = state.get("feedback", [])
    progress = state.get("progress", {})

    if not feedback:
        return samples  # no supervision yet

    # Compute average recent difficulty
    avg_difficulty = sum(
        f["self_reported_difficulty"] for f in feedback
    ) / len(feedback)

    for task in tasks:
        if task["status"] != "completed":
            continue

        sample = {
            # Features
            "priority": task.get("priority", 0),
            "estimated_difficulty": task.get("estimated_difficulty", 0.0),
            "tasks_pending": progress.get("tasks_pending", 0),
            "avg_recent_difficulty": avg_difficulty,

            # Label
            "actual_difficulty": feedback[-1]["self_reported_difficulty"]
        }

        samples.append(sample)

    return samples
